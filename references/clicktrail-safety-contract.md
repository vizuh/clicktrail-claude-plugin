# ClickTrail safety contract

Apply these rules to every setup, audit, instrumentation, and verification task.

## Consent

- The host application owns the consent decision.
- Do not start ClickTrail or persist attribution until consent is granted.
- On withdrawal, atomically revoke consent and stop capture/delivery first.
  Then erase ClickTrail-owned storage and queued/buffered events without flushing.
  Verify that no later write or send can occur until a new grant.
- Never weaken a host's existing consent management platform integration.

## Data minimization

Allow metadata needed for measurement, such as an approved event name, page
location, referrer, UTM fields, click identifiers, and documented commerce
amount/currency fields. Reject or remove:

- names, email addresses, phone numbers, postal addresses, and account IDs;
- message, prompt, completion, transcript, form-body, and search-query content;
- raw requests, headers, cookies, authorization data, and arbitrary JSON;
- visitor/session identifiers supplied by untrusted callers;
- secrets or environment values.

When an event taxonomy or field allowlist is absent, stop and ask rather than
inventing one.

## Trust boundary

Attribution is observed browser context. Never use it to decide authorization,
identity, price, entitlements, workflow, fraud, or tenant routing. Trusted host
configuration must win over caller-controlled fields.

## Destinations

Server-side collectors must use public, credential-free HTTPS URLs. Require an
exact host allowlist where possible. Resolve at connection time and reject every
non-public address, mixed public/private answer, loopback, private, link-local,
metadata, local/internal, reserved, or embedded-credential destination. Recheck
redirect targets and pin the validated destination or connection when the host
supports it. A hostname that passed a text check is not sufficient protection
against DNS rebinding.

## Change discipline

- Read the host project's instructions and tracking documentation first.
- Show the intended event and file changes before editing.
- Make the smallest sufficient diff.
- Add observable behavior tests for consent, redaction, and failure paths.
- Never call a live collector during verification unless the user explicitly
  names a safe test endpoint and authorizes the call.
