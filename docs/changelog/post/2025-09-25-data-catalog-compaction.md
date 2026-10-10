---
url: https://developers.cloudflare.com/changelog/post/2025-09-25-data-catalog-compaction/
title: R2 Data Catalog now supports compaction \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:48.515617+00:00
---

# R2 Data Catalog now supports compaction · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-25-data-catalog-compaction/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 25, 2025

## R2 Data Catalog now supports compaction

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now enable automatic compaction for [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) to improve query performance.

Compaction is the process of taking a group of small files and combining them into fewer larger files. This is an important maintenance operation as it helps ensure that query performance remains consistent by reducing the number of files that needs to be scanned.

To enable automatic compaction in R2 Data Catalog, find it under **R2 Data Catalog** in your R2 bucket settings in the dashboard.

![compaction-dash](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=799,height=400,format=webp/_astro/compaction.MLojYuHL.png)

Or with [Wrangler](https://developers.cloudflare.com/workers/wrangler/), run:
    
    
    npx wrangler r2 bucket catalog compaction enable <BUCKET_NAME>  --target-size 128 --token <API_TOKEN>

To get started with compaction, check out [manage catalogs](https://developers.cloudflare.com/basin-catalog/manage-catalogs/). For best practices and limitations, refer to [about compaction](https://developers.cloudflare.com/basin-catalog/table-maintenance/).
