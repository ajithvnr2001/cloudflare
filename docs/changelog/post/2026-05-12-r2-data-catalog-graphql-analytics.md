---
url: https://developers.cloudflare.com/changelog/post/2026-05-12-r2-data-catalog-graphql-analytics/
title: R2 Data Catalog now exposes metrics via the GraphQL Analytics API \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:38.313763+00:00
---

# R2 Data Catalog now exposes metrics via the GraphQL Analytics API · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-12-r2-data-catalog-graphql-analytics/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 12, 2026

## R2 Data Catalog now exposes metrics via the GraphQL Analytics API

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) is a managed Apache Iceberg data catalog built directly into your R2 bucket that allows you to connect query engines like [R2 SQL](https://developers.cloudflare.com/basin-sql/), Spark, Snowflake, and DuckDB to your data in R2.

You can now query analytics for your R2 Data Catalog warehouses via Cloudflare's [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/). Two new datasets are available:

  * **`r2CatalogDataOperationsAdaptiveGroups`** tracks Iceberg REST API requests made to your catalog, including operation type, request duration, HTTP status, and request body bytes. Use this to monitor request volume and latency across warehouses, namespaces, and tables.
  * **`r2CatalogTableMaintenanceAdaptiveGroups`** tracks table maintenance jobs such as compaction and snapshot expiration. Use this to monitor job success rates, files processed, bytes read and written, and job duration.



Both datasets support filtering by warehouse name, namespace, table name, and time range. They also include percentile aggregations for duration metrics.

For detailed schema information and example queries, refer to the [R2 Data Catalog metrics and analytics documentation](https://developers.cloudflare.com/basin-catalog/observability/metrics/).
