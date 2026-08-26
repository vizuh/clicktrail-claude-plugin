---
name: verify
description: Verify a ClickTrail integration with local tests, package metadata, consent scenarios, payload checks, and build evidence. Use when validating, debugging, gating, or preparing a ClickTrail release.
disable-model-invocation: true
---

# Verify ClickTrail

Use the host project's own environment and documented commands.

1. Read project instructions and `../../references/clicktrail-safety-contract.md`.
2. Inspect every proposed command and the underlying package script before
   running it. Announce read-only registry metadata requests before making them.
3. Ask before any command that can call a live service, access a network other
   than read-only package metadata, mutate persistent state, or run an unclear
   `e2e`, deployment, publication, or integration script.
4. Confirm installed package versions and registry dist-tags without changing
   them.
5. Run focused consent, withdrawal, redaction, destination, retry, and tenant
   boundary tests before the full test suite.
6. Run approved typecheck, lint, and build commands using the project's package
   manager.
7. Inspect packed artifacts when the task concerns publication. Confirm license,
   manifest, expected files, exact internal versions, and absence of secrets or
   internal documentation.
8. Use a clean-room import when verifying a package release.
9. Do not call a live collector by default. A user must name and authorize a safe
   test endpoint explicitly.

Return a compact evidence table with command, result, and artifact or log path.
Separate local readiness from remote CI, registry ownership, and publication
authorization.
