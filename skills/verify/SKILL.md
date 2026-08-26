---
name: verify
description: Verify a ClickTrail integration with local tests, package metadata, consent scenarios, payload checks, and build evidence. Use when validating, debugging, gating, or preparing a ClickTrail release.
---

# Verify ClickTrail

Use the host project's own environment and documented commands.

1. Read project instructions and `../../references/clicktrail-safety-contract.md`.
2. Confirm installed package versions and registry dist-tags without changing
   them.
3. Run focused consent, withdrawal, redaction, destination, retry, and tenant
   boundary tests before the full test suite.
4. Run typecheck, lint, and build using the project's package manager.
5. Inspect packed artifacts when the task concerns publication. Confirm license,
   manifest, expected files, exact internal versions, and absence of secrets or
   internal documentation.
6. Use a clean-room import when verifying a package release.
7. Do not call a live collector by default. A user must name and authorize a safe
   test endpoint explicitly.

Return a compact evidence table with command, result, and artifact or log path.
Separate local readiness from remote CI, registry ownership, and publication
authorization.
