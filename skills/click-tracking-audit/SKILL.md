---
name: click-tracking-audit
description: Diagnose lost click IDs and attribution handoffs across landing pages, redirects, consent, forms, CRM records, and offline conversions. Use when someone asks to check my click tracking, debug GCLID/GBRAID/WBRAID/FBCLID/MSCLKID loss, preserve UTMs, fix offline conversion tracking, explain a GA4 versus Google Ads discrepancy, or attach click IDs to a CRM lead.
when-to-use:
  - check my click tracking
  - why did my GCLID disappear
  - UTM persistence
  - offline conversion tracking
  - GA4 Google Ads discrepancy
  - CRM click ID handoff
user-invocable: true
metadata:
  author: Vizuh OÜ
  short-description: Find where acquisition context is lost before conversion.
---

# Audit a click-tracking handoff

Remain read-only. Do not install packages, edit files, submit forms, call an ad
platform, write to a CRM, or claim provider delivery.

1. Read the host project's instructions, tracking documentation, manifests, and
   canonical acquisition, consent, form, server, CRM, and conversion entry points.
2. Read `../../references/clicktrail-safety-contract.md`. Treat browser
   attribution as untrusted context and keep the host application authoritative
   for consent, identity, tenant, lifecycle, credentials, retries, and business
   records.
3. Trace the same allowlisted touchpoint through each boundary:
   `CAPTURE -> PERSIST -> CARRY -> ATTACH -> REPORT -> DEDUPE -> VERIFY`.
   Check GCLID, GBRAID, WBRAID, FBCLID, MSCLKID, and UTMs only where the host
   contract permits them. Look for query loss in redirects, consent-gated
   storage, SPA navigation, cross-domain transfer, form serialization, CRM
   mapping, stable event IDs, and reconciliation.
4. If the ClickTrail MCP server is already attached, pass only a caller-supplied
   source snapshot to `inspect_project`, then use
   `detect_attribution_gaps` and `diagnose_missing_click_ids`. Use
   `simulate_ad_click`, `verify_capture`, `verify_form_attachment`,
   `verify_crm_attachment`, and `attribution_health` with synthetic values only.
   `verify_conversion_delivery` is `unknown` without an explicit provider
   receipt. Never pass PII, raw requests, secrets, or arbitrary payloads.
5. Report a compact stage table with file evidence, the host-owned seam, and the
   smallest correction. Classify findings as **Critical**, **Important**, or
   **Minor**. Separate source evidence, synthetic evidence, runtime behavior,
   and provider receipt. A captured click ID alone is not conversion
   attribution.

If a user asks for current ClickTrail or Grok documentation, use public sources
and cite them. Do not turn web or X search results into implementation or
provider proof.
