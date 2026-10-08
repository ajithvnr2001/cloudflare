---
url: https://developers.cloudflare.com/workers/examples/bulk-redirects/
title: Bulk redirects \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:20.451863+00:00
---

# Bulk redirects · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/examples/bulk-redirects/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Examples](https://developers.cloudflare.com/workers/examples/)
  4. /Bulk Redirects



# Bulk redirects

Redirect requests to certain URLs based on a mapped object to the request's URL.

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/examples/bulk-redirects/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		const externalHostname = "examples.cloudflareworkers.com";
    
    		const redirectMap = new Map([
    			["/bulk1", "https://" + externalHostname + "/redirect2"],
    			["/bulk2", "https://" + externalHostname + "/redirect3"],
    			["/bulk3", "https://" + externalHostname + "/redirect4"],
    			["/bulk4", "https://google.com"],
    		]);
    
    		const requestURL = new URL(request.url);
    		const path = requestURL.pathname;
    		const location = redirectMap.get(path);
    
    		if (location) {
    			return Response.redirect(location, 301);
    		}
    		// If request not in map, return the original request
    		return fetch(request);
    	},
    };
    
    
    export default {
    	async fetch(request): Promise<Response> {
    		const externalHostname = "examples.cloudflareworkers.com";
    
    		const redirectMap = new Map([
    			["/bulk1", "https://" + externalHostname + "/redirect2"],
    			["/bulk2", "https://" + externalHostname + "/redirect3"],
    			["/bulk3", "https://" + externalHostname + "/redirect4"],
    			["/bulk4", "https://google.com"],
    		]);
    
    		const requestURL = new URL(request.url);
    		const path = requestURL.pathname;
    		const location = redirectMap.get(path);
    
    		if (location) {
    			return Response.redirect(location, 301);
    		}
    		// If request not in map, return the original request
    		return fetch(request);
    	},
    } satisfies ExportedHandler;
    
    
    from workers import WorkerEntrypoint, Response, fetch
    from urllib.parse import urlparse
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            external_hostname = "examples.cloudflareworkers.com"
    
            redirect_map = {
              "/bulk1": "https://" + external_hostname + "/redirect2",
              "/bulk2": "https://" + external_hostname + "/redirect3",
              "/bulk3": "https://" + external_hostname + "/redirect4",
              "/bulk4": "https://google.com",
              }
    
            url = urlparse(request.url)
            location = redirect_map.get(url.path, None)
    
            if location:
                return Response.redirect(location, 301)
    
            # If request not in map, return the original request
            return fetch(request)
    
    
    import { Hono } from "hono";
    
    const app = new Hono();
    
    // Configure your redirects
    const externalHostname = "examples.cloudflareworkers.com";
    
    const redirectMap = new Map([
    	["/bulk1", `https://${externalHostname}/redirect2`],
    	["/bulk2", `https://${externalHostname}/redirect3`],
    	["/bulk3", `https://${externalHostname}/redirect4`],
    	["/bulk4", "https://google.com"],
    ]);
    
    // Middleware to handle redirects
    app.use("*", async (c, next) => {
    	const path = c.req.path;
    	const location = redirectMap.get(path);
    
    	if (location) {
    		// If path is in our redirect map, perform the redirect
    		return c.redirect(location, 301);
    	}
    
    	// Otherwise, continue to the next handler
    	await next();
    });
    
    // Default handler for requests that don't match any redirects
    app.all("*", async (c) => {
    	// Pass through to origin
    	return fetch(c.req.raw);
    });
    
    export default app;

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/examples/bulk-redirects.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
