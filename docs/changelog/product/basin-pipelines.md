---
url: https://developers.cloudflare.com/changelog/product/basin-pipelines/
title: Basin Pipelines Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:11.450931+00:00
---

# Basin Pipelines Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/basin-pipelines/

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

Apr 20, 2026

## [Cloudflare Pipelines as a Logpush destination](https://developers.cloudflare.com/changelog/post/2026-04-20-pipelines-logpush-destination/)

[Logs](https://developers.cloudflare.com/logs/)[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)

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

Sep 25, 2025

## [Pipelines now supports SQL transformations and Apache Iceberg](https://developers.cloudflare.com/changelog/post/2025-09-25-pipelines-sql/)

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin](https://developers.cloudflare.com/basin/)

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

Apr 10, 2025

## [Cloudflare Pipelines now available in beta](https://developers.cloudflare.com/changelog/post/2025-04-10-launching-pipelines/)

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)[Workers](https://developers.cloudflare.com/workers/)

[Cloudflare Pipelines](https://developers.cloudflare.com/basin-pipelines/) is now available in beta, to all users with a [Workers Paid](https://developers.cloudflare.com/workers/platform/pricing/) plan.

Pipelines let you ingest high volumes of real time data, without managing the underlying infrastructure. A single pipeline can ingest up to 100 MB of data per second, via HTTP or from a [Worker](https://developers.cloudflare.com/workers). Ingested data is automatically batched, written to output files, and delivered to an [R2 bucket](https://developers.cloudflare.com/r2) in your account. You can use Pipelines to build a data lake of clickstream data, or to store events from a Worker.

Create your first pipeline with a single command:

Create a pipelinebash
    
    
    $ npx wrangler@latest pipelines create my-clickstream-pipeline --r2-bucket my-bucket
    
    🌀 Authorizing R2 bucket "my-bucket"
    🌀 Creating pipeline named "my-clickstream-pipeline"
    ✅ Successfully created pipeline my-clickstream-pipeline
    
    Id:    0e00c5ff09b34d018152af98d06f5a1xvc
    Name:  my-clickstream-pipeline
    Sources:
      HTTP:
        Endpoint:        https://0e00c5ff09b34d018152af98d06f5a1xvc.pipelines.cloudflare.com/
        Authentication:  off
        Format:          JSON
      Worker:
        Format:  JSON
    Destination:
      Type:         R2
      Bucket:       my-bucket
      Format:       newline-delimited JSON
      Compression:  GZIP
    Batch hints:
      Max bytes:     100 MB
      Max duration:  300 seconds
      Max records:   100,000
    
    🎉 You can now send data to your pipeline!
    
    Send data to your pipeline's HTTP endpoint:
    curl "https://0e00c5ff09b34d018152af98d06f5a1xvc.pipelines.cloudflare.com/" -d '[{ ...JSON_DATA... }]'
    
    To send data to your pipeline from a Worker, add the following configuration to your config file:
    {
      "pipelines": [
        {
          "pipeline": "my-clickstream-pipeline",
          "binding": "PIPELINE"
        }
      ]
    }

Head over to our [getting started guide](https://developers.cloudflare.com/basin-pipelines/getting-started/) for an in-depth tutorial to building with Pipelines.
