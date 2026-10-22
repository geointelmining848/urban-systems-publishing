# Urban and Regional Manuscript Writing

[简体中文](README.zh-CN.md) · [Install](docs/installation.md) · [Writing workflows](docs/manuscript-workflows.md) · [Contributing](CONTRIBUTING.md)

A manuscript-writing skill for researchers and scholars working on urban and regional
research. Use it with Codex, Claude Code and other compatible agent environments to turn
your research question, evidence and notes into a coherent paper, improve sections,
check spatial reasoning, identify suitable readers and journals, and prepare responses
to reviewers. It explains consequential suggestions so you can make informed decisions.

It supports quantitative, qualitative and mixed-method studies in urban/regional economics,
planning, transport, population/environmental health, and urban complex systems.

The same [skill folder](skills/urban-systems-publishing/SKILL.md) can be used across compatible clients.
Instructions and references work without Python, API keys, or a downloaded corpus.
Python is needed only for the optional corpus helpers.

## Install

Follow the [installation and compatibility guide](docs/installation.md) for documented
local-directory and UI import methods. It covers Codex, Claude Code, WorkBuddy,
Qwen Work, Doubao Work, Pi, DeepSeek Harness (`dsh`), Gemini CLI, Antigravity,
Cursor, Copilot, OpenCode and other environments, with dated official sources.
It distinguishes native support, manual adaptation and unverified details.

Install the complete `skills/urban-systems-publishing/` folder. Compare and back up any
existing installation first. The guide assumes you already have access to your chosen
client. Core writing guidance needs no Python or literature API key.

## Use

In Codex, invoke `$urban-systems-publishing`; in Claude Code, invoke
`/urban-systems-publishing`, or ask for a matching task. Automatic selection depends on
the client and model; other clients use the invocation in the installation guide.
The skill responds in your language; specify a different language
for the manuscript if needed.

Examples:

- “Review my claim that transit expansion caused rent increases. I have a cross-sectional
  spatial Durbin model, no intervention design, and tract-level data.”
- “Help position my interview-based study of informal housing governance. Preserve the
  interpretive contribution and recommend what evidence I should check for journal fit.”
- “Discuss the revisions in Chinese, but draft the abstract in English. Use placeholders
  for results I have not supplied.”
- “Check whether my urban growth model's random pixel split really validates forecasting
  into a later decade, then help revise the validation paragraph.”

Supply the question, design, spatial/temporal units, main evidence, desired output, and
target journal if known. Omit confidential identifiers. Start with the part you need:
an outline, one paragraph, an abstract, a figure caption, or a response to a reviewer.
See the [step-by-step writing workflows](docs/manuscript-workflows.md) for prompts and
examples, including discussion in one language and manuscript text in another.

Check every factual claim and reference, and retain responsibility for your manuscript.
Follow your institution and journal's rules on authorship and AI use.
When results are missing, the skill uses labeled placeholders instead of inventing them.

## Optional corpus tools

No literature corpus or publisher abstracts are distributed. Local metadata can help find
precedents; it cannot establish novelty, acceptance probability, or a journal's current
requirements. See [corpus setup and limitations](skills/urban-systems-publishing/references/corpus-tools.md).
Do not upload confidential manuscripts or research data to build or query a corpus.

## Rights

See [rights and scholarly sources](RIGHTS.md) for repository permissions and third-party
materials. No open-source license grant is specified.
