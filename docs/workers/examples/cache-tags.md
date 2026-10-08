---
url: https://developers.cloudflare.com/workers/examples/cache-tags/
title: Cache Tags using Workers \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:21.051378+00:00
---

# Cache Tags using Workers · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/examples/cache-tags/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Examples](https://developers.cloudflare.com/workers/examples/)
  4. /Cache Tags



# Cache Tags using Workers

Send Additional Cache Tags using Workers

Last updated Jul 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/examples/cache-tags/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/cache-tags)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.
    
    
    export default {
    	async fetch(request) {
    		const requestUrl = new URL(request.url);
    		const params = requestUrl.searchParams;
    		const tags =
    			params && params.has("tags") ? params.get("tags").split(",") : [];
    		const url = params && params.has("uri") ? params.get("uri") : "";
    		if (!url) {
    			const errorObject = {
    				error: "URL cannot be empty",
    			};
    			return new Response(JSON.stringify(errorObject), { status: 400 });
    		}
    		const init = {
    			cf: {
    				cacheTags: tags,
    			},
    		};
    		return fetch(url, init)
    			.then((result) => {
    				const cacheStatus = result.headers.get("cf-cache-status");
    				const lastModified = result.headers.get("last-modified");
    				const response = {
    					cache: cacheStatus,
    					lastModified: lastModified,
    				};
    				return new Response(JSON.stringify(response), {
    					status: result.status,
    				});
    			})
    			.catch((err) => {
    				const errorObject = {
    					error: err.message,
    				};
    				return new Response(JSON.stringify(errorObject), { status: 500 });
    			});
    	},
    };
    
    
    export default {
    	async fetch(request): Promise<Response> {
    		const requestUrl = new URL(request.url);
    		const params = requestUrl.searchParams;
    		const tags =
    			params && params.has("tags") ? params.get("tags").split(",") : [];
    		const url = params && params.has("uri") ? params.get("uri") : "";
    		if (!url) {
    			const errorObject = {
    				error: "URL cannot be empty",
    			};
    			return new Response(JSON.stringify(errorObject), { status: 400 });
    		}
    		const init = {
    			cf: {
    				cacheTags: tags,
    			},
    		};
    		return fetch(url, init)
    			.then((result) => {
    				const cacheStatus = result.headers.get("cf-cache-status");
    				const lastModified = result.headers.get("last-modified");
    				const response = {
    					cache: cacheStatus,
    					lastModified: lastModified,
    				};
    				return new Response(JSON.stringify(response), {
    					status: result.status,
    				});
    			})
    			.catch((err) => {
    				const errorObject = {
    					error: err.message,
    				};
    				return new Response(JSON.stringify(errorObject), { status: 500 });
    			});
    	},
    } satisfies ExportedHandler;
    
    
    import { Hono } from "hono";
    
    const app = new Hono();
    
    app.all("*", async (c) => {
    	const tags = c.req.query("tags") ? c.req.query("tags").split(",") : [];
    	const uri = c.req.query("uri") ? c.req.query("uri") : "";
    
    	if (!uri) {
    		return c.json({ error: "URL cannot be empty" }, 400);
    	}
    
    	const init = {
    		cf: {
    			cacheTags: tags,
    		},
    	};
    
    	const result = await fetch(uri, init);
    	const cacheStatus = result.headers.get("cf-cache-status");
    	const lastModified = result.headers.get("last-modified");
    
    	const response = {
    		cache: cacheStatus,
    		lastModified: lastModified,
    	};
    
    	return c.json(response, result.status);
    });
    
    app.onError((err, c) => {
    	return c.json({ error: err.message }, 500);
    });
    
    export default app;
    
    
    from workers import WorkerEntrypoint, Response, fetch
    from js import URL
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            request_url = URL.new(request.url)
            params = request_url.searchParams
            tags = params["tags"].split(",") if "tags" in params else []
            url = params["uri"] or None
    
            if url is None:
                return Response.json({"error": "URL cannot be empty"}, status=400)
    
            result = await fetch(url, cf={"cacheTags": tags})
    
            cache_status = result.headers["cf-cache-status"]
            last_modified = result.headers["last-modified"]
    
            return Response.json({"cache": cache_status, "lastModified": last_modified}, status=result.status)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/examples/cache-tags.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
