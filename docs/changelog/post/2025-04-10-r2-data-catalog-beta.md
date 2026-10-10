---
url: https://developers.cloudflare.com/changelog/post/2025-04-10-r2-data-catalog-beta/
title: R2 Data Catalog is a managed Apache Iceberg data catalog built directly into R2 buckets \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:52.916501+00:00
---

# R2 Data Catalog is a managed Apache Iceberg data catalog built directly into R2 buckets · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-10-r2-data-catalog-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 10, 2025

## R2 Data Catalog is a managed Apache Iceberg data catalog built directly into R2 buckets

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Today, we are launching [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) in open beta, a managed Apache Iceberg catalog built directly into your [Cloudflare R2](https://developers.cloudflare.com/r2/) bucket.

If you are not already familiar with it, [Apache Iceberg ↗︎](https://iceberg.apache.org/) is an open table format designed to handle large-scale analytics datasets stored in object storage, offering ACID transactions and schema evolution. R2 Data Catalog exposes a standard Iceberg REST catalog interface, so you can connect engines like [Spark](https://developers.cloudflare.com/basin-catalog/config-examples/spark-scala/), [Snowflake](https://developers.cloudflare.com/basin-catalog/config-examples/snowflake/), and [PyIceberg](https://developers.cloudflare.com/basin-catalog/config-examples/pyiceberg/) to start querying your tables using the tools you already know.

To enable a data catalog on your R2 bucket, find **R2 Data Catalog** in your buckets settings in the dashboard, or run:
    
    
    npx wrangler r2 bucket catalog enable my-bucket

And that's it. You'll get a catalog URI and warehouse you can plug into your favorite Iceberg engines.

Visit our [getting started guide](https://developers.cloudflare.com/basin-catalog/get-started/) for step-by-step instructions on enabling R2 Data Catalog, creating tables, and running your first queries.
