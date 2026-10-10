---
url: https://developers.cloudflare.com/changelog/post/2026-06-25-durable-object-eviction-test-helpers/
title: Test Durable Object eviction with new cloudflare:test helpers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:36.036102+00:00
---

# Test Durable Object eviction with new cloudflare:test helpers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-25-durable-object-eviction-test-helpers/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 25, 2026

## Test Durable Object eviction with new cloudflare:test helpers

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The `@cloudflare/vitest-pool-workers` package now includes `evictDurableObject` and `evictAllDurableObjects` test helpers, exported from `cloudflare:test`.

These helpers let you test how a Durable Object behaves across evictions, simulating the production lifecycle where an idle Durable Object can be evicted from memory.

For more context, refer to [Lifecycle of a Durable Object](https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/).
    
    
    import { evictDurableObject, evictAllDurableObjects } from "cloudflare:test";
    import { env } from "cloudflare:workers";
    
    const id = env.COUNTER.idFromName("my-counter");
    const stub = env.COUNTER.get(id);
    
    // Evict the Durable Object instance pointed to by a specific stub
    await evictDurableObject(stub);
    
    // Close WebSockets instead of hibernating them
    await evictDurableObject(stub, { webSockets: "close" });
    
    // Evict all currently-running Durable Objects in evictable namespaces
    await evictAllDurableObjects();

These helpers are available in `@cloudflare/vitest-pool-workers@0.16.20` and later.

Learn more in the [Test APIs reference](https://developers.cloudflare.com/workers/testing/vitest-integration/test-apis/#durable-objects) and the [Testing Durable Objects guide](https://developers.cloudflare.com/durable-objects/examples/testing-with-durable-objects/#testing-eviction).
