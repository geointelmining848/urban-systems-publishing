# 城市与区域研究论文写作助手

[English](README.md) · [论文写作流程](docs/manuscript-workflows.zh-CN.md) · [贡献指南](CONTRIBUTING.zh-CN.md)

这是面向学生的城市与区域研究论文写作技能，可用于 Codex 和 Claude Code。
它帮助你把研究问题、证据和笔记组织成清晰的论文，修改章节，检查空间推理，选择合适的读者与期刊，
并准备审稿回复。对重要修改，它会解释理由，帮助你作出自己的学术判断。

适用于城市与区域经济、规划、交通、人口与环境健康、城市复杂系统等领域的定量、定性和混合方法研究。

两个客户端使用[同一份技能目录](skills/urban-systems-publishing/SKILL.md)。
核心指导无需 Python、API 密钥或文献语料库；可选文献脚本才需要 Python。

## 安装

先克隆并检查文件，然后复制**完整技能目录**，保留 `references/`、`scripts/` 和 `agents/`。
每个客户端和作用域只保留一份，避免重名。若目标已存在，先比较差异，并把备份放在客户端
技能目录之外，再进行替换。以下命令不会覆盖已有安装。

```sh
git clone https://github.com/geointelmining848/urban-systems-publishing.git
cd urban-systems-publishing
```

Linux、macOS 或 WSL，安装到 Codex：

```sh
target="$HOME/.agents/skills/urban-systems-publishing"
if [ -e "$target" ]; then
  printf '%s\n' '已安装：请先比较并备份。'
else
  mkdir -p "$HOME/.agents/skills"
  cp -R skills/urban-systems-publishing "$target"
fi
```

安装到 Claude Code 时，将上面两处 `$HOME/.agents/skills` 改为 `$HOME/.claude/skills`。
项目级安装则使用项目根目录下的 `.agents/skills`（Codex）或 `.claude/skills`（Claude Code）。
WSL 和 Windows 的用户目录彼此独立，应安装到实际运行客户端的环境中。

Windows PowerShell，安装到 Codex：

```powershell
$skillRoot = Join-Path $env:USERPROFILE '.agents\skills'
$target = Join-Path $skillRoot 'urban-systems-publishing'
if (Test-Path -LiteralPath $target) { throw '已安装：请先比较并备份。' }
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
Copy-Item -LiteralPath '.\skills\urban-systems-publishing' -Destination $target -Recurse
```

安装到 Claude Code 时，把 `.agents\skills` 改为 `.claude\skills`。
重新打开客户端或会话，确认技能可见。客户端的具体设置参见
[Codex](https://learn.chatgpt.com/docs/build-skills)和
[Claude Code](https://code.claude.com/docs/en/skills)。

## 使用

Codex 中输入 `$urban-systems-publishing`，Claude Code 中输入 `/urban-systems-publishing`，
也可以直接提出匹配的研究发表任务。是否自动触发取决于客户端和模型。
技能按你的语言回答；讨论语言与论文语言可以分别指定。

- “请审查‘轨道交通建设导致租金上涨’这个结论。我只有横截面的空间杜宾模型和普查小区数据，没有政策识别设计。”
- “请帮助定位我基于访谈的非正规住房治理研究，保留解释性贡献，并说明判断期刊匹配还需核实哪些证据。”
- “用中文讨论修改，但用英文写摘要。未提供的结果请保留明确占位符，不要编造。”
- “我的城市增长模型采用随机像元划分，是否足以验证未来十年的预测？请检查并修改验证段落。”

尽量提供研究问题、设计、空间与时间单位、主要证据、所需成果，以及已确定的目标期刊。
不要附带机密身份标识。可以从一个提纲、一段正文、摘要、图注或审稿回复开始。
[论文写作流程](docs/manuscript-workflows.zh-CN.md)提供具体提示与示例，也支持讨论语言和论文语言分别指定。

请核实每项事实与引用，并对自己的论文负责。遵守课程、导师、学校与期刊关于署名和 AI 使用的要求。
尚未获得的结果应保留明确占位符，不得编造。

## 可选文献工具

本仓库不分发文献语料、出版社摘要或私人研究数据。本地元数据检索可帮助寻找先例，
但不能证明首创性、录用概率或当前投稿要求。参见[语料工具说明](skills/urban-systems-publishing/references/corpus-tools.md)。
不要为了检索或期刊匹配上传机密论文、地理位置或研究数据。

## 权利说明

仓库内容的使用权限和第三方材料说明见[权利与学术来源](RIGHTS.md)。本仓库未指定开源许可授权。
