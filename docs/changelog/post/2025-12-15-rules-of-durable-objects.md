---
url: https://developers.cloudflare.com/changelog/post/2025-12-15-rules-of-durable-objects/
title: New Best Practices guide for Durable Objects \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:31.808910+00:00
---

# New Best Practices guide for Durable Objects · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-15-rules-of-durable-objects/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 15, 2025

## New Best Practices guide for Durable Objects

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-15-rules-of-durable-objects/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new [Rules of Durable Objects](https://developers.cloudflare.com/durable-objects/best-practices/rules-of-durable-objects/) guide is now available, providing opinionated best practices for building effective Durable Objects applications. This guide covers design patterns, storage strategies, concurrency, and common anti-patterns to avoid.

Key guidance includes:

  * **Design around your "atom" of coordination** — Create one Durable Object per logical unit (chat room, game session, user) instead of a global singleton that becomes a bottleneck.
  * **Use SQLite storage with RPC methods** — SQLite-backed Durable Objects with typed RPC methods provide the best developer experience and performance.
  * **Understand input and output gates** — Learn how Cloudflare's runtime prevents data races by default, how write coalescing works, and when to use `blockConcurrencyWhile()`.
  * **Leverage Hibernatable WebSockets** — Reduce costs for real-time applications by allowing Durable Objects to sleep while maintaining WebSocket connections.



The [testing documentation](https://developers.cloudflare.com/durable-objects/examples/testing-with-durable-objects/) has also been updated with modern patterns using `@cloudflare/vitest-pool-workers`, including examples for testing SQLite storage, alarms, and direct instance access:

test/counter.test.jsjs
    
    
    import { env, runDurableObjectAlarm } from "cloudflare:test";
    import { it, expect } from "vitest";
    
    it("can test Durable Objects with isolated storage", async () => {
    	const stub = env.COUNTER.getByName("test");
    
    	// Call RPC methods directly on the stub
    	await stub.increment();
    	expect(await stub.getCount()).toBe(1);
    
    	// Trigger alarms immediately without waiting
    	await runDurableObjectAlarm(stub);
    });

test/counter.test.tsts
    
    
    import { env, runDurableObjectAlarm } from "cloudflare:test";
    import { it, expect } from "vitest";
    
    it("can test Durable Objects with isolated storage", async () => {
    	const stub = env.COUNTER.getByName("test");
    
    	// Call RPC methods directly on the stub
    	await stub.increment();
    	expect(await stub.getCount()).toBe(1);
    
    	// Trigger alarms immediately without waiting
    	await runDurableObjectAlarm(stub);
    });
