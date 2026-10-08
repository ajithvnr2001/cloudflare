---
url: https://developers.cloudflare.com/workers/examples/block-on-tls/
title: Block on TLS \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:20.056907+00:00
---

# Block on TLS · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/examples/block-on-tls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Examples](https://developers.cloudflare.com/workers/examples/)
  4. /Block On Tls



# Block on TLS

Inspects the incoming request's TLS version and blocks if under TLSv1.2.

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/examples/block-on-tls/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		try {
    			const tlsVersion = request.cf.tlsVersion;
    			// Allow only TLS versions 1.2 and 1.3
    			if (tlsVersion !== "TLSv1.2" && tlsVersion !== "TLSv1.3") {
    				return new Response("Please use TLS version 1.2 or higher.", {
    					status: 403,
    				});
    			}
    			return fetch(request);
    		} catch (err) {
    			console.error(
    				"request.cf does not exist in the previewer, only in production",
    			);
    			return new Response(`Error in workers script ${err.message}`, {
    				status: 500,
    			});
    		}
    	},
    };
    
    
    export default {
    	async fetch(request): Promise<Response> {
    		try {
    			const tlsVersion = request.cf.tlsVersion;
    			// Allow only TLS versions 1.2 and 1.3
    			if (tlsVersion !== "TLSv1.2" && tlsVersion !== "TLSv1.3") {
    				return new Response("Please use TLS version 1.2 or higher.", {
    					status: 403,
    				});
    			}
    			return fetch(request);
    		} catch (err) {
    			console.error(
    				"request.cf does not exist in the previewer, only in production",
    			);
    			return new Response(`Error in workers script ${err.message}`, {
    				status: 500,
    			});
    		}
    	},
    } satisfies ExportedHandler;
    
    
    import { Hono } from "hono";
    
    const app = new Hono();
    
    // Middleware to check TLS version
    app.use("*", async (c, next) => {
    	// Access the raw request to get the cf object with TLS info
    	const request = c.req.raw;
    	const tlsVersion = request.cf?.tlsVersion;
    
    	// Allow only TLS versions 1.2 and 1.3
    	if (tlsVersion !== "TLSv1.2" && tlsVersion !== "TLSv1.3") {
    		return c.text("Please use TLS version 1.2 or higher.", 403);
    	}
    
    	await next();
    
    });
    
    app.onError((err, c) => {
    		console.error(
    			"request.cf does not exist in the previewer, only in production",
    		);
    		return c.text(`Error in workers script: ${err.message}`, 500);
    });
    
    app.get("/", async (c) => {
    	return c.text(`TLS Version: ${c.req.raw.cf.tlsVersion}`);
    });
    
    export default app;
    
    
    from workers import WorkerEntrypoint, Response, fetch
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            tls_version = request.cf.tlsVersion
            if tls_version not in ("TLSv1.2", "TLSv1.3"):
                return Response("Please use TLS version 1.2 or higher.", status=403)
            return fetch(request)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/examples/block-on-tls.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
