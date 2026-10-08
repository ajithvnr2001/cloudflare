---
url: https://developers.cloudflare.com/changelog/post/2026-09-29-workers-cache-invalidate/
title: Workers Cache \u2014 mark cached responses stale with invalidate() \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:17.302966+00:00
---

# Workers Cache — mark cached responses stale with invalidate() · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-29-workers-cache-invalidate/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 29, 2026

## Workers Cache — mark cached responses stale with invalidate()

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-29-workers-cache-invalidate/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers Cache](https://developers.cloudflare.com/workers/cache/) now supports `invalidate()`, the soft counterpart of `purge()`. `purge()` deletes matching cached responses, so the next request is a cache miss. `invalidate()` keeps them but marks them stale, so the cache revalidates them with your Worker instead.

To revalidate a response, the cache sends your Worker a conditional request built from the validators stored with it — for example, `If-None-Match` carrying the cached `ETag`. If your Worker answers `304 Not Modified`, the cache keeps the stored body. If your Worker answers with a full `200` response, that response replaces the cached one.

`invalidate()` accepts the same options as `purge()`: `tags`, `pathPrefixes`, or `purgeEverything`. It follows the same per-entrypoint scoping and resolves to the same result object. Call it as `ctx.cache.invalidate()`, or import `cache` from `cloudflare:workers` and call `cache.invalidate()`.

Use `invalidate()` when one call covers many cached responses but only some of them changed. Your Worker needs to emit `ETag` or `Last-Modified` and answer matching conditional requests with `304`. Each unchanged response then costs a validator check instead of a full regeneration:

src/index.jsjs
    
    
    export default {
    	async fetch(request, env, ctx) {
    		if (request.method === "POST") {
    			// Write the updated catalog, then mark every cached product page stale.
    			await syncCatalog(env, await request.json());
    			await ctx.cache.invalidate({ tags: ["products"] });
    			return new Response("Synced");
    		}
    
    		const product = await getProduct(env, request);
    		const etag = `"${product.revision}"`;
    		const headers = {
    			"Cache-Control": "public, max-age=86400",
    			"Cache-Tag": "products",
    			ETag: etag,
    		};
    
    		// The product has not changed since it was cached. Answer 304, and the
    		// cache keeps the body it already has.
    		if (request.headers.get("If-None-Match") === etag) {
    			return new Response(null, { status: 304, headers });
    		}
    
    		return new Response(renderProductPage(product), { headers });
    	},
    };

src/index.tsts
    
    
    export default {
    	async fetch(request, env, ctx): Promise<Response> {
    		if (request.method === "POST") {
    			// Write the updated catalog, then mark every cached product page stale.
    			await syncCatalog(env, await request.json());
    			await ctx.cache.invalidate({ tags: ["products"] });
    			return new Response("Synced");
    		}
    
    		const product = await getProduct(env, request);
    		const etag = `"${product.revision}"`;
    		const headers = {
    			"Cache-Control": "public, max-age=86400",
    			"Cache-Tag": "products",
    			ETag: etag,
    		};
    
    		// The product has not changed since it was cached. Answer 304, and the
    		// cache keeps the body it already has.
    		if (request.headers.get("If-None-Match") === etag) {
    			return new Response(null, { status: 304, headers });
    		}
    
    		return new Response(renderProductPage(product), { headers });
    	},
    } satisfies ExportedHandler<Env>;

For more information, refer to [Invalidate cached responses](https://developers.cloudflare.com/workers/cache/purge/#invalidate-cached-responses).
