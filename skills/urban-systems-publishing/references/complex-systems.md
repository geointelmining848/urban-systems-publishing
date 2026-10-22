# Complex systems and urban analytics: when the paper is a model

Load this for agent-based models (ABM), system dynamics (SD), cellular automata (CA),
microsimulation, urban scaling, network models, and empirical dynamic modeling (EDM).
Retain the publication question: what claim does the model support, for what purpose,
and what evidence discriminates it from plausible alternatives?

Contents: [validation](#validation-is-purpose-specific), [structural checks](#structural-checks),
[ABM](#agent-based-models), [system dynamics](#system-dynamics),
[scaling](#urban-science-and-scaling), [land change and networks](#land-change-and-network-models),
[EDM and CCM](#nonlinear-dynamics-edm-and-convergent-cross-mapping),
[framing](#framing-and-deliverable).

## Validation is purpose-specific

Separate four tasks rather than using "validated" as a blanket endorsement:

- **Verification:** does the implementation match the equations/rules? Check units,
  indexing, numerical integration, conservation where applicable, and degenerate cases.
- **Structural evaluation:** are mechanisms, assumptions and parameters defensible from
  theory, independent observations or institutional evidence?
- **Calibration:** what data/objective were used to choose parameters or model structure?
- **Predictive/behavioral validation:** what genuinely independent information tests the
  claimed behavior, forecast, transfer, or policy comparison?

A good in-sample fit is not proof of the mechanism. It is also not inherently evidence
that the model learned less. Many structures can fit the same observations; test
discriminating predictions, identifiability and sensitivity. Name data reused in model
selection, calibration and validation, including informal tuning after seeing a test set.

Hold out a period, region or regime when that matches the claim. For prospective
forecasts, train only on information available at the forecast origin and evaluate
successive future horizons. Ordinary leave-one-time-point-out can train on future data;
it is not equivalent to a forward forecast test. Compare persistence, seasonal and
credible simple-model baselines on the same observations and metrics. Correlation alone
does not assess bias, calibration or absolute error.

When no independent data exist, describe structural checks and compatibility with
observed patterns, disclose the reuse, and limit external-validity claims. Pattern-oriented
modeling can constrain a model with multiple observations, but patterns used for tuning
are still calibration evidence. Scenario usefulness and conceptual insight can be valid
contributions without a claim of accurate future prediction.

## Structural checks

Adapt these checks to the model's intended domain; do not apply every SD criterion as a
universal gate for an empirical regression or predictive classifier.

- **Boundary and extreme conditions:** test physically or socially meaningful limits,
  empty populations, zero exposure and numerical edges. Specify the valid input range.
  Failure under impossible extrapolation does not by itself invalidate an in-domain
  approximation; an unexplained failure inside its stated domain matters.
- **Dimensions, accounting and constraints:** check equation units, stocks versus flows,
  identities, allowed states and time steps. A population cannot be negative; a financial
  net stock may legitimately be. Apply conservation only to quantities actually conserved.
- **Behavior reproduction:** evaluate the dynamics relevant to the claim, such as
  oscillation, delay, segregation or saturation, in addition to pointwise fit.
- **Endogenous versus driven behavior:** holding external inputs fixed can expose feedback
  structure, but disappearance of a response does not mean the model explains nothing.
  Weather, migration, policy shocks and other external drivers can be real causes.
  State which mechanisms are endogenous, which are inputs, and why the boundary is useful.
- **Parameter and structural sensitivity:** vary plausible parameters, initial conditions,
  topology, rules and assumptions. Distinguish parameter uncertainty, stochastic
  variability and model uncertainty. Show where conclusions change instead of hiding
  unfavorable settings.

Choose a calibration loss aligned with the use case and observation process. Do not add
unjustified drivers merely to track history; equally, do not prohibit measured exogenous
drivers simply because they improve prediction.

## Agent-based models

- **ODD:** document Overview, Design concepts and Details, including entities, state
  variables, scheduling, initialization, inputs and submodels. Use the current applicable
  ODD guidance; it supports reproducibility, not proof of realism.
  [Grimm et al., updated ODD protocol](https://doi.org/10.18564/jasss.4259).
- **Sensitivity:** one-factor-at-a-time sweeps can miss interactions. Choose a feasible
  global design (for example Morris screening, Latin hypercube sampling, or variance-based
  analysis), respecting parameter dependence and simulation budget. Report sampling
  distributions and convergence, not just the method's name.
- **Stochastic runs:** for stochastic models, report distributions across seeds and
  relevant initial conditions and justify enough replicates for the reported precision.
  Deterministic ABMs do not need artificial seed sweeps; they still need sensitivity.
- **Emergence:** check topology, boundary conditions, synchronous/asynchronous scheduling,
  rounding and numerical resolution. A topology-dependent pattern may be substantive or
  an implementation artifact; diagnose which before claiming a universal mechanism.
- **Multiple patterns:** use different scales and behaviors to constrain the model, record
  their dependence and data reuse, and reserve some evidence for evaluation when possible.
- **Reproducibility:** release permitted code, rules, parameter ranges, environment,
  seed protocol and runnable synthetic inputs. Do not expose sensitive individual agents.

## System dynamics

Document the stock-flow structure, equations, units, delays, feedback polarity, parameter
sources and simulation time step. Test numerical stability and behavior under reasonable
alternative time steps. Explain model boundary and endogenous versus exogenous drivers.

Policy resistance, adaptation and unintended feedback may be the insight, but they are not
mandatory conclusions. A model may instead explain successful adjustment or a threshold.
Compare policy scenarios under explicit assumptions; separate scenario uncertainty from
estimated parameter uncertainty and from sampling uncertainty.

Conditional forecasts are permissible when supported by validation and calibrated
uncertainty. Do not turn systems humility into a categorical ban on prediction. Avoid false
precision, especially over long horizons or structural change; show which assumptions drive
the result and where the model was not tested.

## Urban science and scaling

Distinguish three different questions:

1. **A distributional tail** such as city sizes or network degrees: choose the continuous
   or discrete model, estimate the lower-tail cutoff when appropriate, and compare a
   power law against plausible alternatives. Use likelihood/goodness-of-fit procedures
   appropriate to the data rather than judging a straight log-log plot.
   [Clauset, Shalizi & Newman](https://doi.org/10.1137/070710111).
2. **An allometric relationship** between population and an urban quantity: specify the
   conditional mean, error scale, heteroskedasticity, retransformation, repeated-city
   dependence and influential observations. A log-log regression can be appropriate
   under its assumptions; the power-law-distribution critique does not automatically
   prohibit it. Test nonlinear alternatives and uncertainty in the exponent.
3. **Rank-size or fractal descriptions:** document the rank/sample definition or box-count
   scales, fitting range and finite-size/resolution effects. A descriptive fit is not a
   universal law.

City definition is load-bearing: administrative boundaries, built-up areas and functional
labor markets change populations and measured outputs. Examine plausible definitions,
spatial dependence, sampling coverage and temporal stability. Do not infer an individual
mechanism or a policy effect solely from a cross-city exponent. A robust regularity may
suggest a theory, but multiple mechanisms can reproduce it.

## Land-change and network models

**Land-change validation.** Report the transition period and information cutoff, calibration
data, target map and accuracy of the reference data. A model that predicts no change can
have high overall accuracy when change is rare. Compare against persistence using the
same change-sensitive metrics: hits, misses, false alarms, figure of merit, or another
justified measure; show quantity and allocation errors where relevant.

Keep common spatial support and masks across models and baselines. A fitted transition
tested on the same transition is calibration, not future validation. Separate uncertainty
from land-cover labels, predictors, model fitting and future scenario inputs.

For ML classification:

- Match spatial blocks/buffers to the deployment task; neighboring training pixels may
  be legitimate for interpolation but create optimism for distant transfer.
- Keep preprocessing and tuning within training data and preserve the temporal cutoff.
- Report precision-recall behavior, prevalence, operating threshold and confusion matrix
  for a rare change class. ROC-AUC can supplement these; it need not be forbidden.
  Use the same metric implementation for model and baseline. A deterministic no-change
  baseline has no useful ranking score; compare its decision outcomes rather than inventing
  a favorable PR curve.
- Compare with credible simple models using the same features/information and test set.
  If the complex model does not improve the chosen target, report that finding honestly.
- Release safe fold identifiers or code to reconstruct them, seeds, environment, cutoff,
  preprocessing and baseline implementation.

**Networks.** State nodes, edge meaning, direction, weights, boundary, period and missingness.
Degree-preserving or configuration-model nulls can test a specified structural claim; they
are not mandatory for every descriptive statistic. Preserve the properties the null needs
(distance, degree, temporal availability, or constraints). A null that permits impossible
long-distance ties can exaggerate evidence of spatial organization. Network association
does not alone identify contagion versus homophily or common exposure.

## Nonlinear dynamics, EDM and convergent cross mapping

EDM uses reconstructed state spaces for prediction and dynamical analysis. Choose embedding,
lag, library, forecast horizon, exclusion window and sampling protocol deliberately. Do not
silently treat a cross-sectional ordering of places as a time series. Report stationarity,
sampling interval, missingness, measurement/process noise and plausible external drivers.

**S-map diagnostics.** Out-of-sample improvement at nonzero localization can support
state-dependent predictability. An optimum near zero is consistent with a global linear
approximation at the available resolution; it does not prove a linear-stochastic system,
and it is not a universal prerequisite for applying CCM.
[EDM authors' algorithms documentation](https://sugiharalab.github.io/EDM_Documentation/algorithms_in_depth/).

**CCM interpretation.** Under its dynamical/embedding assumptions, an effect variable's
reconstructed state can carry information about its driver. State the direction carefully:
cross-mapping X from the manifold reconstructed from Y is evidence relevant to X driving Y,
not automatically the reverse. Check software column/target conventions explicitly.

- Evaluate cross-map skill over library size with repeated library sampling and uncertainty.
  Finite-sample curves need not rise monotonically, and a visible plateau is not a universal
  binary requirement. Increasing skill alone is insufficient to prove causal direction.
- Examine lagged cross-map behavior, temporal exclusion, embedding sensitivity, synchrony,
  common drivers and seasonal structure. Use null simulations/surrogates designed for the
  specific hypothesis; phase-randomized or twin surrogates preserve different properties.
  Do not claim they all preserve shared seasonality or remove every common-driver bias.
- Report limitations from short series, process noise, observation noise, nonstationarity,
  aggregation and sampling interval. There is no universal 20 dB reliability threshold.
  Weak/nonconvergent skill can reflect limited information rather than absence of coupling.
- Avoid a blanket claim that Granger methods, VAR or transfer entropy fail in all nonlinear
  systems. Methods target different notions of predictive dependence and rely on different
  assumptions; nonlinear/conditional variants exist. Compare methods and simulated systems
  representative of the intended use rather than declaring a universal winner.

CCM is evidence under model assumptions, not a substitute for experimental intervention
or a design-based causal estimate of a policy effect. The literature contains substantive
debate about seasonal forcing and causal criteria; present that uncertainty.
See [Cobey & Baskerville](https://doi.org/10.1371/journal.pone.0169050) and the
[response by Sugihara, Deyle & Ye](https://doi.org/10.1073/pnas.1700998114).
For reproducible settings, consult the authors' [CCM API documentation](https://sugiharalab.github.io/EDM_Documentation/ccm_/).

## Framing and deliverable

Name the contribution: methodological improvement, substantive urban/regional insight,
useful scenario comparison, a documented empirical regularity, or reusable research software.
These can overlap; the choice is not a forced methods-versus-substance binary.

A methods paper needs evidence of performance, scope and limitations; a substantive paper
needs evidence that the modeled mechanism informs its claim. A software paper can be useful
without claiming a newly discovered social law. Use journal profiles as starting hypotheses,
then verify current scope and comparable papers when tools are available.

Return a short record of verification, structural evidence, calibration data, independent
validation (or its absence), sensitivity, uncertainty, baseline comparison, reproducibility,
and the strongest defensible claim. Mark proposed analyses as proposed. Optional modeling
skills may help if installed; none is required to apply this guidance.
