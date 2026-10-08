---
url: https://developers.cloudflare.com/changelog/post/2026-05-11-r2-data-catalog-pricing-announced/
title: R2 Data Catalog pricing announced \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:52.343325+00:00
---

# R2 Data Catalog pricing announced · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-11-r2-data-catalog-pricing-announced/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 28, 2026

## R2 Data Catalog pricing announced

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-11-r2-data-catalog-pricing-announced/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) is a managed [Apache Iceberg ↗︎](https://iceberg.apache.org/) data catalog built directly into R2 buckets, queryable by any Iceberg-compatible engine such as Spark, Snowflake, and DuckDB. R2 Data Catalog now has published pricing for catalog operations and table compaction, in addition to standard [R2 storage and operations](https://developers.cloudflare.com/r2/pricing/).

Billing is not yet enabled. We will provide at least 30 days notice before we start charging for R2 Data Catalog usage.

Pricing is based on two dimensions:

  * **Catalog operations** : $9.00 / million operations for metadata requests such as creating tables, reading table metadata, and updating table properties.
  * **Compaction** : $0.005 / GB processed and $2.00 / million objects processed. These charges only apply when automatic compaction is turned on for a table.



Both dimensions include a monthly free tier: 1 million catalog operations, 10 GB of compaction data processed, and 1 million compaction objects processed.

For full pricing details and billing examples, refer to [R2 Data Catalog pricing](https://developers.cloudflare.com/basin-catalog/platform/pricing/).
