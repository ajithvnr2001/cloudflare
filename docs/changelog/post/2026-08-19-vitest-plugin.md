---
url: https://developers.cloudflare.com/changelog/post/2026-08-19-vitest-plugin/
title: @cloudflare/vitest-pool-workers is now @cloudflare/vitest-plugin \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:09.311760+00:00
---

# @cloudflare/vitest-pool-workers is now @cloudflare/vitest-plugin · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-19-vitest-plugin/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 19, 2026

## @cloudflare/vitest-pool-workers is now @cloudflare/vitest-plugin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-19-vitest-plugin/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Version 1 of the Workers Vitest integration is published as [`@cloudflare/vitest-plugin` ↗︎](https://www.npmjs.com/package/@cloudflare/vitest-plugin). The package was formerly named `@cloudflare/vitest-pool-workers`.

The Vitest configuration API is unchanged. Existing projects must update the dependency name, package imports, and TypeScript `types` entries.

To migrate automatically, run:

npmyarnpnpm
    
    
    npx @cloudflare/codemods vitest:pool-workers-to-vitest-plugin
    
    
    yarn @cloudflare/codemods vitest:pool-workers-to-vitest-plugin
    
    
    pnpm @cloudflare/codemods vitest:pool-workers-to-vitest-plugin

The codemod updates your dependency, imports, and test TypeScript configuration. For manual migration steps, refer to [Migrate to Vitest plugin](https://developers.cloudflare.com/workers/testing/vitest-integration/migration-guides/migrate-to-vitest-plugin/).

For outbound request mocks in Workers tests, use the [`@msw/cloudflare` ↗︎](https://github.com/mswjs/cloudflare) integration. Refer to [Mock outbound requests](https://developers.cloudflare.com/workers/testing/vitest-integration/mock-outbound-requests/).
