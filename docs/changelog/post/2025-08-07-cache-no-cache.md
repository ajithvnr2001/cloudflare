---
url: https://developers.cloudflare.com/changelog/post/2025-08-07-cache-no-cache/
title: Requests made from Cloudflare Workers can now force a revalidation of their cache with the origin \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:18.504482+00:00
---

# Requests made from Cloudflare Workers can now force a revalidation of their cache with the origin · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-07-cache-no-cache/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 7, 2025

## Requests made from Cloudflare Workers can now force a revalidation of their cache with the origin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-07-cache-no-cache/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

By setting the value of the `cache` property to `no-cache`, you can force [Cloudflare's cache](https://developers.cloudflare.com/workers/reference/how-the-cache-works/) to revalidate its contents with the origin when making subrequests from [Cloudflare Workers](https://developers.cloudflare.com/workers).

index.jsjs
    
    
    export default {
    	async fetch(req, env, ctx) {
    		const request = new Request("https://cloudflare.com", {
    			cache: "no-cache",
    		});
    		const response = await fetch(request);
    		return response;
    	},
    };

index.tsts
    
    
    export default {
      async fetch(req, env, ctx): Promise<Response> {
    		const request = new Request("https://cloudflare.com", { cache: 'no-cache'});
    		const response = await fetch(request);
        return response;
      }
    } satisfies ExportedHandler<Environment>

When `no-cache` is set, the Worker request will first look for a match in Cloudflare's cache, then:

  * If there is a match, a conditional request is sent to the origin, regardless of whether or not the match is fresh or stale. If the resource has not changed, the cached version is returned. If the resource has changed, it will be downloaded from the origin, updated in the cache, and returned.
  * If there is no match, Workers will make a standard request to the origin and cache the response.



This increases compatibility with NPM packages and JavaScript frameworks that rely on setting the [`cache`](https://developers.cloudflare.com/workers/runtime-apis/request/#options) property, which is a cross-platform standard part of the [`Request`](https://developers.cloudflare.com/workers/runtime-apis/request/) interface. Previously, if you set the `cache` property on `Request` to `'no-cache'`, the Workers runtime threw an exception.

  * Learn [how the Cache works with Cloudflare Workers](https://developers.cloudflare.com/workers/reference/how-the-cache-works/)
  * Enable [Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/) for your Cloudflare Worker
  * Explore [Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/) and [Bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) available in Cloudflare Workers


