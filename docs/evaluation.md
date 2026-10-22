# Evaluation and release evidence

Review date: 2026-10-22. This is a qualitative audit with software tests and a small set
of model smoke tests, not a numeric skill-quality score or a benchmark of publication success.

## Source comparison and strengths

The installed Codex and Claude variants on Windows and active WSL were identical across
all 18 substantive files. Consequently, the same findings apply to both variants;
there was no evidence that one client's copy was newer or stronger.
[Provenance](provenance.md) records the comparison and canonical-source choice.

The original skill had a useful, distinctive purpose: candid publication mentoring for
urban/regional, spatial, health and complex-systems research. Its strongest features were
the audience/reach and epistemic-culture lenses, detailed reference modules, early scrutiny
of claim form, MAUP and ecological inference, impact interpretation, simulation validation,
and concrete drafting/reviewer-response workflows. It already warned that corpus absence
does not establish novelty and that restricted data cannot simply be made public.

## Meaningful gaps and changes

| Area | Original issue and example | Revision |
|---|---|---|
| Spatial model reasoning | Reversed the consistency implications of omitting a spatial response lag versus spatial-error dependence. | Separates endogenous mean misspecification from residual covariance; states exogeneity and asymptotic assumptions rather than promising consistency automatically. |
| Multiple testing | Treated dependence as invalidating Bonferroni. | Explains valid marginal p-values and family-wise control under arbitrary dependence; distinguishes FDR procedures and permutation validity. |
| Advanced spatial methods | Overstated dynamic SDM non-identification and denied the SPDE approximation. | Replaced universal claims with model-specific identification, approximation, and uncertainty conditions and primary references. |
| Nonlinear dynamics | Required positive S-map localization, strictly monotonic CCM convergence/plateau and a universal 20 dB threshold; declared competing methods generally inapplicable. | Treats these as diagnostics with finite-sample and dynamical assumptions; covers forcing, synchrony, lag, noise and methodological disagreement without causal proof claims. |
| Scale and health inference | Could treat contextual area exposure with individual outcomes as automatically ecological; some generalizations overstated standard-error inflation. | Separates contextual effects from ecological inference, emphasizes process/support, selection, denominators, temporal alignment and model-dependent uncertainty. |
| Systems and prediction | Strong validation instincts mixed with universal rules. | Retains structural/calibration/validation separation and persistence baselines; matches spatial/temporal holdouts to deployment and avoids pretending a fit statistic validates a policy effect. |
| Journal fit | Categorical stereotypes and rejection predictions; empirical work was sometimes equated with an inadequate conceptual contribution. | Keeps audience/culture as hypotheses; permits quantitative theory, description, measurement, prediction, qualitative and formal-theory contributions. |
| Journal policies | Claimed Nature-family titles were OA-only; inconsistent enquiry rules and stale numerical caps. | Removes obsolete limits and checks exact current article-type policies, with dated official-source examples. |
| Evidence quality | Claimed near-full abstract coverage while its own table showed much lower coverage for several Nature titles; treated private corpus norms as live evidence. | Removes the unsupported current-norms presentation; records search coverage, metadata versus full text, citation verification and unknowns. |
| Triggers and workflow | Broad precedence over other writing skills, mandatory corpus use, sequential gating and user-specific persona assumptions. | Concise task-specific description, narrow-task completion, optional corpus and companion tools, no assumed identity, user-language responses. |
| Corpus scripts | Embedded personal contact address; import-time writes; capped pulls marked done; failed pulls could still appear successful; multi-journal norms used only one tag. | Explicit bounded build, external storage, existing-key-only access, truthful partial/failure status, hashes/provenance, cache checks, multiple-tag norms and synthetic tests. |
| Public packaging | Local corpus, logs and private dependencies were mixed into an installed skill directory; no multilingual installation/contribution guide. | Clean scoped history, public-safe file selection, one shared client package, English/Chinese guides and CI. No new license grant is invented. |

Relevant evidence is linked in the revised reference modules. Examples include the
[PySAL specification experiments](https://pysal.org/spreg/notebooks/7_spatial_models.html),
[R multiple-testing documentation](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/p.adjust.html),
[Urban Studies scope](https://www.urbanstudiesjournal.com/about/), and
[Nature Sustainability publishing options](https://www.nature.com/natsustain/submission-guidelines/publishing-options).
These support particular corrections; they do not validate every instruction in the skill.

## Software and structural checks

The original and revised entrypoints both passed the local skill-creator frontmatter
validator. That check cannot detect the scientific problems above.

The repository's 21 unit/structural tests cover:

- Metadata consistency, routed references, local Markdown links, scenario integrity,
  Unicode, account-path/secret patterns and excluded corpus payloads.
- No network or writes for help/dry runs; invalid tags/dates/missing keys; bounded topic
  filters; credential redaction; correct cursor encoding; cache mismatch/tamper handling.
- Partial caps, repeated/inconsistent pages, failed fetches and legacy completion markers.
- Unicode and nullable metadata, literal AND/OR/phrase search, explicit filters,
  multiple-journal norms and legacy quality-flag handling.

Local checks use Windows Python 3.14 with pandas 3.0.0 and pyarrow 23.0.0. The CI workflow
runs the suite on Windows and Ubuntu with Python 3.12. See the repository's Actions run
for the exact release commit; the workflow definition alone is not a claim that CI passed.
All corpus tests use synthetic records and mocked requests. No live OpenAlex harvest ran.

## Actual model behavior versus defined scenarios

[evals.json](../skills/urban-systems-publishing/evals/evals.json) contains 18 synthetic
scenarios: positive tasks, adjacent negative triggers, and edge cases. They are test
definitions, not 18 completed model runs. Expected behavior and failure conditions are
written for human review rather than matching a few keywords.

Independent Codex subagents in this authoring session performed these forced-invocation
smoke tests with no browser, corpus, or empirical data. They received a task and a skill
path, without the expected answer or prior audit conclusions; the parent inspected the
saved outputs. The exact underlying model build was not exposed in the run record.

| Scenario | Version exercised | Observed behavior |
|---|---|---|
| Spatial-error OLS and dependent local tests (case 9) | Original and revised, separate runs | Both corrected the two claims, supplied a methods paragraph, explained exogeneity/consistency and valid p-values, and disclosed that no diagnostics ran. The original run overcame contradictory reference guidance, so this case does not demonstrate an observed performance improvement. |
| Short-series CCM and asserted universal prerequisites (case 8) | Revised | Rejected universal theta/plateau/20 dB requirements, qualified causal interpretation, supplied a cautious paragraph and marked all diagnostics as proposed. |
| Two Chinese suggestions plus one English sentence (case 10) | Revised | Respected the narrow qualitative-edit task and avoided journal routing or invented estimates. Unicode code-point inspection confirmed two Chinese sentences and the English revision; a terminal display issue did not affect the saved UTF-8 artifact. |

Raw local test artifacts remain outside the public repository. No private research data
or previous conversation histories are published. These small, forced-use tests do not
measure automatic trigger accuracy, repeatability, superiority across models, or behavior
inside a separately launched Claude client. No Claude-model behavioral test was run.
The remaining scenarios have not been behaviorally executed in this release.

## Remaining limitations

The skill can improve questions and drafts, but cannot certify study validity or predict
editorial decisions. All 45 journal policies were not individually reverified. The Annals
official listing was visible while its full page returned HTTP 403; that limit is recorded
in the profiles. Current requirements must still be checked when used. OpenAlex API
documentation was inspected, but real pagination/authentication was not exercised.
Automated publication scans complement manual review; they cannot prove the absence of
every possible secret or rights issue. No source license was present, and none was added.

## 中文摘要

四份 Codex/Claude 源文件完全一致，因此原始优点与问题相同。保留了研究发表辅导、空间优先审查、
读者与学术传统匹配的核心思路，修正了空间误差模型、Bonferroni、动态空间模型、SPDE 与 CCM 等
实质性问题，并消除了过时投稿政策、私人语料必需性和固定流程的假设。

仓库包含 21 项代码/结构测试与 18 个合成场景定义；两者不能混为模型表现。实际运行了三个修改后
场景，以及一个原始版本对照。原始与修改后版本都答对了空间推断场景，不能据此声称普遍性能提升。
尚未测试 Claude 模型、自动触发准确率或真实 API 采集，也没有逐一核实全部 45 本期刊的当前规则。
