---
url: https://developers.cloudflare.com/changelog/post/2026-01-13-wrangler-types-multi-environment/
title: `wrangler types` now generates types for all environments \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:33.561019+00:00
---

# `wrangler types` now generates types for all environments · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-13-wrangler-types-multi-environment/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 13, 2026

## `wrangler types` now generates types for all environments

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-13-wrangler-types-multi-environment/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The `wrangler types` command now generates TypeScript types for bindings from **all environments** defined in your Wrangler configuration file by default.

Previously, `wrangler types` only generated types for bindings in the top-level configuration (or a single environment when using the `--env` flag). This meant that if you had environment-specific bindings — for example, a KV namespace only in production or an R2 bucket only in staging — those bindings would be missing from your generated types, causing TypeScript errors when accessing them.

Now, running `wrangler types` collects bindings from all environments and includes them in the generated `Env` type. This ensures your types are complete regardless of which environment you deploy to.

#### Generating types for a specific environment

If you want the previous behavior of generating types for only a specific environment, you can use the `--env` flag:
    
    
    wrangler types --env production

Learn more about [generating types for your Worker](https://developers.cloudflare.com/workers/wrangler/commands/general/#types) in the Wrangler documentation.
