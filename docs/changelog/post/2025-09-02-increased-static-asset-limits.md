---
url: https://developers.cloudflare.com/changelog/post/2025-09-02-increased-static-asset-limits/
title: Increased static asset limits for Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:49.373545+00:00
---

# Increased static asset limits for Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-02-increased-static-asset-limits/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 4, 2025

## Increased static asset limits for Workers

[Workers](https://developers.cloudflare.com/workers/)[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now upload up to **100,000 static assets** per Worker version

  * Paid and Workers for Platforms users can now upload up to **100,000 static assets** per Worker version, a 5x increase from the previous limit of 20,000.
  * Customers on the free plan still have the same limit as before — 20,000 static assets per version of your Worker
  * The individual file size limit of 25 MiB remains unchanged for all customers.



This increase allows you to build larger applications with more static assets without hitting limits.

#### Wrangler

To take advantage of the increased limits, you must use **Wrangler version 4.34.0 or higher**. Earlier versions of Wrangler will continue to enforce the previous 20,000 file limit.

#### Learn more

For more information about Workers static assets, see the [Static Assets documentation](https://developers.cloudflare.com/workers/static-assets/) and [Platform Limits](https://developers.cloudflare.com/workers/platform/limits/#static-assets).
