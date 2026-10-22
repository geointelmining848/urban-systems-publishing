# Stage 2 - Analysis & Evidence

Audit the gap between what the data show and what the manuscript claims. Preserve the
user's requested task: for a title or paragraph edit, flag the material inference problem
and provide a defensible revision; a full study audit is not a prerequisite to every edit.
Load [spatial-methods.md](spatial-methods.md) for spatial specification and
[reporting-standards.md](reporting-standards.md) for the applicable study design.

## Start with the estimand and the claim

State the population, place, period, observational unit, outcome, exposure/intervention,
and target quantity. Separate a descriptive contrast, predictive skill, a causal effect,
and a theoretical explanation. Each can be a valuable contribution; journal prestige is
not a reason to convert an association into a causal claim.

| Claim | Question that changes the conclusion |
|---|---|
| Causal effect | What comparison identifies the counterfactual, under what assumptions, for which population and exposure? |
| Individual behavior | Are individual data actually observed, or is an area-level association being transferred to people? |
| Spatial spillover | Can an exposure of one unit affect another, and can that pathway be distinguished from common shocks, sorting, or measurement? |
| Spatial clustering | What is the null model, including population at risk and dependence? Clustering is a pattern to describe, not inherently an artifact. |
| Scale robustness | How do support, zoning, boundary choice, temporal aggregation, and population composition affect the result? |
| Prediction | Does evaluation match the intended deployment location, horizon, and information available at prediction time? |
| Mechanism or theory | Which observations discriminate this explanation from plausible alternatives? |

Record what evidence exists, what is missing, and what analysis would resolve the gap.
Do not invent results, preregistration, tests, sample sizes, or effect estimates. A proposed
robustness check is not a completed one.

## Identification: assumptions before method names

- **Panel fixed effects** remove time-invariant unit differences under the model, not
  time-varying confounding, reverse causation, differential trends, or measurement error.
- **Difference-in-differences / event studies:** define treatment and comparison cohorts,
  timing, anticipation, outcome scale, and the parallel-trends assumption. Inspect pre-period
  patterns, but failure to reject a pre-trend does not establish parallel counterfactual
  trends. Consider heterogeneous effects under staggered adoption, appropriate cohort/time
  estimands, overlap, spillovers, and inference at the level of assignment. Modern estimators
  address particular failures of conventional two-way fixed effects; their name alone does
  not validate a design. See [Callaway & Sant'Anna](https://doi.org/10.1016/j.jeconom.2020.12.001).
- **Instrumental variables:** defend relevance, exclusion, independence and, where a local
  average treatment effect is claimed, monotonicity. Report first-stage evidence and weak-IV
  robust inference where warranted. A first-stage F statistic is not a universal validity
  certificate; shift-share and historical instruments need design-specific justification.
- **Regression discontinuity:** justify continuity of potential outcomes, the assignment
  rule, manipulation checks, bandwidth, functional form, and local estimand. Geographic
  boundaries can coincide with many changes, so a border alone is not an instrument.
- **Synthetic control:** describe donor eligibility, pre-treatment fit, anticipation,
  interference and sensitivity to influential donors. Placebo exercises are informative
  only under their exchangeability/comparability assumptions.
- **Observational adjustment:** use substantive causal structure to choose covariates;
  avoid conditioning on colliders or post-treatment mediators when estimating a total
  effect. Regression, matching, weighting, spatial random effects, and machine learning do
  not automatically remove unmeasured confounding.

Distinguish **interference** (one unit's treatment changes another unit's outcome) from
correlated errors. Cluster-robust standard errors can address some dependence in inference;
they do not repair a contaminated control group or identify direct and spillover effects.
State the exposure mapping and the direct/indirect estimands when interference matters.

## Spatial threats that materially change a manuscript

1. **MAUP and change of support.** Justify spatial support from the process and the data
   available. Separate scale effects from zonation effects; document boundary crosswalks,
   aggregation weights and temporal units. Where feasible, compare defensible supports.
   An association appearing only at one scale may reflect aggregation, composition, noise,
   or a real process; it does not by itself identify the process scale. With only one
   geography available, bound the claim and explain the untested sensitivity.
2. **Ecological inference.** Area-level coefficients do not identify individual
   associations. Individual outcomes with contextual area exposures are not automatically
   an ecological fallacy: define the contextual estimand and account for dependence,
   individual composition, selection and confounding. A multilevel model needs appropriate
   individual data; it cannot recover individual effects from aggregate data by its name.
   Consider cross-level interactions when substantively relevant, not as a mandatory cure.
3. **Dependence and heterogeneity.** Use residual diagnostics appropriate to the fitted
   model and sampling design. Moran's I depends on W and its null; non-rejection is not
   evidence of independence. Positive residual dependence can make conventional inference
   too optimistic, but the direction is not universal. A correlated-error process need not
   bias exogenous-regressor OLS coefficients; an omitted endogenous lag or confounder can.
4. **Spatial confounding.** Spatial adjustment can change the estimand and redistribute
   variation between exposure and residual terms. Describe the assumed causal/spatial
   structure, sensitivity to spatial scale, and remaining uncertainty. No spatial model
   automatically solves confounding.
5. **W and network definition.** Defend distance metric, edges, direction, normalization,
   islands and temporal alignment. Compare plausible specifications without selecting only
   the one that yields a preferred sign or p-value. Endogenous networks need special care.
6. **Spatial impacts.** In SAR/SDM/SAC models, distinguish raw coefficients from direct,
   indirect and total marginal responses; report uncertainty on those responses. A fitted
   indirect response is model-based evidence, not itself identification of causal diffusion.
7. **Edges, denominators and measurement.** Check missing neighbors outside the study
   boundary, rates based on small populations, exposure misclassification, geocoding error,
   selective coverage and uncertainty in modeled denominators.

## Alternatives, selection and uncertainty

Build a compact table of competing explanation, diagnostic, observed result and remaining
limitation. Negative controls and placebo tests require their own assumptions; a passed
placebo cannot exclude every rival explanation. Spatial/temporal permutations must preserve
the features required by the null; unrestricted shuffling can destroy relevant dependence.

Report effect sizes and interval estimates, not only statistical significance. Distinguish
sampling uncertainty, measurement error, specification uncertainty and transportability.
Address missingness and informative coverage. Report subgroup and model searches, including
unfavorable results. For a defined family of tests, choose an error-control method suited
to the inferential goal and dependence. Bonferroni/Holm control family-wise error under
arbitrary dependence when the component p-values are valid; ordinary BH FDR needs additional
conditions, while BY allows more general dependence at a power cost. A local permutation
p-value is not itself a multiple-testing correction.
[Official R adjustment documentation](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/p.adjust.html).

Data-dependent analysis choices can invalidate nominal inference even when only one test
is reported. Remedies include preregistration for future analyses, honest exploratory
labeling, held-out confirmation, selective-inference methods where justified, and transparent
specification sensitivity. A specification curve does not by itself restore valid p-values.
Use Type S/M design analysis when sign or magnitude errors are consequential; do not present
observed post-hoc power as new evidence. Bayesian models need prior sensitivity, computational
diagnostics and posterior predictive checks. Simulation-based calibration is useful for
validating an inference implementation under the generative model, not proof that the model
matches the real world or a compulsory ritual for every routine fit.

## Prediction and validation

Define the use case first: interpolation within sampled areas, a new region, a future
period, or a changed regime. The split must mimic it. Random folds can be optimistic for
spatial transfer, yet nearby training observations may legitimately be available for
interpolation. Choose blocking, buffering, leave-region-out or temporal splits accordingly;
report block sizes, buffer distances, fold membership and why they fit the deployment task.
[Roberts et al.](https://doi.org/10.1111/ecog.02881).

- Keep feature construction, imputation, scaling and model/hyperparameter selection inside
  training folds. Avoid test-informed variable selection, spatial smoothers or target encoding.
- For forecasts, use forward/rolling-origin validation with the actual information cutoff.
  Ordinary leave-one-time-point-out may train on future observations and is not prospective
  forecast validation. Report performance by horizon against persistence, seasonal and other
  credible simple baselines using the same metrics and evaluation periods.
- For rare events, include precision-recall performance, prevalence, threshold-specific
  sensitivity/precision and a confusion matrix. ROC-AUC can be reported alongside these;
  neither AUC alone specifies operational value. Define the PR summary and its baseline.
- Evaluate calibration as well as discrimination where probabilities matter. Use uncertainty
  methods that respect dependent observations; naive independent resampling may mislead.
- Simulation verification, structural checks, calibration and held-out validation are distinct.
  Use [complex-systems.md](complex-systems.md) when a model is the central contribution.

## Evidence and output

Verify novelty against the relevant literature, not only a local journal corpus. Record
search sources, dates, scope and unavailable full texts. If browsing or the corpus is
unavailable, still audit the supplied design and mark literature-dependent judgments as
provisional. A missing search hit does not establish novelty.

Return the supported claim, identification/inference assumptions, material spatial threats,
completed versus proposed checks, uncertainty and remaining limits, followed by a concrete
revision or next analysis. Use GO / REFINE / RECONSIDER only when a triage verdict is requested;
explain the evidence behind it without unsupported journal acceptance predictions.
