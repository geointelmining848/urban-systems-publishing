# Install in your agent environment

[简体中文](installation.zh-CN.md) · [Overview](../README.md) · [Writing workflows](manuscript-workflows.md)

Official documentation checked **2026-10-22**. This guide covers a broad selection of
agent environments; it is not an exhaustive market inventory. Product versions,
operating systems, account plans and organization policies can affect availability.

**Native** means the vendor documents skill discovery or import. **Adaptation** means
loading the writing instructions as context, without native skill discovery. **Unverified**
means a specific installation detail or package compatibility is not established.
These labels do not claim local end-to-end testing in every client. Repository CI checks
the package and optional scripts; it does not launch these clients.

## Get the complete skill

With Git already available:

```sh
git clone https://github.com/geointelmining848/urban-systems-publishing.git
cd urban-systems-publishing
```

Alternatively use GitHub's **Code → Download ZIP**, extract it, and open the extracted
repository folder. The installable directory is **`skills/urban-systems-publishing/`**.
Keep `SKILL.md`, `references/`, `scripts/` and `agents/` together. Do not upload the entire
repository as a skill. `agents/openai.yaml` is optional Codex UI metadata; the writing
instructions are in `SKILL.md` and its linked references.

Choose **one** destination for each client and scope. Shared directories such as
`.agents/skills/` can be read by several clients; avoid duplicate copies with the same
name. Compare and back up an existing installation outside discovery directories before
updating it. Install in the environment where the client runs: Windows, WSL, containers
and remote sessions have separate filesystems and home directories.

## Native local-directory installation

Each table entry is a **parent directory**. Place the complete `urban-systems-publishing`
folder inside it, so the result ends in `urban-systems-publishing/SKILL.md`.
Project paths are relative to your research project's root; `~` denotes the home directory
used by that client. Configured roots and managed policies take precedence over defaults.
For a project-level Pi installation, start Pi from that project's root: its `.pi/`
directory is relative to the working directory.
OpenClaw's workspace is a configured agent directory, which need not be your current repository.

| Environment | User-level parent | Project-level parent | Discover or use it; official instructions |
| --- | --- | --- | --- |
| OpenAI Codex, local app/CLI/IDE sessions | `~/.agents/skills/` | `.agents/skills/` | Select the skill or use `$urban-systems-publishing`. Confirm discovery in the session. [Codex](https://learn.chatgpt.com/docs/build-skills) |
| Claude Code, local sessions | `~/.claude/skills/` | `.claude/skills/` | `/urban-systems-publishing <request>`. Cloud/Cowork sessions have separate loading rules; see the upload section below. [Claude Code](https://code.claude.com/docs/en/skills) |
| Cursor editor / CLI | `~/.cursor/skills/` | `.cursor/skills/` | Start/reload the client; type `/` and select the skill. Local user skills do not automatically become remote/cloud skills. [Cursor](https://cursor.com/docs/skills) |
| GitHub Copilot CLI | `~/.copilot/skills/` | `.github/skills/` | Ask Copilot to use the named skill; inspect available skills in the client. [Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) |
| GitHub Copilot in VS Code | `~/.copilot/skills/` | `.github/skills/` | Open **Agent Customizations → Skills** and select the skill in chat. For Copilot cloud agent, commit the project copy to its repository; a local home directory is not a cloud install. [VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills), [cloud agent](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) |
| Gemini CLI | `~/.gemini/skills/` | `.gemini/skills/` | `/skills reload`, then `/skills list`; ask to use the named skill and follow its activation prompt. [Gemini CLI](https://geminicli.com/docs/cli/skills/), [management](https://geminicli.com/docs/cli/using-agent-skills/) |
| Google Antigravity App / IDE | `~/.gemini/config/skills/` | `.agents/skills/` | App: `/urban-systems-publishing`; IDE: check **Customizations**, then request it by name. [Antigravity](https://antigravity.google/docs/skills) |
| Google Antigravity CLI | `~/.gemini/antigravity-cli/skills/` | `.agents/skills/` | Use `/urban-systems-publishing` in the TUI. Its user directory differs from the App/IDE and Gemini CLI. [Antigravity CLI](https://antigravity.google/docs/skills#cli-skill-locations) |
| Pi coding-agent harness (`pi.dev`) | `~/.pi/agent/skills/` | `.pi/skills/` | `/reload`, then `/skill:urban-systems-publishing <request>`. A configured `PI_CODING_AGENT_DIR` changes the user root. [Pi skills](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md), [configuration](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/configuration.md) |
| DeepSeek Harness (`dsh`) | `~/.dsh/skills/` | `.dsh/skills/` | Start a session and request the skill by name. Put it directly under the chosen root, without an extra repository wrapper. `DSH_HOME` / `DSH_AGENTS_HOME` can change user roots. [Discovery](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md), [configuration](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/config-catalog.md) |
| OpenCode | `~/.config/opencode/skills/` | `.opencode/skills/` | Ask OpenCode to load and use the named skill through its skill tool. This package does not opt in to OpenCode's optional slash-command metadata. [OpenCode](https://opencode.ai/docs/skills/) |
| Amp | `~/.config/agents/skills/` | `.agents/skills/` | `amp skills list`; ask an existing thread to reload its skills before use. A separate listing command does not refresh an active thread. [Amp](https://ampcode.com/docs/customize/skills) |
| Factory Droid | `~/.factory/skills/` | `.factory/skills/` | `/skills` to inspect discovery, then `/urban-systems-publishing <request>`; start a fresh session if necessary. [Factory](https://docs.factory.com/harness/skills) |
| Cline | `~/.cline/skills/` | `.cline/skills/` | In chat type `/` and select the skill, or request matching manuscript work. [Cline](https://docs.cline.bot/customization/skills) |
| Windsurf / Devin Desktop, Cascade | `~/.codeium/windsurf/skills/` | `.devin/skills/` | `@urban-systems-publishing` in Cascade. The official guide also accepts `.windsurf/skills/` and `~/.config/devin/skills/`. This row is for Cascade, not a claim about every Devin surface. [Cascade](https://docs.devin.ai/desktop/cascade/skills) |
| Qwen Work / 千问办公 (`qwenwork.cn`) | `~/.qwenworkcn/skills/` | No project root verified here | Copy the complete folder, then type `/` and choose it or request it by name. This is **Qwen Work**, distinct from Qwen Code. A UI import is also documented below. [Qwen Work](https://qwenwork.cn/docs/features/skills), [Alibaba product identification](https://help.aliyun.com/en/rpa/getting-started/develop-skills-for-qwenwork) |
| Qwen Code | `~/.qwen/skills/` | `.qwen/skills/` | `/skills` opens the panel; `/urban-systems-publishing <request>` invokes it. This is a separate product from Qwen Work. [Qwen Code](https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/) |
| Kimi Code CLI | `~/.kimi-code/skills/` | `.kimi-code/skills/` at the enclosing Git project root | Start a new session; `/skill:urban-systems-publishing <request>`. `KIMI_CODE_HOME` can change the user root. [Kimi Code](https://moonshotai.github.io/kimi-code/en/customization/skills) |
| Kiro IDE / CLI | `~/.kiro/skills/` | `.kiro/skills/` | `/urban-systems-publishing <request>`. IDE import also supports **Agent Steering & Skills → + → Import a skill → Local folder**; select this skill's directory. Local user skills are not automatically Web/Mobile skills. [Kiro](https://kiro.dev/docs/skills/) |
| OpenClaw | `~/.openclaw/skills/` by default; `<state-dir>/skills/` if configured | `<configured-agent-workspace>/skills/` | Install on the host serving the agent workspace/Gateway. `openclaw skills list`; use the Control UI's `$` skill picker. [Skills](https://docs.openclaw.ai/tools/skills), [CLI](https://docs.openclaw.ai/cli/skills) |

### Copy on Linux, macOS or WSL

Run from the cloned/extracted repository. Set `skill_root` to a documented parent above.
This example chooses Codex's user directory; for a project scope use the full path to
the selected project's parent directory instead.

```sh
skill_root="$HOME/.agents/skills"
target="$skill_root/urban-systems-publishing"
if [ -e "$target" ] || [ -L "$target" ]; then
  printf '%s\n' 'Already installed: compare and back up before replacing.'
else
  mkdir -p "$skill_root"
  cp -R skills/urban-systems-publishing "$target"
fi
```

### Copy on Windows PowerShell

Run from the cloned/extracted repository. Replace `.agents\skills` with the chosen
user-level parent, or set `$skillRoot` to a project directory's full path.

```powershell
$skillRoot = Join-Path $env:USERPROFILE '.agents\skills'
$target = Join-Path $skillRoot 'urban-systems-publishing'
if (Test-Path -LiteralPath $target) { throw 'Already installed: compare and back up first.' }
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
Copy-Item -LiteralPath '.\skills\urban-systems-publishing' -Destination $target -Recurse
```

These commands copy the skill only. They do not install a client, sign in, change
permissions or install Python dependencies. Use only an already authorized environment.

## Native UI imports

These products document custom skill import. Packaging controls can differ by version;
check that all reference files survived the import before using the skill.

### Tencent WorkBuddy

Open **专家·技能·连接器 → 技能 → 添加技能 → 上传技能**
(Experts, Skills & Connectors → Skills → Add skill → Upload skill).
Select the local skill package, then confirm it is enabled under **已安装** (Installed).
Start a new conversation and ask to use `urban-systems-publishing`.
The documented conversational installer searches marketplace entries; it is not the
custom-package upload route. The official prose does not specify an archive extension or
root layout, so this guide does not invent one. Follow the file picker in your version;
if it cannot import the complete package, use the manual-context option below.
[Official WorkBuddy guide](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)

### Qwen Work / 千问办公

Open **扩展 → 技能 → 安装技能** (Extensions → Skills → Install skill) and upload
`SKILL.md` with its auxiliary files. Keep the `references/` and `scripts/` structure intact.
After import, type `/` to select the skill or ask for it by name. The local-directory
method in the table is also documented. Neither method is an instruction for Qwen Code.
[Official Qwen Work guide](https://qwenwork.cn/docs/features/skills)

### Doubao Work / 豆包工作

Open **插件·技能·伙伴 → 技能 → 上传技能**, upload the local skill files or folder,
and check **我安装的** (My installed skills). Use the skill in a manuscript-writing task.
This refers to the distinct **Doubao Work** product, not ordinary Doubao chat.

**Package compatibility remains unverified:** the official indexed guide spells the
entry file `skill.md`, while this standard package uses `SKILL.md`. Filename-case
acceptance and archive layout are not verified here. Do not rename
the canonical package or assume a successful import. Check your client's requirements;
if uppercase `SKILL.md` is rejected, use a separate import copy only after confirming
the required format, or use manual context. No filesystem install path is asserted here.
[Official Doubao Work skill guide](https://www.doubao.com/work/docs/zh-cn/articles/081010973544-skills)

### Claude apps / Cowork

Create a ZIP containing the **`urban-systems-publishing/` folder**, not the repository.
Open **Customize → Skills → + → Create skill → Upload a skill**, select that ZIP,
and enable the uploaded skill. Account skills serve Cowork; copying to a local
`~/.claude/skills/` directory alone does not install it in Cowork. Check your account's
existing feature availability and organization policy rather than changing permissions.
[Claude upload guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude),
[Cowork loading rules](https://code.claude.com/docs/en/skills#use-skills-in-cowork-and-cloud-sessions)

## Instruction-file and manual-context adaptation

These routes reuse the writing guidance but do not establish native skill discovery or
automatic loading of linked references.

| Environment | Practical adaptation | Evidence and limits |
| --- | --- | --- |
| Continue | Add a short project rule in `.continue/rules/` asking the agent to read this package's `SKILL.md` when doing manuscript work; retain the package at an accessible project path. Do not replace unrelated rules. | [Continue rules](https://docs.continue.dev/customize/deep-dives/rules) documents instruction files. Native import of this skill package is not verified here. |
| Aider | From this repository, use `/read skills/urban-systems-publishing/SKILL.md`, then `/read` the relevant reference files when needed. Ask for the writing task. | [Aider conventions](https://aider.chat/docs/usage/conventions.html) documents read-only context. This is manual adaptation, not a native skills installation. |
| Other file-capable agents or chat clients | Attach/read `SKILL.md` and only the references relevant to the task; explicitly ask the assistant to follow them. If file access is unavailable, paste the relevant instructions and identify them as your requested workflow. | Generic manual context only. A model name or chat subscription does not establish a skill loader, filesystem access, script execution or persistent installation. |

For example:

> Read `skills/urban-systems-publishing/SKILL.md` and use it to help revise my abstract.
> Read the relevant linked references if you can access them. If a file is unavailable,
> tell me which one. Discuss suggestions in my chosen language and preserve my evidence.

For an instruction-file adapter, keep this short routing request in the client's rule
format and keep the full skill in its own folder. Do not paste YAML skill metadata into
an unrelated configuration format or assume that relative references load automatically.

## Unavailable or unresolved environments

- **Roo Code:** its official site states that the extension shut down on May 15, 2026.
  Its archived skill documentation is not a current installation recommendation.
  Community forks need their own documentation checks. [Official notice](https://docs.roocode.com/)
- **Other products named pi, dsh, Qwen Work or Doubao Work:** the entries above refer
  only to the explicitly named vendors/products. If your client is different, identify
  its official URL and version before selecting a directory or import recipe.
- **No verified native support:** do not make up a hidden skills directory or install
  a similarly named tool. Use manual context if the client supports it, or wait for
  a documented import mechanism.

## Confirm it is ready

1. Confirm the discovered skill name is `urban-systems-publishing`, and inspect its
   instructions and reference files in the client's supported skill view or filesystem.
2. Start with a small task using your own research: ask for an outline or a revision of
   one paragraph. Confirm that the assistant preserves evidence, explains important
   suggestions and uses your requested discussion/manuscript languages.
3. Use the [writing workflows](manuscript-workflows.md). Python, API credentials and
   network access are unnecessary for core writing guidance. Optional corpus scripts
   require a separately available execution environment and explicit authorization.
4. If discovery fails, check the chosen scope, exact folder nesting, `SKILL.md` case,
   duplicate names, feature availability and the current official guide. Do not grant
   broad permissions merely to make a writing skill appear.
