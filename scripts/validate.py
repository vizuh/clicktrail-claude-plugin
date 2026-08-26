#!/usr/bin/env python3
"""Small dependency-free structural check before Claude's authoritative validator."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
assert manifest["name"] == "clicktrail"
assert manifest["license"] == "MIT"

skill_root = ROOT / "skills"
expected = {"setup", "audit", "instrument", "verify"}
actual = {path.parent.name for path in skill_root.glob("*/SKILL.md")}
assert actual == expected, (actual, expected)

for path in skill_root.glob("*/SKILL.md"):
    text = path.read_text()
    parts = text.split("---\n", 2)
    assert len(parts) == 3 and parts[0] == "", f"missing frontmatter: {path}"
    frontmatter = parts[1]
    assert f"name: {path.parent.name}" in frontmatter
    assert "description:" in frontmatter

print("ClickTrail plugin structure OK")
