---
url: https://developers.cloudflare.com/changelog/product/basin/
title: Basin Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:41.651513+00:00
---

# Basin Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/basin/

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

## [Basin Pipelines ingest limit increased to 1 GB/s](https://developers.cloudflare.com/changelog/post/2026-10-01-stream-ingest-limit-increase/)

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin](https://developers.cloudflare.com/basin/)

Each [Basin Pipelines stream](https://developers.cloudflare.com/basin-pipelines/streams/) can now ingest up to 1 GB/s, increased from 5 MB/s.

The higher per-stream limit gives high-volume application events, telemetry, and logs more room to grow without splitting ingestion across streams solely to stay within the previous limit.

For the full list of stream, sink, and pipeline limits, refer to [Basin Pipelines limits](https://developers.cloudflare.com/basin-pipelines/platform/limits/).

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

Sep 16, 2026

## [R2 Data Catalog adds table maintenance visibility and manual queueing](https://developers.cloudflare.com/changelog/post/2026-09-16-table-maintenance-dashboard/)

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) now provides table-level maintenance visibility and manual compaction queueing in the Cloudflare dashboard. These updates make it easier to understand when maintenance is eligible to run, inspect completed operations, and request maintenance without leaving the table view.

To view table maintenance details:

  1. In the Cloudflare dashboard, go to **R2 Data Catalog**.
  2. Select a catalog, then select the **Explorer** tab. The **Explorer** tab opens by default.
  3. Select a table.
  4. Select the **Maintenance** tab.



![Maintenance tab for an R2 Data Catalog table showing schedules and recent runs](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1850,height=1544,format=webp/_astro/table-maintenance-view.C7KRSK-K.png)

The updated dashboard includes:

  * **Maintenance tab** — View compaction and snapshot expiration settings, schedules, and next eligibility alongside the table's **Schema** and **Metadata** tabs.
  * **Recent runs** — Review a paginated audit log with job status, duration, and expandable details for manifest rewrites, compaction, and snapshot expiration. Expanded rows include operation metrics for each maintenance operation.
  * **Manual queueing** — Select **Queue maintenance** to request compaction during normal scheduler polling. The dashboard checks permissions and explains when another maintenance job conflicts with the request or the daily accepted-request limit has been reached.
  * **Updated catalog layout** — Find catalog metrics in the **Metrics** tab, use the renamed **Explorer** tab to browse data, and switch between table details using tabs instead of a scroll-to-section sidebar.
  * **Improved schema browser** — For accounts with the schema browser enabled, select a namespace to open its tables in the right pane while also expanding the namespace tree. The tree can now be collapsed to provide more space for table details.



For more information about compaction and snapshot expiration, refer to [Table maintenance](https://developers.cloudflare.com/basin-catalog/table-maintenance/).

Aug 3, 2026

## [Billing is now enabled for R2 Data Catalog](https://developers.cloudflare.com/changelog/post/2026-08-03-r2-data-catalog-billing-enabled/)

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

Billing is now enabled for [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) on non-enterprise accounts. R2 Data Catalog usage beyond the included free tier will appear on your next invoice.

R2 Data Catalog charges based on two dimensions, in addition to standard [R2 storage and operations](https://developers.cloudflare.com/r2/pricing/):

  * **Catalog operations** : $9.00 / million operations for metadata requests such as creating tables, reading table metadata, and updating table properties.
  * **Compaction** : $0.005 / GB processed and $2.00 / million objects processed. These charges only apply when [automatic compaction](https://developers.cloudflare.com/basin-catalog/table-maintenance/) is turned on for a table.



Each dimension includes a monthly free tier: 1 million catalog operations, 10 GB of compaction data processed, and 1 million compaction objects processed.

For example, a single Iceberg table with 50 GB of data, 500,000 catalog operations per month, and compaction turned on that processes 20 GB across 200,000 files would be billed as follows:

Dimension | Usage | Included | Billable | Cost  
---|---|---|---|---  
Catalog operations | 500,000 | 1,000,000 | 0 | $0.00  
Compaction (data processed) | 20 GB | 10 GB | 10 GB | $0.05  
Compaction (objects) | 200,000 | 1,000,000 | 0 | $0.00  
**Total (Data Catalog)** |  |  |  | **$0.05**  
  
Standard R2 storage charges ($0.015 / GB-month) apply separately for the 50 GB of data stored.

For full pricing details and billing examples, refer to [R2 Data Catalog pricing](https://developers.cloudflare.com/basin-catalog/platform/pricing/).

Aug 3, 2026

## [Billing is now enabled for Pipelines](https://developers.cloudflare.com/changelog/post/2026-08-03-pipelines-billing-enabled/)

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin](https://developers.cloudflare.com/basin/)

Billing is now enabled for [Cloudflare Pipelines](https://developers.cloudflare.com/basin-pipelines/) on non-enterprise accounts. Pipelines usage beyond the included free tier will appear on your next invoice.

Pipelines charges based on two usage dimensions. Ingress into a Pipeline stream remains free regardless of volume:

  * **SQL transforms** : $0.04 / GB for stateless transforms (filter, reshape, unnest, cast, compute).
  * **Sinks (egress)** : $0.03 / GB for JSON output, $0.06 / GB for Parquet or Iceberg output.



Workers Paid plans include 50 GB / month for both SQL transforms and sinks. Standard [R2 storage and operations](https://developers.cloudflare.com/r2/pricing/) charges apply for data written to R2 buckets, and [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/platform/pricing/) charges apply when writing to Iceberg tables.

For example, a pipeline that ingests 500 GB of event data per month, uses a SQL transform to filter and reshape it, and writes 300 GB to an R2 Data Catalog Iceberg table would be billed as follows:

Dimension | Usage | Included | Billable | Cost  
---|---|---|---|---  
Streams | 500 GB | Unlimited | 0 GB | $0.00  
SQL transforms | 500 GB | 50 GB | 450 GB | $18.00  
Sinks (Iceberg) | 300 GB | 50 GB | 250 GB | $15.00  
**Total** |  |  |  | **$33.00**  
  
For full pricing details and billing examples, refer to [Pipelines pricing](https://developers.cloudflare.com/basin-pipelines/platform/pricing/).

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

Jul 13, 2026

## [R2 Data Catalog now supports read-only API tokens](https://developers.cloudflare.com/changelog/post/2026-07-09-r2-data-catalog-read-only-tokens/)

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) now accepts read-only API tokens, so query engines and clients that only read data no longer need a read-write token. Previously, every catalog operation required an **Admin Read & Write** token, which granted read-only clients more access than they needed.

You can now authenticate your Iceberg engine based on your workload:

  * **Read-only** operations (such as listing namespaces, loading tables, and querying data) work with an **Admin Read only** token (R2 Data Catalog read and R2 storage read).
  * **Write** operations (such as creating or dropping tables and committing transactions) continue to require an **Admin Read & Write** token.



This lets you follow the principle of least privilege — for example, using a read-write token for the pipeline that writes to your tables and read-only tokens for engines like [R2 SQL](https://developers.cloudflare.com/basin-sql/), [DuckDB](https://developers.cloudflare.com/basin-catalog/config-examples/duckdb/), or [PyIceberg](https://developers.cloudflare.com/basin-catalog/config-examples/pyiceberg/) that query them.

Note that credentials vended by the catalog inherit the R2 storage permissions of the token used to authenticate. To ensure read-only access to your underlying data, scope the R2 storage permission to read-only as well.

For details on choosing and creating the right token, refer to [Authenticate your Iceberg engine](https://developers.cloudflare.com/basin-catalog/manage-catalogs/#authenticate-your-iceberg-engine).

Jul 13, 2026

## [R2 Data Catalog compaction now optimizes manifest files](https://developers.cloudflare.com/changelog/post/2026-07-13-r2-data-catalog-manifest-optimization/)

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/), a managed [Apache Iceberg ↗︎](https://iceberg.apache.org/) catalog built into R2, now automatically optimizes manifest files as part of [compaction](https://developers.cloudflare.com/basin-catalog/table-maintenance/).

Manifest files track the data files that make up an Iceberg table. As a table accumulates many small or fragmented manifests, query engines must read more metadata during query planning, which slows down queries even before any data is scanned.

When compaction runs, R2 Data Catalog now rewrites and clusters manifest files by partition as a best-effort pre-step. This consolidates fragmented manifests, reduces the number of manifests a query engine must open, and lowers metadata I/O overhead. Tables that are already well-clustered are skipped, so the operation only runs when it provides a benefit.

This happens automatically for tables with compaction enabled — no configuration changes are required.

For more information, refer to [Table maintenance](https://developers.cloudflare.com/basin-catalog/table-maintenance/).

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

Jul 7, 2026

## [R2 Data Catalog warns before you delete data manually](https://developers.cloudflare.com/changelog/post/2026-07-06-r2-data-catalog-delete-warnings/)

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

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

Jun 4, 2026

## [Pipeline binding configuration field renamed to stream](https://developers.cloudflare.com/changelog/post/2026-05-27-pipeline-binding-stream-field/)

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin](https://developers.cloudflare.com/basin/)[Workers](https://developers.cloudflare.com/workers/)

The `pipeline` field inside the `pipelines` binding configuration in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) has been renamed to `stream`. The old field is deprecated but still accepted.

Update your configuration to use `stream` to avoid the deprecation warning.

**Before (deprecated):**
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "pipelines": [
        {
          "binding": "MY_PIPELINE",
          "pipeline": "<STREAM_ID>"
        }
      ]
    }
    
    
    [[pipelines]]
    binding = "MY_PIPELINE"
    pipeline = "<STREAM_ID>"

**After:**
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "pipelines": [
        {
          "binding": "MY_PIPELINE",
          "stream": "<STREAM_ID>"
        }
      ]
    }
    
    
    [[pipelines]]
    binding = "MY_PIPELINE"
    stream = "<STREAM_ID>"

No other changes are required. The binding name, TypeScript types, and runtime API (`env.MY_PIPELINE.send(...)`) remain the same.

For more information on configuring pipeline bindings, refer to [Writing to streams](https://developers.cloudflare.com/basin-pipelines/streams/writing-to-streams/#configure-pipeline-binding).

May 28, 2026

## [R2 Data Catalog pricing announced](https://developers.cloudflare.com/changelog/post/2026-05-11-r2-data-catalog-pricing-announced/)

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) is a managed [Apache Iceberg ↗︎](https://iceberg.apache.org/) data catalog built directly into R2 buckets, queryable by any Iceberg-compatible engine such as Spark, Snowflake, and DuckDB. R2 Data Catalog now has published pricing for catalog operations and table compaction, in addition to standard [R2 storage and operations](https://developers.cloudflare.com/r2/pricing/).

Billing is not yet enabled. We will provide at least 30 days notice before we start charging for R2 Data Catalog usage.

Pricing is based on two dimensions:

  * **Catalog operations** : $9.00 / million operations for metadata requests such as creating tables, reading table metadata, and updating table properties.
  * **Compaction** : $0.005 / GB processed and $2.00 / million objects processed. These charges only apply when automatic compaction is turned on for a table.



Both dimensions include a monthly free tier: 1 million catalog operations, 10 GB of compaction data processed, and 1 million compaction objects processed.

For full pricing details and billing examples, refer to [R2 Data Catalog pricing](https://developers.cloudflare.com/basin-catalog/platform/pricing/).

May 28, 2026

## [R2 Data Catalog gets a dedicated dashboard experience](https://developers.cloudflare.com/changelog/post/2026-05-28-r2-data-catalog-dashboard/)

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) is a managed [Apache Iceberg ↗︎](https://iceberg.apache.org/) data catalog built directly into your R2 bucket. It exposes a standard Iceberg REST catalog interface so you can connect query engines like [Spark](https://developers.cloudflare.com/basin-catalog/config-examples/spark-scala/), [Snowflake](https://developers.cloudflare.com/basin-catalog/config-examples/snowflake/), [DuckDB](https://developers.cloudflare.com/basin-catalog/config-examples/duckdb/), and [R2 SQL](https://developers.cloudflare.com/basin-sql/) to your data in R2.

R2 Data Catalog now has a dedicated section in the Cloudflare dashboard, replacing the previous settings panel embedded in R2 bucket configuration. The new experience includes:

![R2 Data Catalog dashboard overview](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3070,height=1486,format=webp/_astro/data-catalog-dashboard.BsKDvUQn.png)

  * **Catalog overview** — View all your catalogs in one place with catalog request counts, bucket sizes, and table maintenance status at a glance.
  * **Guided setup wizard** — Create a catalog in three steps: choose or create an R2 bucket, configure table maintenance (compaction and snapshot expiration), and review. The wizard creates the bucket and generates a service credential automatically.
  * **Settings management** — A dedicated settings page for each catalog with sections for general configuration, table maintenance, service credentials, and disabling the catalog. You can now enable and configure [snapshot expiration](https://developers.cloudflare.com/basin-catalog/table-maintenance/) directly from the dashboard.
  * **Built-in metrics** — Five charts on each catalog's metrics tab: bytes compacted, files compacted, catalog requests, storage size, and snapshots expired.



To get started, go to **R2 Data Catalog** in the Cloudflare dashboard or refer to the [getting started guide](https://developers.cloudflare.com/basin-catalog/get-started/) and [manage catalogs documentation](https://developers.cloudflare.com/basin-catalog/manage-catalogs/).

May 28, 2026

## [Pipelines pricing announced](https://developers.cloudflare.com/changelog/post/2026-05-11-pipelines-pricing-announced/)

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin](https://developers.cloudflare.com/basin/)

[Cloudflare Pipelines](https://developers.cloudflare.com/basin-pipelines/) is a streaming data platform that ingests events, transforms them with SQL, and writes to [R2](https://developers.cloudflare.com/r2/) as JSON, Parquet, or [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables. Pipelines now has published pricing based on two usage dimensions: the volume of data processed by SQL transforms and the volume of data delivered to sinks. Ingress into a Pipeline stream is free.

**Billing is not yet enabled. We will provide at least 30 days notice before we start charging for Pipelines usage.**

Pipelines pricing model is designed to charge per GB based on what you use:

  * **Streams (ingress)** : Free, regardless of volume.
  * **SQL transforms** : $0.04 / GB for stateless transforms (filter, reshape, unnest, cast, compute).
  * **Sinks** : $0.03 / GB for JSON, $0.06 / GB for Parquet or Iceberg output.



Workers Free plans include 1 GB / month for each dimension. Workers Paid plans include 50 GB / month.

For full pricing details and billing examples, refer to [Pipelines pricing](https://developers.cloudflare.com/basin-pipelines/platform/pricing/).

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

May 12, 2026

## [R2 Data Catalog now exposes metrics via the GraphQL Analytics API](https://developers.cloudflare.com/changelog/post/2026-05-12-r2-data-catalog-graphql-analytics/)

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) is a managed Apache Iceberg data catalog built directly into your R2 bucket that allows you to connect query engines like [R2 SQL](https://developers.cloudflare.com/basin-sql/), Spark, Snowflake, and DuckDB to your data in R2.

You can now query analytics for your R2 Data Catalog warehouses via Cloudflare's [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/). Two new datasets are available:

  * **`r2CatalogDataOperationsAdaptiveGroups`** tracks Iceberg REST API requests made to your catalog, including operation type, request duration, HTTP status, and request body bytes. Use this to monitor request volume and latency across warehouses, namespaces, and tables.
  * **`r2CatalogTableMaintenanceAdaptiveGroups`** tracks table maintenance jobs such as compaction and snapshot expiration. Use this to monitor job success rates, files processed, bytes read and written, and job duration.



Both datasets support filtering by warehouse name, namespace, table name, and time range. They also include percentile aggregations for duration metrics.

For detailed schema information and example queries, refer to the [R2 Data Catalog metrics and analytics documentation](https://developers.cloudflare.com/basin-catalog/observability/metrics/).

May 4, 2026

## [Pipelines and R2 Data Catalog now supported in Terraform](https://developers.cloudflare.com/changelog/post/2026-04-27-terraform-support/)

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin](https://developers.cloudflare.com/basin/)

[Cloudflare Pipelines](https://developers.cloudflare.com/basin-pipelines/) ingests streaming data via [Workers](https://developers.cloudflare.com/workers/) or HTTP endpoints, transforms it with SQL, and writes it to [R2](https://developers.cloudflare.com/r2/) as Apache Iceberg tables. [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) manages those Iceberg tables, compaction, and compatibility with query engines like [R2 SQL](https://developers.cloudflare.com/basin-sql/), [Spark](https://developers.cloudflare.com/basin-catalog/config-examples/spark-scala/), and [DuckDB](https://developers.cloudflare.com/basin-catalog/config-examples/duckdb/).

You can now create and manage both products using Terraform, supported in the [Cloudflare Terraform provider v5.19.0 ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs).

This adds four new resources that let you define your entire data pipeline as infrastructure-as-code: a data catalog, a stream for ingestion, a sink that writes to R2 Data Catalog or R2, and a pipeline that connects them with SQL.

The new Terraform resources are:

  * [`cloudflare_r2_data_catalog` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/r2_data_catalog) — enable the data catalog on an R2 bucket
  * [`cloudflare_pipeline_stream` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline_stream) — create a stream that receives events via HTTP or Worker bindings
  * [`cloudflare_pipeline_sink` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline_sink) — create a sink that writes to R2 Data Catalog or R2
  * [`cloudflare_pipeline` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline) — create a pipeline with SQL connecting a stream to a sink



Here is a minimal example that creates a stream, an R2 Data Catalog sink, and a pipeline:
    
    
    resource "cloudflare_pipeline_stream" "my_stream" {
      account_id = var.cloudflare_account_id
      name       = "my_stream"
      format     = { type = "json" }
      schema = {
        fields = [{
          name     = "value"
          type     = "json"
          required = true
        }]
      }
      http           = { enabled = true, authentication = false, cors = {} }
      worker_binding = { enabled = false }
    }
    
    resource "cloudflare_pipeline_sink" "my_sink" {
      account_id = var.cloudflare_account_id
      name       = "my_sink"
      type       = "r2_data_catalog"
      format     = { type = "parquet" }
      schema     = { fields = [] }
      config = {
        account_id = var.cloudflare_account_id
        bucket     = "my-pipeline-bucket"
        table_name = "my_table"
        token      = var.catalog_token
      }
    }
    
    resource "cloudflare_pipeline" "my_pipeline" {
      account_id = var.cloudflare_account_id
      name       = "my_pipeline"
      sql        = "INSERT INTO ${cloudflare_pipeline_sink.my_sink.name} SELECT * FROM ${cloudflare_pipeline_stream.my_stream.name}"
    }

For a full end-to-end example that includes R2 bucket creation, data catalog setup, and scoped API token provisioning, refer to the [Pipelines Terraform documentation](https://developers.cloudflare.com/basin-pipelines/reference/terraform/).

Apr 22, 2026

## [R2 Data Catalog snapshot expiration now removes unreferenced data files](https://developers.cloudflare.com/changelog/post/2026-04-22-snapshot-expiration-cleans-data-files/)

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/), a managed [Apache Iceberg ↗︎](https://iceberg.apache.org/) catalog built into R2, now removes unreferenced data files during automatic snapshot expiration. This improvement reduces storage costs and eliminates the need to run manual maintenance jobs to reclaim space from deleted data.

Previously, snapshot expiration only cleaned up Iceberg metadata files such as manifests and manifest lists. Data files that were no longer referenced by active snapshots remained in R2 storage until you manually ran `remove_orphan_files` or `expire_snapshots` through an engine like Spark. This required extra operational overhead and left stale data files consuming storage.

Snapshot expiration now handles both metadata and data file cleanup automatically. When a snapshot is expired, any data files that are no longer referenced by retained snapshots are removed from R2 storage.
    
    
    # Enable catalog-level snapshot expiration
    npx wrangler r2 bucket catalog snapshot-expiration enable my-bucket \
      --older-than-days 7 \
      --retain-last 10

For more information, refer to the [table maintenance documentation](https://developers.cloudflare.com/basin-catalog/table-maintenance/).

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

Feb 24, 2026

## [Dropped event metrics, typed Pipelines bindings, and improved setup](https://developers.cloudflare.com/changelog/post/2026-02-24-typed-bindings-setup-improvements-error-metrics/)

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin](https://developers.cloudflare.com/basin/)[Workers](https://developers.cloudflare.com/workers/)

[Cloudflare Pipelines](https://developers.cloudflare.com/basin-pipelines/) ingests streaming data via [Workers](https://developers.cloudflare.com/workers/) or HTTP endpoints, transforms it with SQL, and writes it to [R2](https://developers.cloudflare.com/r2/) as Apache Iceberg tables. Today we are shipping three improvements to help you understand why streaming events get dropped, catch data quality issues early, and set up Pipelines faster.

#### Dropped event metrics

When [stream](https://developers.cloudflare.com/basin-pipelines/streams/) events don't match the expected schema, Pipelines accepts them during ingestion but drops them when attempting to deliver them to the [sink](https://developers.cloudflare.com/basin-pipelines/sinks/). To help you identify the root cause of these issues, we are introducing a new dashboard and metrics that surface dropped events with detailed error messages.

![The Errors tab in the Cloudflare dashboard showing deserialization errors grouped by type with individual error details](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3066,height=1466,format=webp/_astro/pipelines-error-log-dash.6JIa7r5d.png)

Dropped events can also be queried programmatically via the new `pipelinesUserErrorsAdaptiveGroups` GraphQL dataset. The dataset breaks down failures by specific error type (`missing_field`, `type_mismatch`, `parse_failure`, or `null_value`) so you can trace issues back to the source.
    
    
    query GetPipelineUserErrors(
    	$accountTag: String!
    	$pipelineId: String!
    	$datetimeStart: Time!
    	$datetimeEnd: Time!
    ) {
    	viewer {
    		accounts(filter: { accountTag: $accountTag }) {
    			pipelinesUserErrorsAdaptiveGroups(
    				limit: 100
    				filter: {
    					pipelineId: $pipelineId
    					datetime_geq: $datetimeStart
    					datetime_leq: $datetimeEnd
    				}
    				orderBy: [count_DESC]
    			) {
    				count
    				dimensions {
    					errorFamily
    					errorType
    				}
    			}
    		}
    	}
    }

For the full list of dimensions, error types, and additional query examples, refer to [User error metrics](https://developers.cloudflare.com/basin-pipelines/observability/metrics/#user-error-metrics).

#### Typed Pipelines bindings

Sending data to a Pipeline from a Worker previously used a generic `Pipeline<PipelineRecord>` type, which meant schema mismatches (wrong field names, incorrect types) were only caught at runtime as dropped events.

Running `wrangler types` now generates schema-specific TypeScript types for your [Pipeline bindings](https://developers.cloudflare.com/basin-pipelines/streams/writing-to-streams/#send-via-workers). TypeScript catches missing required fields and incorrect field types at compile time, before your code is deployed.
    
    
    declare namespace Cloudflare {
    	type EcommerceStreamRecord = {
    		user_id: string;
    		event_type: string;
    		product_id?: string;
    		amount?: number;
    	};
    	interface Env {
    		STREAM: import("cloudflare:pipelines").Pipeline<Cloudflare.EcommerceStreamRecord>;
    	}
    }

For more information, refer to [Typed Pipeline bindings](https://developers.cloudflare.com/basin-pipelines/streams/writing-to-streams/#typed-pipeline-bindings).

#### Improved Pipelines setup

Setting up a new Pipeline previously required multiple manual steps: creating an R2 bucket, enabling R2 Data Catalog, generating an API token, and configuring format, compression, and rolling policies individually.

The `wrangler pipelines setup` command now offers a **Simple** setup mode that applies recommended defaults and automatically creates the [R2 bucket](https://developers.cloudflare.com/r2/buckets/) and enables [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) if they do not already exist. Validation errors during setup prompt you to retry inline rather than restarting the entire process.

For a full walkthrough, refer to the [Getting started guide](https://developers.cloudflare.com/basin-pipelines/getting-started/).

Dec 18, 2025

## [R2 Data Catalog now supports automatic snapshot expiration](https://developers.cloudflare.com/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/)

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

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

← Prev

1[2](https://developers.cloudflare.com/changelog/product/basin/2/)

[Next →](https://developers.cloudflare.com/changelog/product/basin/2/)
