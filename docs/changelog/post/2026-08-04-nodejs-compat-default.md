---
url: https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/
title: Node.js compatibility is now enabled by default \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:06.591289+00:00
---

# Node.js compatibility is now enabled by default · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 4, 2026

## Node.js compatibility is now enabled by default

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers now enable the `nodejs_compat` and `nodejs_compat_v2` compatibility flags by default for [compatibility dates](https://developers.cloudflare.com/workers/configuration/compatibility-dates/) of `2026-08-04` or later. These flags are not used for these compatibility dates because the compatibility date enables the same behavior.

This means all [Node.js built-in APIs](https://developers.cloudflare.com/workers/runtime-apis/nodejs/) supported by the Workers runtime are available by default, including `node:crypto`, `node:buffer`, `node:stream`, `node:net`, `node:dns`, `node:fs`, `node:http`, and more. npm packages that depend on these APIs will work without additional configuration.

Workers using an earlier compatibility date are not affected. They can still opt in by adding `nodejs_compat` to `compatibility_flags`.

New projects do not need to add either flag. Existing projects can update their compatibility date without removing them. Wrangler, Miniflare, the Cloudflare Vite plugin, and Vitest Pool Workers ignore these redundant flags when starting the runtime.

To turn off Node.js compatibility completely, remove any `nodejs_compat` and `nodejs_compat_v2` flags. Then add both of the following flags:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      // Set this to today's date
      "compatibility_date": "2026-10-08",
      "compatibility_flags": [
        "no_nodejs_compat",
        "no_nodejs_compat_v2"
      ]
    }
    
    
    # Set this to today's date
    compatibility_date = "2026-10-08"
    compatibility_flags = ["no_nodejs_compat", "no_nodejs_compat_v2"]

For more information, refer to the [Node.js compatibility documentation](https://developers.cloudflare.com/workers/runtime-apis/nodejs/).
