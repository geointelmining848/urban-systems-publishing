# Stage 3a - Journal Selection

Recommend a journal from the claim and evidence, intended readers, and author constraints.
Use **reach x epistemic culture** to compare options, not to assign immutable journal ranks
or predict editorial decisions. A narrow request for a journal comparison need not restart
the entire workflow. Read [journal-profiles.md](journal-profiles.md) for the catalog and
[significance-and-framing.md](significance-and-framing.md) for the contribution pitch.

## Build a defensible shortlist

1. **State what the paper contributes.** Separate the value of a descriptive pattern,
   prediction, causal estimate, concept, formal theory, method, or applied intervention.
   Causal identification is needed for a causal claim, not as a universal entry requirement.
2. **Find the readers who need it.** A strong technical result may speak to a methods
   audience, a substantive urban debate, or both. A place-specific study can matter more
   widely when it illuminates a process or boundary condition; multiple cities alone do
   not establish generalizability.
3. **Compare two to four candidates using current evidence.** For each, consult the
   official aims/scope, article type, current author guide, and several recent relevant
   papers. State why each precedent is comparable. Use the optional corpus, authorized web
   search, or supplied literature; report access gaps instead of inventing a scope check.
4. **Plan an alternative.** A rejection may call for a different audience, a different
   article type, a substantive repair, or another venue of similar scope. Read the actual
   decision before changing the argument. Do not assume every rejection means moving down
   a prestige ladder or rewriting the same evidence for the opposite "culture."

## Useful comparisons to investigate

These are starting hypotheses from the original skill, not categorical admissions rules.

| Comparison | What should determine the choice |
|---|---|
| Urban Studies / Cities | Contribution to a wider urban debate and conceptual understanding versus the particular policy/planning application; both publish varied methods. |
| Annals AAG / Applied Geography | Disciplinary or methodological contribution versus a geographic approach to a practical problem; Annals also has Geographic Methods and other editorial areas. |
| J. Regional Science / Papers in Regional Science / Annals of Regional Science | Which regional-science debate, theory, estimator, or empirical question the study advances; compare relevant recent articles rather than inferring a fixed hierarchy. |
| J. Urban Economics / Regional Science and Urban Economics | Economic mechanism and estimand, theory or empirical contribution, and urban versus regional emphasis; assess identification where causal effects are claimed. |
| Environment and Planning A / Environment and Planning B | Economy-and-space debates versus urban analytics/city science; a conceptual contribution and a quantitative method can coexist in either argument. |
| Health & Place / Social Science & Medicine / AJPH | Place-and-health processes, a social-science account of health, or population-health practice/policy; choose by contribution and article type. |
| IJHG / GeoHealth / Health & Place | A health-geographic method, an environmental/Earth-system health linkage, or an account of place and health. |
| CEUS / EPB / Geographical Analysis | Computational/spatial method with urban use, city-science understanding, or a formal geographic/statistical method. |
| J. Transport Geography / Travel Behaviour and Society | Spatial accessibility, networks, and equity versus travel behavior, activity, choice, and social context; do not assume qualitative studies are excluded. |
| J. Cleaner Production / Sustainable Cities and Society / Ecological Economics | Production/consumption and life-cycle questions, urban sustainability systems, or ecological-economic relations and theory. |
| Tobacco Control / Nicotine & Tobacco Research | Policy and tobacco-control implications versus the substantive nicotine/tobacco-science contribution; verify funding and disclosure rules for the actual venue. |
| Addiction / International Journal of Drug Policy / Drug and Alcohol Dependence | Addiction science, policy and harm reduction, or dependence epidemiology/treatment/pharmacology; choose by what the study establishes. |
| Nature Cities / Nature Sustainability / Lancet Public or Planetary Health / GEC / PNAS / Science Advances | Which broad readership needs the result, what evidence supports that reach, and whether the proposed article type is in scope. These are alternatives, not a fixed fallback order. |

For any other journal, use the same process. This catalog does not define the field's
boundaries; regional, non-English-language, practitioner, and emerging venues may fit the
study or intended community better.

## Precedent searches and their limits

Optional local examples, run from the skill directory:

```bash
python scripts/query_corpus.py "street network accessibility equity" --journal UrbanStud,Cities --sort recent
python scripts/query_corpus.py "spatial spillover house prices" --journal JRegSci,RSUE,PapersRegSci --sort cited
python scripts/query_corpus.py "greenspace mental health" --journal HealthPlace,SSM,AJPH --show-abstract
```

A cited-first search can favor old, highly visible papers; pair it with recent work. Keyword
search misses synonyms, methods not named in abstracts, other languages, and records with
missing text. `--has-abstract` changes the retrieved population and does **not** make it a
full-text search. Missing abstracts can vary by journal and year; inspect the actual
coverage. Metadata may also be incomplete. Do not infer absence, selectivity, quality, or
novelty directly from query counts or article volume.

## Practical constraints are part of fit

- **Publication model and cost:** verify subscription, hybrid, and fully open access
  options for the exact journal and article type. Check funder requirements, embargoes,
  institutional agreements, waivers, and whether any fee is mandatory. Do not generalize
  from a publisher brand. For example, the official Nature Cities and Nature Sustainability
  pages offer subscription and Gold OA options for primary research (checked 2026-10-22):
  [Nature Cities options](https://www.nature.com/natcities/submission-guidelines/publishing-options),
  [Nature Sustainability options](https://www.nature.com/natsustain/submission-guidelines/publishing-options).
  Recheck before quoting a price or advising a financial commitment.
- **Timing:** use the author's actual deadline and dated publisher metrics where available.
  Distinguish time to first decision, time in external review, and time to publication.
  Do not promise that applied journals are faster than theoretical journals or infer an
  individual manuscript's duration from a median.
- **Transfers:** evaluate the receiving journal's scope, costs, policies, and treatment of
  earlier reviews. A transfer invitation is neither acceptance nor proof of better odds.
- **Indexing and reputation:** verify the relevant index directly when it matters to the
  author, identify the date, and distinguish indexing status from article validity. A
  historical exclusion flag in a local corpus is a search choice, not a permanent journal
  blacklist or evidence that every paper in that venue is unreliable.
- **Presubmission enquiries:** consult the exact journal/article-type policy. Some permit
  enquiries or proposals only for particular formats. Draft one when useful and permitted;
  do not infer policy across Nature, Lancet, Elsevier, or another family. An encouraging
  reply does not guarantee review or acceptance.

## Recommendation output

Lead with the best-supported candidate and the reason, then compare alternatives:

| Candidate | Readers and contribution fit | Closest verified precedents | Main risk or adaptation | Practical constraints / source date |
|---|---|---|---|---|
| [Journal and article type] | [Specific reason] | [Links and relevance] | [Evidence or framing change] | [Verified requirement or unknown] |

State what is inference from scope and precedents, what is an official requirement, and
what remains uncertain. Keep the author's preferred venue visible even if advising another
option. Complete useful framing work while unresolved practical details are checked.
