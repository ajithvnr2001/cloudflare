---
url: https://developers.cloudflare.com/changelog/post/2025-09-25-pipelines-sql/
title: Pipelines now supports SQL transformations and Apache Iceberg \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:48.350023+00:00
---

# Pipelines now supports SQL transformations and Apache Iceberg · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-25-pipelines-sql/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 25, 2025

## Pipelines now supports SQL transformations and Apache Iceberg

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Today, we are launching the new [Cloudflare Pipelines](https://developers.cloudflare.com/basin-pipelines/): a streaming data platform that ingests events, transforms them with [SQL](https://developers.cloudflare.com/basin-pipelines/sql-reference/select-statements/), and writes to [R2](https://developers.cloudflare.com/r2/) as [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables or Parquet files.

Pipelines can receive events via [HTTP endpoints](https://developers.cloudflare.com/basin-pipelines/streams/writing-to-streams/#send-via-http) or [Worker bindings](https://developers.cloudflare.com/basin-pipelines/streams/writing-to-streams/#send-via-workers), transform them with SQL, and deliver to R2 with exactly-once guarantees. This makes it easy to build analytics-ready warehouses for server logs, mobile application events, IoT telemetry, or clickstream data without managing streaming infrastructure.

For example, here is a pipeline that ingests clickstream events and filters out bot traffic while extracting domain information:
    
    
    INSERT into events_table
    SELECT
      user_id,
      lower(event) AS event_type,
      to_timestamp_micros(ts_us) AS event_time,
      regexp_match(url, '^https?://([^/]+)')[1]  AS domain,
      url,
      referrer,
      user_agent
    FROM events_json
    WHERE event = 'page_view'
      AND NOT regexp_like(user_agent, '(?i)bot|spider');

Get started by creating a pipeline in the dashboard or running a single command in [Wrangler](https://developers.cloudflare.com/workers/wrangler/):
    
    
    npx wrangler pipelines setup

Check out our [getting started guide](https://developers.cloudflare.com/basin-pipelines/getting-started/) to learn how to create a pipeline that delivers events to an [Iceberg table](https://developers.cloudflare.com/basin-catalog/) you can query with R2 SQL. Read more about today's announcement in our [blog post ↗︎](https://blog.cloudflare.com/cloudflare-data-platform).
