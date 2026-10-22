# Public health, tobacco, cannabis and spatial epidemiology

Load this for population health, spatial epidemiology, urban-environmental exposure or
tobacco/drug-policy manuscripts. Use [analysis-rigor.md](analysis-rigor.md) for the claim
and identification design, [spatial-methods.md](spatial-methods.md) for spatial models,
and [reporting-standards.md](reporting-standards.md) for design-specific reporting.
This is publication/research guidance, not individualized clinical advice.

## Surveillance and survey design

Define the target population and estimand before choosing weights. Complex surveys may
involve unequal inclusion probabilities, clustering, stratification, nonresponse
adjustment and calibration. Unweighted descriptive estimates need not represent the
population; simple-random-sampling standard errors can be misleading in either direction.
Report unweighted sample size alongside population estimates and their uncertainty.

For population inference, use the release's appropriate weights and design-based variance
procedure, or justify a model-based alternative and its assumptions. Do not claim that
every unweighted regression coefficient is necessarily biased. Explain how the sampling
design, nonresponse and population target are handled. Subpopulation analyses often need
domain estimation retaining the survey design, not deletion followed by a naive variance.

The following table is a planning aid. Read the exact wave/cycle documentation before
naming weight variables, replicate counts, geographic access or trend comparability.

| Dataset | What to check for the manuscript |
|---|---|
| PATH (Population Assessment of Tobacco and Health) | Cross-sectional versus longitudinal target, wave/cohort eligibility, appropriate person/replicate weights, attrition and restricted geography. |
| NHANES | Interview versus examination or subsample weights; cycle-combination rules; strata/PSU; special release periods and nonresponse; restricted subnational geography. |
| NSDUH | Survey-year analysis weights/design variables, target population and redesign or collection-mode breaks; distinguish direct survey estimates from modeled small-area products. |
| BRFSS | Year/state design and weighting, module/subsample weights where applicable, geographic representativeness and instability of small domains; SMART eligibility varies. |
| NYTS | School/student sampling, clustering, coverage, response and questionnaire/mode changes before comparing years. |
| Monitoring the Future | Grade/cohort, school design, form-split items, follow-up target and appropriate weights. |
| TUS-CPS | Supplement wave, self/proxy response, sample/replicate weights, population coverage and available geography. |
| GATS | Country/year protocol, multistage design, weights and cross-country measurement comparability. |

The [NHANES weighting tutorial](https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx)
shows why the analytic component and population target determine weight choice.
Its [release-specific analytic guidance](https://wwwn.cdc.gov/nchs/nhanes/analyticguidelines.aspx)
also covers exceptional periods; do not assume every release is a standard two-year cycle.
Use the corresponding official manual for other surveys, not NHANES rules by analogy.

State outcome/exposure definitions, eligible ages, exclusions, missingness, design degrees
of freedom and variance method. A large record count does not eliminate design effects,
measurement error, attrition or coverage bias. Preserve the release DOI/version and access
date where available.

## Denominators, exposure and measurement

For area-level rates, match numerator and denominator populations, periods and support.
ACS estimates have uncertainty, and overlapping multi-year releases are dependent.
Distinguish a population rate, an age-standardized rate, retailer density per land area,
retailers per resident, network travel time and access subject to capacity/competition.

A neighborhood variable may represent context, proximity or an administrative proxy.
State how exposure was assigned, residential history or mobility limits, buffer/network
choice, temporal alignment, geocoding error and availability of facilities. Distance to
the nearest service is not equivalent to access if transport, capacity, eligibility,
quality or opening hours differ. Spatial proximity alone does not establish exposure
or uptake.

For tobacco/cannabis, define product, route, frequency, duration and measurement window.
Ever-use, current use, dependence and dose are different constructs. Report potency
where observed and distinguish measurement from assumptions; avoid converting an
imprecise survey category into a dose-response estimate.

## Tobacco and regulatory framing

Surface funding and competing interests early, including indirect support, in-kind data
access and relevant personal financial relationships. Some venues have specific exclusions
for tobacco-related funding or ties. Verify the exact journal's current scope and policy
before deciding eligibility; do not treat a remembered policy as identical across all
publishers, products or article types.
[Official Tobacco Control author guidance](https://tobaccocontrol.bmj.com/pages/authors).

Where relevant, distinguish the scientific question about population benefit/harm from
a regulatory claim about a product or authorization pathway. Use current official
regulatory sources for terms and requirements. Identify the population, comparator and
outcome: adult switching, cessation, youth initiation and sustained dependence cannot be
collapsed into a single "harm reduction" or "gateway" slogan.

Frame conclusions around the study's evidence and uncertainty, not a presumed editor's
ideological preference. Findings for one product, group or time period do not establish
effects for all products or populations. Do not claim regulatory approval or compliance
from epidemiological association.

## Cannabis and drug-policy studies

Do not embed a permanent legal-status assertion in the manuscript or this skill. Verify
jurisdiction, dates and policy definitions against official legislation/regulatory sources
for the **study period** and, if discussing today's status, the publication date.
Separate enactment, effective date, retail opening, implementation intensity and enforcement.
A current policy map cannot reconstruct historical treatment exposure.

For policy-effect designs, define treatment versions and relevant comparison groups.
Address anticipation, concurrent policies, spillovers, cross-border purchasing and changing
survey modes. A modern staggered-adoption estimator helps with specific heterogeneity
problems; it does not repair a wrongly dated treatment or violated identification assumptions.

Disclose industry ties and data-provider constraints. Verify any reporting-unit convention
against the applicable funding/program guidance; a standard THC reporting unit is not a
universal safe dose or clinical recommendation.

## Causal and cross-level inference

Cross-sectional associations generally do not, without additional design assumptions,
identify effects of changing an exposure. Match verbs to the supported estimand throughout
the abstract, results and discussion. Statistical adjustment does not automatically
justify "causes," and odds ratios are not risk ratios when outcomes are common.

Choose confounders using substantive causal structure, avoiding indiscriminate control
for mediators/colliders. An E-value or other sensitivity measure addresses a specified
unmeasured-confounding problem under assumptions; it does not measure all bias, prove
causality, or replace assessment of selection and measurement error. Explain the chosen
scale, uncertainty and what the sensitivity analysis leaves unaddressed.

**Ecological fallacy:** do not infer individual associations from an area-level regression.
However, an area exposure paired with observed individual outcomes is not automatically
ecological inference. It can target a contextual association/effect. Account for clustering,
individual composition, sorting and confounding; consider contextual and compositional
terms separately. A multilevel label does not identify a causal contextual effect or
recover individual information absent from aggregate data. Cross-level interactions
are substantive hypotheses to evaluate where relevant, not mandatory proof of validity.

## Small areas, smoothing and MRP

Rare counts and small denominators can produce unstable extremes. Show counts, denominators,
uncertainty and disclosure status. Raw rates can be useful descriptively when clearly
qualified; avoid presenting a noisy rank as established risk. Smoothing/partial pooling
trades variance for assumptions and possible bias; document those assumptions, sensitivity
and uncertainty rather than calling a smoothed map the truth.

For count models, justify distribution, offsets, overdispersion, zero structure and
expected-rate standardization. CAR/BYM/BYM2 are common areal models; a continuous SPDE model
requires an appropriate observation/support model. INLA is an inference approach, not
synonymous with either CAR or SPDE. See [spatial-methods.md](spatial-methods.md).

**Multilevel regression and poststratification (MRP)** estimates population/domain
summaries by modeling outcomes and aggregating cell predictions with a target population
frame. It does not identify each unobserved person's outcome. Document:

- Population cells, predictors, interactions and their connection to selection/nonresponse.
- Availability and accuracy of joint poststratification counts, not merely marginal totals.
- Sparse/empty cells, extrapolation, pooling assumptions and prior sensitivity.
- Validation against credible direct/held-out estimates and propagation of model/frame
  uncertainty where feasible.
- Between-area variance and what drives shrinkage. A posterior near zero indicates little
  residual area variation under this model; it does not prove no real area differences.

Not all small-area estimation is MRP; direct estimates, area-level models and unit-level
models may fit different data. Choose the approach from the estimand and available
information. Use simulation-based calibration when checking an inference implementation
is material, plus computational and predictive diagnostics; it is not a mandatory
precondition to every multilevel analysis.

## Spatial policy diffusion and environmental justice

Policy diffusion can be part of the scientific question and a source of interference.
Model the relevant exposure or bound the estimand; merely clustering standard errors
does not remove spillovers into controls. Shared political/economic changes can produce
adoption clusters without causal diffusion.

For inequalities, quantify absolute and relative differences with a justified reference,
standardization and uncertainty. Race/ethnicity and neighborhood categories are social
and measurement constructs, not automatic biological mechanisms. Explain composition,
segregation, exposure assignment and relevant institutional processes. Co-location of
disadvantage and hazards supports an area-level disparity description; individual harm
or a causal discrimination mechanism requires additional evidence.

## Ethics, disclosure and venue fit

State the actual ethics determination, responsible body, consent/access basis and any
disclosure approval. Do not infer that public or de-identified data automatically establish
exemption; do not invent an approval, waiver, reviewer clearance or conflict declaration.
Follow the data provider's release rules for maps, tables and small cells.
[data-and-reproducibility.md](data-and-reproducibility.md) covers access and preservation.

Choose venues by the contribution and audience, then verify current scope and comparable
papers. Useful starting points include Health & Place for place/health relationships,
IJHG for spatial health methods, AJPH for public-health significance, Tobacco Control or
NTR for tobacco questions, Addiction/IJDP/DAD for substance-use or drug-policy work,
and EHP/GeoHealth for environmental exposures. These are hypotheses about fit, not
promises of acceptance or rigid journal cultures. Publication status, limits, funding
rules and abstract formats must be checked against current official guidance.

Deliver the defensible population/individual claim, design and survey requirements,
material measurement/cross-level threats, disclosure facts, and a concrete revision or
analysis plan. Optional specialist skills are aids when installed; a named imagined
reviewer is not evidence or a prerequisite to completing the user's request.
