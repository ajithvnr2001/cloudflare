---
url: https://developers.cloudflare.com/cache/concepts/retention-vs-freshness/
title: Retention vs Freshness (TTL) \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:41.688160+00:00
---

# Retention vs Freshness (TTL) · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/concepts/retention-vs-freshness/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /Concepts
  4. /Retention vs Freshness (TTL)



# Retention vs Freshness (TTL)

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/concepts/retention-vs-freshness/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRetentionFreshness (TTL)

In the context of Cloudflare CDN (Content Delivery Network), retention and freshness refer to two separate but related concepts. For an object in cache, freshness is how long it should be considered valid without consulting its source, while retention refers to how long it stays in cache before being removed.

## Retention

When a resource is requested, Cloudflare caches it so that subsequent requests can be served without contacting the origin server. If a cached object is not requested again, it is eventually removed to make room for newer, more popular content. This removal process is called eviction.

Cloudflare uses a Least Recently Used (LRU) algorithm to decide which objects to evict when the cache is full. An object's retention period is how long it stays in cache before being evicted. Retention is determined by the object's relative popularity and the size of the cache, and is not configurable.

## Freshness (TTL)

Freshness, also known as Time to Live (TTL), determines how long a cache can use an object without checking with the origin again. For example, if an object has a TTL of five minutes, the cache serves it directly for five minutes after first receiving it. After five minutes, Cloudflare must check with the origin to confirm the object is still valid before serving it again. There are a few ways to configure TTLs for resources served through Cloudflare's CDN:

  * Include [Origin Cache Control](https://developers.cloudflare.com/cache/concepts/cache-control/) or [CDN Cache Control](https://developers.cloudflare.com/cache/concepts/cache-control/) directives, like `max-age` or `s-maxage`, in the origin cache-control response header.

  * Use [Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/) or [Workers](https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers/).




If an object in cache is no longer fresh, Cloudflare revalidates it with the origin. When [`stale-while-revalidate`](https://developers.cloudflare.com/cache/concepts/cache-control/#revalidation) is set, revalidation happens asynchronously at expiry — visitors continue to be served from cache while Cloudflare fetches a fresh copy in the background. Without this directive, incoming requests wait for the origin to respond before receiving content. The origin can either confirm the cached object is still valid (refreshing its TTL) or return a new version to replace it. Refer to [Revalidation](https://developers.cloudflare.com/cache/concepts/revalidation/) for details.

[PreviousOrigin Cache Control](https://developers.cloudflare.com/cache/concepts/cache-control/)[NextRevalidation](https://developers.cloudflare.com/cache/concepts/revalidation/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/concepts/retention-vs-freshness.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
