---
url: https://developers.cloudflare.com/changelog/post/2025-04-07-durable-objects-free-tier/
title: Durable Objects on Workers Free plan \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:08.677369+00:00
---

# Durable Objects on Workers Free plan · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-07-durable-objects-free-tier/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 7, 2025

## Durable Objects on Workers Free plan

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-07-durable-objects-free-tier/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Durable Objects can now be used with zero commitment on the [Workers Free plan](https://developers.cloudflare.com/workers/platform/pricing/) allowing you to build AI agents with [Agents SDK](https://developers.cloudflare.com/agents/), collaboration tools, and real-time applications like chat or multiplayer games.

Durable Objects let you build stateful, serverless applications with millions of tiny coordination instances that run your application code alongside (in the same thread!) your durable storage. Each Durable Object can access its own SQLite database through a [Storage API](https://developers.cloudflare.com/durable-objects/best-practices/access-durable-objects-storage/). A Durable Object class is defined in a Worker script encapsulating the Durable Object's behavior when accessed from a Worker. To try the code below, click the button:

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/hello-world-do-template)
    
    
    import { DurableObject } from "cloudflare:workers";
    
    // Durable Object
    export class MyDurableObject extends DurableObject {
      ...
    	async sayHello(name) {
    		return `Hello, ${name}!`;
    	}
    }
    
    // Worker
    export default {
    	async fetch(request, env) {
    		// Every unique ID refers to an individual instance of the Durable Object class
    		const id = env.MY_DURABLE_OBJECT.idFromName("foo");
    
    		// A stub is a client used to invoke methods on the Durable Object
    		const stub = env.MY_DURABLE_OBJECT.get(id);
    
    		// Methods on the Durable Object are invoked via the stub
    		const response = await stub.sayHello("world");
    
    		return response;
    	},
    };

Free plan [limits](https://developers.cloudflare.com/durable-objects/platform/pricing/) apply to Durable Objects compute and storage usage. Limits allow developers to build real-world applications, with every Worker request able to call a Durable Object on the free plan.

For more information, checkout:

  * [Documentation](https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/)
  * [Zero-latency SQLite storage in every Durable Object blog ↗︎](https://blog.cloudflare.com/sqlite-in-durable-objects/)


