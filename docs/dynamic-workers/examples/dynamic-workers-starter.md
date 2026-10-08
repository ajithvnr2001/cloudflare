---
url: https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-starter/
title: Dynamic Workers Starter \u00b7 Cloudflare Dynamic Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:11.003840+00:00
---

# Dynamic Workers Starter · Cloudflare Dynamic Workers docs

> Source: https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-starter/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/)
  3. /Examples
  4. /Dynamic Workers Starter



# Dynamic Workers Starter

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-starter/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat it doesConfigurationLoading and executing a Dynamic WorkerRunning locally

A [starter template ↗︎](https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers) for deploying a Worker that loads and runs [Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/).

[![Deploy to Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers)

## What it does

This template demonstrates how to use the [Worker Loader API](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/) to execute code at runtime. The host Worker exposes an `/api/run` endpoint that accepts code from the frontend, loads it into a sandboxed Dynamic Worker, and returns the result.

Use this pattern for AI agents that need to execute a snippet of code to complete an action.

## Configuration

Add a `worker_loaders` binding to your Wrangler file:
    
    
    {
    	"worker_loaders": [
    		{
    			"binding": "LOADER"
    		}
    	]
    }
    
    
    [[worker_loaders]]
    binding = "LOADER"

## Loading and executing a Dynamic Worker

In this example:

  * `env.LOADER.load()` creates a one-off dynamic isolate
  * `globalOutbound: null` blocks all outbound network access from the Dynamic Worker


    
    
    export default {
    	async fetch(request, env) {
    		const { code } = await request.json();
    
    		const worker = env.LOADER.load({
    			compatibilityDate: "2026-05-01",
    			mainModule: "worker.js",
    			modules: {
    				"worker.js": code,
    			},
    			// Block all outbound network access
    			globalOutbound: null,
    		});
    
    		const result = await worker.getEntrypoint().fetch(request);
    		return result;
    	},
    };
    
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		const { code } = await request.json();
    
    		const worker = env.LOADER.load({
    			compatibilityDate: "2026-05-01",
    			mainModule: "worker.js",
    			modules: {
    				"worker.js": code,
    			},
    			// Block all outbound network access
    			globalOutbound: null,
    		});
    
    		const result = await worker.getEntrypoint().fetch(request);
    		return result;
    	},
    } satisfies ExportedHandler;

## Running locally
    
    
    npm install
    npm run dev

[PreviousDynamic Workflows](https://developers.cloudflare.com/dynamic-workers/usage/dynamic-workflows/)[NextDynamic Workers Playground](https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-playground/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dynamic-workers/examples/dynamic-workers-starter.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
