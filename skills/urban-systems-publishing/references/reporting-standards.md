# Reporting standards: choose by design, document what actually happened

Use a reporting guideline to expose missing information and help readers assess the
study. It is not a validity score, a license to fill gaps with invented methods, or a
reason to stop a requested small edit. Map relevant items to manuscript sections and
identify what is missing, not yet done, or inapplicable.

Check the current official guideline, extensions and target-journal instructions before
quoting item counts, versions or mandatory uploads. When browsing is unavailable, label
the checklist mapping provisional. Preserve the distinction between completed work and a
recommendation for a future study.

## Design-to-guideline routing

| Design / output | Starting point | Boundary |
|---|---|---|
| Observational cohort, case-control or cross-sectional health study | STROBE | Reporting, not a study-quality or causal-validity score. |
| Observational study using routinely collected health data | STROBE plus RECORD; RECORD-PE for applicable pharmacoepidemiology | Focus on data definitions, linkage, selection and validation; not every administrative dataset is a health record. |
| Molecular epidemiology | Relevant STROBE extension such as STROBE-ME | Use only when its scope fits. |
| Systematic review / meta-analysis | PRISMA 2020 and applicable extensions | Scoping, diagnostic and other reviews may need their specific extension. |
| Randomized trial | CONSORT 2025 plus relevant design extensions | Cluster/place-based trials need cluster-specific reporting; verify the extension's compatibility/version. |
| Health estimates across populations/time using multiple information sources | GATHER | Not automatically required for every fitted spatial surface or regression. |
| Clinical prediction model | TRIPOD family / TRIPOD+AI where applicable | Predictive performance and development/evaluation transparency; not proof of clinical benefit. |
| Qualitative interviews/focus groups | COREQ when suitable; SRQR for broader qualitative reporting | Respect methodology; do not force quantitative criteria onto interpretive work. |
| Simulation / agent-based model | ODD and model-specific reproducibility guidance | See [complex-systems.md](complex-systems.md). |

A conceptual/theoretical paper may not fit a health checklist. An empirical qualitative
paper still benefits from appropriate reporting of sampling, reflexivity, analysis and
evidence. Match standards to the **study**, not a fixed "positivist versus interpretive"
label assigned to a journal. Use the
[EQUATOR registry](https://www.equator-network.org/reporting-guidelines/) to locate the
actual scope and current documents.

## Observational studies: STROBE and RECORD

STROBE has 22 items spanning design, setting, participants, measurement, bias, analysis,
results, limitations, interpretation and funding. It does not prescribe a particular study
design or confer causal validity. Use the design-specific checklist and its explanation.
[Official STROBE site](https://www.strobe-statement.org/).

For this skill, the recurrent omissions to surface are:

- Population, place, period, eligibility and how the analytic sample was selected.
- Exposure/outcome definitions, measurement support and temporal alignment.
- Confounders/effect modifiers, missingness, sampling design and sensitivity decisions.
- Estimates with uncertainty, denominators, subgroup analyses and data-dependent choices.
- Limits on inference across people, places, scales and periods.
- Funding, access restrictions and the role of data providers.

Name the design in the title or abstract. Provide a balanced summary; a structured abstract
is a journal/article-type requirement to verify, not a universal STROBE command. State
objectives/hypotheses honestly, including whether they were prespecified. STROBE reporting
does not allow retrospective claims of preregistration.

Explain sample-size determination rather than computing observed power to justify the
result. A flow diagram can clarify selection; do not claim one is universally compulsory
for every observational report. Add spatial metadata and W/uncertainty details from
[spatial-methods.md](spatial-methods.md) and
[data-and-reproducibility.md](data-and-reproducibility.md).

RECORD adds attention to code lists/algorithms, database selection, linkage, cleaning and
access to routine-data definitions. Locate the actual supplement/extension before
declaring compliance. [RECORD statement](https://doi.org/10.1371/journal.pmed.1001885).

## Systematic reviews: PRISMA 2020

PRISMA 2020 has a 27-item checklist, abstract guidance and flow diagrams. Record sources,
search dates/strategies, eligibility criteria, selection, data extraction, risk-of-bias
assessment, synthesis methods and reporting of exclusions. Document protocol/registration,
amendments and their timing when they exist. PROSPERO eligibility varies; neither a
registration number nor the label "systematic" establishes methodological quality.
[PRISMA 2020 statement](https://doi.org/10.1136/bmj.n71).

A missing flow diagram or search appendix is a reporting gap to repair from records,
not automatic proof that a review was narrative. If the underlying reproducible search
and selection process never occurred, describe the actual review method and avoid
mislabeling it. Do not fabricate screening counts, exclusions or a retrospective protocol.

Search coverage and eligibility must match the question; a local journal corpus alone
rarely supports a comprehensive systematic review. Language restrictions, unavailable
full texts, database limitations and duplicate handling belong in the limitations.

## Randomized trials: CONSORT 2025

CONSORT 2025 supersedes the earlier 25-item 2010 statement with a 30-item checklist and
flow diagram. Verify the current statement and design extension before preparing a
submission. [Official SPIRIT-CONSORT guidance](https://www.consort-spirit.org/) and
[CONSORT 2025 statement](https://doi.org/10.1136/bmj-2024-081123).

For place/cluster trials, make the randomization unit, participant recruitment timing,
allocation, cluster/individual flow, analysis unit and dependence assumptions explicit.
Report adherence, deviations, harms, missing outcomes, effect estimates and uncertainty.
Do not imply masking occurred where impossible or invent a trial registration.

Cluster dependence affects precision and power; its effect is not universally a fixed
inflation factor. Describe the estimator, variance method, number and size of clusters
and any small-sample correction. An intention-to-treat estimand should be clearly defined;
alternative estimands/analyses need justification rather than a blanket label.

## Modeled health estimates: GATHER

GATHER addresses estimates for multiple populations in time/space assembled from multiple
information sources. Its 18-item framework emphasizes source identification, data access,
modeling assumptions, methods and uncertainty. Verify scope before applying it to a local
prediction surface merely because a model was used.
[WHO GATHER resources](https://data.who.int/about/data/gather).

For relevant spatial estimates, show input coverage, harmonization, observation models,
estimation choices, validation and uncertainty intervals. Distinguish uncertainty sources
included in the intervals from omitted structural/measurement uncertainty. A narrow
posterior interval can still be conditional on a misspecified model.

## Prediction and qualitative research

For applicable prediction studies, report target population/outcome, predictor availability
at deployment, data partitions, tuning, missing-data handling, calibration, discrimination
and external/temporal/spatial evaluation. Avoid presenting resubstitution performance as
validation or promising clinical utility from discrimination alone.
[TRIPOD+AI statement](https://doi.org/10.1136/bmj-2023-078378).

For qualitative studies, describe the methodological position, recruitment, context,
researcher role/reflexivity, data collection, analytic process, disconfirming evidence and
how quotations/cases support interpretations. Keep participant privacy and consent
constraints. COREQ or SRQR may support reporting, but an interview study's credibility is
not measured by a spatial-regression checklist.
[COREQ](https://doi.org/10.1093/intqhc/mzm042);
[SRQR](https://doi.org/10.1097/ACM.0000000000000388).

## Working output

Return a design/standard/version mapping and an item-location table with four possible
statuses: documented, missing information, not performed, or not applicable with reason.
Prioritize gaps that change interpretation. Fill manuscript locations only when the text
exists. Check the journal's actual submission requirements before calling a checklist
mandatory. Reporting completeness and scientific validity require separate judgments.
