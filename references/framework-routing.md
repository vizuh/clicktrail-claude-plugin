# Framework routing

Choose a published package only after checking its current npm metadata.

| Host | Preferred package | Notes |
|---|---|---|
| Astro | `@vizuh/clicktrail-astro` | Use the integration's consent-aware client and first-party proxy when required. |
| Nuxt | `@vizuh/clicktrail-nuxt` | Nuxt is the supported Vue-framework route. |
| Plain Vue | `@vizuh/clicktrail-browser` | There is no standalone Vue adapter. Integrate lifecycle explicitly. |
| React or Next.js | `@vizuh/clicktrail-browser` | No standalone React adapter. Keep startup client-side and consent-gated. |
| Browser JavaScript | `@vizuh/clicktrail-browser` | Use the smallest browser API surface. |
| Server-only JavaScript | `@vizuh/clicktrail-core` plus an approved server integration | Do not invent a server collector contract. |

SvelteKit, Qwik, consent, server, Formbricks, Typebot, Directus, n8n, and other
packages may exist in source without being approved for the current npm release
wave. Verify registry availability and project documentation before recommending
them. Activepieces is explicitly deferred while its SDK dependency risk remains.

Never install a package just because a source directory exists.
