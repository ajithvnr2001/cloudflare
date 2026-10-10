---
url: https://developers.cloudflare.com/changelog/post/2026-02-24-deleteall-deletes-alarms/
title: deleteAll() now deletes Durable Object alarm \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.352326+00:00
---

# deleteAll() now deletes Durable Object alarm · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-24-deleteall-deletes-alarms/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 24, 2026

## deleteAll() now deletes Durable Object alarm

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`deleteAll()` now deletes a Durable Object alarm in addition to stored data for Workers with a compatibility date of `2026-02-24` or later. This change simplifies clearing a Durable Object's storage with a single API call.

Previously, `deleteAll()` only deleted user-stored data for an object. Alarm usage stores metadata in an object's storage, which required a separate `deleteAlarm()` call to fully clean up all storage for an object. The `deleteAll()` change applies to both KV-backed and SQLite-backed Durable Objects.
    
    
    // Before: two API calls required to clear all storage
    await this.ctx.storage.deleteAlarm();
    await this.ctx.storage.deleteAll();
    
    // Now: a single call clears both data and the alarm
    await this.ctx.storage.deleteAll();

For more information, refer to the [Storage API documentation](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/#deleteall).
