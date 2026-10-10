---
url: https://developers.cloudflare.com/changelog/post/2026-05-26-bypass-status-for-uncacheable-responses/
title: BYPASS status now returned for uncacheable responses \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:37.866636+00:00
---

# BYPASS status now returned for uncacheable responses · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-26-bypass-status-for-uncacheable-responses/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 26, 2026

## BYPASS status now returned for uncacheable responses

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare now returns a `BYPASS` [cache status](https://developers.cloudflare.com/cache/concepts/cache-responses/) whenever a response is not cacheable, instead of the previous mix of `BYPASS` and `MISS` that depended on why Cloudflare chose not to cache the response.

There are multiple reasons Cloudflare may refuse to cache a response — for example, the response exceeds the [maximum cacheable file size](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/#cacheable-size-limits) for your plan, the origin sends `Cache-Control: no-cache`, `private`, or `max-age=0`, the response includes a `Set-Cookie` header, or the request includes an `Authorization` header.

Previously, only some of these conditions returned `BYPASS`. Others — such as responses exceeding the maximum cacheable file size — returned `MISS` on every request, regardless of whether [Origin Cache Control](https://developers.cloudflare.com/cache/concepts/cache-control/#origin-cache-control-behavior) was on or off. Because the response could never be cached, every subsequent request also returned `MISS`, which looked indistinguishable from a broken cache and made it hard to tell whether Cloudflare was trying and failing to cache the asset or had deliberately chosen not to cache it.

`BYPASS` now consistently signals that Cloudflare refused to cache the response, regardless of the reason. `MISS` is reserved for cacheable responses that simply were not in the local cache at request time.

#### What to expect in your analytics

After this change rolls out, you should see:

  * **MISS rate decreases** : Uncacheable responses no longer count as cache misses.
  * **BYPASS rate increases** : These same responses are now reported as bypasses.
  * **Cache hit ratio increases** : Hit ratio calculations no longer include uncacheable traffic that could never have been cached, giving you a more accurate view of cache effectiveness.



Your total request volume and origin traffic are unchanged — only the cache status label is different.

#### Browser cache TTL behavior is preserved

The cache status label is the only thing changing — browser cache TTL handling for any given response is identical to what it was before:

  * Responses that historically returned `MISS` because Cloudflare refused to cache them (for example, responses over the maximum cacheable file size) now return `BYPASS`, but continue to have browser cache TTL applied — exactly as they did when they were labeled `MISS`.
  * Responses that historically returned `BYPASS` and skipped browser cache TTL continue to skip browser cache TTL.



In both cases, the decision to apply browser cache TTL depends on the underlying reason Cloudflare did not cache the response, not on the new `BYPASS` label.
