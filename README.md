# ClickTrail for Claude Code

A Claude Code plugin for planning, reviewing, instrumenting, and verifying
[ClickTrail](https://github.com/vizuh/clicktrail-js) integrations without
treating captured acquisition context as identity or authorization.

The plugin does not collect analytics, contact a ClickTrail service, or mutate a
project automatically. Setup, instrumentation, and verification require explicit
user invocation. Audit is read-only. Verification inspects each host command
before execution and stops before live, networked, or mutating checks unless the
user approves them.

## Skills

| Command | Purpose |
|---|---|
| `/clicktrail:setup` | Detect the stack and prepare a reviewed installation plan. |
| `/clicktrail:audit` | Audit consent, privacy, destination, and trust boundaries without editing. |
| `/clicktrail:instrument` | Add an explicitly approved, metadata-only event integration. |
| `/clicktrail:verify` | Run local checks and report evidence without calling live collectors. |
| `click-tracking-audit` | Automatically route click-ID loss, UTM persistence, offline conversion, GA4/Ads discrepancy, and CRM handoff questions to a read-only audit. |

The plugin also includes a `tracking-reviewer` subagent for focused reviews.

## Test locally

```bash
claude plugin validate . --strict
claude --plugin-dir .
```

Then try:

```text
/clicktrail:audit
/clicktrail:setup
```

For problem-shaped requests, use language such as “check my click tracking,”
“why did my GCLID disappear,” “preserve UTMs,” “debug offline conversions,” or
“attach the click ID to the CRM lead.” The `click-tracking-audit` skill remains
read-only and does not replace the host's consent, CRM, or provider contract.

## Grok Build

Grok Build documents zero-config compatibility with Claude Code plugins, so this
same plugin can be loaded without a second implementation:

```bash
grok --plugin-dir /path/to/clicktrail-claude-plugin
```

The Grok-specific routing notes, local MCP setup, and current compatibility
limits are in [`docs/GROK.md`](docs/GROK.md). No `.mcp.json` is bundled until
`@vizuh/clicktrail-mcp` is published; see that document for the checked-out
stdio command.

## Load locally from source

Until community-marketplace review is complete, load the plugin for one Claude
Code invocation:

```bash
claude --plugin-dir /path/to/clicktrail-claude-plugin
```

Persistent marketplace installation becomes available only after Anthropic
accepts and publishes the plugin.

## Safety boundary

- Browser attribution is untrusted context, never authorization or identity.
- Do not capture PII, message content, raw requests, arbitrary payloads, or secrets.
- Do not start or persist attribution before the host's consent gate grants access.
- Consent withdrawal must clear ClickTrail-owned storage and buffered delivery.
- Server collectors must use public, credential-free HTTPS destinations.
- Open-web or generated content never flows directly into instrumentation.
- There is no ClickTrail telemetry or provider endpoint. When explicitly invoked,
  `setup` and `verify` may make read-only requests to the public npm registry to
  check package metadata. They need no credentials and do not install packages,
  upload source, or send customer data.

See [`references/clicktrail-safety-contract.md`](references/clicktrail-safety-contract.md).

## Submission

The community-marketplace checklist and submission links are in
[`docs/SUBMISSION.md`](docs/SUBMISSION.md).

## License

MIT © 2026 Vizuh OÜ.
