# jd-skill-template

> Agent Skill — 按 honghaoxiang 规范初始化和自检 skill 的工具

## 功能特性

- 按规范初始化新 skill 目录（README + SKILL + references + examples + LICENSE）
- 自动写入署名 `author: honghaoxiang`
- 自动设置版本号 `version: "1.0.0"`
- 发布前自检结构是否符合规范

## 安装方式

### Agent 用户

1. 下载 [Release zip](../../releases/latest)
2. 在 Agent 客户端的 Skill 管理 → 上传技能，选择 zip 文件

### 从源码安装

```bash
git clone https://github.com/hugohung/jd-skill-template.git ~/.codex/skills/jd-skill-template
```

## 使用方式

### 初始化新 skill

```bash
python ~/.codex/skills/jd-skill-template/scripts/init.py jd-my-skill --path ~/.codex/skills/
```

### 自检现有 skill

```bash
python ~/.codex/skills/jd-skill-template/scripts/check.py ~/.codex/skills/jd-my-skill
```

### 在支持 Skill 的 Agent 对话中

直接说：
> "帮我创建一个新 skill，叫 jd-xxx"
> "检查一下 jd-xxx 的结构是否符合规范"

## 规范说明

| 文件/目录 | 是否必需 |
|----------|---------|
| README.md | ✅ 必需 |
| SKILL.md | ✅ 必需 |
| references/ | ✅ 必需 |
| examples/ | ✅ 必需 |
| LICENSE | 推荐 |
| scripts/ | 可选 |

详细规范见 `references/structure-spec.md` 和 `references/frontmatter-spec.md`。

## License

MIT License
