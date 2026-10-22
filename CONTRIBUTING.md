# Contributing

[简体中文](CONTRIBUTING.zh-CN.md)

Help make the skill useful for researchers and scholars writing urban and regional research manuscripts.
Suggestions may improve explanations, examples, scientific accuracy, language support or
the optional corpus tools. Support quantitative, qualitative and mixed-method work.

1. Describe the writing task and the difficulty a researcher encounters. Use a short,
   fictional example when possible.
2. Keep shared guidance in `SKILL.md` and detailed methods in the relevant references.
   Keep English and Chinese guides consistent.
3. Support scientific corrections with primary sources and journal requirements with
   current official guidance. Preserve scholarly citations and attribution.
4. Check that a suggested prompt produces useful writing feedback and explains important
   changes without inventing evidence or taking over the author's research decisions.
5. For code or package changes, install `requirements-dev.txt` and run
   `python -m unittest discover -s tests -v`. The tests use synthetic records and mocked
   requests; they do not require a literature download.

Never submit credentials, local account paths, chat history, identifiable geodata,
unpublished manuscripts, corpus dumps, or third-party excerpts without redistribution
rights. Use synthetic examples. The CI checks are a supplement to manual review.
Read [RIGHTS.md](RIGHTS.md) before proposing contributed material or a license change;
this repository currently does not provide an open-source license grant.
