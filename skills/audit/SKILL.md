---
name: audit
description: Audit an existing ClickTrail or attribution implementation for consent, PII, unsafe destinations, tenant spoofing, trust-boundary errors, and missing tests. Use for tracking reviews, privacy checks, or pre-release audits.
---

# Audit ClickTrail

Remain read-only. Do not install packages, edit files, or call live endpoints.

1. Read project instructions, tracking docs, manifests, and the integration entry
   points.
2. Read `../../references/clicktrail-safety-contract.md`.
3. Trace startup, capture, persistence, delivery, withdrawal, stop, and retry
   paths. Inspect every caller of shared constructors or serializers.
4. Check that trusted host configuration wins over caller-controlled attribution.
5. Check server destinations for public credential-free HTTPS enforcement.
6. Check payloads against a concrete allowlist. Treat arbitrary objects and raw
   passthrough as findings even when current callers appear safe.
7. Check tests for observable consent-denial, withdrawal-erasure, redaction,
   SSRF, delivery-failure, and tenant-collision behavior.

Report findings as **Critical**, **Important**, or **Minor**. Each finding must
name the file, behavior, impact, and smallest safe correction. End with verified
passes and unresolved evidence. Do not turn missing evidence into a pass.
