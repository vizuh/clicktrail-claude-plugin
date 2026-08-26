# Marketplace submission copy

Use this text in Anthropic's community-plugin submission form after PR #1 is
reviewed, merged, and tagged.

## Plugin name

ClickTrail

## Repository

https://github.com/vizuh/clicktrail-claude-plugin

## Short description

Consent-safe ClickTrail setup, instrumentation, audit, and verification for web
applications in Claude Code.

## Detailed description

ClickTrail helps developers add and review privacy-aware attribution in Astro,
Nuxt, Vue, React, Next.js, and browser JavaScript projects. The plugin provides
four skills: setup planning, read-only auditing, explicitly approved event
instrumentation, and local verification. It also includes a read-only tracking
reviewer agent.

The plugin enforces data minimization, host-owned consent, withdrawal erasure,
public HTTPS destinations, and an explicit trust boundary: browser attribution
is context, never authorization, identity, pricing, fraud, or tenant routing.
It does not operate a collector, transmit analytics, or call live endpoints by
default.

## Category

Developer tools / observability / analytics.

## Components

- Skills: `setup`, `audit`, `instrument`, `verify`
- Agent: `tracking-reviewer`
- Hooks: none
- MCP servers: none
- Executables: none

## Invocation and mutation behavior

`setup`, `instrument`, and `verify` set `disable-model-invocation: true`;
users must invoke them explicitly. `audit` is read-only. `verify` uses the host project's local
commands and does not call live collectors without a separately explicit user
authorization.

## Data and network behavior

The plugin stores and sends no telemetry. It contains no credentials. It makes
no network call by itself. A skill may recommend read-only npm metadata checks
or package installation after user review. Live collector calls are forbidden
by default.

## Validation

```bash
python3 scripts/validate.py
claude plugin validate . --strict
```

GitHub Actions runs both checks on every pull request.

## Maintainer

Vizuh OÜ — https://vizuh.com

## License

MIT
