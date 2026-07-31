#!/usr/bin/env python3
"""Generate index.json from skill frontmatter in skills/**/*.md.

Usage:
    python3 scripts/generate_index.py            # write index.json
    python3 scripts/generate_index.py --check     # verify index.json is up to date, exit 1 if not

Also validates every skill file's frontmatter: required fields present,
and `category` matches the directory the file actually lives in. This
catches the most common submission mistake (copy-pasting the template
without updating `category`) before it reaches review.
"""

import json
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
INDEX_PATH = REPO_ROOT / "index.json"

REQUIRED_FIELDS = [
    "name",
    "description",
    "version",
    "author",
    "license",
    "category",
    "platforms",
    "agent_compatibility",
]

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def load_skill_files():
    files = sorted(SKILLS_DIR.glob("*/*.md"))
    return [f for f in files if f.name != "README.md"]


def parse_skill(path: Path):
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, f"{path}: missing YAML frontmatter"

    try:
        data = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        return None, f"{path}: invalid YAML frontmatter ({exc})"

    missing = [f for f in REQUIRED_FIELDS if f not in data or data[f] in (None, "")]
    if missing:
        return None, f"{path}: missing required field(s): {', '.join(missing)}"

    actual_category = path.parent.name
    if data["category"] != actual_category:
        return None, (
            f"{path}: frontmatter category '{data['category']}' does not match "
            f"directory '{actual_category}'"
        )

    slug = path.stem
    entry = {
        "name": data["name"],
        "slug": slug,
        "description": data["description"],
        "version": str(data["version"]),
        "author": data["author"],
        "license": data["license"],
        "category": data["category"],
        "platforms": data["platforms"],
        "agent_compatibility": data["agent_compatibility"],
        "tags": data.get("tags", []),
        "quality_label": data.get("quality_label", "community"),
        "path": str(path.relative_to(REPO_ROOT)),
    }
    return entry, None


def main():
    check_only = "--check" in sys.argv

    entries = []
    errors = []
    for path in load_skill_files():
        entry, error = parse_skill(path)
        if error:
            errors.append(error)
        else:
            entries.append(entry)

    if errors:
        print(f"{len(errors)} skill file(s) failed validation:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    entries.sort(key=lambda e: (e["category"], e["slug"]))
    output = json.dumps(
        {"generated_by": "scripts/generate_index.py", "skill_count": len(entries), "skills": entries},
        indent=2,
        ensure_ascii=False,
    ) + "\n"

    if check_only:
        current = INDEX_PATH.read_text(encoding="utf-8") if INDEX_PATH.exists() else ""
        if current != output:
            print(
                "index.json is out of date. Run `python3 scripts/generate_index.py` "
                "and commit the result.",
                file=sys.stderr,
            )
            sys.exit(1)
        print(f"index.json is up to date ({len(entries)} skills).")
        return

    INDEX_PATH.write_text(output, encoding="utf-8")
    print(f"Wrote index.json with {len(entries)} skills.")


if __name__ == "__main__":
    main()
