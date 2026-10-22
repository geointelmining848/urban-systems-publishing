# Stage 1 - Data and reproducibility

Plan an inspectable route from source data to every material claim. Establish what exists,
what can be shared, who controls access, and what is still undocumented. A reproducibility
plan is not authorization to upload data, create accounts, publish repositories or accept
new access terms; perform those actions only within the user's authorization.

## A geospatial provenance record

For each layer/table, retain source, version, retrieval date, permitted use, checksum where
feasible, geographic/time coverage, schema and transformations. Distinguish observed values
from estimates, modeled surfaces, imputed records and synthetic inputs.

- **CRS, datum and measurement:** record an EPSG code where one exists, otherwise a complete
  CRS/WKT definition, units, axis order and relevant transformation details. Planar distance
  or area calculations on longitude/latitude degrees are inappropriate. Geodesic algorithms
  on geographic coordinates can be valid; a projected CRS is not the only correct route.
  Use an appropriate metric/equal-area projection or ellipsoidal method for the quantity.
- **Geographic vintage:** name the exact boundary product and release, not merely "census
  tracts." Document splits, mergers, ID changes and any crosswalk/interpolation. Combining
  vintages can be defensible with an explicit alignment method and uncertainty; silently
  joining unmatched units is not.
- **Support and resolution:** record raster cell size, grid alignment, resampling method,
  areal units, network topology and temporal intervals. Explain change of support and
  aggregation weights. Fine display resolution does not create fine measurement resolution.
- **Join keys:** preserve stable IDs and leading zeros; test uniqueness, unmatched joins,
  duplicate geometries and coverage. Document geocoding match rate and error.
- **Weights/network:** retain W or reproducible construction code, row/column ID ordering,
  metric, contiguity/tolerance, k/bandwidth, normalization, direction, islands and edge policy.
  Sharing a matrix without its observation ordering is insufficient.
- **Cleaning and exclusion:** preserve the raw-to-analysis transformation record, inclusion
  rules, missingness handling, exposure windows, denominator definitions and manual changes.
  Record which observations are excluded from each reported result.

## Reproducible computation

Provide a runnable path from permissible input to tables/figures with entry commands,
software versions, dependencies/lockfile, seeds, parameters and expected outputs.
Record platform-sensitive geospatial libraries and coordinate databases where material.
Document nondeterminism and numerical tolerances rather than promising bitwise identity
when the implementation cannot deliver it.

For predictive work, retain fold assignments or safe reconstruction code, training/test
boundaries, tuning procedure, feature cutoff and baseline implementation. For survey work,
record weights, strata/PSU or replicate weights and the estimator. For simulation work,
record initialization, time step, stochastic replicate design and calibration inputs.

Test a clean run on permitted data or clearly labeled synthetic fixtures. Distinguish
"the code executed on a synthetic schema example" from "the published results reproduced."
A container can improve portability but does not archive external APIs, guarantee hardware
compatibility or confer data rights.

## Restricted geographies and health data

Assess the actual license, consent, ethics approval, data-use agreement and provider rules.
Individual coordinates, linked records and fine-area health tables can be identifying even
without names. Public availability does not automatically authorize republication or linkage.

Use the disclosure controls required for the dataset and release: controlled access,
aggregation, suppression with complementary suppression where necessary, or approved
masking/perturbation. There is no universally safe small-cell threshold or displacement
distance. These transformations affect spatial inference and should be documented.
Do not claim HIPAA/GDPR/IRB compliance from this skill; the responsible institution/provider
determines requirements and release approval.

When raw data cannot be shared:

1. Share permitted code, schema and a description of the processing route.
2. Provide a clearly labeled synthetic/example dataset if useful and safe. Synthetic
   does not automatically mean anonymous; avoid reproducing sensitive geography or records.
3. Give the actual access route, provider, eligibility and restrictions. State when
   independent access is limited or unavailable rather than promising it.
4. Obtain required disclosure review for outputs before release; report only approvals
   that actually occurred.

Synthetic inputs demonstrate pipeline mechanics, not reproducibility of the real estimates.
Separate public layers, restricted layers, code and derived outputs in the availability
statement so the scope of each access condition is clear.

## Preservation and repositories

Choose an archive with suitable access control, preservation, versioning and identifiers.
Zenodo, OSF, Dryad, Dataverse and ICPSR are candidates, not interchangeable defaults; verify
current services, limits, costs and suitability when recommending a deposit. A controlled
access archive may fit restricted microdata better than a general public repository.

A mutable GitHub branch is useful for development but is not a frozen research record.
Cite the exact commit/release and, when available and authorized, an archival DOI or other
persistent version identifier. Do not fabricate a DOI or claim a deposit is complete before
verifying it. Release only data/code the author has rights to distribute; preserve third-
party attribution and select licenses only with authority from the rights holder.

FAIR means findable, accessible under stated conditions, interoperable and reusable with
clear provenance/rights. It does not require every dataset to be open. Use publisher
requirements and the [FAIR principles](https://doi.org/10.1038/sdata.2016.18) as a framework,
not a guarantee that a deposit is reusable merely because it has a DOI.

## Recurring data-source checks

| Source | Reproducibility detail to resolve |
|---|---|
| Census / ACS | Product, period (1-year versus 5-year), geography vintage, universe, estimates and uncertainty. Overlapping multi-year releases are not independent annual observations. |
| LEHD / LODES | Version, year, job type, origin/destination definitions, geography and release-specific confidentiality methods. Do not label all noise infusion as differential privacy. |
| OpenStreetMap | Extract date, coverage, feature/tag selection and required attribution/license conditions. Missing mapped features need not mean absent real features. |
| GHSL, WorldPop, LandScan and other population surfaces | Product, release, resolution, reference year and modeling/disaggregation assumptions; these are not error-free ground truth. |
| Remote sensing | Sensor/product/collection, dates, QA/cloud mask, compositing, training labels, resolution and resampling. |
| Administrative data | Inclusion/coverage, operational definitions, linkage quality, dates and policy changes. |
| Public-health surveys | Release-specific design, weights, variance method, population coverage and comparability across waves; see [public-health.md](public-health.md). |

For LODES, consult the [Census product documentation](https://lehd.ces.census.gov/data/)
and the relevant release's technical notes. Historical OnTheMap documentation distinguishes
noise infusion for workplace totals from synthetic methods for residential locations; do
not substitute a generic privacy label for the actual procedure.
[Official methods overview](https://lehd.ces.census.gov/doc/learning_guide/LED_Lodes_Intro.pdf).

For ACS ratios/aggregations, use the product's uncertainty guidance and account for
covariance/overlap where material. A numerator and denominator from different populations,
periods or supports may not define the claimed rate. Where uncertainty cannot be propagated,
state the omission and its likely implications without inventing precision.

## Availability and disclosure deliverable

Provide a working statement covering:

- Data products and exact versions; public locations or restricted access routes.
- Code version, environment, commands and what was actually reproduced.
- Spatial metadata: support, CRS, geography vintage, IDs, crosswalks and W.
- Rights, consent/disclosure limitations and release status.
- Missing documentation or checks, each tied to the claim it affects.

Read the target's current author guide before asserting a mandatory repository, statement
heading or open-data rule. When access is unavailable, provide the draft and mark the
policy-dependent details for verification. Funding, competing interests and author
contributions must reflect actual information; CRediT roles describe contributions and
do not alone determine authorship. Do not invent declarations.
