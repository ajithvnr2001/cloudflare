---
url: https://developers.cloudflare.com/workers/examples/accessing-the-cloudflare-object/
title: Accessing the Cloudflare Object \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:21.158493+00:00
---

# Accessing the Cloudflare Object · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/examples/accessing-the-cloudflare-object/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Examples](https://developers.cloudflare.com/workers/examples/)
  4. /Accessing The Cloudflare Object



# Accessing the Cloudflare Object

Access custom Cloudflare properties and control how Cloudflare features are applied to every request.

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/examples/accessing-the-cloudflare-object/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/accessing-the-cloudflare-object)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.
    
    
    export default {
    	async fetch(req) {
    		const data =
    			req.cf !== undefined
    				? req.cf
    				: { error: "The `cf` object is not available inside the preview." };
    
    		return new Response(JSON.stringify(data, null, 2), {
    			headers: {
    				"content-type": "application/json;charset=UTF-8",
    			},
    		});
    	},
    };
    
    
    export default {
    	async fetch(req): Promise<Response> {
    		const data =
    			req.cf !== undefined
    				? req.cf
    				: { error: "The `cf` object is not available inside the preview." };
    
    		return new Response(JSON.stringify(data, null, 2), {
    			headers: {
    				"content-type": "application/json;charset=UTF-8",
    			},
    		});
    	},
    } satisfies ExportedHandler;
    
    
    import { Hono } from "hono";
    
    const app = new Hono();
    
    app.get("*", async (c) => {
    	// Access the raw request to get the cf object
    	const req = c.req.raw;
    
    	// Check if the cf object is available
    	const data =
    		req.cf !== undefined
    			? req.cf
    			: { error: "The `cf` object is not available inside the preview." };
    
    	// Return the data formatted with 2-space indentation
    	return c.json(data);
    });
    
    export default app;
    
    
    import json
    from workers import Response, WorkerEntrypoint
    from js import JSON
    
    class Default(WorkerEntrypoint):
    	async def fetch(self, request):
    		error = json.dumps({ "error": "The `cf` object is not available inside the preview." })
    		data = request.cf if request.cf is not None else error
    		headers = {"content-type":"application/json"}
    		return Response(JSON.stringify(data, None, 2), headers=headers)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/examples/accessing-the-cloudflare-object.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
