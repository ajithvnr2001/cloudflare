---
url: https://developers.cloudflare.com/changelog/post/2026-09-08-miniflare-v5/
title: Miniflare v5 prepares local development for the cf CLI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.560837+00:00
---

# Miniflare v5 prepares local development for the cf CLI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-08-miniflare-v5/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 8, 2026

## Miniflare v5 prepares local development for the cf CLI

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Miniflare v5 prepares Cloudflare local development tooling for the upcoming `cf` CLI.

Miniflare powers local Workers development behind `wrangler dev`, the Cloudflare Vite plugin, and `@cloudflare/vitest-plugin`. Most projects should use those tools instead of depending on Miniflare directly, and Miniflare v5 will not require any action.

The most significant change is a new configuration shape which aligns Miniflare with `cloudflare.config.ts`, the programmatic Cloudflare configuration format now available for testing.

Other breaking changes include:

  * Removed deprecated APIs and options, such as legacy alpha D1 bindings.
  * Removed now-unused, internal APIs like `wrappedBindings`
  * Removed Miniflare's built-in module discovery; higher-level tools like Wrangler and the Vite plugin should be providing the module graph.
  * Moved local-only /cdn-cgi routes under /cdn-cgi/local.
  * Replaced per-resource persistence options with shared persistence root options.



For a more comprehensive list, refer to [Miniflare's changelog ↗︎](https://github.com/cloudflare/workers-sdk/blob/main/packages/miniflare/CHANGELOG.md#5202607300-alpha)

This work sets up a cleaner foundation for the next generation of local development tooling, including the new `cf` CLI.
