# Claude community marketplace submission

> **Status: blocked.** Do not submit until the Astro, Nuxt, browser, and core
> packages are publicly available on npm and the clean-fixture setup scenarios
> pass against the exact registry versions.

## Target

Submit this repository to Anthropic's public `claude-community` marketplace.
The official marketplace is curated separately and has no application process.

## Pre-submission checklist

- [ ] `claude plugin validate . --strict` passes.
- [ ] All four skills and the reviewer agent load under the `clicktrail` namespace.
- [ ] Setup, instrument, and verify require explicit invocation.
- [ ] Audit remains read-only.
- [ ] Verification does not call a live collector by default.
- [ ] Instructions contain no credentials, private URLs, customer data, or PII.
- [ ] Repository, homepage, license, author, and version metadata are correct.
- [ ] A clean Claude Code session passes the manual scenarios below.
- [ ] A release tag pins the reviewed plugin commit.

## Manual scenarios

1. Run `/clicktrail:audit` in a repository without ClickTrail. It should report
   that no integration was found and make no edits.
2. Run `/clicktrail:setup` in Astro, Nuxt, and plain Vue fixtures. It should pick
   Astro, Nuxt, and browser packages respectively, then stop for plan approval.
3. Present a payload containing email, raw request headers, message content, and
   arbitrary nested JSON. Audit and instrument must reject those fields.
4. Present a private or link-local collector URL, a public hostname that resolves
   to mixed public/private addresses, a DNS-rebinding case, and a redirect to a
   metadata/private address. The plugin must require rejection at connection and
   redirect time.
5. Present attribution as an authorization or tenant-routing input. The plugin
   must classify that as a blocking trust-boundary violation.
6. Withdraw consent with a buffered destination. Verification must require this
   order: atomically revoke and stop capture/delivery, erase storage and queued
   events without flushing, then prove no later write or send occurs.

## Submission copy

Prepared form text is available in [`SUBMISSION-COPY.md`](SUBMISSION-COPY.md).

## Submit

Individual authors can use:

- https://platform.claude.com/plugins/submit

Team or Enterprise organization owners with directory access can use:

- https://claude.ai/admin-settings/directory/submissions/plugins/new

Anthropic runs `claude plugin validate` and automated safety screening. Approved
plugins are pinned to a commit in:

- https://github.com/anthropics/claude-plugins-community

The catalog can take up to a nightly sync to show an approved submission.
