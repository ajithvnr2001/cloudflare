---
url: https://developers.cloudflare.com/changelog/post/2026-01-20-auxiliary-workers/
title: Use auxiliary Workers alongside full-stack frameworks \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:34.042399+00:00
---

# Use auxiliary Workers alongside full-stack frameworks · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-20-auxiliary-workers/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 20, 2026

## Use auxiliary Workers alongside full-stack frameworks

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-20-auxiliary-workers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Auxiliary Workers are now fully supported when using full-stack frameworks, such as [React Router](https://developers.cloudflare.com/workers/framework-guides/web-apps/react-router/) and [TanStack Start](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/), that integrate with the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/reference/api/). They are included alongside the framework's build output in the build output directory. Note that this feature requires Vite 7 or above.

Auxiliary Workers are additional Workers that can be called via [service bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) from your main (entry) Worker. They are defined in the plugin config, as in the example below:

vite.config.tsts
    
    
    import { defineConfig } from "vite";
    import { tanstackStart } from "@tanstack/react-start/plugin/vite";
    import { cloudflare } from "@cloudflare/vite-plugin";
    
    export default defineConfig({
    	plugins: [
    		tanstackStart(),
    		cloudflare({
    			viteEnvironment: { name: "ssr" },
    			auxiliaryWorkers: [{ configPath: "./wrangler.aux.jsonc" }],
    		}),
    	],
    });

See the Vite plugin [API docs](https://developers.cloudflare.com/workers/vite-plugin/reference/api/) for more info.
