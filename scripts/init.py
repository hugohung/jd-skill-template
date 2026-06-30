#!/usr/bin/env python3
"""
jd-skill-template init script
按 honghaoxiang 规范初始化一个新 skill 目录。

Usage:
    python init.py <skill-name> --path <target-dir> [--with-scripts]
"""

import argparse
import os
import sys
from pathlib import Path


LICENSE_TEMPLATE = """MIT License

Copyright (c) {year} honghaoxiang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

SKILL_TEMPLATE = """---
name: {name}
version: "1.0.0"
description: TODO: 用第三人称描述这个 skill 的用途（This skill should be used when...）
author: honghaoxiang
agent_created: true
trigger:
  - TODO: 触发关键词1
  - TODO: 触发关键词2
---

# {title}

## 用途

TODO: 描述这个 skill 做什么。

## 工作流程

TODO: 描述 skill 被触发后的执行步骤。

## References

TODO: 列出 references/ 下的参考文件。
"""

README_TEMPLATE = """# {title}

> WorkBuddy Skill — TODO: 一句话描述

## 功能特性

- TODO: 核心功能点

## 安装方式

### WorkBuddy 用户

1. 下载 [Release zip](../../releases/latest)
2. 在 WorkBuddy 技能管理 → 上传技能，选择 zip 文件

### 从源码安装

```bash
git clone https://github.com/hugohung/{name}.git ~/.workbuddy/skills/{name}
```

## 使用方式

在 WorkBuddy 对话中直接说：
> "TODO: 触发示例"

## License

MIT License
"""


def init_skill(skill_name: str, target_dir: Path, with_scripts: bool = False):
    skill_dir = target_dir / skill_name
    if skill_dir.exists():
        print(f"❌ 目录已存在: {skill_dir}")
        sys.exit(1)

    skill_dir.mkdir(parents=True)

    # 必需目录
    (skill_dir / "references").mkdir()
    (skill_dir / "examples").mkdir()
    (skill_dir / "references" / ".gitkeep").touch()
    (skill_dir / "examples" / ".gitkeep").touch()

    # 可选 scripts
    if with_scripts:
        (skill_dir / "scripts").mkdir()

    # 必需文件
    import datetime
    year = datetime.datetime.now().year

    (skill_dir / "LICENSE").write_text(
        LICENSE_TEMPLATE.format(year=year), encoding="utf-8"
    )

    title = skill_name.replace("-", " ").title()
    (skill_dir / "SKILL.md").write_text(
        SKILL_TEMPLATE.format(name=skill_name, title=title),
        encoding="utf-8",
    )
    (skill_dir / "README.md").write_text(
        README_TEMPLATE.format(name=skill_name, title=title),
        encoding="utf-8",
    )

    print(f"✅ 已创建 skill: {skill_dir}")
    print(f"   - SKILL.md (含 author: honghaoxiang, version: 1.0.0)")
    print(f"   - README.md")
    print(f"   - LICENSE (MIT, Copyright honghaoxiang)")
    print(f"   - references/.gitkeep")
    print(f"   - examples/.gitkeep")
    if with_scripts:
        print(f"   - scripts/ (空目录)")
    print(f"\n下一步: 编辑 SKILL.md 和 README.md 补全内容")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="初始化符合 honghaoxiang 规范的 skill")
    parser.add_argument("name", help="skill 名称（如 jd-my-skill）")
    parser.add_argument("--path", required=True, help="目标目录")
    parser.add_argument("--with-scripts", action="store_true", help="创建 scripts/ 目录")
    args = parser.parse_args()

    init_skill(args.name, Path(args.path), args.with_scripts)
