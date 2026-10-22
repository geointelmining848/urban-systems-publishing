"""Deterministic synthetic tests; no private corpus and no live API calls."""
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import urllib.error
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'skills' / 'urban-systems-publishing' / 'scripts'
sys.path.insert(0, str(SCRIPTS))
import build_corpus as build
import query_corpus as query


def work(number, title='Urban 公共交通 access', **extra):
    return {'id': f'https://openalex.org/W{number}', 'title': title,
            'publication_year': 2024, 'cited_by_count': 0, **extra}


def page(works, total=None, cursor=None):
    return {'results': works, 'meta': {'count': len(works) if total is None else total,
                                     'next_cursor': cursor}}


class CorpusBuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=os.environ.get('CORPUS_TEST_TMP'))
        self.root = Path(self.temp.name)
        self.config = build.parameters('Cities', '2020-01-01', '2024-12-31', 3)

    def tearDown(self):
        self.temp.cleanup()

    def test_help_and_dry_run_have_no_network_or_files(self):
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
        env.pop('OPENALEX_API_KEY', None)
        for arguments in (['--help'], ['Cities', '--corpus-dir', str(self.root / 'output'),
                                     '--dry-run', '--to-date', '2024-12-31']):
            result = subprocess.run([sys.executable, str(SCRIPTS / 'build_corpus.py'), *arguments],
                                    cwd=self.root, capture_output=True, text=True, env=env)
            self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_invalid_scope_and_missing_key_fail_before_writes(self):
        with patch.dict(os.environ, {}, clear=True):
            for args in (['TYPO'], ['Cities', '--from-date', '2025-01-01', '--to-date', '2024-01-01'],
                         ['Cities', '--max-records', '0'], ['Cities']):
                with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                    build.main([*args, '--corpus-dir', str(self.root / 'output')])
        self.assertFalse((self.root / 'output').exists())

    def test_unicode_and_nullable_metadata_survive(self):
        record = build.flatten('Cities', work(1, abstract_inverted_index={'城市': [1], 'Healthy': [0]}))
        self.assertEqual(record['abstract'], 'Healthy 城市')
        self.assertEqual(record['abstract_nwords'], 2)
        self.assertIsNone(record['n_refs'])
        with self.assertRaises(ValueError):
            build.flatten('Cities', {'title': 'no ID'})

    def test_broad_journal_query_records_bounded_primary_field_scope(self):
        config = build.parameters('PNAS', '2020-01-01', '2024-12-31', 250)
        self.assertIn('primary_topic.field.id:33|23|27|20', config['filter'])
        self.assertIn('to_publication_date:2024-12-31', config['filter'])
        self.assertEqual(config['per_page'], 100)
        self.assertEqual(config['max_pages'], 4)

    def test_auth_is_header_only_and_http_error_is_redacted(self):
        secret = 'synthetic-secret-for-test'
        def reject(request, timeout):
            self.assertNotIn(secret, request.full_url)
            self.assertEqual(request.get_header('Authorization'), 'Bearer ' + secret)
            raise urllib.error.HTTPError(request.full_url + '?private=' + secret, 401, secret, {}, None)
        with patch.object(build.urllib.request, 'urlopen', side_effect=reject):
            with self.assertRaises(RuntimeError) as caught:
                build.fetch_json({'cursor': '*'}, secret)
        self.assertIn('401', str(caught.exception))
        self.assertNotIn(secret, str(caught.exception))

    def test_cap_is_partial_not_complete(self):
        result = build.fetch_journal(self.root, 'Cities', self.config, 'test',
                                     fetcher=lambda *_: page([work(1), work(2), work(3)], 10, 'next'))
        self.assertEqual((result['status'], result['reason'], result['records']), ('partial', 'cap_reached', 3))
        self.assertEqual(result['sha256'], build.digest(self.root / 'raw' / 'Cities.jsonl'))
        self.assertFalse(list(self.root.rglob('*.done')))

    def test_complete_cache_is_reused_and_mismatch_rejected(self):
        result = build.fetch_journal(self.root, 'Cities', self.config, 'test', fetcher=lambda *_: page([work(1)]))
        self.assertEqual(result['status'], 'complete')
        reused = build.fetch_journal(self.root, 'Cities', self.config, 'test',
                                     fetcher=lambda *_: self.fail('Complete matching cache made a network call'))
        self.assertEqual(result, reused)
        with self.assertRaises(ValueError):
            build.fetch_journal(self.root, 'Cities', {**self.config, 'cap': 4}, 'test')
        (self.root / 'raw' / 'Cities.jsonl').write_text('changed', encoding='utf-8')
        with self.assertRaises(ValueError):
            build.fetch_journal(self.root, 'Cities', self.config, 'test')

    def test_legacy_done_marker_cannot_claim_completion(self):
        (self.root / 'raw').mkdir()
        (self.root / 'raw' / 'Cities.jsonl').write_text('', encoding='utf-8')
        (self.root / 'raw' / 'Cities.jsonl.done').write_text('1', encoding='utf-8')
        with self.assertRaises(ValueError):
            build.fetch_journal(self.root, 'Cities', self.config, 'test')

    def test_failed_fetch_is_recorded_without_consolidation(self):
        with patch.dict(os.environ, {'OPENALEX_API_KEY': 'test'}), \
                patch.object(build, 'fetch_json', side_effect=RuntimeError('OpenAlex HTTP 403')), \
                contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            code = build.main(['Cities', '--corpus-dir', str(self.root)])
        self.assertEqual(code, 1)
        metadata = json.loads((self.root / 'raw' / 'Cities.meta.json').read_text(encoding='utf-8'))
        self.assertEqual(metadata['status'], 'failed')
        self.assertIn('403', metadata['reason'])
        self.assertFalse((self.root / 'corpus.parquet').exists())

    def test_duplicate_or_inconsistent_pages_do_not_claim_complete(self):
        calls = []
        def duplicates(params, _):
            calls.append(params)
            return page([work(1)], 5, 'next' + str(len(calls)))
        with patch.object(build.time, 'sleep'):
            result = build.fetch_journal(self.root, 'Cities', self.config, 'test', fetcher=duplicates)
        self.assertEqual(result['reason'], 'page_limit_reached')
        self.assertEqual(len(calls), self.config['max_pages'])
        self.assertEqual(result['records'], 1)
        result = build.fetch_journal(self.root, 'Cities', self.config, 'test',
                                     fetcher=lambda *_: page([work(1)], 4))
        self.assertEqual(result['reason'], 'record_count_mismatch')

    def test_url_cursor_round_trips_reserved_characters(self):
        seen = []
        class Reply(io.StringIO):
            def __enter__(self): return self
            def __exit__(self, *_): self.close()
        def capture(request, timeout):
            seen.append(request.full_url)
            return Reply(json.dumps(page([])))
        cursor = 'a+b/c=d&x'
        with patch.object(build.urllib.request, 'urlopen', side_effect=capture):
            build.fetch_json({'cursor': cursor}, 'test')
        self.assertEqual(build.urllib.parse.parse_qs(build.urllib.parse.urlparse(seen[0]).query)['cursor'], [cursor])


@unittest.skipUnless(importlib.util.find_spec('pandas') and importlib.util.find_spec('pyarrow'),
                     'Install optional requirements-corpus.txt for dataframe tests')
class CorpusQueryTests(unittest.TestCase):
    def setUp(self):
        import pandas as pd
        self.temp = tempfile.TemporaryDirectory(dir=os.environ.get('CORPUS_TEST_TMP'))
        self.root = Path(self.temp.name)
        self.frame = pd.DataFrame([
            {'journal': 'Cities', 'title': 'Transit access', 'abstract': 'Healthy city', 'year': 2024,
             'cited_by_count': None, 'doi': None, 'subfield': None},
            {'journal': 'IJERPH', 'title': 'City health', 'abstract': None, 'year': None,
             'cited_by_count': 10, 'quality_flag': True},
            {'journal': 'UrbanStud', 'title': 'Literal [map] 公共交通', 'abstract': 'Transit and access',
             'year': 2022, 'cited_by_count': 2},
        ])
        self.frame.to_parquet(self.root / 'corpus.parquet', index=False)
        self.df = query.load(self.root)

    def tearDown(self):
        self.temp.cleanup()

    def test_legacy_quality_flag_does_not_hide_records(self):
        self.assertEqual(set(query.search(self.df, [])['journal']), {'Cities', 'IJERPH', 'UrbanStud'})
        self.assertEqual(set(query.search(self.df, [], exclude={'IJERPH'})['journal']), {'Cities', 'UrbanStud'})

    def test_and_or_phrase_literal_and_unicode_matching(self):
        self.assertEqual(len(query.search(self.df, ['transit', 'access'])), 2)
        self.assertEqual(len(query.search(self.df, ['healthy', '公共交通'], any_term=True)), 2)
        self.assertEqual(len(query.search(self.df, ['transit access'])), 1)
        self.assertEqual(len(query.search(self.df, ['[map]'])), 1)

    def test_filtering_and_missing_numbers_are_safe(self):
        selected = query.search(self.df, [], tags={'Cities', 'UrbanStud'}, year_min=2023, has_abstract=True)
        self.assertEqual(list(selected['journal']), ['Cities'])
        self.assertEqual(self.df.iloc[0]['cited_by_count'], 0)
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(query.main(['--corpus-dir', str(self.root), '--show-abstract']), 0)

    def test_norms_handles_multiple_journals_and_null_statistics(self):
        (self.root / 'norms.json').write_text(json.dumps({'journals': {'Cities': {'refs_median': None},
                                                                 'UrbanStud': {'refs_median': 20}}}), encoding='utf-8')
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            query.print_norms(self.root, {'Cities', 'UrbanStud'})
        self.assertIn('Cities:', output.getvalue())
        self.assertIn('UrbanStud:', output.getvalue())
        self.assertIn('refs median=?', output.getvalue())
        with self.assertRaises(ValueError):
            query.print_norms(self.root, {'HealthPlace'})

    def test_bad_tags_and_norm_filters_fail_loudly(self):
        for args in (['--journal', 'Cites'], ['--journal', ','], ['--num', '0'],
                     ['--year-min', '2025', '--year-max', '2024'], ['--norms', '--year-min', '2020']):
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                query.main(args)

    def test_consolidated_provenance_and_tamper_detection(self):
        config = build.parameters('Cities', '2024-01-01', '2024-12-31', 2)
        result = build.fetch_journal(self.root, 'Cities', config, 'test',
                                     fetcher=lambda *_: page([work(1), work(2)], 10, 'next'))
        provenance = build.consolidate(self.root, {'Cities': result})
        self.assertEqual(provenance['status'], 'partial')
        with contextlib.redirect_stdout(io.StringIO()) as output:
            query.check_provenance(self.root)
        self.assertIn('partial', output.getvalue())
        self.assertIn('to_publication_date:2024-12-31', output.getvalue())
        with (self.root / 'corpus.parquet').open('ab') as handle:
            handle.write(b'tamper')
        with self.assertRaises(ValueError):
            query.check_provenance(self.root)


if __name__ == '__main__':
    unittest.main()
