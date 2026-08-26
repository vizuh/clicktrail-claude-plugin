# ClickTrail for Claude Code

A Claude Code plugin for installing, reviewing, and verifying consent-safe
[ClickTrail](https://github.com/vizuh/clicktrail-js) integrations.

The plugin does not collect analytics, contact a ClickTrail service, or mutate a
project automatically. Setup and instrumentation skills require explicit user
invocation. Audit is read-only. Verification uses the host project's own tools.

## Skills

| Command | Purpose |
|---|---|
| `/clicktrail:setup` | Detect the stack and prepare a reviewed installation plan. |
| `/clicktrail:audit` | Audit consent, privacy, destination, and trust boundaries without editing. |
| `/clicktrail:instrument` | Add an explicitly approved, metadata-only event integration. |
| `/clicktrail:verify` | Run local checks and report evidence without calling live collectors. |

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

## Install from source

Until community-marketplace review is complete:

```bash
claude --plugin-dir /path/to/clicktrail-claude-plugin
```

## Safety boundary

- Browser attribution is untrusted context, never authorization or identity.
- Do not capture PII, message content, raw requests, arbitrary payloads, or secrets.
- Do not start or persist attribution before the host's consent gate grants access.
- Consent withdrawal must clear ClickTrail-owned storage and buffered delivery.
- Server collectors must use public, credential-free HTTPS destinations.
- Open-web or generated content never flows directly into instrumentation.

See [`references/clicktrail-safety-contract.md`](references/clicktrail-safety-contract.md).

## Submission

The community-marketplace checklist and submission links are in
[`docs/SUBMISSION.md`](docs/SUBMISSION.md).

## License

MIT © 2026 Vizuh OÜ.
