#!/usr/bin/env python3
"""Validate machine-consumed plugin structure before Claude's validator."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
assert manifest["name"] == "clicktrail"
assert manifest["license"] == "MIT"
assert manifest["repository"] == "https://github.com/vizuh/clicktrail-claude-plugin"

skill_root = ROOT / "skills"
expected = {"setup", "audit", "instrument", "verify", "click-tracking-audit"}
actual = {path.parent.name for path in skill_root.glob("*/SKILL.md")}
assert actual == expected, (actual, expected)

frontmatter_by_skill: dict[str, dict[str, str]] = {}
for path in skill_root.glob("*/SKILL.md"):
    text = path.read_text()
    parts = text.split("---\n", 2)
    assert len(parts) == 3 and parts[0] == "", f"missing frontmatter: {path}"
    fields = {}
    for line in parts[1].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    assert fields.get("name") == path.parent.name
    assert fields.get("description")
    frontmatter_by_skill[path.parent.name] = fields

    for relative in re.findall(r"`(\.\./\.\./references/[^`]+)`", text):
        assert (path.parent / relative).resolve().is_file(), f"missing reference: {relative}"

for explicit_only in {"setup", "instrument", "verify"}:
    assert frontmatter_by_skill[explicit_only].get("disable-model-invocation") == "true"

problem_skill = (ROOT / "skills" / "click-tracking-audit" / "SKILL.md").read_text()
assert "when-to-use:" in problem_skill
for phrase in ("GCLID", "GBRAID", "WBRAID", "FBCLID", "UTM persistence", "offline conversion", "CRM"):
    assert phrase in problem_skill

grok_doc = (ROOT / "docs" / "GROK.md").read_text()
for reference in (
    "https://docs.x.ai/build/features/skills-plugins-marketplaces",
    "https://docs.x.ai/build/features/mcp-servers",
    "https://docs.x.ai/developers/tools/remote-mcp",
):
    assert reference in grok_doc
assert "not currently" in grok_doc and "published on npm" in grok_doc

agent = (ROOT / "agents" / "tracking-reviewer.md").read_text()
agent_parts = agent.split("---\n", 2)
assert len(agent_parts) == 3 and agent_parts[0] == ""
assert "tools: Read, Grep, Glob" in agent_parts[1]
assert "Bash" not in agent_parts[1]
assert "${CLAUDE_PLUGIN_ROOT}/references/clicktrail-safety-contract.md" in agent

for forbidden_surface in ("hooks", "bin", ".mcp.json"):
    assert not (ROOT / forbidden_surface).exists(), f"unexpected executable surface: {forbidden_surface}"

print("ClickTrail plugin structure OK")
