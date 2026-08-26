---
name: instrument
description: Add an explicitly approved ClickTrail event or integration using a metadata allowlist and consent-aware lifecycle. Use when the user asks to instrument a page, conversion, sale, form, or application event.
disable-model-invocation: true
---

# Instrument an approved event

Do not begin when the event name, field allowlist, consent contract, or target
files are unknown.

1. Read project instructions, existing tracking code, and
   `../../references/clicktrail-safety-contract.md`.
2. State the exact files, event name, fields, consent condition, and test changes.
3. Get approval for that mutation set.
4. Reuse the host's ClickTrail client and event taxonomy. Do not add a second
   client, direct vendor SDK, or hardcoded analytics call.
5. Build the payload from an explicit allowlist. Never pass form objects, request
   objects, cookies, user profiles, arbitrary `data`, or spread caller input.
6. Keep attribution informational. Trusted context must control tenant and site
   routing.
7. Add behavior tests proving denial produces no persistence/delivery and
   withdrawal clears owned state and queues.
8. Run the host project's tests, typecheck, lint, and build. Report any skipped
   check and why.

Stop on the first unexpected mutation or live network request.
