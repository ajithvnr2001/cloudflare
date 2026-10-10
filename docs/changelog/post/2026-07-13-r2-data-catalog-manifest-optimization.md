---
url: https://developers.cloudflare.com/changelog/post/2026-07-13-r2-data-catalog-manifest-optimization/
title: R2 Data Catalog compaction now optimizes manifest files \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:34.955567+00:00
---

# R2 Data Catalog compaction now optimizes manifest files · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-13-r2-data-catalog-manifest-optimization/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 13, 2026

## R2 Data Catalog compaction now optimizes manifest files

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/), a managed [Apache Iceberg ↗︎](https://iceberg.apache.org/) catalog built into R2, now automatically optimizes manifest files as part of [compaction](https://developers.cloudflare.com/basin-catalog/table-maintenance/).

Manifest files track the data files that make up an Iceberg table. As a table accumulates many small or fragmented manifests, query engines must read more metadata during query planning, which slows down queries even before any data is scanned.

When compaction runs, R2 Data Catalog now rewrites and clusters manifest files by partition as a best-effort pre-step. This consolidates fragmented manifests, reduces the number of manifests a query engine must open, and lowers metadata I/O overhead. Tables that are already well-clustered are skipped, so the operation only runs when it provides a benefit.

This happens automatically for tables with compaction enabled — no configuration changes are required.

For more information, refer to [Table maintenance](https://developers.cloudflare.com/basin-catalog/table-maintenance/).
