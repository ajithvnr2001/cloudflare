---
url: https://developers.cloudflare.com/changelog/post/2025-12-08-vite-optional-config/
title: Wrangler config is optional when using Vite plugin \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:31.253678+00:00
---

# Wrangler config is optional when using Vite plugin · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-08-vite-optional-config/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 8, 2025

## Wrangler config is optional when using Vite plugin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-08-vite-optional-config/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When using the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/) to build and deploy Workers, a Wrangler configuration file is now optional for assets-only (static) sites. If no `wrangler.toml`, `wrangler.json`, or `wrangler.jsonc` file is found, the plugin generates sensible defaults for an assets-only site. The `name` is based on the `package.json` or the project directory name, and the `compatibility_date` uses the latest date supported by your installed Miniflare version.

This allows easier setup for static sites using Vite. Note that SPAs will still need to [set `assets.not_found_handling` to `single-page-application` ↗︎](https://developers.cloudflare.com/workers/static-assets/routing/single-page-application/) in order to function correctly.
