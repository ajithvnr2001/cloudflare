---
url: https://developers.cloudflare.com/changelog/post/2026-03-26-durable-object-id-jurisdiction/
title: Access Durable Object jurisdiction via `ctx.id.jurisdiction` \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:41.532472+00:00
---

# Access Durable Object jurisdiction via `ctx.id.jurisdiction` · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-26-durable-object-id-jurisdiction/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 26, 2026

## Access Durable Object jurisdiction via `ctx.id.jurisdiction`

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`ctx.id.jurisdiction` inside a Durable Object now reports the [jurisdiction](https://developers.cloudflare.com/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction) the object was created in — for example `"eu"` when accessed through `env.MY_DURABLE_OBJECT.jurisdiction("eu")` — so you can make region-aware decisions without passing the jurisdiction through method arguments or persisting it in storage. For the full list of ID-construction paths that preserve `jurisdiction`, refer to the [Durable Object ID documentation](https://developers.cloudflare.com/durable-objects/api/id/#jurisdiction).
    
    
    export class RegionalRoom extends DurableObject {
    	async fetch(request) {
    		// "eu" when accessed through env.MY_DURABLE_OBJECT.jurisdiction("eu")
    		const region = this.ctx.id.jurisdiction;
    		return new Response(`Hello from ${region ?? "the default region"}!`);
    	}
    }
    
    // Worker
    export default {
    	async fetch(request, env) {
    		const stub = env.MY_DURABLE_OBJECT.jurisdiction("eu").getByName("general");
    		return stub.fetch(request);
    	},
    };

`ctx.id.jurisdiction` is `undefined` for Durable Objects that were not created in a jurisdiction-restricted namespace. Alarms scheduled before 2026-03-15 also do not have `jurisdiction` stored; to backfill the value, reschedule the alarm from a `fetch()` or RPC handler.
