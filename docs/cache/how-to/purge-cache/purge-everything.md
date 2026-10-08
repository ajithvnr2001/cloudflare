---
url: https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/
title: \u200bPurge everything \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:45.230814+00:00
---

# ​Purge everything · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /…

Cache configuration

  4. /[Purge cache](https://developers.cloudflare.com/cache/how-to/purge-cache/)
  5. /​Purge everything



# ​Purge everything

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewResulting cache status

To maintain optimal site performance, Cloudflare strongly recommends using single-file (by URL) purging instead of a complete cache purge.

Purging everything instantly clears all resources from your CDN cache in all Cloudflare data centers. Each new request for a purged resource is a cache miss. Cloudflare fetches the full resource from your origin server and caches it again.

To have Cloudflare revalidate cached resources with your origin server instead, [invalidate everything](https://developers.cloudflare.com/cache/guides/invalidate-cache/). If your origin server confirms that a resource has not changed, Cloudflare reuses the cached copy.

Caution

When you purge everything, all cached content for your zone is removed at once. Every subsequent request must be served from your origin until the cache is repopulated. On high-traffic sites with many assets, this can cause a large spike in origin requests and may significantly slow down your site or overload your origin server.

Before using purge everything, consider whether a more targeted method — such as [purge by URL](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/), [purge by prefix](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/), or [purge by tag](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/) — can achieve the same result with less impact on your origin. If your zone uses [Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/), cache repopulation also propagates across cache tiers, which can further increase origin load during this period.

  1. In the Cloudflare dashboard, go to the **Configuration** page.

[ Go to **Configuration** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/caching/configuration)
  2. Under **Purge Cache** , select **Purge Everything**. A warning window appears.

  3. If you agree, select **Purge Everything**.




Note

When purging everything for a non-production cache environment, all files for that specific cache environment will be purged. However, when purging everything for the production environment, all files will be purged across all environments.

For information on rate limits, refer to the [Availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits) section.

## Resulting cache status

After you purge everything, the next request for each resource returns a `CF-Cache-Status` header of [`MISS`](https://developers.cloudflare.com/cache/concepts/cache-responses/#miss).

[PreviousPurge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/)[NextPurge cache by cache-tags](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/how-to/purge-cache/purge-everything.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
