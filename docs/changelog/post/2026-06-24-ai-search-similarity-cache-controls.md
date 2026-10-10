---
url: https://developers.cloudflare.com/changelog/post/2026-06-24-ai-search-similarity-cache-controls/
title: Control AI Search similarity cache freshness \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:36.146852+00:00
---

# Control AI Search similarity cache freshness · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-24-ai-search-similarity-cache-controls/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 24, 2026

## Control AI Search similarity cache freshness

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now gives you more control over [similarity cache](https://developers.cloudflare.com/ai-search/configuration/retrieval/cache/) freshness. Similarity cache helps reduce latency and inference cost by reusing responses for semantically similar queries.

With these updates, you can choose how long responses are eligible for reuse and clear cached responses when they may be stale.

#### Cache duration now defaults to 48 hours

Previously, AI Search cached responses for a fixed duration of 30 days. Cached responses now use the instance's `cache_ttl` setting, and the default is **48 hours**.

You can set `cache_ttl` when creating or updating an instance to choose a cache duration from 10 minutes to 6 days.

Use a shorter TTL when your source content changes frequently and freshness is more important. Use a longer TTL when your content is stable and you want more cache reuse.

For example, set `cache_ttl` to `518400` to retain cached responses for 6 days:
    
    
    {
    	"cache_ttl": 518400
    }

#### Purge cached responses

You can also purge all cached responses for an instance on demand. Purging cached responses does not delete indexed content or source files.

It prevents AI Search from reusing previous cached responses, so subsequent similar queries generate fresh answers and repopulate the cache.
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/instances/$INSTANCE_NAME/purge_cache" \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

You can also purge cached responses from the instance settings page in the Cloudflare dashboard.

Refer to [similarity cache](https://developers.cloudflare.com/ai-search/configuration/retrieval/cache/) for the full list of supported `cache_ttl` values and more details about cache behavior.
