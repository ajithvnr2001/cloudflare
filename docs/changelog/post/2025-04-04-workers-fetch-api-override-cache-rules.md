---
url: https://developers.cloudflare.com/changelog/post/2025-04-04-workers-fetch-api-override-cache-rules/
title: Workers Fetch API can override Cache Rules \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:53.498476+00:00
---

# Workers Fetch API can override Cache Rules · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-04-workers-fetch-api-override-cache-rules/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 4, 2025

## Workers Fetch API can override Cache Rules

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now programmatically override Cache Rules using the `cf` object in the `fetch()` command. This feature gives you fine-grained control over caching behavior on a per-request basis, allowing Workers to customize cache settings dynamically based on request properties, user context, or business logic.

#### How it works

Using the `cf` object in `fetch()`, you can override specific Cache Rules settings by:

  1. **Setting custom cache options** : Pass cache properties in the `cf` object as the second argument to `fetch()` to override default Cache Rules.
  2. **Dynamic cache control** : Apply different caching strategies based on request headers, cookies, or other runtime conditions.
  3. **Per-request customization** : Bypass or modify Cache Rules for individual requests while maintaining default behavior for others.
  4. **Programmatic cache management** : Implement complex caching logic that adapts to your application's needs.



#### What can be configured

Workers can override the following Cache Rules settings through the `cf` object:

  * **`cacheEverything`** : Treat all content as static and cache all file types beyond the default cached content.
  * **`cacheTtl`** : Set custom time-to-live values in seconds for cached content at the edge, regardless of origin headers.
  * **`cacheTtlByStatus`** : Set different TTLs based on the response status code (for example, `{ "200-299": 86400, 404: 1, "500-599": 0 }`).
  * **`cacheKey`** : Customize cache keys to control which requests are treated as the same for caching purposes (Enterprise only).
  * **`cacheTags`** : Append additional cache tags for targeted cache purging operations.



#### Benefits

  * **Enhanced flexibility** : Customize cache behavior without modifying zone-level Cache Rules.
  * **Dynamic optimization** : Adjust caching strategies in real-time based on request context.
  * **Simplified configuration** : Reduce the number of Cache Rules needed by handling edge cases programmatically.
  * **Improved performance** : Fine-tune cache behavior for specific use cases to maximize hit rates.



#### Get started

To get started, refer to the [Workers Fetch API documentation](https://developers.cloudflare.com/workers/runtime-apis/fetch/) and the [cf object properties documentation](https://developers.cloudflare.com/workers/runtime-apis/request/#the-cf-property-requestinitcfproperties).
