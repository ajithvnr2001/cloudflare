---
url: https://developers.cloudflare.com/changelog/post/2026-05-26-public-beta/
title: Flagship now in public beta \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:54.535304+00:00
---

# Flagship now in public beta · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-26-public-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 26, 2026

## Flagship now in public beta

[Flagship](https://developers.cloudflare.com/flagship/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-26-public-beta/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**[Flagship](https://developers.cloudflare.com/flagship/)** is now in public beta. Evaluate feature flags directly from Cloudflare Workers with no outbound HTTP calls, using globally distributed flag configuration backed by Workers KV and Durable Objects. Flagship supports typed flag values, targeting rules, percentage rollouts, audit history, and OpenFeature-compatible SDKs.

Evaluate a flag from a Worker in a few lines of code:

src/index.jsjs
    
    
    export default {
    	async fetch(request, env) {
    		const showNewCheckout = await env.FLAGS.getBooleanValue(
    			"new-checkout",
    			false,
    		);
    
    		return new Response(showNewCheckout ? "New checkout" : "Standard checkout");
    	},
    };

src/index.tsts
    
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const showNewCheckout = await env.FLAGS.getBooleanValue("new-checkout", false);
    
    		return new Response(
    			showNewCheckout ? "New checkout" : "Standard checkout",
    		);
    	},
    } satisfies ExportedHandler<Env>;

Start creating flags from the Cloudflare dashboard today. Refer to the [Flagship documentation](https://developers.cloudflare.com/flagship/get-started/) to get started.
