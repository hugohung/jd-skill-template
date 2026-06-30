# SKILL.md Frontmatter 规范

## 必需字段

| 字段 | 格式 | 示例 |
|------|------|------|
| `name` | skill 名称，与目录名一致 | `jd-my-skill` |
| `version` | 字符串格式，遵循 semver | `"1.0.0"` |
| `description` | 第三人称描述 | `This skill should be used when...` |
| `author` | 固定值 | `honghaoxiang` |
| `agent_created` | 固定值 | `true` |
| `trigger` | 触发关键词列表 | `[关键词1, 关键词2]` |

## 完整示例

```yaml
---
name: jd-my-skill
version: "1.0.0"
description: This skill should be used when doing something specific. It provides...
author: honghaoxiang
agent_created: true
trigger:
  - 触发词1
  - 触发词2
---
```

## 注意事项

- `version` 必须用引号包起来（字符串格式），如 `"1.0.0"` 而不是 `1.0.0`
- `description` 用第三人称（This skill should be used when...），不要用第二人称指令
- `author` 必须是 `honghaoxiang`
- `trigger` 关键词用中文，覆盖用户可能的表述方式
