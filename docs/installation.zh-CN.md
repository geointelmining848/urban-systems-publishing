# 在你的智能体环境中安装

[English](installation.md) · [概览](../README.zh-CN.md) · [论文写作流程](manuscript-workflows.zh-CN.md)

官方文档核对日期：**2026-10-22**。本指南覆盖多种常见智能体环境，并非市场上所有产品的完整清单。
产品版本、操作系统、账户方案与机构政策可能影响功能可用性。

**原生支持**表示厂商文档明确说明技能发现或导入机制；**适配**表示把写作指导作为上下文加载，
不具备原生技能发现机制；**未核实**表示某个安装细节或本技能包的兼容性尚未得到确认。
这些标签不代表已在每个客户端完成本地端到端测试。仓库 CI 检查技能包与可选脚本，不启动这些客户端。

## 获取完整技能目录

如果已经安装 Git：

```sh
git clone https://github.com/geointelmining848/urban-systems-publishing.git
cd urban-systems-publishing
```

也可以在 GitHub 点击 **Code → Download ZIP**，解压后进入仓库目录。
可安装的内容是 **`skills/urban-systems-publishing/`**，请保留其中的 `SKILL.md`、
`references/`、`scripts/` 与 `agents/`。不要把整个仓库当作一个技能上传。
`agents/openai.yaml` 是可选的 Codex 界面元数据；写作指导位于 `SKILL.md` 及其链接的参考文件中。

为每个客户端和作用域选择**一个**安装位置。`.agents/skills/` 等共享目录可能被多个客户端读取，
应避免同名副本。更新已有安装前，请先比较差异，并在技能发现目录之外备份。
应安装到客户端实际运行的环境：Windows、WSL、容器与远程会话的文件系统和用户目录可能不同。

## 原生本地目录安装

下表给出的是**父目录**。将完整的 `urban-systems-publishing` 文件夹放入其中，
最终路径应以 `urban-systems-publishing/SKILL.md` 结尾。
项目路径相对于研究项目根目录，`~` 表示该客户端使用的用户主目录。
自定义根目录和机构管理策略优先于默认设置。
Pi 的项目级 `.pi/` 目录相对于运行时工作目录，因此使用项目级安装时，应从该项目根目录启动 Pi。
OpenClaw 的工作区是配置中指定的智能体目录，不一定是当前仓库。

| 环境 | 用户级父目录 | 项目级父目录 | 发现或使用方式；官方文档 |
| --- | --- | --- | --- |
| OpenAI Codex，本地应用、CLI 或 IDE 会话 | `~/.agents/skills/` | `.agents/skills/` | 选择技能或输入 `$urban-systems-publishing`，确认当前会话能够发现它。[Codex](https://learn.chatgpt.com/docs/build-skills) |
| Claude Code，本地会话 | `~/.claude/skills/` | `.claude/skills/` | `/urban-systems-publishing <任务>`。云端与 Cowork 的加载规则不同，见下方上传说明。[Claude Code](https://code.claude.com/docs/en/skills) |
| Cursor 编辑器 / CLI | `~/.cursor/skills/` | `.cursor/skills/` | 启动或重新加载客户端，输入 `/` 并选择技能。本地用户技能不会自动成为远程或云端技能。[Cursor](https://cursor.com/docs/skills) |
| GitHub Copilot CLI | `~/.copilot/skills/` | `.github/skills/` | 按名称要求 Copilot 使用技能，并检查客户端中的可用技能。[Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) |
| VS Code 中的 GitHub Copilot | `~/.copilot/skills/` | `.github/skills/` | 在 **Agent Customizations → Skills** 查看，并在聊天中选择。Copilot 云端智能体应使用提交到其仓库中的项目副本；本地主目录不等于云端安装。[VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills)、[云端智能体](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) |
| Gemini CLI | `~/.gemini/skills/` | `.gemini/skills/` | `/skills reload` 后执行 `/skills list`，按名称请求使用技能，并遵循激活确认提示。[Gemini CLI](https://geminicli.com/docs/cli/skills/)、[管理说明](https://geminicli.com/docs/cli/using-agent-skills/) |
| Google Antigravity App / IDE | `~/.gemini/config/skills/` | `.agents/skills/` | App 中使用 `/urban-systems-publishing`；IDE 中查看 **Customizations**，然后按名称请求使用。[Antigravity](https://antigravity.google/docs/skills) |
| Google Antigravity CLI | `~/.gemini/antigravity-cli/skills/` | `.agents/skills/` | 在终端界面使用 `/urban-systems-publishing`。其用户目录与 App、IDE 及 Gemini CLI 不同。[Antigravity CLI](https://antigravity.google/docs/skills#cli-skill-locations) |
| Pi 编程智能体框架（`pi.dev`） | `~/.pi/agent/skills/` | `.pi/skills/` | `/reload`，然后 `/skill:urban-systems-publishing <任务>`。设置 `PI_CODING_AGENT_DIR` 会改变用户根目录。[Pi 技能](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md)、[配置](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/configuration.md) |
| DeepSeek Harness（`dsh`） | `~/.dsh/skills/` | `.dsh/skills/` | 启动会话，按名称请求技能。将技能文件夹直接放在所选父目录下，不要多套一层仓库目录。`DSH_HOME` / `DSH_AGENTS_HOME` 可改变用户根目录。[发现机制](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md)、[配置](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/config-catalog.md) |
| OpenCode | `~/.config/opencode/skills/` | `.opencode/skills/` | 要求 OpenCode 通过技能工具加载并使用该技能。本技能包未启用 OpenCode 可选的斜杠命令元数据。[OpenCode](https://opencode.ai/docs/skills/) |
| Amp | `~/.config/agents/skills/` | `.agents/skills/` | 用 `amp skills list` 查看；已有会话应先要求重新加载技能。另开终端列出技能不会刷新当前会话。[Amp](https://ampcode.com/docs/customize/skills) |
| Factory Droid | `~/.factory/skills/` | `.factory/skills/` | `/skills` 检查发现结果，再输入 `/urban-systems-publishing <任务>`；必要时新建会话。[Factory](https://docs.factory.com/harness/skills) |
| Cline | `~/.cline/skills/` | `.cline/skills/` | 在聊天中输入 `/` 并选择技能，或提出匹配的论文写作任务。[Cline](https://docs.cline.bot/customization/skills) |
| Windsurf / Devin Desktop 的 Cascade | `~/.codeium/windsurf/skills/` | `.devin/skills/` | 在 Cascade 中使用 `@urban-systems-publishing`。官方也支持 `.windsurf/skills/` 与 `~/.config/devin/skills/`。本行仅针对 Cascade，不代表所有 Devin 产品界面。[Cascade](https://docs.devin.ai/desktop/cascade/skills) |
| Qwen Work / 千问办公（`qwenwork.cn`） | `~/.qwenworkcn/skills/` | 此处未核实项目级目录 | 复制完整文件夹后，输入 `/` 选择技能或按名称请求使用。这里是**千问办公**，与 Qwen Code 不同；也可使用下方界面导入方式。[千问办公](https://qwenwork.cn/docs/features/skills)、[阿里云产品说明](https://help.aliyun.com/en/rpa/getting-started/develop-skills-for-qwenwork) |
| Qwen Code | `~/.qwen/skills/` | `.qwen/skills/` | `/skills` 打开面板；`/urban-systems-publishing <任务>` 调用技能。这是与千问办公不同的独立产品。[Qwen Code](https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/) |
| Kimi Code CLI | `~/.kimi-code/skills/` | 所属 Git 项目根目录中的 `.kimi-code/skills/` | 新建会话后使用 `/skill:urban-systems-publishing <任务>`。`KIMI_CODE_HOME` 可改变用户根目录。[Kimi Code](https://moonshotai.github.io/kimi-code/en/customization/skills) |
| Kiro IDE / CLI | `~/.kiro/skills/` | `.kiro/skills/` | `/urban-systems-publishing <任务>`。IDE 也支持 **Agent Steering & Skills → + → Import a skill → Local folder**，选择本技能目录。本地用户技能不会自动成为 Web 或移动端技能。[Kiro](https://kiro.dev/docs/skills/) |
| OpenClaw | 默认 `~/.openclaw/skills/`；自定义时为 `<state-dir>/skills/` | `<configured-agent-workspace>/skills/` | 安装到提供智能体工作区或 Gateway 的主机。用 `openclaw skills list` 查看，再通过 Control UI 的 `$` 技能选择器调用。[技能](https://docs.openclaw.ai/tools/skills)、[CLI](https://docs.openclaw.ai/cli/skills) |

### Linux、macOS 或 WSL 复制命令

在克隆或解压后的仓库目录运行，把 `skill_root` 设置为上表中对应的父目录。
下面示例使用 Codex 用户目录；项目级安装应填写所选项目父目录的完整路径。

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

若目标已经存在，命令只提示先比较并备份，不覆盖内容。

### Windows PowerShell 复制命令

在克隆或解压后的仓库目录运行。将 `.agents\skills` 替换为所选用户级父目录，
或将 `$skillRoot` 设为项目目录中的完整路径。

```powershell
$skillRoot = Join-Path $env:USERPROFILE '.agents\skills'
$target = Join-Path $skillRoot 'urban-systems-publishing'
if (Test-Path -LiteralPath $target) { throw 'Already installed: compare and back up first.' }
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
Copy-Item -LiteralPath '.\skills\urban-systems-publishing' -Destination $target -Recurse
```

这些命令只复制技能，不安装客户端、不登录、不更改权限，也不安装 Python 依赖。
请使用已经获得授权的运行环境。

## 原生界面导入

以下产品的文档说明了自定义技能导入方式。不同版本的打包要求可能不同，
使用前请确认所有参考文件都已保留。

### 腾讯 WorkBuddy

打开 **专家·技能·连接器 → 技能 → 添加技能 → 上传技能**，选择本地技能包，
然后在**已安装**中确认启用。新建对话，并要求使用 `urban-systems-publishing`。
文档中的对话安装方式搜索的是技能市场条目，不是自定义技能包上传入口。
官方正文没有明确压缩包扩展名或根目录结构，本指南不臆造这些要求。
请以当前版本的文件选择器为准；若不能导入完整技能包，可使用下方手动上下文方式。
[WorkBuddy 官方指南](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)

### Qwen Work / 千问办公

打开 **扩展 → 技能 → 安装技能**，上传 `SKILL.md` 及辅助文件，保留 `references/`
和 `scripts/` 的目录结构。导入后输入 `/` 选择技能，或按名称要求使用。
上表的本地目录方式也有官方文档支持。这两种方式都不是 Qwen Code 的安装说明。
[千问办公官方指南](https://qwenwork.cn/docs/features/skills)

### Doubao Work / 豆包工作

打开 **插件·技能·伙伴 → 技能 → 上传技能**，上传本地技能文件或文件夹，
在**我安装的**中检查，然后在论文写作任务中使用。这里指独立的**豆包工作**产品，不是普通豆包聊天。

**本技能包的导入兼容性尚未核实：**官方可检索的指南将入口文件写作 `skill.md`，
而本标准技能包使用 `SKILL.md`。文件名大小写的接受规则和压缩包结构尚未核实。
请勿改动标准源目录，也不要把上传尝试当作导入成功。先确认客户端要求；如果它拒绝大写文件名，
应在确认格式后另做一份导入副本，或使用手动上下文方式。此处不提供未经核实的本地安装路径。
[豆包工作官方技能指南](https://www.doubao.com/work/docs/zh-cn/articles/081010973544-skills)

### Claude 应用 / Cowork

创建包含 **`urban-systems-publishing/` 文件夹**的 ZIP，不要压缩整个仓库作为技能。
打开 **Customize → Skills → + → Create skill → Upload a skill**，选择该 ZIP 并启用技能。
Cowork 使用账户技能；只复制到本机 `~/.claude/skills/` 并不能完成 Cowork 安装。
请确认账户现有功能与机构政策，不为此自行扩大权限。
[Claude 上传指南](https://support.claude.com/en/articles/12512180-use-skills-in-claude)、
[Cowork 加载规则](https://code.claude.com/docs/en/skills#use-skills-in-cowork-and-cloud-sessions)

## 指令文件与手动上下文适配

这些方式可以复用写作指导，但不代表原生技能发现，也不会保证自动加载链接的参考文件。

| 环境 | 实用适配方式 | 依据与限制 |
| --- | --- | --- |
| Continue | 在 `.continue/rules/` 添加一条简短项目规则，要求处理论文写作时读取本技能的 `SKILL.md`；把完整技能保存在可访问的项目目录中，不覆盖其他规则。 | [Continue 规则](https://docs.continue.dev/customize/deep-dives/rules)说明指令文件机制；此处未核实本技能包的原生导入支持。 |
| Aider | 在本仓库中输入 `/read skills/urban-systems-publishing/SKILL.md`，再按需用 `/read` 加载相关参考文件，然后提出写作任务。 | [Aider 写作约定](https://aider.chat/docs/usage/conventions.html)说明只读上下文机制。这是手动适配，不是原生技能安装。 |
| 其他可读取文件的智能体或聊天客户端 | 附加或读取 `SKILL.md` 和与任务相关的参考文件，并明确要求遵循。若不能访问文件，可粘贴相关指导，并说明这是你要求采用的工作流程。 | 仅作为通用手动上下文使用。模型名称或聊天订阅本身并不代表具备技能加载、文件系统访问、脚本执行或持久安装能力。 |

例如：

> 请读取 `skills/urban-systems-publishing/SKILL.md`，用其中的指导帮助我修改摘要。
> 如能访问，请按需读取相关参考文件；如果某文件不可用，请明确说明。
> 用我指定的语言讨论建议，并保留我的研究证据。

使用指令文件适配时，按客户端自己的规则格式保留这条简短的读取请求，完整技能仍放在独立文件夹中。
不要把技能的 YAML 元数据直接粘贴进其他配置格式，也不要假设相对路径文件会自动加载。

## 已停止服务或尚未明确的环境

- **Roo Code：**官方说明该扩展已于 2026 年 5 月 15 日停止服务。
  留存的技能文档不构成当前安装建议；社区分支应另外核对其自身文档。[官方说明](https://docs.roocode.com/)
- **其他名为 pi、dsh、Qwen Work 或 Doubao Work 的产品：**上文仅对应明确列出的厂商和产品。
  如果你使用的是不同客户端，应先提供其官网和版本，再选择目录或导入方式。
- **没有已核实的原生支持时：**不要猜测隐藏的技能目录，也不要安装名称相似的工具来替代。
  客户端支持时可使用手动上下文，否则等待明确的官方导入机制。

## 确认可用

1. 确认发现的技能名为 `urban-systems-publishing`，并在客户端支持的技能界面或文件系统中
   检查指导与参考文件。
2. 用自己的研究做一个小任务，例如拟定提纲或修改一段正文；确认助手保留证据、解释重要建议，
   并遵循分别指定的讨论语言与论文语言。
3. 使用[论文写作流程](manuscript-workflows.zh-CN.md)。核心写作指导不需要 Python、API 密钥
   或网络访问；可选语料脚本需要另行可用的执行环境与明确授权。
4. 若未发现技能，检查作用域、目录嵌套、`SKILL.md` 大小写、重名副本、功能可用性与当前官方文档。
   不要仅为显示一个写作技能而授予宽泛权限。
