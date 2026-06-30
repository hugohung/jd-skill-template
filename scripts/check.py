#!/usr/bin/env python3
"""
jd-skill-template check script
检查一个 skill 目录是否符合 honghaoxiang 规范。

Usage:
    python check.py <skill-dir>
"""

import re
import sys
from pathlib import Path


REQUIRED_FILES = ["README.md", "SKILL.md", "LICENSE"]
REQUIRED_DIRS = ["references", "examples"]
REQUIRED_FRONTMATTER = ["name", "version", "description", "author", "agent_created"]
EXPECTED_AUTHOR = "honghaoxiang"


def parse_frontmatter(skill_md: Path):
    """解析 SKILL.md 的 frontmatter。"""
    if not skill_md.exists():
        return {}
    content = skill_md.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    fm_text = content[3:end].strip()
    fm = {}
    for line in fm_text.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            fm[key] = value
    return fm


def check_skill(skill_dir: Path):
    results = []

    # 检查必需文件
    for f in REQUIRED_FILES:
        path = skill_dir / f
        if path.exists():
            results.append(("pass", f"{f}"))
        else:
            results.append(("fail", f"{f} 缺失"))

    # 检查必需目录
    for d in REQUIRED_DIRS:
        path = skill_dir / d
        if path.is_dir():
            results.append(("pass", f"{d}/"))
        else:
            results.append(("fail", f"{d}/ 缺失"))

    # 检查 frontmatter
    fm = parse_frontmatter(skill_dir / "SKILL.md")
    if not fm and (skill_dir / "SKILL.md").exists():
        results.append(("fail", "frontmatter 解析失败"))
    else:
        for field in REQUIRED_FRONTMATTER:
            if field in fm:
                if field == "author" and fm[field] != EXPECTED_AUTHOR:
                    results.append(("fail", f"frontmatter: author 不是 {EXPECTED_AUTHOR} (实际: {fm[field]})"))
                elif field == "agent_created" and fm[field].lower() != "true":
                    results.append(("fail", f"frontmatter: agent_created 不是 true (实际: {fm[field]})"))
                else:
                    results.append(("pass", f"frontmatter: {field} ({fm[field]})"))
            else:
                results.append(("fail", f"frontmatter: {field} 缺失"))

    return results


def main():
    if len(sys.argv) != 2:
        print("Usage: python check.py <skill-dir>")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])
    if not skill_dir.is_dir():
        print(f"❌ 目录不存在: {skill_dir}")
        sys.exit(1)

    results = check_skill(skill_dir)
    pass_count = sum(1 for status, _ in results if status == "pass")
    fail_count = sum(1 for status, _ in results if status == "fail")
    total = len(results)

    for status, msg in results:
        icon = "✅" if status == "pass" else "❌"
        print(f"{icon} {msg}")

    print(f"\n结果: {pass_count}/{total} 通过", end="")
    if fail_count > 0:
        print(f"，{fail_count} 项失败")
        sys.exit(1)
    else:
        print()


if __name__ == "__main__":
    main()
