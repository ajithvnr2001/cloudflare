---
url: https://developers.cloudflare.com/changelog/product/basin-sql/
title: Basin SQL Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:11.193267+00:00
---

# Basin SQL Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/basin-sql/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Oct 1, 2026

## [Cloudflare Basin is now generally available](https://developers.cloudflare.com/changelog/post/2026-10-01-basin-ga/)

[Basin](https://developers.cloudflare.com/basin/)[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin SQL](https://developers.cloudflare.com/basin-sql/)

[Basin](https://developers.cloudflare.com/basin/), formerly the Cloudflare Data Platform, is now generally available. Basin brings an end-to-end analytics platform to the Developer Platform, enabling you to collect data from a variety of sources, such as apps, infrastructure, devices, and other Cloudflare services, then query it to answer analytical questions.

#### Basin Pipelines

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/), formerly Cloudflare Pipelines, ingests events from Workers, HTTP endpoints, and Cloudflare [Logpush](https://developers.cloudflare.com/logpush/). It transforms events with SQL and ingests them into Iceberg tables or files on R2. With Basin Pipelines you can:

  * Ingest application and device events through HTTP endpoints or Workers bindings.
  * Filter and reshape Cloudflare logs before storing them as Iceberg tables, Parquet, or JSON.
  * Catch schema mismatches with typed bindings and investigate dropped events in the dashboard.



#### Basin Catalog

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/), formerly R2 Data Catalog, manages and automatically maintains [Apache Iceberg tables ↗︎](https://iceberg.apache.org/) to keep them fast, cost-efficient, and accessible to any compatible query engine. With Basin Catalog you can:

  * Connect DuckDB, Spark, Snowflake, or PyIceberg to the same tables.
  * Maintain growing tables with compaction, snapshot expiration, and manifest optimization.
  * Share analytical data across tools and clouds without paying egress fees.



#### Basin SQL

[Basin SQL](https://developers.cloudflare.com/basin-sql/), formerly R2 SQL, is a serverless, distributed SQL engine for querying large Apache Iceberg tables in Basin Catalog without managing or scaling compute. With Basin SQL you can:

  * Summarize and rank data with standard and approximate aggregates, grouping sets, and window functions.
  * Combine and inspect datasets with joins, subqueries, common table expressions, set operations, schema discovery, and `EXPLAIN`.
  * Transform strings, timestamps, JSON, and complex values with more than 190 functions.



#### Get started

To get started with creating an end-to-end data pipeline, run:

npmyarnpnpm
    
    
    npx wrangler basin pipelines setup
    
    
    yarn wrangler basin pipelines setup
    
    
    pnpm wrangler basin pipelines setup

Or get started by referring to the [Basin getting started guide](https://developers.cloudflare.com/basin/get-started/guide/).

Note

Existing Cloudflare Pipelines, R2 Data Catalog, and R2 SQL resources and configurations will continue to work and will be deprecated over time.

Aug 3, 2026

## [Billing is now enabled for R2 SQL](https://developers.cloudflare.com/changelog/post/2026-08-03-r2-sql-billing-enabled/)

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

Billing is now enabled for [R2 SQL](https://developers.cloudflare.com/basin-sql/) on non-enterprise accounts. R2 SQL usage beyond the included free tier will appear on your next invoice.

R2 SQL charges based on a single dimension:

  * **Data scanned** : $0.0025 / GB ($2.50 / TB) of compressed data read from R2 to execute your query.



All plans include 10 GB of data scanned per month. Each query is billed for a minimum of 10 MB of data scanned. R2 SQL pricing is additive to standard [R2 storage and operations](https://developers.cloudflare.com/r2/pricing/) and [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/platform/pricing/) charges. R2 does not charge for egress, so there is no additional data transfer cost.

For example, a user who stores 500 GB of Parquet data in R2 Data Catalog and runs queries that scan a total of 50 GB of compressed data during the month would be billed as follows:

Dimension | Usage | Included | Billable | Cost  
---|---|---|---|---  
R2 storage | 500 GB-month | 10 GB-month | 490 GB-month | $7.35  
R2 SQL (data scanned) | 50 GB | 10 GB | 40 GB | $0.10  
**Total** |  |  |  | **$7.45**  
  
For full pricing details and billing examples, refer to [R2 SQL pricing](https://developers.cloudflare.com/basin-sql/platform/pricing/).

Jul 8, 2026

## [Query R2 Data Catalog tables with R2 SQL from the dashboard](https://developers.cloudflare.com/changelog/post/2026-07-08-query-r2-sql-from-dashboard/)

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

You can now query your [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) tables with [R2 SQL](https://developers.cloudflare.com/basin-sql/) directly from the Cloudflare dashboard, without installing a CLI or wiring up a client. This makes it easy to explore your [Apache Iceberg ↗︎](https://iceberg.apache.org/) data, validate queries, and inspect results in one place.

![R2 SQL Query Editor](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3080,height=1696,format=webp/_astro/r2-sql-studio.DCmHJaqy.png)

To get started, go to [R2 Data Catalog ↗︎](https://dash.cloudflare.com/?to=/:account/data-catalog/overview) in the Cloudflare dashboard and select **Query data** to launch the built-in SQL editor. From there you can:

  * **Write and run queries interactively** — Iterate on R2 SQL directly in the browser with syntax highlighting and autocomplete, instead of re-running commands through Wrangler or the REST API.
  * **Explore your data** — Explore your namespaces and tables alongside the editor so you can discover what's queryable without leaving the page or using other tools.
  * **Understand results and performance** — View result sets with per-query statistics, export them, and get helpful `EXPLAIN` outputs to see exactly how a query runs.



Note

Your R2 SQL credential is generated and stored for you and can be rotated in the R2 Data Catalog settings page.

Jun 22, 2026

## [R2 SQL now supports window functions, DISTINCT, and set operations](https://developers.cloudflare.com/changelog/post/2026-06-21-window-functions-distinct-set-operations/)

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

R2 SQL now supports window functions, `SELECT DISTINCT`, set operations, and additional aggregates, making it easier to write analytical queries without preprocessing your data elsewhere.

[R2 SQL](https://developers.cloudflare.com/basin-sql/) is Cloudflare's serverless, distributed SQL engine for querying [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables stored in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/).

#### New capabilities

  * **Window functions** — `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `PERCENT_RANK`, `CUME_DIST`, `NTILE`, `LAG`, `LEAD`, `FIRST_VALUE`, `LAST_VALUE`, `NTH_VALUE`, and aggregates with an `OVER (...)` clause, including `PARTITION BY` and explicit frames
  * **QUALIFY** — filter rows based on a window function result
  * **DISTINCT** — `SELECT DISTINCT`, `DISTINCT ON (...)`, and the `DISTINCT` modifier on aggregates such as `COUNT(DISTINCT ...)`
  * **Set operations** — `UNION`, `UNION ALL`, `INTERSECT`, and `EXCEPT`
  * **Grouping extensions** — `GROUPING SETS`, `ROLLUP`, and `CUBE`
  * **Exact aggregates** — `MEDIAN`, `PERCENTILE_CONT`, `ARRAY_AGG`, and `STRING_AGG`



#### Examples

#### Rank rows with a window function
    
    
    SELECT customer_id, region,
           ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC) AS rank_in_region
    FROM my_namespace.sales_data

#### Filter with QUALIFY
    
    
    SELECT customer_id, region, total_amount
    FROM my_namespace.sales_data
    QUALIFY ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC) <= 3

#### Combine tables with a set operation
    
    
    SELECT customer_id FROM my_namespace.sales_data
    EXCEPT
    SELECT customer_id FROM my_namespace.archived_sales

The named `WINDOW` clause is not supported — inline the `OVER (...)` specification at each call site. For the full syntax reference, refer to the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/). For supported features and performance guidance, refer to [Limitations and best practices](https://developers.cloudflare.com/basin-sql/reference/limitations-best-practices/).

Jun 8, 2026

## [R2 SQL now supports UNION, INTERSECT, EXCEPT, and SELECT DISTINCT](https://developers.cloudflare.com/changelog/post/2026-06-05-union-intersect-except-select-distinct/)

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

[R2 SQL](https://developers.cloudflare.com/basin-sql/) now supports set operations (`UNION`, `INTERSECT`, `EXCEPT`) and `SELECT DISTINCT`, expanding the range of analytical queries you can run directly on [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/).

#### Set operations

Combine the results of multiple `SELECT` statements:

  * **`UNION`** — returns all rows from both queries, removing duplicates
  * **`UNION ALL`** — returns all rows from both queries, including duplicates
  * **`INTERSECT`** — returns only rows that appear in both queries
  * **`EXCEPT`** — returns rows from the first query that do not appear in the second


    
    
    -- Find zones that had either firewall blocks OR high-risk requests
    SELECT zone_id FROM my_namespace.firewall_events WHERE action = 'block'
    UNION
    SELECT zone_id FROM my_namespace.http_requests WHERE risk_score > 0.8
    
    
    -- Find zones with both firewall blocks AND high traffic
    SELECT zone_id FROM my_namespace.firewall_events WHERE action = 'block'
    INTERSECT
    SELECT zone_id FROM my_namespace.http_requests
    GROUP BY zone_id
    HAVING COUNT(*) > 10000
    
    
    -- Find enterprise zones that have not been compacted
    SELECT zone_id FROM my_namespace.zones WHERE plan = 'enterprise'
    EXCEPT
    SELECT zone_id FROM my_namespace.compaction_history

#### Select distinct

Eliminate duplicate rows from query results:
    
    
    SELECT DISTINCT region, department
    FROM my_namespace.sales_data
    WHERE total_amount > 1000
    ORDER BY region, department
    LIMIT 100

For large datasets where approximate results are acceptable, `approx_distinct()` remains a faster alternative for counting unique values.

For the full syntax reference, refer to the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/). For performance guidance, refer to [Limitations and best practices](https://developers.cloudflare.com/basin-sql/reference/limitations-best-practices/).

May 28, 2026

## [R2 SQL pricing announced](https://developers.cloudflare.com/changelog/post/2026-05-11-r2-sql-pricing-announced/)

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

[R2 SQL](https://developers.cloudflare.com/basin-sql/) is a serverless, distributed query engine that runs SQL against [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables stored in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/). R2 SQL now has published pricing based on a single dimension: the volume of compressed data scanned to execute your queries. At $2.50 / TB ($0.0025 / GB), R2 SQL is priced at half the cost of AWS Athena and less than half of Google BigQuery on-demand.

Billing is not yet enabled. We will provide at least 30 days notice before we start charging for R2 SQL usage.

Data scanned is measured on compressed bytes read from R2 object storage. This matches what you see in your R2 bucket — if a Parquet file is 100 MB on disk, scanning that file bills for 100 MB. Each query has a minimum billing increment of 10 MB.

All plans include 10 GB of data scanned per month. Standard [R2 storage and operations](https://developers.cloudflare.com/r2/pricing/) and [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/platform/pricing/) charges apply separately.

For full pricing details and billing examples, refer to [R2 SQL pricing](https://developers.cloudflare.com/basin-sql/platform/pricing/).

May 15, 2026

## [R2 SQL now supports JOINs, subqueries, and multi-table queries](https://developers.cloudflare.com/changelog/post/2026-05-14-joins-subqueries-multi-table-queries/)

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

[R2 SQL](https://developers.cloudflare.com/basin-sql/) is Cloudflare's serverless, distributed SQL engine for querying [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables stored in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/). R2 SQL runs directly on Cloudflare's global network with no infrastructure to manage, so you can analyze data in R2 without exporting it to an external warehouse.

R2 SQL now supports joining multiple Iceberg tables in a single query. You can combine tables with JOINs, filter with subqueries, and define multi-table CTEs to build complex analytical queries.

#### New capabilities

  * **JOINs** — `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL OUTER JOIN`, `CROSS JOIN`, and implicit joins (comma-separated `FROM` with conditions in `WHERE`)
  * **Subqueries** — `IN` / `NOT IN`, `EXISTS` / `NOT EXISTS`, scalar subqueries in `SELECT` / `WHERE` / `HAVING`, and derived tables (subqueries in `FROM`)
  * **Multi-table CTEs** — `WITH` clauses can reference different tables and include JOINs
  * **Self-joins** — join a table with itself using different aliases
  * **Multi-way joins** — join three or more tables in a single query



#### Examples

#### Two-table JOIN with aggregation
    
    
    SELECT z.domain, z.plan, COUNT(*) AS request_count
    FROM my_namespace.zones z
    INNER JOIN my_namespace.http_requests h ON z.zone_id = h.zone_id
    WHERE z.plan = 'enterprise'
    GROUP BY z.domain, z.plan
    ORDER BY request_count DESC
    LIMIT 20

#### `EXISTS` subquery
    
    
    SELECT z.domain, z.plan
    FROM my_namespace.zones z
    WHERE EXISTS (
        SELECT 1 FROM my_namespace.firewall_events f
        WHERE f.zone_id = z.zone_id AND f.action = 'block'
    )
    ORDER BY z.domain
    LIMIT 20

#### Multi-table CTE with JOIN
    
    
    WITH top_zones AS (
        SELECT zone_id, COUNT(*) AS req_count
        FROM my_namespace.http_requests
        GROUP BY zone_id
        ORDER BY req_count DESC
        LIMIT 50
    ),
    zone_threats AS (
        SELECT zone_id, COUNT(*) AS threat_count
        FROM my_namespace.firewall_events
        WHERE risk_score > 0.5
        GROUP BY zone_id
    )
    SELECT tz.zone_id, tz.req_count, COALESCE(zt.threat_count, 0) AS threat_count
    FROM top_zones tz
    LEFT JOIN zone_threats zt ON tz.zone_id = zt.zone_id
    ORDER BY tz.req_count DESC
    LIMIT 20

For the full syntax reference, refer to the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/). For performance guidance with joins, refer to [Limitations and best practices](https://developers.cloudflare.com/basin-sql/reference/limitations-best-practices/).

Apr 20, 2026

## [R2 SQL adds JSON functions, EXPLAIN FORMAT JSON, and unpartitioned table support](https://developers.cloudflare.com/changelog/post/2026-04-20-r2-sql-json-functions-explain-format/)

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

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

Mar 23, 2026

## [R2 SQL now supports over 190 new functions, expressions, and complex types](https://developers.cloudflare.com/changelog/post/2026-03-23-expanded-sql-functions-expressions-complex-types/)

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

[R2 SQL](https://developers.cloudflare.com/basin-sql/) now supports an expanded SQL grammar so you can write richer analytical queries without exporting data. This release adds CASE expressions, column aliases, arithmetic in clauses, 163 scalar functions, 33 aggregate functions, EXPLAIN, Common Table Expressions (CTEs),and full struct/array/map access. R2 SQL is Cloudflare's serverless, distributed, analytics query engine for querying [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables stored in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/). This page documents the supported SQL syntax.

#### Highlights

  * **Column aliases** — `SELECT col AS alias` now works in all clauses
  * **CASE expressions** — conditional logic directly in SQL (searched and simple forms)
  * **Scalar functions** — 163 new functions across math, string, datetime, regex, crypto, encoding, and type inspection categories
  * **Aggregate functions** — statistical (variance, stddev, correlation, regression), bitwise, boolean, and positional aggregates join the existing basic and approximate functions
  * **Complex types** — query struct fields with bracket notation, use 46 array functions, and extract map keys/values
  * **Common table expressions (CTEs)** — use `WITH ... AS` to define named temporary result sets. Chained CTEs are supported. All CTEs must reference the same single table.
  * **Full expression support** — arithmetic, type casting (`CAST`, `TRY_CAST`, `::` shorthand), and `EXTRACT` in SELECT, WHERE, GROUP BY, HAVING, and ORDER BY



#### Examples

#### CASE expressions with statistical aggregates
    
    
    SELECT source,
        CASE
            WHEN AVG(price) > 30 THEN 'premium'
            WHEN AVG(price) > 10 THEN 'mid-tier'
            ELSE 'budget'
        END AS tier,
        round(stddev(price), 2) AS price_volatility,
        approx_percentile_cont(price, 0.95) AS p95_price
    FROM my_namespace.sales_data
    GROUP BY source

#### Struct and array access
    
    
    SELECT product_name,
        pricing['price'] AS price,
        array_to_string(tags, ', ') AS tag_list
    FROM my_namespace.products
    WHERE array_has(tags, 'Action')
    ORDER BY pricing['price'] DESC
    LIMIT 10

#### Chained CTEs with time-series analysis
    
    
    WITH monthly AS (
        SELECT date_trunc('month', sale_timestamp) AS month,
            department,
            COUNT(*) AS transactions,
            round(AVG(total_amount), 2) AS avg_amount
        FROM my_namespace.sales_data
        WHERE sale_timestamp BETWEEN '2025-01-01T00:00:00Z' AND '2025-12-31T23:59:59Z'
        GROUP BY date_trunc('month', sale_timestamp), department
    ),
    ranked AS (
        SELECT month, department, transactions, avg_amount,
            CASE
                WHEN avg_amount > 1000 THEN 'high-value'
                WHEN avg_amount > 500 THEN 'mid-value'
                ELSE 'standard'
            END AS tier
        FROM monthly
        WHERE transactions > 100
    )
    SELECT * FROM ranked
    ORDER BY month, avg_amount DESC

For the full function reference and syntax details, refer to the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/). For limitations and best practices, refer to [Limitations and best practices](https://developers.cloudflare.com/basin-sql/reference/limitations-best-practices/).

Feb 9, 2026

## [R2 SQL now supports approximate aggregation functions](https://developers.cloudflare.com/changelog/post/2026-02-09-approximate-aggregation-functions/)

[Basin SQL](https://developers.cloudflare.com/basin-sql/)

R2 SQL now supports five approximate aggregation functions for fast analysis of large datasets. These functions trade minor precision for improved performance on high-cardinality data.

#### New functions

  * `APPROX_PERCENTILE_CONT(column, percentile)` — Returns the approximate value at a given percentile (0.0 to 1.0). Works on integer and decimal columns.
  * `APPROX_PERCENTILE_CONT_WITH_WEIGHT(column, weight, percentile)` — Weighted percentile calculation where each row contributes proportionally to its weight column value.
  * `APPROX_MEDIAN(column)` — Returns the approximate median. Equivalent to `APPROX_PERCENTILE_CONT(column, 0.5)`.
  * `APPROX_DISTINCT(column)` — Returns the approximate number of distinct values. Works on any column type.
  * `APPROX_TOP_K(column, k)` — Returns the `k` most frequent values with their counts as a JSON array.



All functions support `WHERE` filters. All except `APPROX_TOP_K` support `GROUP BY`.

#### Examples
    
    
    -- Percentile analysis on revenue data
    SELECT approx_percentile_cont(total_amount, 0.25),
           approx_percentile_cont(total_amount, 0.5),
           approx_percentile_cont(total_amount, 0.75)
    FROM my_namespace.sales_data
    
    
    -- Median per department
    SELECT department, approx_median(total_amount)
    FROM my_namespace.sales_data
    GROUP BY department
    
    
    -- Approximate distinct customers by region
    SELECT region, approx_distinct(customer_id)
    FROM my_namespace.sales_data
    GROUP BY region
    
    
    -- Top 5 most frequent departments
    SELECT approx_top_k(department, 5)
    FROM my_namespace.sales_data
    
    
    -- Combine approximate and standard aggregations
    SELECT COUNT(*),
           AVG(total_amount),
           approx_percentile_cont(total_amount, 0.5),
           approx_distinct(customer_id)
    FROM my_namespace.sales_data
    WHERE region = 'North'

For the full syntax and additional examples, refer to the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/).

Dec 12, 2025

## [R2 SQL now supports aggregations and schema discovery](https://developers.cloudflare.com/changelog/post/2025-12-12-aggregation-support-and-more/)

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

R2 SQL now supports aggregation functions, `GROUP BY`, `HAVING`, along with schema discovery commands to make it easy to explore your data catalog.

#### Aggregation Functions

You can now perform aggregations on Apache Iceberg tables in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) using standard SQL functions including `COUNT(*)`, `SUM()`, `AVG()`, `MIN()`, and `MAX()`. Combine these with `GROUP BY` to analyze data across dimensions, and use `HAVING` to filter aggregated results.
    
    
    -- Calculate average transaction amounts by department
    SELECT department, COUNT(*), AVG(total_amount)
    FROM my_namespace.sales_data
    WHERE region = 'North'
    GROUP BY department
    HAVING COUNT(*) > 50
    ORDER BY AVG(total_amount) DESC
    
    
    -- Find high-value departments
    SELECT department, SUM(total_amount)
    FROM my_namespace.sales_data
    GROUP BY department
    HAVING SUM(total_amount) > 50000

#### Schema Discovery

New metadata commands make it easy to explore your data catalog and understand table structures:

  * `SHOW DATABASES` or `SHOW NAMESPACES` \- List all available namespaces
  * `SHOW TABLES IN namespace_name` \- List tables within a namespace
  * `DESCRIBE namespace_name.table_name` \- View table schema and column types


    
    
    ❯ npx wrangler r2 sql query "{ACCOUNT_ID}_{BUCKET_NAME}" "DESCRIBE default.sales_data;"
    
     ⛅️ wrangler 4.54.0
    ─────────────────────────────────────────────
    
    ┌──────────────────┬────────────────┬──────────┬─────────────────┬───────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────┐
    │ column_name      │ type           │ required │ initial_default │ write_default │ doc                                                                                               │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ sale_id          │ BIGINT         │ false    │                 │               │ Unique identifier for each sales transaction                                                      │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ sale_timestamp   │ TIMESTAMPTZ    │ false    │                 │               │ Exact date and time when the sale occurred (used for partitioning)                                │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ department       │ TEXT           │ false    │                 │               │ Product department (8 categories: Electronics, Beauty, Home, Toys, Sports, Food, Clothing, Books) │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ category         │ TEXT           │ false    │                 │               │ Product category grouping (4 categories: Premium, Standard, Budget, Clearance)                    │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ region           │ TEXT           │ false    │                 │               │ Geographic sales region (5 regions: North, South, East, West, Central)                            │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ product_id       │ INT            │ false    │                 │               │ Unique identifier for the product sold                                                            │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ quantity         │ INT            │ false    │                 │               │ Number of units sold in this transaction (range: 1-50)                                            │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ unit_price       │ DECIMAL(10, 2) │ false    │                 │               │ Price per unit in dollars (range: $5.00-$500.00)                                                  │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ total_amount     │ DECIMAL(10, 2) │ false    │                 │               │ Total sale amount before tax (quantity × unit_price with discounts applied)                       │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ discount_percent │ INT            │ false    │                 │               │ Discount percentage applied to this sale (0-50%)                                                  │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ tax_amount       │ DECIMAL(10, 2) │ false    │                 │               │ Tax amount collected on this sale                                                                 │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ profit_margin    │ DECIMAL(10, 2) │ false    │                 │               │ Profit margin on this sale as a decimal percentage                                                │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ customer_id      │ INT            │ false    │                 │               │ Unique identifier for the customer who made the purchase                                          │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ is_online_sale   │ BOOLEAN        │ false    │                 │               │ Boolean flag indicating if sale was made online (true) or in-store (false)                        │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ sale_date        │ DATE           │ false    │                 │               │ Calendar date of the sale (extracted from sale_timestamp)                                         │
    └──────────────────┴────────────────┴──────────┴─────────────────┴───────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────┘
    Read 0 B across 0 files from R2
    On average, 0 B / s

To learn more about the new aggregation capabilities and schema discovery commands, check out the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/). If you're new to R2 SQL, visit our [getting started guide](https://developers.cloudflare.com/basin-sql/get-started/) to begin querying your data.

Sep 25, 2025

## [Announcing R2 SQL](https://developers.cloudflare.com/changelog/post/2025-09-25-announcing-r2-sql-open-beta/)

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

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
