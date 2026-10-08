---
url: https://developers.cloudflare.com/cache/how-to/purge-cache/
title: Purge cache \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:44.825104+00:00
---

# Purge cache · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/how-to/purge-cache/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /Cache configuration
  4. /Purge cache



# Purge cache

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/how-to/purge-cache/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailability and limits Hostname, tag, prefix URL, and purge everything limits Single-file purge limits Token bucket rate limiting

Cloudflare's Instant Purge ensures that updates to your content are reflected immediately. Multiple options are available for purging content, with single-file cache purging (purge by URL) being the recommended method. However, the following additional options are also available:

  * [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/)
  * [​Purge everything](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/)
  * [Purge cache by cache-tags](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/)
  * [​Purge cache by hostname](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/)
  * [​Purge cache by prefix (URL)](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/)
  * [Purge cache key resources](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-cache-key/)
  * [P​urge varied images](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-varied-images/)
  * [Purge zone versions via API](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-zone-versions/)



To purge cached content using the Cloudflare API, refer to [Purge Cached Content](https://developers.cloudflare.com/api/resources/cache/methods/purge/).

To mark content as stale instead of removing it, [invalidate cached content](https://developers.cloudflare.com/cache/guides/invalidate-cache/). Cloudflare revalidates invalidated content on the next request and reuses content that has not changed.

Note

A successful purge request returns `HTTP 200`. This indicates that Cloudflare received the request — it does not confirm that Cloudflare cached the targeted content or evicted any content. To verify a purge, request the asset after purging and confirm that [`CF-Cache-Status`](https://developers.cloudflare.com/cache/concepts/cache-responses/) is no longer `HIT`.

Note

If versioning is active on your zone and multiple environments are configured, you can select the specific environment you want to purge. For more details, refer to the [Version Management](https://developers.cloudflare.com/version-management/) documentation.

## Availability and limits

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
Purge options | URL, Hostname, Tag, Prefix, and Purge Everything | URL, Hostname, Tag, Prefix, and Purge Everything | URL, Hostname, Tag, Prefix, and Purge Everything | URL, Hostname, Tag, Prefix, and Purge Everything  
  
Invalidation requests count toward the same limits as purge requests. For details, refer to [Invalidation limits](https://developers.cloudflare.com/cache/guides/invalidate-cache/#limits).

### Hostname, tag, prefix URL, and purge everything limits

The following limits apply per **account** to purge and invalidation requests:

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Requests | 5 requests per minute | 5 requests per second | 10 requests per second | 50 requests per second  
Bucket size | 25 | 25 | 50 | 500  
Max operations per request | 100 | 100 | 100 | 100  
  
If your account includes zones with different Cloudflare plans, the above limits are shared between all the zones with the same plan. For example, all the zones in your account with a Pro plan will share the limits for the Pro plan, and all the zones in your account with a Business plan will share the limits for the Business plan.

### Single-file purge limits

The following limits apply per **account** to purge and invalidation requests:

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
URLs | 800 URLs per second | 1500 URLs per second | 1500 URLs per second | 3000 URLs per second  
Max operations per request | 100 | 100 | 100 | 500  
  
If your account includes zones with different Cloudflare plans, the above limits are shared between all the zones with the same plan. For example, all the zones in your account with a Pro plan will share the limits for the Pro plan, and all the zones in your account with a Business plan will share the limits for the Business plan.

Note that the thresholds for URLs are calculated using a moving average.

### Token bucket rate limiting

Cloudflare uses token bucket rate limiting to limit the number of purge requests flowing through the system at any given time, ensuring a steady and manageable flow.

Each account tier has a defined request rate (for example, Free: 5 requests per minute, Business: 10 requests per second), and requests are only allowed if there are available tokens in the bucket. Tokens refill at a consistent rate, but each bucket has a maximum capacity (for example, Free: 25 tokens, Enterprise: 500 tokens), allowing short bursts of requests if tokens have accumulated.

If the bucket is empty, further requests must wait until new tokens are added. This system maintains fair usage while allowing occasional bursts within the bucket's capacity.

If you are an Enterprise customer and you need more operations, reach out to your account team for support.

[PreviousInvalidate cached content](https://developers.cloudflare.com/cache/guides/invalidate-cache/)[NextPurge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/how-to/purge-cache/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
