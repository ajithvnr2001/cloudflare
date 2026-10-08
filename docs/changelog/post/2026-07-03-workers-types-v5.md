---
url: https://developers.cloudflare.com/changelog/post/2026-07-03-workers-types-v5/
title: Simpler runtime types with @cloudflare/workers-types v5 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:01.326658+00:00
---

# Simpler runtime types with @cloudflare/workers-types v5 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-03-workers-types-v5/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 3, 2026

## Simpler runtime types with @cloudflare/workers-types v5

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-03-workers-types-v5/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We have released version 5 of [`@cloudflare/workers-types` ↗︎](https://www.npmjs.com/package/@cloudflare/workers-types). This release simplifies the package to expose only the latest runtime types.

We still recommend that you generate types for your Worker using [`wrangler types`](https://developers.cloudflare.com/workers/wrangler/commands/general/#types), but if you want to use the package directly, you can install it with your package manager of choice:

npmyarnpnpmbun
    
    
    npm i -D @cloudflare/workers-types@latest
    
    
    yarn add -D @cloudflare/workers-types@latest
    
    
    pnpm add -D @cloudflare/workers-types@latest
    
    
    bun add -d @cloudflare/workers-types@latest

The package now exposes two entrypoints:

  * `@cloudflare/workers-types` reflects the latest compatibility date, using the latest stable compatibility flags.
  * `@cloudflare/workers-types/experimental` reflects APIs behind experimental compatibility flags.



The dated entrypoints, such as `@cloudflare/workers-types/2022-11-30` and `@cloudflare/workers-types/2023-03-01`, are removed. With runtime type generation in [Wrangler v4](https://developers.cloudflare.com/workers/wrangler/), you can generate these with the `wrangler types` command to create types locked to your Worker's compatibility date.

For more information, refer to [TypeScript language support](https://developers.cloudflare.com/workers/languages/typescript/).
