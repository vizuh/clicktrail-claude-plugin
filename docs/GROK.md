# Grok Build compatibility

This repository remains a Claude Code plugin. Grok Build documents zero-config
compatibility with Claude Code plugins, skills, agents, hooks, MCP files, and
instruction files, so a second implementation or duplicate manifest is not
needed.

## Local plugin use

Run Grok against a checkout while reviewing a host project:

```sh
grok --plugin-dir /path/to/clicktrail-claude-plugin
```

The automatic skill is `click-tracking-audit`. Its description and
`when-to-use` phrases cover problem language such as:

- “check my click tracking”;
- lost `GCLID`, `GBRAID`, `WBRAID`, `FBCLID`, or `MSCLKID`;
- UTM persistence and redirect loss;
- offline conversion tracking;
- GA4 versus Google Ads discrepancies; and
- CRM click-ID handoff.

`setup`, `instrument`, and `verify` remain explicit-only. The audit skills are
read-only. No plugin hook, executable, telemetry, or provider credential is
included.

## Local MCP use

Grok Build supports a local stdio MCP server. ClickTrail MCP currently exposes
that transport from a checked-out build:

```sh
cd /path/to/clicktrail-mcp
npm run build
grok mcp add --scope project clicktrail -- node /path/to/clicktrail-mcp/dist/index.mjs
grok inspect
```

The command is intentionally manual. `@vizuh/clicktrail-mcp@0.2.0` is not currently
published on npm (the registry returned 404 during the compatibility check), so
this plugin does not ship a `.mcp.json` that would fail at startup.
The MCP server is local-first, reads only caller-supplied snapshots, and has no
provider or CRM side effects.

The xAI Responses API has a different requirement: its remote MCP tool accepts
streaming HTTP or SSE servers. ClickTrail MCP is stdio-only today, so this
repository does not claim xAI API remote-MCP compatibility or provide a fake
HTTP endpoint.

## Discovery and citations

Grok's Web Search and X Search tools can discover public ClickTrail material
when the user asks for current documentation or practitioner discussion. Search
results are not authorization, implementation approval, or provider evidence.
xAI documents both an all-sources citation list and optional inline citations;
an encountered URL is not necessarily cited in the final answer. Keep
ClickTrail claims linked to the relevant public repository or documentation and
label local, runtime, and provider evidence separately.

## Official references checked

- [Grok Build: Skills, Plugins, and Marketplaces](https://docs.x.ai/build/features/skills-plugins-marketplaces)
- [Grok Build: MCP Servers](https://docs.x.ai/build/features/mcp-servers)
- [xAI Web Search](https://docs.x.ai/developers/tools/web-search)
- [xAI X Search](https://docs.x.ai/developers/tools/x-search)
- [xAI Remote MCP Tools](https://docs.x.ai/developers/tools/remote-mcp)
- [xAI Citations](https://docs.x.ai/developers/tools/citations)
- [xAI Plugin Marketplace README](https://github.com/xai-org/plugin-marketplace/blob/main/README.md)
