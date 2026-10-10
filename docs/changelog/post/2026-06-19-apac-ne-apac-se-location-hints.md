---
url: https://developers.cloudflare.com/changelog/post/2026-06-19-apac-ne-apac-se-location-hints/
title: New Asia-Pacific location hints: apac-ne and apac-se \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:36.265946+00:00
---

# New Asia-Pacific location hints: apac-ne and apac-se · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-19-apac-ne-apac-se-location-hints/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 19, 2026

## New Asia-Pacific location hints: apac-ne and apac-se

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Durable Objects now supports two new location hints for Asia-Pacific: `apac-ne` (Northeast Asia-Pacific) and `apac-se` (Southeast Asia-Pacific). Use `apac-ne` or `apac-se` when you want finer-grained placement within Asia-Pacific rather than the broader `apac` hint.

Use the new hints the same way as any other `locationHint`:
    
    
    // Northeast Asia-Pacific (Japan, Korea, etc.)
    const stubNE = env.MY_DURABLE_OBJECT.get(id, { locationHint: "apac-ne" });
    
    // Southeast Asia-Pacific (Singapore, Indonesia, etc.)
    const stubSE = env.MY_DURABLE_OBJECT.get(id, { locationHint: "apac-se" });

If your users are spread across all of Asia-Pacific, the existing `apac` hint remains the right choice. Only reach for `apac-ne` or `apac-se` when your traffic is clearly concentrated in one sub-region and you want to minimize round-trip time to that audience. The default behavior and what we generally recommended is not adding a location hint unless absolutely needed, this will create the Durable Object as close to the initializing request as possible to reduce latency.

As with all location hints, these are best-effort suggestions. Cloudflare will place the Durable Object in a nearby data center, not necessarily the exact hinted location.

For the full list of supported hints, refer to [Data location — Provide a location hint](https://developers.cloudflare.com/durable-objects/reference/data-location/#provide-a-location-hint).
