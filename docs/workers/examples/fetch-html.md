---
url: https://developers.cloudflare.com/workers/examples/fetch-html/
title: Fetch HTML \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:22.675714+00:00
---

# Fetch HTML · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/examples/fetch-html/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Examples](https://developers.cloudflare.com/workers/examples/)
  4. /Fetch Html



# Fetch HTML

Send a request to a remote server, read HTML from the response, and serve that HTML.

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/examples/fetch-html/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/fetch-html)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.
    
    
    export default {
      async fetch(request) {
        /**
         * Replace `remote` with the host you wish to send requests to
         */
        const remote = "https://example.com";
    
        return await fetch(remote, request);
      },
    };
    
    
    export default {
    	async fetch(request: Request): Promise<Response> {
    		/**
    		 * Replace `remote` with the host you wish to send requests to
    		 */
    		const remote = "https://example.com";
    
    		return await fetch(remote, request);
    	},
    };
    
    
    from workers import WorkerEntrypoint
    from js import fetch
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            # Replace `remote` with the host you wish to send requests to
            remote = "https://example.com"
            return await fetch(remote, request)
    
    
    import { Hono } from "hono";
    
    const app = new Hono();
    
    app.all("*", async (c) => {
    	/**
    	 * Replace `remote` with the host you wish to send requests to
    	 */
    	const remote = "https://example.com";
    
    	// Forward the request to the remote server
    	return await fetch(remote, c.req.raw);
    });
    
    export default app;

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/examples/fetch-html.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
