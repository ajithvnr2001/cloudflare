---
url: https://developers.cloudflare.com/changelog/post/2026-07-06-r2-data-catalog-delete-warnings/
title: R2 Data Catalog warns before you delete data manually \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.511742+00:00
---

# R2 Data Catalog warns before you delete data manually · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-06-r2-data-catalog-delete-warnings/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 7, 2026

## R2 Data Catalog warns before you delete data manually

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) is a managed [Apache Iceberg ↗︎](https://iceberg.apache.org/) catalog built directly into your R2 bucket. Iceberg tracks your data through a tree of metadata files, so every insert, update, and delete must go through a catalog transaction. Manually adding, modifying, or deleting objects outside the catalog can leave pointers referencing files that no longer exist, corrupting the table into an inconsistent state that is difficult to recover from.

To help prevent this, the R2 dashboard and Wrangler now warn you when you attempt a manual delete operation on a Data Catalog-enabled bucket.

#### Dashboard

When you try to delete objects from a bucket that has R2 Data Catalog enabled, the dashboard displays a warning explaining that the operation could leave the catalog in an invalid state, with a link to the documentation for deleting data correctly. You can cancel the operation or choose to proceed anyway.

![R2 dashboard warning shown before deleting objects from a Data Catalog-enabled bucket](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1886,height=684,format=webp/_astro/data-catalog-delete-warning.DoBR0sFO.png)

#### Wrangler

Wrangler now checks whether a bucket is Data Catalog-enabled before running a delete and warns you before continuing:
    
    
    Data Catalog is enabled for this bucket. 
    Proceeding may leave the data catalog in an invalid state. Continue?

To learn how to safely manage and delete data in your tables, refer to the [R2 Data Catalog documentation](https://developers.cloudflare.com/basin-catalog/).
