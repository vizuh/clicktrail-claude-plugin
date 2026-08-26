---
name: setup
description: Prepare a consent-safe ClickTrail installation plan for Astro, Nuxt, Vue, React, Next.js, or browser JavaScript projects. Use when the user asks to install, add, configure, or set up ClickTrail.
disable-model-invocation: true
---

# Set up ClickTrail

This skill plans setup before changing files. Explicit invocation authorizes
inspection, not automatic mutation.

1. Read the nearest project instructions and tracking documentation.
2. Detect the framework, package manager, runtime boundary, and existing consent
   management platform. Do not infer consent from cookie presence.
3. Read `../../references/framework-routing.md` and select only a package that
   is currently published. Confirm with `npm view <package> version dist-tags --json`.
4. Read `../../references/clicktrail-safety-contract.md`.
5. Ask for the approved event taxonomy, consent-grant signal, withdrawal signal,
   collector destination, and retention policy when any is missing.
6. Present a file-by-file plan covering installation, lifecycle, storage,
   withdrawal erasure, destination validation, and tests.
7. Stop for approval before installing dependencies or editing code.

Never create a standalone Vue/React adapter, invent event names, call a live
collector, or add a direct analytics vendor dependency during setup.
