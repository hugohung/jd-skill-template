---
name: jd-skill-template
version: "1.0.1"
description: 为 honghaoxiang 账号创建、初始化或验证 WorkBuddy skill。强制执行标准目录结构（README.md、SKILL.md、references/、examples/、LICENSE），自动填入 author: honghaoxiang，设置初始版本号，检查缺失文件。在发布新 skill 到 GitHub 前使用。
author: honghaoxiang
agent_created: true
trigger:
  - 创建skill
  - 新建skill
  - 初始化skill
  - skill模板
  - skill自检
  - 检查skill结构
  - 创建技能
  - 新建技能
---

# Skill 模板与自检工具

## 用途

为 `honghaoxiang` 账号创建符合规范的 WorkBuddy skill，并在发布前自检结构。

## 强制规范

所有 `author: honghaoxiang` 的 skill 必须遵循以下目录结构：

```
<skill-name>/
  ├── README.md          ← 必须有
  ├── SKILL.md           ← 必须有（含 frontmatter）
  ├── references/        ← 必须有（至少含 .gitkeep）
  ├── examples/          ← 必须有（至少含 .gitkeep）
  ├── scripts/           ← 可选（有可执行脚本时才建）
  └── LICENSE             ← 推荐 MIT
```

SKILL.md frontmatter 必须包含：
- `name`: skill 名称
- `version`: 版本号（字符串格式，如 `"1.0.0"`）
- `description`: 第三人称描述
- `author`: `honghaoxiang`
- `agent_created`: `true`
- `trigger`: 触发关键词列表

## 工作流程

### 1. 初始化新 skill

运行 `scripts/init.py`：

```bash
python <skill-path>/scripts/init.py <skill-name> --path <目标目录>
```

脚本会：
- 创建标准目录结构（README/SKILL/references/examples/LICENSE）
- 不创建 scripts/ 和 assets/（除非用 `--with-scripts` 参数）
- SKILL.md 自动填入 author: honghaoxiang、version: "1.0.0"
- README.md 自动填入基础模板
- LICENSE 自动生成为 MIT（Copyright honghaoxiang）

### 2. 自检现有 skill

运行 `scripts/check.py`：

```bash
python <skill-path>/scripts/check.py <待检查的skill目录>
```

脚本会检查：
- 必需文件是否存在（README/SKILL/references/examples/LICENSE）
- frontmatter 是否包含 name/version/description/author/agent_created
- author 是否为 honghaoxiang
- version 是否为字符串格式
- references/ 和 examples/ 是否存在（即使为空也要有 .gitkeep）

输出格式：
```
✅ README.md
✅ SKILL.md
✅ references/
✅ examples/
✅ LICENSE
✅ frontmatter: name
✅ frontmatter: version (1.0.0)
✅ frontmatter: author (honghaoxiang)
✅ frontmatter: agent_created (true)

结果: 9/9 通过
```

或：
```
❌ LICENSE 缺失
❌ frontmatter: author 不是 honghaoxiang (实际: unknown)

结果: 7/9 通过，2 项失败
```

## 触发场景

- 用户说"创建一个新 skill" / "新建 skill" / "初始化 skill"
- 用户说"检查 skill 结构" / "自检 skill"
- 用户准备发布 skill 到 GitHub 前

## 与其他 skill 的配合

- 与 `jd-github-skill-publisher` 配合：先用本 skill 初始化和自检，再用 publisher 上传
- 与内置 `skill-creator` 区别：内置的会多生成 scripts/assets，不写署名，不自检；本 skill 严格按 honghaoxiang 规范

## References

- `references/structure-spec.md` — 完整目录结构规范
- `references/frontmatter-spec.md` — frontmatter 字段规范
- `references/license-template.md` — MIT License 模板
