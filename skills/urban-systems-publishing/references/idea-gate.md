# Stage 0 - Idea Gate and Triage

Use triage when the user wants to judge, position, or strengthen a study. Answer: what
claim can the evidence support, who needs the contribution, and what would make the work
ready for the intended venue? Give a candid judgment with a path forward, rather than an
acceptance prediction. If the user requests a narrow edit, complete that edit and flag any
claim problem affecting it; do not force the entire study through a gate first.

## Two useful axes, applied as hypotheses

Consider **reach x epistemic culture**:

- **Reach:** a focused contribution for specialists, a contribution to a wider disciplinary
  debate, or a result connecting several disciplines or policy communities.
- **Epistemic culture:** quantitative explanation, descriptive measurement, prediction,
  methodological development, interpretive/theoretical argument, or a mixture.

These are dimensions of the manuscript and its audience, not fixed ranks of journal
quality. Journals contain multiple article types and intellectual traditions. A quantitative
paper can advance urban theory; an interpretive paper can provide systematic empirical
evidence. Do not equate geography with qualitative work or regional science with causal
estimation. For example, Urban Studies asks for wider urban conceptual understanding while
welcoming empirical and theoretical contributions across social science; Annals includes a
Geographic Methods area. See the official scope links in [journal-profiles.md](journal-profiles.md).

## Establish the claim and its basis

Use information already supplied before asking questions. Ask for the smallest missing
piece that changes the judgment. Useful inputs are:

- The proposed central claim, its geographic/temporal scope, and whether it is descriptive,
  predictive, causal, methodological, interpretive, or theoretical.
- Data or empirical material, unit of observation, sampling/case-selection rationale,
  measurement, uncertainty, and the design supporting the inference.
- The closest competing explanations and prior contributions, including work outside the
  selected journals or the dominant language of publication.
- Intended readers, manuscript/article type, and practical constraints such as funding,
  deadlines, access requirements, and the author's preferred journal.

A missing causal identification strategy blocks a causal claim, not every quantitative
paper. A careful descriptive atlas, a measurement contribution, a validated prediction,
or a theoretically generative case can stand on its own terms. When results are not yet
available, draft a proposal, outline, or explicitly marked placeholders without inventing
numbers, citations, approvals, or completed analyses.

## Benchmark against relevant literature

Use a local corpus **if available** to find close precedents; otherwise use authorized
scholarly search, publisher pages, or the references supplied by the user. Do not require a
corpus build before useful mentoring. An optional query from the skill directory is:

```bash
python scripts/query_corpus.py "street network accessibility" --journal CEUS,EPB,Cities --sort recent -n 15
```

Read the relevant work, not just its title, before attributing a finding to it. Record the
search date, coverage, terms, and any abstract/full-text limitations. A missing keyword
match is not evidence of novelty or of journal exclusion. Use citation chains, synonyms,
regional terminology, and literature beyond this journal catalog before making a bounded
novelty statement. Never turn "not found in this search" into "first in the field."

Separate precedent roles:

- **Extension:** establishes what this study adds to an existing result or approach.
- **Alternative explanation:** makes a different account plausible and suggests a test or
  a limitation. Evaluate it; do not promise to eliminate all alternatives.
- **Context or boundary condition:** explains why the result may differ across places,
  populations, periods, or methods.

Same-place studies are not automatically rivals. They may study another outcome, scale,
or estimand. Compare claims before deciding how to use them.

## Evidence-led assessment

Discuss only dimensions that matter for this task; use supported judgments such as strong,
adequate, uncertain, or needs work, not a numeric quality score.

| Dimension | Questions that change the recommendation |
|---|---|
| Claim validity | Does the evidence support the logical form and scale of the claim? What is the most consequential unresolved threat? |
| Advance | What changes relative to the closest work: explanation, measurement, method, prediction, concept, or application? |
| Reach | Which readers can use the contribution, and what evidence supports transfer beyond the study setting? |
| Novelty | Is the comparison specific and current? Is a replication or contextual extension valuable even without priority? |
| Evidence depth | Are sampling, measurement, spatial dependence, MAUP, uncertainty, and identification addressed as appropriate to the claim? |
| Audience fit | Does the contribution engage the debate, practical problem, or technical standard the candidate venue addresses? |
| Reproducibility and ethics | Can the path from permissible data to claims be audited? Are restrictions and participant risks handled honestly? |

A new conceptual frame can broaden a contribution, but "paradigm shift" is not a target
that every manuscript should pursue. Do not add fashionable theory or policy language
that the evidence cannot sustain. Read [analysis-rigor.md](analysis-rigor.md) for design
issues and [spatial-methods.md](spatial-methods.md) for scale and specification.

## Verdict with a concrete next move

For a full triage request, use a verdict with an explanation and next action:

- **GO:** the supplied evidence supports moving to the requested writing or submission
  preparation stage. State what was checked, unresolved limits, and candidate fit. This
  does not mean acceptance is likely or guaranteed.
- **REFINE:** identify a fixable obstacle and an achievable change: narrow a causal claim,
  clarify the conceptual contribution, report uncertainty, test a credible spatial
  alternative, or improve literature positioning.
- **RECONSIDER:** explain why the current framing or target is a weak fit, then offer a
  better fit or a meaningful redesign. Avoid predicting a desk rejection or treating a
  journal as a consolation prize.

For example: "REFINE: the station-accessibility coefficient is an association under this
cross-sectional design. Report the spatial impacts and uncertainty, then choose whether
the paper's contribution is a measured urban pattern or a causal policy evaluation. Urban
Studies remains a possibility if the result advances a broader urban debate; a regional
science venue may fit a more technical contribution. Check recent precedents in each."

## Output shape

Scale the response to the user's request. A full assessment can use:

```text
Verdict and confidence: [GO / REFINE / RECONSIDER; scope of assessment]
Claim supported now: [one sentence; population, place, period, inference type]
Strengths: [specific evidence]
Most consequential gaps: [claim affected; why; feasible remedy]
Positioning: [verified precedents and their roles; search limitations]
Audience and candidate venues: [fit rationale, tradeoffs, current sources]
Next deliverable: [concrete revision, analysis plan, or package]
```

A technically strong study can have modest reach and still be worth publishing. The task
is to make its real contribution visible to the right readers, not to manufacture breadth.
