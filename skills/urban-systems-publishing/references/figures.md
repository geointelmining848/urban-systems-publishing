# Stage 5 - Figures, maps and tables

Make the main finding understandable without hiding uncertainty, scale or design.
A figure is evidence and an argument; its caption must say what is observed or estimated
without upgrading association to causation. Use the user's requested output format and
available plotting tools. Do not invent data to make a convincing display.

## Plan the main display

State the question, estimand, unit, comparison and take-home message for each figure.
A coherent multi-panel figure can combine a map, design diagram and impact plot when
they jointly explain one argument; there is no rule that these must be separate figures.

Use clear units, legends, labels and panel references at the final viewing size.
Captions should identify data source/period, sample/support, transformations and interval
definitions. Show uncertainty and substantive magnitude; stars or a p-value alone do
not communicate the finding. An effect inferred from aggregate data must remain an
aggregate claim in the caption.

Axes need honest visual encoding. Bars generally need a meaningful zero baseline because
length carries magnitude; line/scatter/coefficient plots may use a restricted range if
clearly labeled and appropriate to the comparison. Log scales, broken axes, aspect ratio
and smoothing should be explicit. Do not impose a zero baseline that hides the relevant
variation, or truncate a bar axis to exaggerate it.

## Choropleths and thematic maps

- **Quantity and denominator:** distinguish counts, rates, density, standardized risk and
  estimates. Counts can be the relevant quantity, but do not describe them as per-person
  risk. Proportional symbols may suit counts better than a filled-area map.
- **Support:** state the geographic unit, boundary vintage, denominator period and any
  crosswalk. A smooth surface is not automatically more precise than the underlying data.
- **Classification:** explain quantiles, equal intervals, natural breaks or continuous
  scales. Quantiles can amplify tiny differences; natural breaks can prevent comparison
  across maps. Use common breaks/ranges for panels intended to be directly compared unless
  the difference is explicit. Choose legible, meaningful classes, not a fixed universal count.
- **Small populations:** show denominators and uncertainty, or accompany raw rates with a
  justified smoothed estimate. Explain the smoothing model and whether it borrows from
  nearby areas or a broader population. Smoothing can hide true extremes as well as reduce
  noise; do not label every extreme raw rate a spurious hotspot.
- **MAUP:** display sensitivity to a second plausible support when it informs the claim.
  If the pattern changes, discuss aggregation, composition and measurement as well as
  possible process scale. A stable map is useful evidence but does not eliminate MAUP.
- **Missingness and suppression:** use distinct symbols for missing, suppressed, zero and
  outside-scope observations. A blank or pale polygon must not silently mean all four.
- **Bivariate maps:** use only when the joint spatial pattern is central and the two-
  dimensional legend is readable. A small-multiple alternative is often easier to assess.
- **Cartograms:** they can emphasize population rather than land, but explain the distortion
  and retain geographic context when readers need it.

## Color and accessibility

Prefer perceptually ordered palettes for continuous quantities and distinct, interpretable
categories for nominal data. Rainbow/jet can create false visual boundaries; do not use it
as the default for continuous scientific fields. Avoid relying on red-versus-green alone.
Consider viridis/cividis, appropriate scientific color maps or accessible ColorBrewer
schemes, then inspect the actual rendered figure.
[Crameri, Shephard & Heron on scientific colour maps](https://doi.org/10.1038/s41467-020-19160-7).

Use sequential color for ordered magnitude and diverging color around a justified midpoint
such as zero change or a null ratio. Align the normalization to that reference; a centered
palette is not meaningful if the center has no substantive interpretation. Qualitative
classes should not imply an artificial ordering.

Check grayscale, contrast and common color-vision differences. Reinforce critical
distinctions with labels, shapes, line styles or restrained hatching. Include useful
alt text or an accessible description where supported. Redundant patterns on every
polygon can make a map less legible, so target the important comparisons.

## Uncertainty and local inference

Select an uncertainty display that answers the decision, not just the available software:

- Side-by-side estimate and standard-error/interval-width maps often make uncertainty clear.
- Bayesian posterior SD/probabilities, kriging prediction variance and frequentist GWR
  standard errors are different objects. Label the one actually computed; do not call all
  of them posterior uncertainty. State which parameter/measurement uncertainties are omitted.
- Exceedance-probability maps can answer a threshold question, but the threshold and model
  assumptions must be explicit. Pointwise probabilities do not control a joint spatial
  excursion claim.
- Bivariate color/texture or hatching can summarize precision if the legend is readable.
  Explain whether hatching denotes uncertainty, missingness or an inferential threshold.
- For local Moran/Gi-star maps, state W, null, permutations, sidedness and tested family,
  including multiplicity treatment. Distinguish unadjusted exploratory patterns from
  adjusted results. "Not significant" does not mean no association or no public-health risk.

See [spatial-methods.md](spatial-methods.md) for local-test and impact interpretation.
Never fabricate error bars when uncertainty was not estimated; report the absence.

## Projection, geography and provenance

Choose the display projection to suit region and purpose, and distinguish it from the
method used to compute area/distance. An equal-area projection is useful for area
comparisons; it is not mandatory for every rate map. A projection affects perceived area,
while an already correctly calculated rate is not changed merely by reprojection.
Use valid planar/geodesic measurement methods and document CRS/datum and units.

Add scale and orientation information when meaningful. A scale bar can vary across a
global map; a north arrow can be misleading under some projections and is not always
necessary. Use graticules or local scale information where they communicate more clearly.
Include a locator/inset if it helps readers place the study.

Attribute basemaps and source layers according to their actual licenses, include dates
and boundary vintages, and explain disputed/administrative boundary conventions neutrally.
Maps can reveal sensitive locations: apply the approved disclosure controls from
[data-and-reproducibility.md](data-and-reproducibility.md) before public export.

## Network and flow maps

Define nodes, direction, edge weights, period, missing links and what was filtered.
Thresholding or showing top-k flows, aggregation, transparency and bundling can improve
readability, but can also hide small or peripheral flows. State the threshold and check
whether the substantive conclusion depends on it. Use an origin-destination matrix,
small multiples or ranked flow plot when geometry obscures the comparison. Do not let
edge bundling suggest an actual route when it represents only an abstract connection.

## Analytical plots and tables

- **Coefficient/forest plots:** show units, reference categories, uncertainty and sample.
  For SAR/SDM/SAC substantive changes, plot direct/indirect/total impacts as appropriate;
  raw coefficients still have model meanings but are not generally marginal responses.
- **Event studies:** display timing, reference period, cohort/comparison definition,
  estimates and interval method. Pre-period estimates are diagnostics, not proof of
  parallel counterfactual trends. Address simultaneous bands/multiplicity when relevant.
- **Predictive explanations:** partial dependence, ALE and SHAP describe model behavior
  under assumptions; they are not automatically causal effects. Correlated predictors,
  extrapolated combinations and data leakage need care.
- **Diagnostic plots:** show relevant residual/spatial checks, calibration and held-out
  performance; do not demand an OLS LM/Moran test for every model class indiscriminately.
- **Descriptive tables:** define unit/support, N, period, sources, missingness, and weights.
  Distinguish sample counts from weighted population estimates.
- **Model tables:** report estimator, specification, W/network, uncertainty, comparable
  fit measures and diagnostics suited to that model. AIC comparisons require compatible
  likelihoods/data and are not causal evidence.
- **Large tables:** supply permitted machine-readable data with metadata rather than
  forcing a long PDF appendix to serve as the data archive.

## Publisher specifications and production

Verify current article-type requirements before quoting dimensions, resolution, fonts,
color space, file format, accessibility or figure-count limits. Distinguish actual hard
limits from examples and preferences. Vector output often suits line art; raster output
needs enough resolution at the final display size. Inspect legibility and exported files,
not only the plotting code.

Use available libraries or document tools; optional visualization/geospatial skills are
accelerants, not prerequisites. Preserve data and scripts, inspect final renders for
cropping/overlap, and confirm captions agree with the analysis. Report which figures were
generated and visually checked, which remain proposed, and any source/uncertainty gaps.
