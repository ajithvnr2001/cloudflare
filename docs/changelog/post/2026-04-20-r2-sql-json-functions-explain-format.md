---
url: https://developers.cloudflare.com/changelog/post/2026-04-20-r2-sql-json-functions-explain-format/
title: R2 SQL adds JSON functions, EXPLAIN FORMAT JSON, and unpartitioned table support \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:39.969053+00:00
---

# R2 SQL adds JSON functions, EXPLAIN FORMAT JSON, and unpartitioned table support · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-20-r2-sql-json-functions-explain-format/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 20, 2026

## R2 SQL adds JSON functions, EXPLAIN FORMAT JSON, and unpartitioned table support

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 SQL](https://developers.cloudflare.com/basin-sql/) is Cloudflare's serverless, distributed, analytics query engine for querying [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables stored in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/).

R2 SQL now supports functions for querying JSON data stored in Apache Iceberg tables, an easier way to parse query plans with `EXPLAIN FORMAT JSON`, and querying tables without partition keys stored in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/).

JSON functions extract and manipulate JSON values directly in SQL without client-side processing:
    
    
    SELECT
      json_get_str(doc, 'name') AS name,
      json_get_int(doc, 'user', 'profile', 'level') AS level,
      json_get_bool(doc, 'active') AS is_active
    FROM my_namespace.sales_data
    WHERE json_contains(doc, 'email')

For a full list of available functions, refer to [JSON functions](https://developers.cloudflare.com/basin-sql/sql-reference/scalar-functions/#json-functions).

`EXPLAIN FORMAT JSON` returns query execution plans as structured JSON for programmatic analysis and observability integrations:
    
    
    npx wrangler r2 sql query "${WAREHOUSE}" "EXPLAIN FORMAT JSON SELECT * FROM logpush.requests LIMIT 10;"
    
    ┌──────────────────────────────────────┐
    │ plan                                 │
    ├──────────────────────────────────────┤
    │ {                                    │
    │   "name": "CoalescePartitionsExec",  │
    │   "output_partitions": 1,            │
    │   "rows": 10,                        │
    │   "size_approx": "310B",             │
    │   "children": [                      │
    │     {                                │
    │       "name": "DataSourceExec",      │
    │       "output_partitions": 4,        │
    │       "rows": 28951,                 │
    │       "size_approx": "900.0KB",      │
    │       "table": "logpush.requests",   │
    │       "files": 7,                    │
    │       "bytes": 900019,               │
    │       "projection": [                │
    │         "__ingest_ts",               │
    │         "CPUTimeMs",                 │
    │         "DispatchNamespace",         │
    │         "Entrypoint",                │
    │         "Event",                     │
    │         "EventTimestampMs",          │
    │         "EventType",                 │
    │         "Exceptions",                │
    │         "Logs",                      │
    │         "Outcome",                   │
    │         "ScriptName",                │
    │         "ScriptTags",                │
    │         "ScriptVersion",             │
    │         "WallTimeMs"                 │
    │       ],                             │
    │       "limit": 10                    │
    │     }                                │
    │   ]                                  │
    │ }                                    │
    └──────────────────────────────────────┘

For more details, refer to [EXPLAIN](https://developers.cloudflare.com/basin-sql/sql-reference/#explain).

Unpartitioned Iceberg tables can now be queried directly, which is useful for smaller datasets or data without natural time dimensions. For tables with more than 1000 files, partitioning is still recommended for better performance.

Refer to [Limitations and best practices](https://developers.cloudflare.com/basin-sql/reference/limitations-best-practices/) for the latest guidance on using R2 SQL.
