---
url: https://developers.cloudflare.com/changelog/post/2026-05-28-r2-data-catalog-dashboard/
title: R2 Data Catalog gets a dedicated dashboard experience \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:55.064638+00:00
---

# R2 Data Catalog gets a dedicated dashboard experience · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-28-r2-data-catalog-dashboard/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 28, 2026

## R2 Data Catalog gets a dedicated dashboard experience

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-28-r2-data-catalog-dashboard/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) is a managed [Apache Iceberg ↗︎](https://iceberg.apache.org/) data catalog built directly into your R2 bucket. It exposes a standard Iceberg REST catalog interface so you can connect query engines like [Spark](https://developers.cloudflare.com/basin-catalog/config-examples/spark-scala/), [Snowflake](https://developers.cloudflare.com/basin-catalog/config-examples/snowflake/), [DuckDB](https://developers.cloudflare.com/basin-catalog/config-examples/duckdb/), and [R2 SQL](https://developers.cloudflare.com/basin-sql/) to your data in R2.

R2 Data Catalog now has a dedicated section in the Cloudflare dashboard, replacing the previous settings panel embedded in R2 bucket configuration. The new experience includes:

![R2 Data Catalog dashboard overview](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3070,height=1486,format=webp/_astro/data-catalog-dashboard.BsKDvUQn.png)

  * **Catalog overview** — View all your catalogs in one place with catalog request counts, bucket sizes, and table maintenance status at a glance.
  * **Guided setup wizard** — Create a catalog in three steps: choose or create an R2 bucket, configure table maintenance (compaction and snapshot expiration), and review. The wizard creates the bucket and generates a service credential automatically.
  * **Settings management** — A dedicated settings page for each catalog with sections for general configuration, table maintenance, service credentials, and disabling the catalog. You can now enable and configure [snapshot expiration](https://developers.cloudflare.com/basin-catalog/table-maintenance/) directly from the dashboard.
  * **Built-in metrics** — Five charts on each catalog's metrics tab: bytes compacted, files compacted, catalog requests, storage size, and snapshots expired.



To get started, go to **R2 Data Catalog** in the Cloudflare dashboard or refer to the [getting started guide](https://developers.cloudflare.com/basin-catalog/get-started/) and [manage catalogs documentation](https://developers.cloudflare.com/basin-catalog/manage-catalogs/).
