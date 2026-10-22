#!/usr/bin/env python3
"""Build an optional, bounded local OpenAlex corpus; no network on import.

Existing OPENALEX_API_KEY is read only when fetching, sent as a bearer header,
never written to disk. The caller manages access and spending authorization.
API documentation: https://help.openalex.org/api/paging/
https://help.openalex.org/api/authentication/ and /api/filtering/
Field IDs: https://help.openalex.org/data/fields/
"""
import argparse
from collections import Counter
from datetime import date, datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

SCHEMA_VERSION = 2
PER_PAGE = 100
SELECT = 'id,doi,title,publication_year,publication_date,type,cited_by_count,referenced_works_count,abstract_inverted_index,primary_topic,authorships,biblio'

F_SOC, F_MED, F_ENV, F_ECON, F_HEALTH = "33", "27", "23", "20", "36"

def fields_filter(ids):
    return "primary_topic.field.id:" + "|".join(str(i) for i in ids)

# tag -> (source_id, tier, mega_field_filter_or_None)
SOURCES = {
    # ---- broad-reach / high-impact generalist ----
    "NatCities":   ("S4390297069", "broad", None),
    "NatSust":     ("S4210188283", "broad", None),
    "NatHumBeh":   ("S2764866340", "broad", None),
    "PNAS":        ("S125754415",  "broad", [F_SOC, F_ENV, F_MED, F_ECON]),
    "SciAdv":      ("S2737427234", "broad", [F_SOC, F_ENV, F_MED, F_ECON]),
    "LancetPH":    ("S2764808104", "broad", None),
    "LancetPlan":  ("S2898182138", "broad", None),
    "GEC":         ("S130750583",  "broad", None),  # Global Environmental Change
    # ---- flagship disciplinary ----
    "AnnalsAAG":   ("S2764498735", "flagship", None),
    "UrbanStud":   ("S50366009",   "flagship", None),
    "EPA":         ("S87933477",   "flagship", None),  # Environment & Planning A
    "EconGeog":    ("S38825547",   "flagship", None),
    "RegStud":     ("S175672440",  "flagship", None),
    "JRegSci":     ("S65528657",   "flagship", None),
    "JUrbEcon":    ("S147692640",  "flagship", None),
    "RSUE":        ("S107631327",  "flagship", None),  # Reg Sci & Urban Econ
    "SSM":         ("S106822843",  "flagship", None),  # Social Science & Medicine
    "HealthPlace": ("S43487215",   "flagship", None),
    "AJPH":        ("S168049282",  "flagship", None),
    "TobControl":  ("S149729710",  "flagship", None),
    "Addiction":   ("S70513841",   "flagship", None),
    "EHP":         ("S10446503",   "flagship", None),  # Environmental Health Perspectives
    # ---- specialist / solid-contribution ----
    "Cities":      ("S137445289",  "specialist", None),
    "LUP":         ("S104597489",  "specialist", None),  # Landscape & Urban Planning
    "CEUS":        ("S60115552",   "specialist", None),  # Computers Env & Urban Systems
    "EPB":         ("S4210169418", "specialist", None),  # Environment & Planning B
    "Habitat":     ("S4210229294", "specialist", None),  # Habitat International
    "SCS":         ("S163634330",  "specialist", None),  # Sustainable Cities & Society
    "ApplGeog":    ("S115443327",  "specialist", None),
    "PapersRegSci":("S101788309",  "specialist", None),
    "AnnRegSci":   ("S203746597",  "specialist", None),
    "IJHG":        ("S28612791",   "specialist", None),  # Int J Health Geographics
    "EnvRes":      ("S173943867",  "specialist", [F_ENV, F_MED, F_SOC]),
    "IJERPH":      ("S15239247",   "specialist", [F_MED, F_ENV, F_SOC, F_HEALTH]),
    "JTG":         ("S80150607",   "specialist", None),  # J Transport Geography
    "GeoAnal":     ("S159894308",  "specialist", None),  # Geographical Analysis
    "JCleanProd":  ("S58516903",   "specialist", [F_ENV, F_SOC, F_ECON]),
    "EcolEcon":    ("S136211407",  "specialist", None),  # Ecological Economics
    "UrbanGeog":   ("S153445956",  "specialist", None),
    "PopSpacePlace":("S79946630",  "specialist", None),
    "GeoHealth":   ("S4210174605", "specialist", None),
    "TravBehav":   ("S2764874763", "specialist", None),  # Travel Behaviour & Society
    "NicTobRes":   ("S62426309",   "specialist", None),  # Nicotine & Tobacco Research
    "IJDP":        ("S60503757",   "specialist", None),  # Int J Drug Policy
    "DAD":         ("S109998069",  "specialist", None),  # Drug & Alcohol Dependence
}
TIER = {tag: meta[1] for tag, meta in SOURCES.items()}




def atomic_json(path, value):
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    tmp.replace(path)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fetch_json(params, api_key):
    """Finite retries; errors deliberately omit URLs, headers and response bodies."""
    url = 'https://api.openalex.org/works?' + urllib.parse.urlencode(params)
    headers = {'User-Agent': 'urban-systems-publishing/2', 'Authorization': 'Bearer ' + api_key}
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise RuntimeError(f'OpenAlex HTTP {exc.code}; check access, quota, or API syntax.') from None
            try:
                delay = max(2 ** attempt, float(exc.headers.get('Retry-After', '0')))
            except (TypeError, ValueError):
                delay = 2 ** attempt
            if delay > 60:
                raise RuntimeError('OpenAlex requested a long rate-limit wait; retry later.') from None
            time.sleep(delay)
        except (urllib.error.URLError, TimeoutError):
            if attempt == 2:
                raise RuntimeError('OpenAlex network request failed after three attempts.') from None
            time.sleep(2 ** attempt)
        except (ValueError, UnicodeError):
            raise RuntimeError('OpenAlex returned an invalid JSON response.') from None


def reconstruct_abstract(inv):
    positions = {i: word for word, indices in (inv or {}).items() for i in indices}
    return ' '.join(positions[i] for i in sorted(positions)) or None


def flatten(tag, work):
    identifier = (work.get('id') or '').rsplit('/', 1)[-1]
    if not identifier.startswith('W') or not identifier[1:].isdigit():
        raise ValueError('A work lacks a valid OpenAlex ID.')
    abstract = reconstruct_abstract(work.get('abstract_inverted_index'))
    title = work.get('title') or ''
    topic = work.get('primary_topic') or {}
    return {
        'journal': tag, 'tier': TIER[tag], 'oa_id': identifier,
        'doi': (work.get('doi') or '').removeprefix('https://doi.org/') or None,
        'year': work.get('publication_year'), 'date': work.get('publication_date'),
        'title': title, 'title_nwords': len(title.split()), 'title_has_colon': ':' in title,
        'abstract': abstract, 'abstract_nwords': len((abstract or '').split()),
        'n_authors': len(work.get('authorships') or []),
        'cited_by_count': work.get('cited_by_count'),
        'n_refs': work.get('referenced_works_count'),
        'subfield': (topic.get('subfield') or {}).get('display_name'),
        'topic': topic.get('display_name'), 'type': work.get('type'),
    }


def parameters(tag, start, end, cap):
    source, _, fields = SOURCES[tag]
    filters = f'primary_location.source.id:{source},from_publication_date:{start},to_publication_date:{end},type:article'
    if fields:
        filters += ',' + fields_filter(fields)
    return {'schema_version': SCHEMA_VERSION, 'filter': filters, 'cap': cap,
            'max_pages': (cap + PER_PAGE - 1) // PER_PAGE + 1,
            'per_page': PER_PAGE, 'select': SELECT, 'corpus': 'core'}


def fetch_journal(root, tag, config, api_key, fetcher=fetch_json):
    """Reuse only a complete matching cache; restart incomplete pulls, never append blindly."""
    raw = root / 'raw'
    raw.mkdir(parents=True, exist_ok=True)
    output = raw / (tag + '.jsonl')
    metadata = raw / (tag + '.meta.json')
    if output.exists() or metadata.exists():
        if not output.exists() or not metadata.exists():
            raise ValueError(f'{tag}: incomplete or incompatible cache; choose a fresh corpus directory.')
        previous = json.loads(metadata.read_text(encoding='utf-8'))
        if previous.get('parameters') != config or previous.get('sha256') != digest(output):
            raise ValueError(f'{tag}: cache parameters or checksum differ; choose a fresh corpus directory.')
        if previous.get('status') == 'complete':
            return previous
    rows, seen, cursor, total, status, reason = [], set(), '*', None, 'partial', None
    used_cursors, pages = set(), 0
    try:
        while cursor and len(rows) < config['cap'] and pages < config['max_pages']:
            if cursor in used_cursors:
                raise ValueError('OpenAlex repeated a previously used cursor.')
            used_cursors.add(cursor)
            params = {'filter': config['filter'], 'select': config['select'], 'corpus': 'core',
                      'per_page': min(PER_PAGE, config['cap'] - len(rows)), 'cursor': cursor}
            page = fetcher(params, api_key)
            pages += 1
            if not isinstance(page.get('results'), list) or not isinstance(page.get('meta'), dict):
                raise ValueError('Invalid OpenAlex response structure.')
            meta, works = page['meta'], page['results']
            total = meta.get('count', total)
            if total is not None and (not isinstance(total, int) or total < 0):
                raise ValueError('OpenAlex returned an invalid record count.')
            if len(works) > params['per_page']:
                raise ValueError('OpenAlex returned more records than requested.')
            if 'next_cursor' not in meta:
                raise ValueError('OpenAlex response lacks a cursor state.')
            for work in works:
                row = flatten(tag, work)
                if row['oa_id'] not in seen and len(rows) < config['cap']:
                    rows.append(row)
                    seen.add(row['oa_id'])
            next_cursor = meta['next_cursor']
            if next_cursor is not None and not isinstance(next_cursor, str):
                raise ValueError('OpenAlex returned an invalid cursor.')
            if next_cursor == cursor and next_cursor is not None:
                raise ValueError('OpenAlex repeated its cursor.')
            if not works and next_cursor is not None:
                raise ValueError('OpenAlex returned an empty page with a continuation cursor.')
            cursor = next_cursor
            if cursor is None:
                status = 'complete' if total is None or len(rows) == total else 'partial'
                reason = None if status == 'complete' else 'record_count_mismatch'
                break
            time.sleep(0.12)
        if cursor is not None:
            reason = 'cap_reached' if len(rows) >= config['cap'] else 'page_limit_reached'
    except (RuntimeError, ValueError, TypeError, KeyError) as exc:
        status, reason = 'failed', str(exc)
    tmp = output.with_suffix('.jsonl.tmp')
    tmp.write_text(''.join(json.dumps(row, ensure_ascii=False, allow_nan=False) + '\n' for row in rows), encoding='utf-8')
    tmp.replace(output)
    result = {'parameters': config, 'retrieved_utc': datetime.now(timezone.utc).isoformat(),
              'status': status, 'reason': reason, 'records': len(rows), 'pages': pages,
              'api_total': total, 'sha256': digest(output)}
    atomic_json(metadata, result)
    return result


def compute_norms(df, provenance):
    """Descriptive sample statistics, never journal submission limits."""
    journals = {}
    def quantile(series, proportion):
        import pandas as pd
        clean = pd.to_numeric(series, errors='coerce').dropna()
        return float(clean.quantile(proportion)) if len(clean) else None
    for tag, group in df.groupby('journal'):
        abstracts = group[group['abstract_nwords'] > 0]
        years = group['year'].dropna()
        record = {'tier': TIER[tag], 'n_records': len(group),
                  'year_range': [int(years.min()), int(years.max())] if len(years) else [None, None],
                  'n_with_abstract': len(abstracts),
                  'title_colon_pct': round(100 * group['title_has_colon'].mean(), 1),
                  'top_subfields': Counter(group['subfield'].dropna()).most_common(12)}
        for name, column, sample in [('title_words', 'title_nwords', group),
                                      ('abstract_words', 'abstract_nwords', abstracts),
                                      ('refs', 'n_refs', group), ('n_authors', 'n_authors', group)]:
            record[name + '_median'] = quantile(sample[column], .5)
            record[name + '_p10_p90'] = [quantile(sample[column], .1), quantile(sample[column], .9)]
        journals[tag] = record
    return {'schema_version': SCHEMA_VERSION, 'generated_from': 'OpenAlex',
            'retrieved_utc': provenance['generated_utc'], 'journals': journals}


def consolidate(root, reports):
    import pandas as pd
    rows = []
    for tag, report in reports.items():
        path = root / 'raw' / (tag + '.jsonl')
        if report['sha256'] != digest(path):
            raise ValueError(f'{tag}: checksum changed during consolidation.')
        rows.extend(json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line)
    columns = list(flatten(next(iter(SOURCES)), {'id': 'W1'}))
    df = pd.DataFrame(rows, columns=columns).drop_duplicates(subset=['journal', 'oa_id'])
    provenance = {'schema_version': SCHEMA_VERSION, 'generated_utc': datetime.now(timezone.utc).isoformat(),
                  'source': 'OpenAlex', 'journals': reports, 'records': len(df),
                  'status': 'complete' if all(r['status'] == 'complete' for r in reports.values()) else 'partial',
                  'note': 'Coverage is only the recorded source/date/type/topic filters; metadata may change.'}
    temp = root / 'corpus.parquet.tmp'
    df.to_parquet(temp, index=False)
    temp.replace(root / 'corpus.parquet')
    provenance['parquet_sha256'] = digest(root / 'corpus.parquet')
    atomic_json(root / 'norms.json', compute_norms(df, provenance))
    atomic_json(root / 'provenance.json', provenance)
    return provenance


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('journals', nargs='*', help='Explicit source tags; see query_corpus.py --journals')
    parser.add_argument('--all', action='store_true', help='Select the entire journal catalog')
    parser.add_argument('--corpus-dir', type=Path, required=True, help='Dedicated output directory outside the skill')
    parser.add_argument('--from-date', default='2010-01-01')
    parser.add_argument('--to-date', default=date.today().isoformat())
    parser.add_argument('--max-records', type=int, default=1000, help='Per journal cap; a capped result is partial')
    parser.add_argument('--dry-run', action='store_true', help='Show finite scope without network or file writes')
    args = parser.parse_args(argv)
    if args.all and args.journals or not (args.all or args.journals):
        parser.error('Choose explicit journal tags OR --all.')
    tags = list(SOURCES) if args.all else list(dict.fromkeys(args.journals))
    if set(tags) - SOURCES.keys():
        parser.error('Unknown journal tag(s): ' + ', '.join(sorted(set(tags) - SOURCES.keys())))
    try:
        if date.fromisoformat(args.from_date) > date.fromisoformat(args.to_date):
            raise ValueError()
    except ValueError:
        parser.error('Dates must be valid YYYY-MM-DD and from-date must not follow to-date.')
    if args.max_records < 1:
        parser.error('--max-records must be positive.')
    root = args.corpus_dir.expanduser().resolve()
    if root.is_relative_to(Path(__file__).resolve().parents[1]):
        parser.error('--corpus-dir must be outside the installed skill.')
    configs = {tag: parameters(tag, args.from_date, args.to_date, args.max_records) for tag in tags}
    if args.dry_run:
        print(json.dumps(configs, indent=2))
        return 0
    api_key = os.environ.get('OPENALEX_API_KEY', '').strip()
    if not api_key:
        parser.error('Existing OPENALEX_API_KEY required for cursor paging; no credentials are created.')
    try:
        import pandas  # noqa: F401
        import pyarrow  # noqa: F401
    except ImportError:
        parser.error('Optional corpus dependencies missing; install scripts/requirements.txt from the skill directory in your environment.')
    reports = {}
    try:
        for tag in tags:
            reports[tag] = fetch_journal(root, tag, configs[tag], api_key, fetcher=fetch_json)
            print(f"{tag}: {reports[tag]['status']} ({reports[tag]['records']} records; reason={reports[tag]['reason']})")
            if reports[tag]['status'] == 'failed':
                print('Fetch failed; existing consolidated files were not replaced. Raw attempt metadata retained.', file=sys.stderr)
                return 1
        provenance = consolidate(root, reports)
    except (OSError, ValueError, KeyError) as exc:
        print(f'Corpus build stopped ({type(exc).__name__}); inspect local cache metadata or choose a fresh directory.', file=sys.stderr)
        return 1
    print(f"Corpus: {provenance['records']} records; {provenance['status']} for the recorded filters.")
    return 0 if provenance['status'] == 'complete' else 2


if __name__ == '__main__':
    sys.exit(main())
