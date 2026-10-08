---
url: https://developers.cloudflare.com/workers/vite-plugin/get-started/
title: Get started \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:04.207074+00:00
---

# Get started · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/vite-plugin/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/)
  4. /Get started



# Get started

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/vite-plugin/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewStart with a basic package.jsonInstall the dependenciesCreate your Vite config file and include the Cloudflare pluginCreate your Worker config fileCreate your Worker entry fileDev, build, preview and deploy

Note

This guide demonstrates creating a standalone Worker from scratch. If you would instead like to create a new application from a ready-to-go template, refer to the [TanStack Start](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/), [React Router](https://developers.cloudflare.com/workers/framework-guides/web-apps/react-router/), [React](https://developers.cloudflare.com/workers/framework-guides/web-apps/react/) or [Vue](https://developers.cloudflare.com/workers/framework-guides/web-apps/vue/) framework guides.

## Start with a basic `package.json`

package.jsonjson
    
    
    {
    	"name": "cloudflare-vite-get-started",
    	"private": true,
    	"version": "0.0.0",
    	"type": "module",
    	"scripts": {
    		"dev": "vite dev",
    		"build": "vite build",
    		"preview": "npm run build && vite preview",
    		"deploy": "npm run build && wrangler deploy"
    	}
    }

Note

Ensure that you include `"type": "module"` in order to use ES modules by default.

## Install the dependencies

npmyarnpnpmbun
    
    
    npm i -D vite @cloudflare/vite-plugin wrangler
    
    
    yarn add -D vite @cloudflare/vite-plugin wrangler
    
    
    pnpm add -D vite @cloudflare/vite-plugin wrangler
    
    
    bun add -d vite @cloudflare/vite-plugin wrangler

## Create your Vite config file and include the Cloudflare plugin

vite.config.tsts
    
    
    import { defineConfig } from "vite";
    import { cloudflare } from "@cloudflare/vite-plugin";
    
    export default defineConfig({
    	plugins: [cloudflare()],
    });

The Cloudflare Vite plugin doesn't require any configuration by default and will look for a `wrangler.jsonc`, `wrangler.json` or `wrangler.toml` in the root of your application.

Refer to the [API reference](https://developers.cloudflare.com/workers/vite-plugin/reference/api/) for configuration options.

## Create your Worker config file
    
    
    {
    	"$schema": "./node_modules/wrangler/config-schema.json",
    	"name": "cloudflare-vite-get-started",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"main": "./src/index.ts"
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "cloudflare-vite-get-started"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    main = "./src/index.ts"

The `name` field specifies the name of your Worker. By default, this is also used as the name of the Worker's Vite Environment (see [Vite Environments](https://developers.cloudflare.com/workers/vite-plugin/reference/vite-environments/) for more information). The `main` field specifies the entry file for your Worker code.

For more information about the Worker configuration, see [Configuration](https://developers.cloudflare.com/workers/wrangler/configuration/).

## Create your Worker entry file

src/index.tsts
    
    
    export default {
    	fetch() {
    		return new Response(`Running in ${navigator.userAgent}!`);
    	},
    };

A request to this Worker will return **'Running in Cloudflare-Workers!'** , demonstrating that the code is running inside the Workers runtime.

## Dev, build, preview and deploy

You can now start the Vite development server (`npm run dev`), build the application (`npm run build`), preview the built application (`npm run preview`), and deploy to Cloudflare (`npm run deploy`).

[PreviousOverview](https://developers.cloudflare.com/workers/vite-plugin/)[NextTutorial - React SPA with an API](https://developers.cloudflare.com/workers/vite-plugin/tutorial/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/vite-plugin/get-started.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
