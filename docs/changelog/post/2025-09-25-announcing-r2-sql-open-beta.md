---
url: https://developers.cloudflare.com/changelog/post/2025-09-25-announcing-r2-sql-open-beta/
title: Announcing R2 SQL \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:23.894139+00:00
---

# Announcing R2 SQL · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-25-announcing-r2-sql-open-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 25, 2025

## Announcing R2 SQL

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-25-announcing-r2-sql-open-beta/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Today, we are launching the **open beta** for [R2 SQL](https://developers.cloudflare.com/basin-sql/): A serverless, distributed query engine that can efficiently analyze petabytes of data in [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables managed by [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/).

R2 SQL is ideal for exploring analytical and time-series data stored in R2, such as logs, events from [Pipelines](https://developers.cloudflare.com/basin-pipelines/), or clickstream and user behavior data.

If you already have a table in R2 Data Catalog, running queries is as simple as:
    
    
    npx wrangler r2 sql query YOUR_WAREHOUSE "
    SELECT
        user_id,
        event_type,
        value
    FROM events.user_events
    WHERE event_type = 'CHANGELOG' or event_type = 'BLOG'
      AND __ingest_ts > '2025-09-24T00:00:00Z'
    ORDER BY __ingest_ts DESC
    LIMIT 100"

To get started with R2 SQL, check out our [getting started guide](https://developers.cloudflare.com/basin-sql/get-started/) or learn more about supported features in the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/). For a technical deep dive into how we built R2 SQL, read our [blog post ↗︎](https://blog.cloudflare.com/r2-sql-deep-dive/).
