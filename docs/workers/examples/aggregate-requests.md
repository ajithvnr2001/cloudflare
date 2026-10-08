---
url: https://developers.cloudflare.com/workers/examples/aggregate-requests/
title: Aggregate requests \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:19.578074+00:00
---

# Aggregate requests · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/examples/aggregate-requests/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Examples](https://developers.cloudflare.com/workers/examples/)
  4. /Aggregate Requests



# Aggregate requests

Send two GET request to two urls and aggregates the responses into one response.

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/examples/aggregate-requests/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/aggregate-requests)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.
    
    
    export default {
    	async fetch(request) {
    		// someHost is set up to return JSON responses
    		const someHost = "https://jsonplaceholder.typicode.com";
    		const url1 = someHost + "/todos/1";
    		const url2 = someHost + "/todos/2";
    
    		const responses = await Promise.all([fetch(url1), fetch(url2)]);
    		const results = await Promise.all(responses.map((r) => r.json()));
    
    		const options = {
    			headers: { "content-type": "application/json;charset=UTF-8" },
    		};
    		return new Response(JSON.stringify(results), options);
    	},
    };
    
    
    export default {
    	async fetch(request) {
    		// someHost is set up to return JSON responses
    		const someHost = "https://jsonplaceholder.typicode.com";
    		const url1 = someHost + "/todos/1";
    		const url2 = someHost + "/todos/2";
    
    		const responses = await Promise.all([fetch(url1), fetch(url2)]);
    		const results = await Promise.all(responses.map((r) => r.json()));
    
    		const options = {
    			headers: { "content-type": "application/json;charset=UTF-8" },
    		};
    		return new Response(JSON.stringify(results), options);
    	},
    } satisfies ExportedHandler;
    
    
    import { Hono } from "hono";
    
    const app = new Hono();
    
    app.get("*", async (c) => {
    	// someHost is set up to return JSON responses
    	const someHost = "https://jsonplaceholder.typicode.com";
    	const url1 = someHost + "/todos/1";
    	const url2 = someHost + "/todos/2";
    
    	// Fetch both URLs concurrently
    	const responses = await Promise.all([fetch(url1), fetch(url2)]);
    
    	// Parse JSON responses concurrently
    	const results = await Promise.all(responses.map((r) => r.json()));
    
    	// Return aggregated results
    	return c.json(results);
    });
    
    export default app;
    
    
    from workers import Response, fetch, WorkerEntrypoint
    import asyncio
    import json
    
    class Default(WorkerEntrypoint):
    	async def fetch(self, request):
    		# some_host is set up to return JSON responses
    		some_host = "https://jsonplaceholder.typicode.com"
    		url1 = some_host + "/todos/1"
    		url2 = some_host + "/todos/2"
    
    		responses = await asyncio.gather(fetch(url1), fetch(url2))
    		results = await asyncio.gather(*(r.json() for r in responses))
    
    		headers = {"content-type": "application/json;charset=UTF-8"}
    		return Response.json(results, headers=headers)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/examples/aggregate-requests.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
