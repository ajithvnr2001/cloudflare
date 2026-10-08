---
url: https://developers.cloudflare.com/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/
title: R2 Data Catalog now supports automatic snapshot expiration \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:32.334414+00:00
---

# R2 Data Catalog now supports automatic snapshot expiration · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 18, 2025

## R2 Data Catalog now supports automatic snapshot expiration

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) now supports automatic snapshot expiration for Apache Iceberg tables.

In Apache Iceberg, a snapshot is metadata that represents the state of a table at a given point in time. Every mutation creates a new snapshot which enable powerful features like time travel queries and rollback capabilities but will accumulate over time.

Without regular cleanup, these accumulated snapshots can lead to:

  * Metadata overhead
  * Slower table operations
  * Increased storage costs.



Snapshot expiration in R2 Data Catalog automatically removes old table snapshots based on your configured retention policy, improving performance and storage costs.
    
    
    # Enable catalog-level snapshot expiration
    # Expire snapshots older than 7 days, always retain at least 10 recent snapshots
    npx wrangler r2 bucket catalog snapshot-expiration enable my-bucket \
      --older-than-days 7 \
      --retain-last 10

Snapshot expiration uses two parameters to determine which snapshots to remove:

  * `--older-than-days`: age threshold in days
  * `--retain-last`: minimum snapshot count to retain



Both conditions must be met before a snapshot is expired, ensuring you always retain recent snapshots even if they exceed the age threshold.

This feature complements [automatic compaction](https://developers.cloudflare.com/basin-catalog/table-maintenance/), which optimizes query performance by combining small data files into larger ones. Together, these automatic maintenance operations keep your Iceberg tables performant and cost-efficient without manual intervention.

For more information, refer to [Table maintenance](https://developers.cloudflare.com/basin-catalog/table-maintenance/) or [Manage catalogs](https://developers.cloudflare.com/basin-catalog/manage-catalogs/).
