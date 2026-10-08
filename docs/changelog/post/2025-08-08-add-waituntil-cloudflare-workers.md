---
url: https://developers.cloudflare.com/changelog/post/2025-08-08-add-waituntil-cloudflare-workers/
title: Directly import `waitUntil` in Workers for easily spawning background tasks \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:18.438291+00:00
---

# Directly import `waitUntil` in Workers for easily spawning background tasks · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-08-add-waituntil-cloudflare-workers/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 8, 2025

## Directly import `waitUntil` in Workers for easily spawning background tasks

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-08-add-waituntil-cloudflare-workers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now import [`waitUntil`](https://developers.cloudflare.com/workers/runtime-apis/context/#waituntil) from `cloudflare:workers` to extend your Worker's execution beyond the request lifecycle from anywhere in your code.

Previously, `waitUntil` could only be accessed through the [execution context](https://developers.cloudflare.com/workers/runtime-apis/context/) (`ctx`) parameter passed to your Worker's handler functions. This meant that if you needed to schedule background tasks from deeply nested functions or utility modules, you had to pass the `ctx` object through multiple function calls to access `waitUntil`.

Now, you can import `waitUntil` directly and use it anywhere in your Worker without needing to pass `ctx` as a parameter:
    
    
    import { waitUntil } from "cloudflare:workers";
    
    export function trackAnalytics(eventData) {
    	const analyticsPromise = fetch("https://analytics.example.com/track", {
    		method: "POST",
    		body: JSON.stringify(eventData),
    	});
    
    	// Extend execution to ensure analytics tracking completes
    	waitUntil(analyticsPromise);
    }

This is particularly useful when you want to:

  * Schedule background tasks from utility functions or modules
  * Extend execution for analytics, logging, or cleanup operations
  * Avoid passing the execution context through multiple layers of function calls


    
    
    import { waitUntil } from "cloudflare:workers";
    
    export default {
    	async fetch(request, env, ctx) {
    		// Background task that should complete even after response is sent
    		cleanupTempData(env.KV_NAMESPACE);
    		return new Response("Hello, World!");
    	}
    };
    
    function cleanupTempData(kvNamespace) {
    	// This function can now use waitUntil without needing ctx
    	const deletePromise = kvNamespace.delete("temp-key");
    	waitUntil(deletePromise);
    }

Note

The imported `waitUntil` function works the same way as [`ctx.waitUntil()`](https://developers.cloudflare.com/workers/runtime-apis/context/#waituntil). It extends your Worker's execution to wait for the provided promise to settle, but does not block the response from being sent to the client.

For more information, see the [`waitUntil` documentation](https://developers.cloudflare.com/workers/runtime-apis/context/#waituntil).
