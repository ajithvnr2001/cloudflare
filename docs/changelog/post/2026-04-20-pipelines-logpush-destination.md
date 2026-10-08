---
url: https://developers.cloudflare.com/changelog/post/2026-04-20-pipelines-logpush-destination/
title: Cloudflare Pipelines as a Logpush destination \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:48.213560+00:00
---

# Cloudflare Pipelines as a Logpush destination · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-20-pipelines-logpush-destination/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 20, 2026

## Cloudflare Pipelines as a Logpush destination

[Logs](https://developers.cloudflare.com/logs/)[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-20-pipelines-logpush-destination/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Logpush has traditionally been great at delivering Cloudflare logs to a variety of destinations in JSON format. While JSON is flexible and easily readable, it can be inefficient to store and query at scale.

With this release, you can now send your logs directly to [Pipelines](https://developers.cloudflare.com/basin-pipelines/) to ingest, transform, and store your logs in [R2](https://developers.cloudflare.com/r2/) as Parquet files or Apache Iceberg tables managed by [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/). This makes the data footprint more compact and more efficient at querying your logs instantly with [R2 SQL](https://developers.cloudflare.com/basin-sql/) or any other query engine that supports Apache Iceberg or Parquet.

#### Transform logs before storage

Pipelines SQL runs on each log record in-flight, so you can reshape your data before it is written. For example, you can drop noisy fields, redact sensitive values, or derive new columns:
    
    
    INSERT INTO http_logs_sink
    SELECT
      ClientIP,
      EdgeResponseStatus,
      to_timestamp_micros(EdgeStartTimestamp) AS event_time,
      upper(ClientRequestMethod) AS method,
      sha256(ClientIP) AS hashed_ip
    FROM http_logs_stream
    WHERE EdgeResponseStatus >= 400;

Pipelines SQL supports string functions, regex, hashing, JSON extraction, timestamp conversion, conditional expressions, and more. For the full list, refer to the [Pipelines SQL reference](https://developers.cloudflare.com/basin-pipelines/sql-reference/).

#### Get started

To configure Pipelines as a Logpush destination, refer to [Enable Cloudflare Pipelines](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/pipelines/).
