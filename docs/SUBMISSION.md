# Claude community marketplace submission

## Target

Submit this repository to Anthropic's public `claude-community` marketplace.
The official marketplace is curated separately and has no application process.

## Pre-submission checklist

- [ ] `claude plugin validate . --strict` passes.
- [ ] All four skills load under the `clicktrail` namespace.
- [ ] Setup and instrument require explicit invocation.
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
4. Present a private or link-local collector URL. The plugin must reject it.
5. Present attribution as an authorization or tenant-routing input. The plugin
   must classify that as a blocking trust-boundary violation.
6. Withdraw consent with a buffered destination. Verification must require
   storage and queue erasure evidence.

## Submit

Individual authors can use:

- https://platform.claude.com/plugins/submit

Team or Enterprise organization owners with directory access can use:

- https://claude.ai/admin-settings/directory/submissions/plugins/new

Anthropic runs `claude plugin validate` and automated safety screening. Approved
plugins are pinned to a commit in:

- https://github.com/anthropics/claude-plugins-community

The catalog can take up to a nightly sync to show an approved submission.
