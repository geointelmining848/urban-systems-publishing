# Spatial methods - specification, interpretation and validation

Use this companion when the manuscript's conclusion depends on spatial specification.
[analysis-rigor.md](analysis-rigor.md) covers the claim and identification design. Here,
distinguish a model for substantive interaction, a model for residual covariance, and a
predictive representation of spatial structure. All can be legitimate; a fitted pattern
does not establish a mechanism.

Contents: [weights](#1-the-spatial-weights-matrix-w), [model selection](#2-model-selection),
[impacts](#3-interpretation-the-impacts-framework), [panels](#4-spatial-panels),
[ESDA](#5-exploratory-spatial-data-analysis), [other models](#6-alternatives-and-complements),
[confounding](#7-spatial-confounding), [validation](#8-spatial-cross-validation),
[reporting](#9-reporting-and-specialist-review).

## 1. The spatial weights matrix W

State the observational support, unit ordering, distance metric, self-neighbor convention,
direction, normalization, islands and boundary treatment. Geometry and the interaction
mechanism may differ: commuting flows, travel times, watersheds or trade links may be more
relevant than shared borders. Check that the network/exposure was measured at the correct
time. If W is estimated from outcomes or endogenous choices, disclose that dependence and
justify the estimator and uncertainty treatment.

| Family | What to justify |
|---|---|
| Rook / queen contiguity | Shared edges versus edges or vertices; geometry repair and tolerance; disconnected components. Queen includes at least the rook neighbors. |
| k-nearest neighbors | k, metric and ties; each row usually has k directed links, but reciprocity is not guaranteed. Symmetrization changes the implied network and should be deliberate. |
| Distance band | Interaction radius and units. Isolated units may be substantively correct; enlarging the radius solely to remove them can invent implausible ties. |
| Inverse distance / kernel | Decay, bandwidth, zero-distance pairs and any truncation. A cutoff can improve sparsity, but is not universally required; near-zero distances require separate care. |
| Directed or flow weights | Direction of transmission, period, exposure versus interaction, and whether total flows or shares are the relevant quantity. |

Row-standardization makes a nonempty row sum to one, so Wy is a weighted average.
It changes relative versus absolute connectivity: two and twenty neighbors each carry
total weight one. This may suit average peer exposure, but not total inflow or accumulated
mass. It often breaks symmetry. Zero rows need an explicit policy.

Do not apply a memorized bound for the spatial autoregressive parameter to every W.
The inverse (I - rho W) must exist. For a Neumann-series interpretation, require the
spectral radius of rho W to be below one. Familiar reciprocal-eigenvalue intervals use
particular real-spectrum/normalization assumptions; directed matrices can have complex
eigenvalues. Distinguish invertibility, covariance conditions and dynamic stability.

**Choose and compare W transparently.** For explanatory work, start from plausible
mechanisms and show sensitivity over a defensible set. Predictive tuning is legitimate
inside a validation scheme, but label it and do not reuse the tuned fit as confirmatory
evidence. Report direct and indirect impacts, intervals, fit and prediction as appropriate;
neither direct nor indirect effects are guaranteed stable across W.

An outcome-adaptive search for the W giving the preferred p-value is a selection problem.
Predefine plausible candidates where possible and report the full relevant comparison.
A change in sign, magnitude or uncertainty is substantive evidence about robustness.

**What a scramble can and cannot show.** A node-label permutation PWP' preserves the
spectrum while reassigning ties to observations. Under a justified randomization scheme,
it can be a diagnostic of whether alignment with the observed geography matters. Arbitrary
eigenvector rearrangement can violate sparsity, nonnegativity or graph constraints and is
not a standard validation test. A worse fit after scrambling does not identify the true
mechanism or prove W correct; use such diagnostics only with an explicit null and rationale.

## 2. Model selection

For the linear models below, distinguish the response y, covariates X, innovations
epsilon, spatial error u, spatial-response coefficient rho, spatial-error coefficient
lambda, and lagged-covariate coefficients theta.

| Model | Mean / error structure | Interpretation under its assumptions |
|---|---|---|
| SLX | y = X beta + WX theta + epsilon | Covariate exposure from neighbors; local responses without endogenous feedback. |
| SAR (spatial lag) | y = rho Wy + X beta + epsilon | Simultaneous spatial response with feedback through the multiplier. |
| SEM | y = X beta + u; u = lambda Wu + epsilon | Spatial error covariance; no mean spillover from changing X under this specification. |
| SDM | y = rho Wy + X beta + WX theta + epsilon | Endogenous spatial response plus covariate exposure. |
| SDEM | y = X beta + WX theta + u; u = lambda Wu + epsilon | Local covariate responses plus correlated errors. |
| SAC / SARAR | y = rho Wy + X beta + u; u = lambda Mu + epsilon | Spatial response and error dependence; W and M may differ. |

SDM reduces to SAR when theta = 0 and, under compatible W/design assumptions, to a
SEM representation under the common-factor restriction theta = -rho beta. Clarify
intercepts, normalization and estimation assumptions when testing these restrictions.

**Diagnostics guide, not identify.** Residual Moran's I and LM/Rao-score tests can
indicate misspecification; they do not determine the causal model. The classic adjusted
LM tests address local contamination by the competing lag/error alternative, not arbitrary
heteroskedasticity, omitted variables or every alternative model. Inspect the specific
test's assumptions and implementation; modern suites also contain Durbin-related tests.
[PySAL specification-test documentation](https://pysal.org/spreg/notebooks/9_specification_tests.html).

Do not choose SEM on the premise that omitting a true spatial response lag preserves
coefficient consistency. Ignoring an endogenous Wy generally creates endogeneity.
With a correctly specified conditional mean and exogenous X, spatially correlated errors
alone need not bias OLS coefficients, but conventional efficiency and standard errors
are affected. Omitting WX can also cause ordinary omitted-variable bias.
[PySAL model-specification experiments](https://pysal.org/spreg/notebooks/7_spatial_models.html).

Specific-to-general testing and general-to-specific restrictions are alternative workflows.
A broader model may reduce particular specification risks, but extra parameters can
weaken precision and identification. SDM is not immunity to omitted confounders or a
universal safe default. Prefer the simplest defensible model for the estimand; compare
restrictions, diagnostics, substantive plausibility and relevant predictive performance.

For spatially correlated errors, a defensible covariance estimator may sometimes suffice.
A cluster-robust estimator needs enough suitable clusters and assumptions about between-
cluster dependence; spatial HAC needs its own distance/kernel/bandwidth justification.
Changing standard errors does not repair an incorrect conditional mean.

## 3. Interpretation: the impacts framework

In SAR/SDM/SAC, beta is generally not the marginal response of y to X because the system
contains feedback. For a continuous covariate k in the linear SDM,

S_k = (I - rho W)^(-1) (beta_k I + theta_k W).

For SAR, theta_k is zero. The Neumann expansion is valid when its spectral-radius
condition holds, not merely because an inverse was successfully computed.

- **Average direct impact:** trace(S_k) / n, including feedback that returns to the
  originating unit.
- **Average total impact:** 1' S_k 1 / n.
- **Average indirect impact:** total minus direct, the average off-diagonal row sum.
  The global mean equals the mean off-diagonal column sum, although unit-specific
  "received" and "sent" responses differ, especially with directed W.

State whether the substantive question is a change in one location, a uniform change
everywhere, or a finite intervention. A scalar average can hide strong spatial
heterogeneity. For nonlinear models or discrete covariates, derive the appropriate
derivative or finite change rather than copying this linear formula.

Report intervals for the impacts themselves, using a justified delta method, parameter
simulation, bootstrap or posterior draws. An interval for beta alone is not an interval
for an indirect impact. Compare impacts over plausible W and model specifications.
These are conditional model responses; causal interpretation additionally needs an
identification argument.

For SLX, S_k = beta_k I + theta_k W: the average indirect impact equals theta_k only
under the relevant zero-diagonal, row-sum assumptions. With islands or other scaling,
compute it from W. SEM has no mean response spillover from X in its standard form, though
its shocks are spatially correlated. In SAR, the multiplier restricts the relationship
between own and neighbor responses; do not universally assert the same sign when negative
dependence or nonstandard weights are possible.

See the software authors' [spatial impacts documentation](https://r-spatial.github.io/spatialreg/reference/impacts.html)
for implemented definitions and uncertainty calculations; check the exact model/version used.

## 4. Spatial panels

Repeated observations can separate some unit heterogeneity from within-unit variation;
they do not automatically buy causal identification. Specify unit/time effects, treatment
timing, temporal dependence, missing panels and the source of identifying variation.
A Hausman test can diagnose some FE/RE differences; non-rejection does not prove the
random-effects orthogonality assumption.

A useful dynamic SDM notation is

y_t = tau y_(t-1) + rho W y_t + eta W y_(t-1) + X_t beta + W X_t theta + effects + epsilon_t.

Keep **identification**, **weak identification** and **finite-sample estimation bias**
separate. There is no blanket rule that including all of these terms makes the model
unidentified. Lee and Yu show identification under stated moment/likelihood conditions,
countering an earlier categorical restriction argument. Check the actual regressor
variation, rank/moment conditions, W, effects, initial conditions and estimator assumptions.
[Lee & Yu, Identification of Spatial Durbin Panel Models](https://doi.org/10.1002/jae.2450).

Dynamic fixed-effects estimation can have Nickell-type bias because transformation
correlates lagged outcomes with transformed errors. Bias-corrected likelihood or suitable
GMM may help under their assumptions; inspect instrument validity, proliferation and
sample dimensions. Removing a substantively necessary lag merely for parsimony can
misspecify the process.

**Stability is joint.** For time-invariant W, the transition matrix is

A = (I - rho W)^(-1) (tau I + eta W).

A stable dynamic system requires spectral_radius(A) < 1, alongside the within-period
inverse and other model conditions. Separate checks such as abs(tau) < 1 and abs(rho) < 1
are insufficient. Use the actual spectrum, especially for directed or changing networks.

Contemporaneous Wy_t represents within-period simultaneity. Wy_(t-1) encodes delayed
transmission and may better fit a diffusion mechanism, but lagging does not automatically
make a regressor exogenous when errors persist. Justify the time step and lag structure.

For a sustained change in a time-invariant covariate in a stable linear dynamic SDM,
the short-run impact matrix is S_k above, and the long-run matrix is

[(1 - tau) I - (rho + eta) W]^(-1) (beta_k I + theta_k W).

Report the horizon/intervention definition and uncertainty. A one-time shock instead has
a horizon-specific impulse response; do not present a sustained-change steady state as
the effect of a transient intervention.

## 5. Exploratory spatial data analysis

ESDA can describe patterns, generate hypotheses and diagnose models. Formal inference is
possible when the statistic, null, sampling design and multiplicity are specified; the
word "exploratory" is not a substitute for them.

- **Global Moran's I:** name W, transformation and the null. The usual randomization
  expectation is -1/(n-1), not exactly zero. Residual tests require a null appropriate to
  estimated residuals; freely permuting raw residuals may ignore the fitted design.
  Positive and negative dependence both matter. Non-rejection does not prove independence.
- **Local Moran:** distinguishes high-high/low-low associations and high-low/low-high
  spatial outliers relative to the chosen centering and W.
- **Getis-Ord Gi/Gi-star:** assesses local concentration of high/low values. Gi-star includes
  the focal observation under its definition; it is not a local-outlier test equivalent to
  local Moran. Use null expectations appropriate to rates, population and denominators.
- **Multiplicity:** hundreds of local tests generate a family. State whether maps are
  exploratory, show unadjusted versus adjusted results when useful, and use a justified
  FWER/FDR or joint randomization procedure. Conditional permutation for each location
  does not automatically correct across locations. Bonferroni/Holm remain valid under
  dependence for valid component p-values; ordinary BH needs its dependence conditions,
  while BY accommodates more general dependence. See [R p.adjust](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/p.adjust.html).
- **Heterogeneity:** changing relationships across space differ from dependence between
  observations. A clustered residual map may suggest omitted context or nonstationarity;
  it does not choose the appropriate remedy by itself.

Record permutations, random seed, attainable p-value resolution, one/two-sided choices,
and the tested family. Avoid presenting a thresholded hotspot map as certain boundaries.

## 6. Alternatives and complements

**Eigenvector spatial filtering (ESF).** A selected spatial basis can describe residual
structure in a regression/GLM. For Moran eigenvectors, document the symmetric/centered
operator, candidate eigenvalues and selection rule; directed W needs special treatment.
If negative autocorrelation is plausible, verify that negative-pattern candidates are
available. Do not infer software defaults without checking its version. A graph Laplacian's
nonnegative eigenvalues do not mean its eigenvectors cannot represent oscillating patterns.
Selection uncertainty and spatial confounding remain; decorrelated residuals alone do not
validate all inference. Changing W may change the entire basis.

**GWR / MGWR.** Local coefficient surfaces can describe nonstationarity; MGWR permits
covariate-specific bandwidths. Report kernel/bandwidth selection, local effective sample
size, collinearity, edge sensitivity and multiple local comparisons. Compare against
simpler global or regime models. Smooth surfaces and local t values do not identify
causal heterogeneity. A bandwidth is a fitted smoothing scale, not automatically the
true scale of a social process.

**Areal hierarchical models.** CAR/ICAR/BYM/BYM2 use a neighborhood graph for areal effects.
State likelihood, offsets/denominators, connected components, constraints, priors and
scaling. ICAR is intrinsic rather than an ordinary proper covariance model; islands and
disconnected components need deliberate treatment. BYM2 separates structured and
unstructured components with scaling that supports interpretation and prior calibration.
Its mixing parameter is a model-based variance allocation, not proof of a causal spatial
share. See [Riebler et al. on BYM2](https://doi.org/10.1177/0962280216660421).

**Continuous fields and SPDE.** The SPDE construction links Matérn fields and sparse
GMRF representations. Its finite-element mesh representation is an approximation;
mesh/domain sensitivity is part of validation. Check interior refinement, extension,
triangle quality and boundary conditions against the range and the scientific domain.
There is no universal minimum angle or one-range extension guaranteeing adequate accuracy.
[Lindgren, Rue & Lindström](https://doi.org/10.1111/j.1467-9868.2011.00777.x).

Areal and continuous-support models are not interchangeable without a measurement model:
a continuous field can support areal observations through explicit integration, and
point data can inform aggregates. Represent change of support rather than forbidding
such models or assigning every areal problem to CAR.

**INLA and priors.** INLA targets latent Gaussian model structures with approximation
conditions; it is not a generic solution to every large spatial problem. Inspect
approximation settings, sensitivity and relevant diagnostics. CPO/PIT can help evaluate
conditional predictive behavior, but approximations can fail and need checks/recomputation;
ordinary leave-one-out is not validation of transfer to new regions. PC priors encode
specified shrinkage toward a base model; they do not solve unmeasured confounding.
State units, hyperparameters and interpretable prior probabilities, and examine sensitivity.

**Kriging.** Specify mean, covariance/variogram, nugget, anisotropy and observation support.
The reported kriging variance may condition on estimated covariance parameters and omit
parameter/model uncertainty. Interpolation accuracy is a different claim from mechanism
or causal effect.

## 7. Spatial confounding

Separate statistical collinearity of a covariate with spatial basis functions from causal
confounding by unmeasured spatial variables. Adding a smooth/random effect may change both
precision and the meaning of the coefficient; omitting it may leave biased or inefficient
estimation under different data-generating processes.

Restricted spatial regression, Spatial+, basis restrictions and other approaches make
different assumptions. Do not present orthogonality to X or a particular prior as a
universal fix. Define the target effect, explain scale assumptions, show sensitivity to
the spatial term and measured confounders, and acknowledge what the data cannot identify.
For a primary treatment and its assumptions, see [Spatial+](https://doi.org/10.1111/rssb.12485).
State when the manuscript is estimating a spatially adjusted association rather than an
identified causal effect.

## 8. Spatial cross-validation

Choose the test setting to match deployment. New-region transfer typically requires
holding out regions or spatial blocks; interpolation among sampled neighbors may legitimately
use nearby training data. Buffering is useful when test locations should be separated,
but a universal buffer can evaluate a different task and discard needed information.
Use the empirical dependence range and scientific transport scale to justify candidate
blocks/buffers, rather than treating a noisy range estimate as a universal threshold.

Keep preprocessing and tuning inside training data; use nested selection when needed.
Archive or safely reconstruct fold assignment, temporal cutoff, seeds and baseline code.
Compare the model and a credible spatial/persistence/simple-model baseline on identical
test observations, metrics and information. Report uncertainty and performance variation
across regions, horizons and relevant subgroups. No split guarantees transfer under an
unobserved regime change.
[Roberts et al.](https://doi.org/10.1111/ecog.02881).

## 9. Reporting and specialist review

Return a compact specification record: estimand; support and time step; W/network
definition; mean/error/dynamic model; estimator and identification assumptions; diagnostics;
impacts with uncertainty; sensitivity; validation task; and limitations.

For a difficult specification, seek a specialist review of the actual assumptions and
implementation. Optional installed perspective skills may help generate questions, but
do not assume they exist or impersonate their named scholars. Published methods and
software documentation support technical claims; an imagined reviewer is not a citation.
