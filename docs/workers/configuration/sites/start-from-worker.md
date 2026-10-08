---
url: https://developers.cloudflare.com/workers/configuration/sites/start-from-worker/
title: Start from Worker \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:16.600920+00:00
---

# Start from Worker · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/configuration/sites/start-from-worker/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Configuration](https://developers.cloudflare.com/workers/configuration/)

  4. /[Workers Sites](https://developers.cloudflare.com/workers/configuration/sites/)
  5. /Start from Worker



# Start from Worker

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/configuration/sites/start-from-worker/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGetting started

Use Workers Static Assets Instead

You should use [Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/) to host full-stack applications instead of Workers Sites. It has been deprecated in Wrangler v4, and the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/) does not support Workers Sites. Do not use Workers Sites for new projects.

Workers Sites require [Wrangler ↗︎](https://github.com/cloudflare/workers-sdk/tree/main/packages/wrangler) — make sure to use the [latest version](https://developers.cloudflare.com/workers/wrangler/install-and-update/#update-wrangler).

If you have a pre-existing Worker project, you can use Workers Sites to serve static assets to the Worker.

## Getting started

  1. Create a directory that will contain the assets in the root of your project (for example, `./public`)

  2. Add configuration to your Wrangler file to point to it.
         
         {
           "site": {
             "bucket": "./public" // Add the directory with your static assets!
           }
         }
         
         [site]
         bucket = "./public"

  3. Install the `@cloudflare/kv-asset-handler` package in your project:
         
         npm i -D @cloudflare/kv-asset-handler

  4. Import the `getAssetFromKV()` function into your Worker entry point and use it to respond with static assets.



    
    
    import { getAssetFromKV } from "@cloudflare/kv-asset-handler";
    import manifestJSON from "__STATIC_CONTENT_MANIFEST";
    const assetManifest = JSON.parse(manifestJSON);
    
    export default {
    	async fetch(request, env, ctx) {
    		try {
    			// Add logic to decide whether to serve an asset or run your original Worker code
    			return await getAssetFromKV(
    				{
    					request,
    					waitUntil: ctx.waitUntil.bind(ctx),
    				},
    				{
    					ASSET_NAMESPACE: env.__STATIC_CONTENT,
    					ASSET_MANIFEST: assetManifest,
    				},
    			);
    		} catch (e) {
    			let pathname = new URL(request.url).pathname;
    			return new Response(`"${pathname}" not found`, {
    				status: 404,
    				statusText: "not found",
    			});
    		}
    	},
    };
    
    
    import { getAssetFromKV } from "@cloudflare/kv-asset-handler";
    
    addEventListener("fetch", (event) => {
    	event.respondWith(handleEvent(event));
    });
    
    async function handleEvent(event) {
    	try {
    		// Add logic to decide whether to serve an asset or run your original Worker code
    		return await getAssetFromKV(event);
    	} catch (e) {
    		let pathname = new URL(event.request.url).pathname;
    		return new Response(`"${pathname}" not found`, {
    			status: 404,
    			statusText: "not found",
    		});
    	}
    }

For more information on the configurable options of `getAssetFromKV()` refer to [kv-asset-handler docs ↗︎](https://github.com/cloudflare/workers-sdk/tree/main/packages/kv-asset-handler).

  5. Run `wrangler deploy` or `npx wrangler deploy` as you would normally with your Worker project. Wrangler will automatically upload the assets found in the configured directory.
         
         npx wrangler deploy




[PreviousStart from scratch](https://developers.cloudflare.com/workers/configuration/sites/start-from-scratch/)[NextWorkers Sites configuration](https://developers.cloudflare.com/workers/configuration/sites/configuration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/configuration/sites/start-from-worker.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
