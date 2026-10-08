---
url: https://developers.cloudflare.com/cache/concepts/cache-behavior/
title: Head Requests and Set-Cookie Headers \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:41.183557+00:00
---

# Head Requests and Set-Cookie Headers · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/concepts/cache-behavior/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /Concepts
  4. /Head Requests and Set-Cookie Headers



# Head Requests and Set-Cookie Headers

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/concepts/cache-behavior/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInteraction of HEAD requests with CacheInteraction of Set-Cookie response header with Cache

This page describes how Cloudflare's cache system behaves in interaction with:

  * `HEAD` requests
  * `Set-Cookie` response headers



## Interaction of `HEAD` requests with Cache

Cloudflare converts `HEAD` requests to `GET` requests for [cacheable requests](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/#default-cached-file-extensions).

When you make a `HEAD` request for a cacheable resource and Cloudflare does not have that resource in the edge cache, a cache miss happens. Cloudflare will send a `GET` request to your origin, cache the full response and return the response headers only. Make sure the origin server is set up to handle `GET` requests, even if only `HEAD` requests are expected, so that compatibility with this behavior is ensured.

## Interaction of `Set-Cookie` response header with Cache

For non-cacheable requests, `Set-Cookie` is always preserved. For cacheable requests, there are three possible behaviors:

  * `Set-Cookie` is returned from origin and the default cache level is used. If [origin cache control](https://developers.cloudflare.com/cache/concepts/cache-control/) is not enabled, Cloudflare removes the `Set-Cookie` and caches the asset. If origin cache control is enabled, Cloudflare does not cache the asset and preserves the `Set-Cookie`. A cache status of `BYPASS` is returned.

  * `Set-Cookie` is returned from origin and the cache level is set to `Cache Everything` in Page Rules, or `Eligible for cache` in Cache Rules. In this case, Cloudflare preserves the `Set-Cookie` but does not cache the asset. A cache `MISS` will be returned every time.

  * `Set-Cookie` is returned from origin, the cache level is set to `Cache Everything` in Page Rules, or `Eligible for cache` in Cache Rules, and edge cache TTL is explicitly set using either the "Ignore cache-control header and use this TTL" or "Status code TTL" setting. In this case, Cloudflare removes the `Set-Cookie` and the asset is cached.




[PreviousDefault cache behavior](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/)[NextOrigin Cache Control](https://developers.cloudflare.com/cache/concepts/cache-control/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/concepts/cache-behavior.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
