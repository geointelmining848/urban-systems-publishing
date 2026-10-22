# Contributing

[简体中文](CONTRIBUTING.zh-CN.md)

Keep the skill focused on publication mentoring for the researcher's own urban/regional
study. Preserve analytical, qualitative, and mixed-method work; do not equate a venue's
reputation with a universal method or a causal requirement for every contribution.

1. Describe a concrete failure or missing use case, including the intended output.
2. Make the smallest useful correction. Keep shared guidance in `SKILL.md`; put detailed
   methods in relevant references. Update English and Chinese user documentation together.
3. Support disputed scientific claims with primary sources. Date journal-policy checks
   and link official guidance. Do not fabricate citations, results, or current limits.
4. Add or adapt a synthetic scenario in `skills/urban-systems-publishing/evals/evals.json`.
   Include expected behavior and a failure condition, not just a wording match.
5. Run `python -m unittest discover -s tests -v` after installing `requirements-dev.txt`.
   For changed instructions, also try realistic prompts with and without the revision.
   Record client/model, prompts, sources available, outputs, and limitations; do not label
   static checks as successful model behavior or infer trigger accuracy from forced use.

Never submit credentials, local account paths, chat history, identifiable geodata,
unpublished manuscripts, corpus dumps, or third-party excerpts without redistribution
rights. Use synthetic examples. The CI checks are a supplement to manual review.
Read [RIGHTS.md](RIGHTS.md) before proposing contributed material or a license change;
this repository currently does not provide an open-source license grant.
