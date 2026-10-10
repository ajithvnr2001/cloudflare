---
url: https://developers.cloudflare.com/changelog/post/2026-10-02-hash-in-range-ga/
title: hash_in_range() is globally available for HTTP products \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:29.560122+00:00
---

# hash_in_range() is globally available for HTTP products · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-02-hash-in-range-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 2, 2026

## hash_in_range() is globally available for HTTP products

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`hash_in_range()` is globally available for HTTP products on all plans. It hashes fields into an integer within a specified range. Use this result to select a portion of requests.

Use `cf.random_seed` to select approximately 10% of requests at random:
    
    
    hash_in_range(0, 100, cf.random_seed) < 10

With Cloudflare for SaaS, use [custom metadata](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/) to control rollout progression. Define `rollout_pct` as a custom key for each hostname. Set its value to an integer from 0 to 100. The expression selects approximately that percentage of requests:
    
    
    hash_in_range(0, 100, cf.random_seed) < coalesce(lookup_json_integer(cf.hostname.metadata, "rollout_pct"), 0)

If `rollout_pct` is missing, `coalesce()` supplies `0`. The rule then matches no requests.

For details, refer to the [`hash_in_range()` function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#hash_in_range).
