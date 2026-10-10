---
url: https://developers.cloudflare.com/changelog/post/2024-11-11-cache-no-store/
title: Bypass caching for subrequests made from Cloudflare Workers, with Request.cache \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:55.874711+00:00
---

# Bypass caching for subrequests made from Cloudflare Workers, with Request.cache · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2024-11-11-cache-no-store/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 11, 2024

## Bypass caching for subrequests made from Cloudflare Workers, with Request.cache

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use the [`cache`](https://developers.cloudflare.com/workers/runtime-apis/request/#options) property of the [`Request`](https://developers.cloudflare.com/workers/runtime-apis/request/) interface to bypass [Cloudflare's cache](https://developers.cloudflare.com/workers/reference/how-the-cache-works/) when making subrequests from [Cloudflare Workers](https://developers.cloudflare.com/workers), by setting its value to `no-store`.

index.jsjs
    
    
    export default {
    	async fetch(req, env, ctx) {
    		const request = new Request("https://cloudflare.com", {
    			cache: "no-store",
    		});
    		const response = await fetch(request);
    		return response;
    	},
    };

index.tsts
    
    
    export default {
      async fetch(req, env, ctx): Promise<Response> {
    		const request = new Request("https://cloudflare.com", { cache: 'no-store'});
    		const response = await fetch(request);
        return response;
      }
    } satisfies ExportedHandler<Environment>

When you set the value to `no-store` on a subrequest made from a Worker, the Cloudflare Workers runtime will not check whether a match exists in the cache, and not add the response to the cache, even if the response includes directives in the `Cache-Control` HTTP header that otherwise indicate that the response is cacheable.

This increases compatibility with NPM packages and JavaScript frameworks that rely on setting the [`cache`](https://developers.cloudflare.com/workers/runtime-apis/request/#options) property, which is a cross-platform standard part of the [`Request`](https://developers.cloudflare.com/workers/runtime-apis/request/) interface. Previously, if you set the `cache` property on `Request`, the Workers runtime threw an exception.

If you've tried to use `@planetscale/database`, `redis-js`, `stytch-node`, `supabase`, `axiom-js` or have seen the error message `The cache field on RequestInitializerDict is not implemented in fetch` — you should try again, making sure that the [Compatibility Date](https://developers.cloudflare.com/workers/configuration/compatibility-dates/) of your Worker is set to on or after `2024-11-11`, or the [`cache_option_enabled` compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#enable-cache-no-store-http-standard-api) is enabled for your Worker.

  * Learn [how the Cache works with Cloudflare Workers](https://developers.cloudflare.com/workers/reference/how-the-cache-works/)
  * Enable [Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/) for your Cloudflare Worker
  * Explore [Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/) and [Bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) available in Cloudflare Workers


