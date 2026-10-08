---
url: https://developers.cloudflare.com/workers/testing/vitest-integration/migration-guides/migrate-to-vitest-plugin/
title: Migrate to Vitest plugin \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:59.008464+00:00
---

# Migrate to Vitest plugin · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/vitest-integration/migration-guides/migrate-to-vitest-plugin/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)[Vitest integration](https://developers.cloudflare.com/workers/testing/vitest-integration/)

  4. /Migration guides
  5. /Migrate to Vitest plugin



# Migrate to Vitest plugin

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/vitest-integration/migration-guides/migrate-to-vitest-plugin/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRun the codemodUpdate manuallyUpdate request mocking

`@cloudflare/vitest-plugin` replaces `@cloudflare/vitest-pool-workers`. The package API and Vitest configuration are unchanged.

## Run the codemod

To update your project automatically, run the following command from the project root:

npmyarnpnpm
    
    
    npx @cloudflare/codemods vitest:pool-workers-to-vitest-plugin
    
    
    yarn @cloudflare/codemods vitest:pool-workers-to-vitest-plugin
    
    
    pnpm @cloudflare/codemods vitest:pool-workers-to-vitest-plugin

Use `--dry-run` to preview the changes. Use `--files <glob>` to limit the files the codemod updates.

The codemod updates your dependency, imports, and test TypeScript configuration.

## Update manually

If you cannot run the codemod, update the package name in your `package.json`, imports, and test `tsconfig.json`:
    
    
    - "@cloudflare/vitest-pool-workers": "^0.16.0"
    + "@cloudflare/vitest-plugin": "^1.0.0"
    
    - import { cloudflareTest } from "@cloudflare/vitest-pool-workers";
    + import { cloudflareTest } from "@cloudflare/vitest-plugin";
    
    - "types": ["@cloudflare/vitest-pool-workers/types"]
    + "types": ["@cloudflare/vitest-plugin/types"]

The same rename applies to subpath imports, including `@cloudflare/vitest-plugin/config`.

## Update request mocking

To mock outbound requests, use [`@msw/cloudflare` ↗︎](https://github.com/mswjs/cloudflare). For setup instructions, refer to [Mock outbound requests](https://developers.cloudflare.com/workers/testing/vitest-integration/mock-outbound-requests/).

[PreviousKnown issues](https://developers.cloudflare.com/workers/testing/vitest-integration/known-issues/)[NextMigrate from Vitest 3 to Vitest 4](https://developers.cloudflare.com/workers/testing/vitest-integration/migration-guides/migrate-from-vitest-3-to-vitest-4/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/vitest-integration/migration-guides/migrate-to-vitest-plugin.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
