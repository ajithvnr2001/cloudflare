---
url: https://developers.cloudflare.com/changelog/post/2025-10-24-tanstack-start/
title: Build TanStack Start apps with the Cloudflare Vite plugin \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:27.114965+00:00
---

# Build TanStack Start apps with the Cloudflare Vite plugin · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-24-tanstack-start/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 24, 2025

## Build TanStack Start apps with the Cloudflare Vite plugin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-24-tanstack-start/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/) now supports [TanStack Start ↗︎](https://tanstack.com/start/) apps. Get started with new or existing projects.

#### New projects

Create a new TanStack Start project that uses the Cloudflare Vite plugin via the `create-cloudflare` CLI:

npmyarnpnpm
    
    
    npm create cloudflare@latest -- my-tanstack-start-app --framework=tanstack-start
    
    
    yarn create cloudflare my-tanstack-start-app --framework=tanstack-start
    
    
    pnpm create cloudflare@latest my-tanstack-start-app --framework=tanstack-start

#### Existing projects

Migrate an existing TanStack Start project to use the Cloudflare Vite plugin:

  1. Install `@cloudflare/vite-plugin` and `wrangler`



npmyarnpnpmbun
    
    
    npm i -D @cloudflare/vite-plugin wrangler
    
    
    yarn add -D @cloudflare/vite-plugin wrangler
    
    
    pnpm add -D @cloudflare/vite-plugin wrangler
    
    
    bun add -d @cloudflare/vite-plugin wrangler

  2. Add the Cloudflare plugin to your Vite config

vite.config.tsts
    
    
    import { defineConfig } from "vite";
    import { tanstackStart } from "@tanstack/react-start/plugin/vite";
    import viteReact from "@vitejs/plugin-react";
    import { cloudflare } from "@cloudflare/vite-plugin";
    
    export default defineConfig({
    	plugins: [
    		cloudflare({ viteEnvironment: { name: "ssr" } }),
    		tanstackStart(),
    		viteReact(),
    	],
    });

  3. Add your Worker config file


    
    
    {
    	"$schema": "./node_modules/wrangler/config-schema.json",
    	"name": "my-tanstack-start-app",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"compatibility_flags": [
    		"nodejs_compat"
    	],
    	"main": "@tanstack/react-start/server-entry"
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "my-tanstack-start-app"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    compatibility_flags = [ "nodejs_compat" ]
    main = "@tanstack/react-start/server-entry"

  4. Modify the scripts in your `package.json`

package.jsonjson
    
    
    {
    	"scripts": {
    		"dev": "vite dev",
    		"build": "vite build && tsc --noEmit",
    		"start": "node .output/server/index.mjs",
    		"preview": "vite preview",
    		"deploy": "npm run build && wrangler deploy",
    		"cf-typegen": "wrangler types"
    	}
    }

See the [TanStack Start framework guide](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/) for more info.
