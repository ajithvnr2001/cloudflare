---
url: https://developers.cloudflare.com/workers/examples/bulk-origin-proxy/
title: Bulk origin override \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:20.769871+00:00
---

# Bulk origin override · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/examples/bulk-origin-proxy/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Examples](https://developers.cloudflare.com/workers/examples/)
  4. /Bulk Origin Proxy



# Bulk origin override

Resolve requests to your domain to a set of proxy third-party origin URLs.

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/examples/bulk-origin-proxy/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		/**
    		 * An object with different URLs to fetch
    		 * @param {Object} ORIGINS
    		 */
    		const ORIGINS = {
    			"starwarsapi.yourdomain.com": "swapi.dev",
    			"google.yourdomain.com": "www.google.com",
    		};
    
    		const url = new URL(request.url);
    
    		// Check if incoming hostname is a key in the ORIGINS object
    		if (url.hostname in ORIGINS) {
    			const target = ORIGINS[url.hostname];
    			url.hostname = target;
    			// If it is, proxy request to that third party origin
    			return fetch(url.toString(), request);
    		}
    		// Otherwise, process request as normal
    		return fetch(request);
    	},
    };
    
    
    export default {
    	async fetch(request): Promise<Response> {
    		/**
    		 * An object with different URLs to fetch
    		 * @param {Object} ORIGINS
    		 */
    		const ORIGINS = {
    			"starwarsapi.yourdomain.com": "swapi.dev",
    			"google.yourdomain.com": "www.google.com",
    		};
    
    		const url = new URL(request.url);
    
    		// Check if incoming hostname is a key in the ORIGINS object
    		if (url.hostname in ORIGINS) {
    			const target = ORIGINS[url.hostname];
    			url.hostname = target;
    			// If it is, proxy request to that third party origin
    			return fetch(url.toString(), request);
    		}
    		// Otherwise, process request as normal
    		return fetch(request);
    	},
    } satisfies ExportedHandler;
    
    
    import { Hono } from "hono";
    import { proxy } from "hono/proxy";
    
    // An object with different URLs to fetch
    const ORIGINS: Record<string, string> = {
    	"starwarsapi.yourdomain.com": "swapi.dev",
    	"google.yourdomain.com": "www.google.com",
    };
    
    const app = new Hono();
    
    app.all("*", async (c) => {
    	const url = new URL(c.req.url);
    
    	// Check if incoming hostname is a key in the ORIGINS object
    	if (url.hostname in ORIGINS) {
    		const target = ORIGINS[url.hostname];
    		url.hostname = target;
    
    		// If it is, proxy request to that third party origin
    		return proxy(url, c.req.raw);
    	}
    
    	// Otherwise, process request as normal
    	return proxy(c.req.raw);
    });
    
    export default app;
    
    
    from workers import WorkerEntrypoint
    from js import fetch, URL
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            # A dict with different URLs to fetch
            ORIGINS = {
              "starwarsapi.yourdomain.com": "swapi.dev",
              "google.yourdomain.com": "www.google.com",
            }
    
            url = URL.new(request.url)
    
            # Check if incoming hostname is a key in the ORIGINS object
            if url.hostname in ORIGINS:
                url.hostname = ORIGINS[url.hostname]
                # If it is, proxy request to that third party origin
                return fetch(url.toString(), request)
    
            # Otherwise, process request as normal
            return fetch(request)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/examples/bulk-origin-proxy.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
