---
url: https://developers.cloudflare.com/changelog/post/2026-01-20-sql-module-rule/
title: Import SQL files as additional modules by default \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:44.782137+00:00
---

# Import SQL files as additional modules by default · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-20-sql-module-rule/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 20, 2026

## Import SQL files as additional modules by default

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The `.sql` file extension is now automatically configured to be importable in your Worker code when using [Wrangler](https://developers.cloudflare.com/workers/wrangler/bundling/#including-non-javascript-modules) or the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/reference/non-javascript-modules/). This is particular useful for importing migrations in Durable Objects and means you no longer need to configure custom rules when using [Drizzle ↗︎](https://orm.drizzle.team/docs/connect-cloudflare-do).

SQL files are imported as JavaScript strings:
    
    
    // `example` will be a JavaScript string
    import example from "./example.sql";
