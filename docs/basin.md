---
url: https://developers.cloudflare.com/basin/
title: Overview \u00b7 Cloudflare Basin docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:28.954523+00:00
---

# Overview · Cloudflare Basin docs

> Source: https://developers.cloudflare.com/basin/

  1. [Home](https://developers.cloudflare.com/)
  2. /Basin



# Basin

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIngest with Basin PipelinesManage your data with Basin CatalogQuery your data with Basin SQLWhat's new

Collect, transform, manage, and query analytics data with a serverless platform built on [Apache Iceberg ↗︎](https://iceberg.apache.org/) and [R2](https://developers.cloudflare.com/r2/).

Note

Basin was formerly known as Cloudflare Data Platform. Cloudflare Pipelines, R2 Data Catalog, and R2 SQL are now named Basin Pipelines, Basin Catalog, and Basin SQL. Existing resources and configurations continue to work.

Basin is an end-to-end analytics data platform that brings ingestion, table management, and distributed SQL together to Cloudflare's Developer Platform. It receives data from applications, infrastructure, devices, and Cloudflare services, transforms events during ingestion, stores them in open Iceberg tables, and makes it queryable with Basin SQL or [compatible external engines](https://developers.cloudflare.com/basin-catalog/config-examples/).
    
    
    ---
    title: Basin data flow
    ---
    flowchart LR
    	pipelines["Basin Pipelines"]
    	catalog["Basin Catalog<br/>Apache Iceberg tables"]
    	sql["Basin SQL &<br/>compatible external engines"]
    	pipelines -->|processes and ingests events| catalog
    	catalog -->|queried by| sql
    

With Basin, you can expect to:

  * Ingest and transform events without managing streaming infrastructure
  * Keep data portable through the open Apache Iceberg standard
  * Maintain tables automatically with compaction and snapshot expiration
  * Run globally distributed OLAP queries without managing query clusters
  * Access tables stored in R2 without [egress fees](https://developers.cloudflare.com/r2/pricing/#egress)



To build your first request analytics workflow, follow the [Basin CLI guide](https://developers.cloudflare.com/basin/get-started/guide/).

* * *

## Ingest with Basin Pipelines

Use [Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/) to receive events through HTTP endpoints or [Workers bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/). It transforms events with SQL and writes Iceberg tables or files to R2.

Run the setup command to configure a stream, sink, and pipeline:

npmyarnpnpm
    
    
    npx wrangler basin pipelines setup
    
    
    yarn wrangler basin pipelines setup
    
    
    pnpm wrangler basin pipelines setup

[Basin Pipelines documentation](https://developers.cloudflare.com/basin-pipelines/)

Configure streaming ingestion, SQL transformations, and R2 destinations.

Explore Basin Pipelines

* * *

## Manage your data with Basin Catalog

Use [Basin Catalog](https://developers.cloudflare.com/basin-catalog/) to manage Iceberg metadata in your R2 bucket. It provides an Iceberg REST catalog and automatic table maintenance.

Enable Basin Catalog on an existing R2 bucket:

npmyarnpnpm
    
    
    npx wrangler basin catalog enable YOUR_BUCKET_NAME
    
    
    yarn wrangler basin catalog enable YOUR_BUCKET_NAME
    
    
    pnpm wrangler basin catalog enable YOUR_BUCKET_NAME

[Basin Catalog documentation](https://developers.cloudflare.com/basin-catalog/)

Manage catalogs, maintain tables, and connect compatible Iceberg engines.

Explore Basin Catalog

* * *

## Query your data with Basin SQL

Use [Basin SQL](https://developers.cloudflare.com/basin-sql/) to run distributed online analytical processing (OLAP) queries across catalog tables. It uses Cloudflare's global network without requiring query clusters.

Query a table in your warehouse with SQL:

npmyarnpnpm
    
    
    npx wrangler basin sql query YOUR_WAREHOUSE_NAME "SELECT * FROM default.events LIMIT 10"
    
    
    yarn wrangler basin sql query YOUR_WAREHOUSE_NAME "SELECT * FROM default.events LIMIT 10"
    
    
    pnpm wrangler basin sql query YOUR_WAREHOUSE_NAME "SELECT * FROM default.events LIMIT 10"

[Basin SQL documentation](https://developers.cloudflare.com/basin-sql/)

Run SQL queries, review supported syntax, and monitor query usage.

Explore Basin SQL

* * *

##  What's new 

The latest features and improvements across Basin.

[View Changelog](https://developers.cloudflare.com/changelog/product/basin/)

[Oct 01, 2026Basin PipelinesBasin Pipelines ingest limit increased to 1 GB/sBasin Pipelines streams can ingest up to 1 GB/s each, increased from the previous 5 MB/s limit.Read update](https://developers.cloudflare.com/changelog/post/2026-10-01-stream-ingest-limit-increase/)[Oct 01Basin PipelinesCloudflare Basin is now generally availableCloudflare Data Platform is now Basin, bringing generally available ingestion, Iceberg table management, and SQL analytics together on R2.Read more](https://developers.cloudflare.com/changelog/post/2026-10-01-basin-ga/)[Sep 16Basin CatalogR2 Data Catalog adds table maintenance visibility and manual queueingView table maintenance schedules and run history, queue compaction from the dashboard, and browse catalogs with an updated layout.Read more](https://developers.cloudflare.com/changelog/post/2026-09-16-table-maintenance-dashboard/)[Aug 03Basin CatalogBilling is now enabled for R2 Data CatalogR2 Data Catalog usage is now billed on non-enterprise accounts. R2 Data Catalog usage beyond the included free tier will appear on your next invoice.Read more](https://developers.cloudflare.com/changelog/post/2026-08-03-r2-data-catalog-billing-enabled/)[Aug 03Basin PipelinesBilling is now enabled for PipelinesCloudflare Pipelines usage is now billed on non-enterprise accounts. Pipelines usage beyond the included free tier will appear on your next invoice.Read more](https://developers.cloudflare.com/changelog/post/2026-08-03-pipelines-billing-enabled/)[Aug 03Basin SQLBilling is now enabled for R2 SQLR2 SQL usage is now billed on non-enterprise accounts. R2 SQL usage beyond the included free tier will appear on your next invoice.Read more](https://developers.cloudflare.com/changelog/post/2026-08-03-r2-sql-billing-enabled/)[Jul 13Basin CatalogR2 Data Catalog now supports read-only API tokensConnect query engines to R2 Data Catalog using read-only API tokensRead more](https://developers.cloudflare.com/changelog/post/2026-07-09-r2-data-catalog-read-only-tokens/)[Jul 13Basin CatalogR2 Data Catalog compaction now optimizes manifest filesCompaction automatically rewrites and clusters Apache Iceberg manifest files to reduce metadata overhead and speed up query planningRead more](https://developers.cloudflare.com/changelog/post/2026-07-13-r2-data-catalog-manifest-optimization/)

[NextCLI](https://developers.cloudflare.com/basin/get-started/guide/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
