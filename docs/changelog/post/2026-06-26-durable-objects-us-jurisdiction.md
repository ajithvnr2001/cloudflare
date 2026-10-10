---
url: https://developers.cloudflare.com/changelog/post/2026-06-26-durable-objects-us-jurisdiction/
title: New `us` jurisdiction for Durable Objects \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.953660+00:00
---

# New `us` jurisdiction for Durable Objects · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-26-durable-objects-us-jurisdiction/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 26, 2026

## New `us` jurisdiction for Durable Objects

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Durable Objects now supports a `us` [jurisdiction](https://developers.cloudflare.com/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction), letting you create Durable Objects that only run and store data within the United States. Use the `us` jurisdiction when you need to keep a Durable Object's compute and storage inside the United States to meet data residency requirements.

Create a namespace restricted to the `us` jurisdiction the same way as any other jurisdiction:
    
    
    // Worker
    export default {
    	async fetch(request, env) {
    		const usSubnamespace = env.MY_DURABLE_OBJECT.jurisdiction("us");
    		const stub = usSubnamespace.getByName("general");
    		return stub.fetch(request);
    	},
    };

Workers may still access Durable Objects constrained to the `us` jurisdiction from anywhere in the world. The jurisdiction constraint only controls where the Durable Object itself runs and persists data.

For the full list of supported jurisdictions, refer to [Data location — Restrict Durable Objects to a jurisdiction](https://developers.cloudflare.com/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction).
