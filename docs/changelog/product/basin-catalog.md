---
url: https://developers.cloudflare.com/changelog/product/basin-catalog/
title: Basin Catalog Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:11.522391+00:00
---

# Basin Catalog Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/basin-catalog/

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

May 12, 2026

## [R2 Data Catalog now exposes metrics via the GraphQL Analytics API](https://developers.cloudflare.com/changelog/post/2026-05-12-r2-data-catalog-graphql-analytics/)

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) is a managed Apache Iceberg data catalog built directly into your R2 bucket that allows you to connect query engines like [R2 SQL](https://developers.cloudflare.com/basin-sql/), Spark, Snowflake, and DuckDB to your data in R2.

You can now query analytics for your R2 Data Catalog warehouses via Cloudflare's [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/). Two new datasets are available:

  * **`r2CatalogDataOperationsAdaptiveGroups`** tracks Iceberg REST API requests made to your catalog, including operation type, request duration, HTTP status, and request body bytes. Use this to monitor request volume and latency across warehouses, namespaces, and tables.
  * **`r2CatalogTableMaintenanceAdaptiveGroups`** tracks table maintenance jobs such as compaction and snapshot expiration. Use this to monitor job success rates, files processed, bytes read and written, and job duration.



Both datasets support filtering by warehouse name, namespace, table name, and time range. They also include percentile aggregations for duration metrics.

For detailed schema information and example queries, refer to the [R2 Data Catalog metrics and analytics documentation](https://developers.cloudflare.com/basin-catalog/observability/metrics/).

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

Oct 6, 2025

## [R2 Data Catalog table-level compaction](https://developers.cloudflare.com/changelog/post/2025-10-06-data-catalog-table-compaction/)

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

You can now enable compaction for individual [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/), giving you fine-grained control over different workloads.
    
    
    # Enable compaction for a specific table (no token required)
    npx wrangler r2 bucket catalog compaction enable <BUCKET> <NAMESPACE> <TABLE> --target-size 256

This allows you to:

  * Apply different target file sizes per table
  * Disable compaction for specific tables
  * Optimize based on table-specific access patterns



Learn more at [Manage catalogs](https://developers.cloudflare.com/basin-catalog/manage-catalogs/).

Sep 25, 2025

## [R2 Data Catalog now supports compaction](https://developers.cloudflare.com/changelog/post/2025-09-25-data-catalog-compaction/)

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

You can now enable automatic compaction for [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) to improve query performance.

Compaction is the process of taking a group of small files and combining them into fewer larger files. This is an important maintenance operation as it helps ensure that query performance remains consistent by reducing the number of files that needs to be scanned.

To enable automatic compaction in R2 Data Catalog, find it under **R2 Data Catalog** in your R2 bucket settings in the dashboard.

![compaction-dash](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=799,height=400,format=webp/_astro/compaction.MLojYuHL.png)

Or with [Wrangler](https://developers.cloudflare.com/workers/wrangler/), run:
    
    
    npx wrangler r2 bucket catalog compaction enable <BUCKET_NAME>  --target-size 128 --token <API_TOKEN>

To get started with compaction, check out [manage catalogs](https://developers.cloudflare.com/basin-catalog/manage-catalogs/). For best practices and limitations, refer to [about compaction](https://developers.cloudflare.com/basin-catalog/table-maintenance/).

Apr 10, 2025

## [R2 Data Catalog is a managed Apache Iceberg data catalog built directly into R2 buckets](https://developers.cloudflare.com/changelog/post/2025-04-10-r2-data-catalog-beta/)

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

Today, we are launching [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) in open beta, a managed Apache Iceberg catalog built directly into your [Cloudflare R2](https://developers.cloudflare.com/r2/) bucket.

If you are not already familiar with it, [Apache Iceberg ↗︎](https://iceberg.apache.org/) is an open table format designed to handle large-scale analytics datasets stored in object storage, offering ACID transactions and schema evolution. R2 Data Catalog exposes a standard Iceberg REST catalog interface, so you can connect engines like [Spark](https://developers.cloudflare.com/basin-catalog/config-examples/spark-scala/), [Snowflake](https://developers.cloudflare.com/basin-catalog/config-examples/snowflake/), and [PyIceberg](https://developers.cloudflare.com/basin-catalog/config-examples/pyiceberg/) to start querying your tables using the tools you already know.

To enable a data catalog on your R2 bucket, find **R2 Data Catalog** in your buckets settings in the dashboard, or run:
    
    
    npx wrangler r2 bucket catalog enable my-bucket

And that's it. You'll get a catalog URI and warehouse you can plug into your favorite Iceberg engines.

Visit our [getting started guide](https://developers.cloudflare.com/basin-catalog/get-started/) for step-by-step instructions on enabling R2 Data Catalog, creating tables, and running your first queries.
