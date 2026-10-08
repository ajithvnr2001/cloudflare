---
url: https://developers.cloudflare.com/changelog/post/2026-02-26-async-stale-while-revalidate/
title: Asynchronous stale-while-revalidate \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:38.815556+00:00
---

# Asynchronous stale-while-revalidate · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-26-async-stale-while-revalidate/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 26, 2026

## Asynchronous stale-while-revalidate

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-26-async-stale-while-revalidate/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare's [`stale-while-revalidate`](https://developers.cloudflare.com/cache/concepts/cache-control/#revalidation) support is now fully asynchronous. Previously, the first request for a stale (expired) asset in cache had to wait for an origin response, after which that visitor received a REVALIDATED or EXPIRED status. Now, the first request after the asset expires triggers revalidation in the background and immediately receives stale content with an UPDATING status. All following requests also receive stale content with an `UPDATING` status until the origin responds, after which subsequent requests receive fresh content with a `HIT` status.

`stale-while-revalidate` is a `Cache-Control` directive set by your origin server that allows Cloudflare to serve an expired cached asset while a fresh copy is fetched from the origin.

Asynchronous revalidation brings:

  * **Lower latency** : No visitor is waiting for the origin when the asset is already in cache. Every request is served from cache during revalidation.
  * **Consistent experience** : All visitors receive the same cached response during revalidation.
  * **Reduced error exposure** : The first request is no longer vulnerable to origin timeouts or errors. All visitors receive a cached response while revalidation happens in the background.



#### Availability

This change is live for all Free, Pro, and Business zones. Approximately 75% of Enterprise zones have been migrated, with the remaining zones rolling out throughout the quarter.

#### Get started

To use this feature, make sure your origin includes the `stale-while-revalidate` directive in the `Cache-Control` header. Refer to the [Cache-Control documentation](https://developers.cloudflare.com/cache/concepts/cache-control/#revalidation) for details.
