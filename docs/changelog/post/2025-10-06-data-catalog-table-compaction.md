---
url: https://developers.cloudflare.com/changelog/post/2025-10-06-data-catalog-table-compaction/
title: R2 Data Catalog table-level compaction \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:48.048142+00:00
---

# R2 Data Catalog table-level compaction · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-06-data-catalog-table-compaction/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 6, 2025

## R2 Data Catalog table-level compaction

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now enable compaction for individual [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/), giving you fine-grained control over different workloads.
    
    
    # Enable compaction for a specific table (no token required)
    npx wrangler r2 bucket catalog compaction enable <BUCKET> <NAMESPACE> <TABLE> --target-size 256

This allows you to:

  * Apply different target file sizes per table
  * Disable compaction for specific tables
  * Optimize based on table-specific access patterns



Learn more at [Manage catalogs](https://developers.cloudflare.com/basin-catalog/manage-catalogs/).
