# Urban and Regional Manuscript Writing

[简体中文](README.zh-CN.md) · [Writing workflows](docs/manuscript-workflows.md) · [Contributing](CONTRIBUTING.md)

A manuscript-writing skill for students working on urban and regional research in Codex
or Claude Code. Use it to turn your research question, evidence and notes into a coherent
paper, improve sections, check spatial reasoning, identify suitable readers and journals,
and prepare responses to reviewers. It explains consequential suggestions so you can
make informed writing and research decisions.

It supports quantitative, qualitative and mixed-method studies in urban/regional economics,
planning, transport, population/environmental health, and urban complex systems.

The same [skill folder](skills/urban-systems-publishing/SKILL.md) serves both clients.
Instructions and references work without Python, API keys, or a downloaded corpus.
Python is needed only for the optional corpus helpers.

## Install

Clone this repository, inspect the files, then copy **the whole skill folder**, including
`references/`, `scripts/`, and `agents/`. Install only one copy per client/scope to avoid
ambiguous discovery. If a destination already exists, compare and back it up outside the
client's skills directory before replacing it; the examples deliberately refuse overwrite.

```sh
git clone https://github.com/geointelmining848/urban-systems-publishing.git
cd urban-systems-publishing
```

Linux, macOS, or WSL, for Codex:

```sh
target="$HOME/.agents/skills/urban-systems-publishing"
if [ -e "$target" ]; then
  printf '%s\n' 'Already installed: compare and back up before replacing.'
else
  mkdir -p "$HOME/.agents/skills"
  cp -R skills/urban-systems-publishing "$target"
fi
```

For Claude Code, use `$HOME/.claude/skills` in both paths above. For project-scoped
installation use `.agents/skills` (Codex) or `.claude/skills` (Claude Code) under the
project root. WSL and Windows have separate home directories; install in the environment
where your client runs.

Windows PowerShell, for Codex:

```powershell
$skillRoot = Join-Path $env:USERPROFILE '.agents\skills'
$target = Join-Path $skillRoot 'urban-systems-publishing'
if (Test-Path -LiteralPath $target) { throw 'Already installed: compare and back up first.' }
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
Copy-Item -LiteralPath '.\skills\urban-systems-publishing' -Destination $target -Recurse
```

For Claude Code, change `.agents\skills` to `.claude\skills`.
Reopen the client/session and confirm that the skill appears. For client-specific setup,
consult [Codex skill discovery](https://learn.chatgpt.com/docs/build-skills) and
[Claude Code skills](https://code.claude.com/docs/en/skills).

## Use

In Codex, invoke `$urban-systems-publishing`; in Claude Code, invoke
`/urban-systems-publishing`, or ask for a matching task. Automatic selection depends on
the client and model. The skill responds in your language; specify a different language
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
Follow your course, supervisor, institution and journal's rules on authorship and AI use.
When results are missing, the skill uses labeled placeholders instead of inventing them.

## Optional corpus tools

No literature corpus or publisher abstracts are distributed. Local metadata can help find
precedents; it cannot establish novelty, acceptance probability, or a journal's current
requirements. See [corpus setup and limitations](skills/urban-systems-publishing/references/corpus-tools.md).
Do not upload confidential manuscripts or research data to build or query a corpus.

## Rights

See [rights and scholarly sources](RIGHTS.md) for repository permissions and third-party
materials. No open-source license grant is specified.
