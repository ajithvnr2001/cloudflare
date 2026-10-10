---
url: https://developers.cloudflare.com/changelog/post/2026-08-25-durable-object-alarm-abort-no-retry/
title: Prevent Durable Object alarm retries when using `ctx.abort()` \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.297158+00:00
---

# Prevent Durable Object alarm retries when using `ctx.abort()` · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-25-durable-object-alarm-abort-no-retry/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 25, 2026

## Prevent Durable Object alarm retries when using `ctx.abort()`

[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

By default, an alarm interrupted by `ctx.abort()` retries after the Durable Object resets. Pass `{ retryAlarm: false }` when the alarm should stop instead:

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class CleanupTask extends DurableObject {
    	async alarm() {
    		await this.ctx.storage.deleteAll();
    
    		this.ctx.abort("Cleanup complete", { retryAlarm: false });
    	}
    }

src/index.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class CleanupTask extends DurableObject {
    	async alarm(): Promise<void> {
    		await this.ctx.storage.deleteAll();
    
    		this.ctx.abort("Cleanup complete", { retryAlarm: false });
    	}
    }

For example, an alarm that deletes its storage can use this option to avoid repeating the cleanup or re-running the Durable Object constructor.

Alarms can run concurrently with other requests to the same Durable Object. If another request calls `ctx.abort()` while an alarm is running, the `retryAlarm` option on that call also controls whether the alarm retries.

The default retry prevents an unrelated request from permanently canceling the alarm. Set `retryAlarm: false` on every abort path that should stop an in-progress alarm, not only on calls from the alarm handler. Existing calls to `ctx.abort()` keep retrying alarms.

For local development, `retryAlarm` requires Wrangler 4.126.0 or later.

For more information, refer to [`ctx.abort()`](https://developers.cloudflare.com/durable-objects/api/state/#abort).
