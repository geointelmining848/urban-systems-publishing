# Urban and Regional Systems Publishing

[简体中文](README.zh-CN.md) · [Contributing](CONTRIBUTING.md) · [Evaluation](docs/evaluation.md)

A publication mentor for your own urban and regional research, usable in Codex and
Claude Code. It helps review spatial reasoning, sharpen a defensible contribution,
choose an audience, draft manuscript and submission materials, and respond to reviewers.
It covers urban/regional economics, planning, transport, population/environmental health,
and urban complex systems. It does not promise acceptance or perform a full empirical
analysis merely because you ask for a manuscript review.

The same [skill folder](skills/urban-systems-publishing/SKILL.md) serves both clients.
Instructions and references work without Python, API keys, or a downloaded corpus.
Python is needed only for the optional helpers and development checks.

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

For Claude Code, change `.agents\skills` to `.claude\skills`. Some older/local Codex
installations use `~/.codex/skills`; update that existing location if your client discovers
it, rather than creating a duplicate. Current official local-discovery guidance uses
`.agents/skills`. Reopen the client/session and confirm that the skill appears.
Sources checked 2026-10-22: [Codex skill discovery](https://learn.chatgpt.com/docs/build-skills),
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
target journal if known. Omit confidential identifiers. The skill loads the relevant
reference modules instead of imposing its full workflow on every request.

## Optional corpus tools

No literature corpus or publisher abstracts are distributed. Local metadata can help find
precedents; it cannot establish novelty, acceptance probability, or a journal's current
requirements. See [corpus setup and limitations](skills/urban-systems-publishing/references/corpus-tools.md).
Do not upload confidential manuscripts or research data to build or query a corpus.

## Validation and rights

See [evaluation](docs/evaluation.md) for concrete findings, scenarios, checks, and the
distinction between structural tests and model behavior. Development checks:

```sh
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
```

Tests use synthetic records and mocked requests, with no live API harvesting.
The reviewed source copies contained no license file; this release adds no license grant.
See [rights and attribution](RIGHTS.md) and [source provenance](docs/provenance.md).
