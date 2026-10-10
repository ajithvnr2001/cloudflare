---
url: https://developers.cloudflare.com/changelog/post/2026-04-27-cache-response-rules-zone-versioning/
title: Cache Response Rules now support zone versioning \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:39.600895+00:00
---

# Cache Response Rules now support zone versioning · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-27-cache-response-rules-zone-versioning/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 27, 2026

## Cache Response Rules now support zone versioning

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cache Response Rules now work with [Version Management](https://developers.cloudflare.com/version-management/). You can version response-phase cache settings and promote them through environments, just like Cache Rules and other supported configurations.

#### What changed

Previously, Cache Response Rules were excluded from zone versioning. Any response-phase rule you created applied globally across all environments with no way to test changes in staging first. Cache Rules already supported versioning, but the response phase, where you modify `Cache-Control` directives, manage cache tags, and strip headers, did not.

Cache Response Rules are now fully integrated with Version Management. You can create or modify response-phase rules within a version, and those changes stay scoped to that version until promoted.

#### Benefits

  * **Safe rollout of cache behavior changes** : Test response-phase rules in a staging environment before promoting to production. Catch unintended caching side effects early.
  * **Parity with Cache Rules** : Cache Response Rules now follow the same versioning workflow as Cache Rules, so you can manage all cache configuration through a single promotion pipeline.
  * **Independent environment control** : Run different response-phase cache settings per environment. For example, strip `Set-Cookie` headers in staging to validate cacheability without affecting production traffic.



#### Get started

Configure Cache Response Rules in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules) under **Caching** > **Cache Rules** , or via the [Rulesets API](https://developers.cloudflare.com/ruleset-engine/rulesets-api/). For more details, refer to the [Cache Response Rules documentation](https://developers.cloudflare.com/cache/how-to/cache-response-rules/) and the [Version Management documentation](https://developers.cloudflare.com/version-management/).
