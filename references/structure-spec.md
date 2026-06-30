# Skill 目录结构规范

## 强制要求（缺一不可）

| 文件/目录 | 说明 |
|----------|------|
| `README.md` | 项目说明、安装方式、使用示例 |
| `SKILL.md` | skill 定义，含 frontmatter |
| `references/` | 参考资料，至少含 `.gitkeep` |
| `examples/` | 使用示例，至少含 `.gitkeep` |

## 推荐项

| 文件/目录 | 说明 |
|----------|------|
| `LICENSE` | MIT License，Copyright honghaoxiang |
| `scripts/` | 有可执行脚本时才建 |

## 不需要的

- `assets/` — honghaoxiang 的 skill 通常不需要
- `templates/` — 除非 skill 本身是模板类

## 完整结构示例

```
jd-my-skill/
  ├── README.md
  ├── SKILL.md
  ├── LICENSE
  ├── references/
  │   ├── .gitkeep
  │   └── some-reference.md
  ├── examples/
  │   ├── .gitkeep
  │   └── some-example.yml
  └── scripts/           ← 可选
      └── some-script.py
```
