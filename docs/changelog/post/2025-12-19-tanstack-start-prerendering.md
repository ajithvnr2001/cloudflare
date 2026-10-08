---
url: https://developers.cloudflare.com/changelog/post/2025-12-19-tanstack-start-prerendering/
title: Static prerendering support for TanStack Start \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:32.553939+00:00
---

# Static prerendering support for TanStack Start · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-19-tanstack-start-prerendering/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 19, 2025

## Static prerendering support for TanStack Start

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-19-tanstack-start-prerendering/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[TanStack Start ↗︎](https://tanstack.com/start/) apps can now prerender routes to static HTML at build time with access to build time environment variables and bindings, and serve them as [static assets](https://developers.cloudflare.com/workers/static-assets/). To enable prerendering, configure the `prerender` option of the TanStack Start plugin in your Vite config:

vite.config.tsts
    
    
    import { defineConfig } from "vite";
    import { cloudflare } from "@cloudflare/vite-plugin";
    import { tanstackStart } from "@tanstack/react-start/plugin/vite";
    
    export default defineConfig({
      plugins: [
        cloudflare({ viteEnvironment: { name: "ssr" } }),
        tanstackStart({
          prerender: {
            enabled: true,
          },
        }),
      ],
    });

This feature requires `@tanstack/react-start` v1.138.0 or later. See the [TanStack Start framework guide](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/#static-prerendering) for more details.
