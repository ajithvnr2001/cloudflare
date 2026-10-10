---
url: https://developers.cloudflare.com/changelog/product-group/storage/
title: Storage Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:14.650711+00:00
---

# Storage Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product-group/storage/

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

Oct 9, 2026

## [R2 bandwidth by Cloudflare location](https://developers.cloudflare.com/changelog/post/2026-10-09-r2-bandwidth-by-location/)

[R2](https://developers.cloudflare.com/r2/)

You can now view R2 bandwidth by the Cloudflare location that served each request in the Cloudflare UI. This helps you see which locations consume the most bandwidth with options to select a specific bucket and download (read) vs upload (write) bandwidth.

[ Go to **R2 overview** ↗ ](https://dash.cloudflare.com/?to=/:account/r2/metrics) ![R2 bandwidth by location chart showing throughput for the top five Cloudflare locations](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=665,height=427,format=webp/_astro/r2-bandwidth-by-location.JMiyoI-0.png)

By default, the chart shows the top five locations by total bandwidth consumed during the selected time range. Use the **Top 5 locations** dropdown to select other locations, up to six at a time.

For more information, refer to [R2 metrics and analytics](https://developers.cloudflare.com/r2/platform/metrics-analytics/).

Oct 2, 2026

## [United States jurisdiction](https://developers.cloudflare.com/changelog/post/2026-10-02-us-jurisdiction/)

[D1](https://developers.cloudflare.com/d1/)

You can create D1 databases with the `us` jurisdiction. These databases run and persist data within the United States.

Use this option for regional data residency requirements.

To create a database with the `us` jurisdiction, run:
    
    
    npx wrangler@latest d1 create db-with-us-jurisdiction --jurisdiction=us

For more information, refer to [D1 data location](https://developers.cloudflare.com/d1/configuration/data-location/).

Oct 2, 2026

## [Workers KV namespace jurisdictions are now generally available](https://developers.cloudflare.com/changelog/post/2026-10-02-kv-jurisdictions-ga/)

[KV](https://developers.cloudflare.com/kv/)

Jurisdictions for [Workers KV](https://developers.cloudflare.com/kv/) namespaces are now generally available. When you create a namespace, you can set a [jurisdiction](https://developers.cloudflare.com/kv/reference/data-location/) to make sure the namespace's data is only durably stored within that region. Jurisdictions can help you comply with data localization regulations such as GDPR or FedRAMP. Supported jurisdictions are `eu`, `us`, and `fedramp`.

A jurisdiction can only be set when a namespace is created, using the Cloudflare dashboard, Wrangler, the `cf` CLI, or the REST API, and cannot be added or changed afterwards.
    
    
    npx wrangler@latest kv namespace create <NAMESPACE_NAME> --jurisdiction=eu
    
    
    cf kv namespaces create --title <NAMESPACE_NAME> --jurisdiction eu
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/storage/kv/namespaces" \
      --request POST \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "title": "<NAMESPACE_NAME>",
        "jurisdiction": "eu"
      }'

Workers can still access a namespace restricted to a jurisdiction from anywhere in the world, and KV data can be cached outside the jurisdiction on Cloudflare's network. The jurisdiction only controls where the namespace's data is durably stored.

To learn more, refer to [Data location](https://developers.cloudflare.com/kv/reference/data-location/).

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

Oct 1, 2026

## [Pending I/O operations allow Durable Objects to continue long-running work without a connected client](https://developers.cloudflare.com/changelog/post/2026-10-01-pending-io-keep-alive/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Durable Objects remain active while handling a request from a connected client. This change applies when no client is connected, such as when an agent continues a submitted job after its client disconnects.

This behavior is the default for Workers with a compatibility date of `2026-10-01` or later. To use it with an earlier date, add the [`durable_object_io_tasks_prevent_eviction`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#durable-object-io-tasks-prevent-eviction) compatibility flag. To opt out, add the `durable_object_io_tasks_do_not_prevent_eviction` flag.

Pending [service binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) requests now keep Durable Objects running while they wait for a response. Pending calls to another Durable Object through remote procedure call (RPC) or `fetch()`, as well as `this.ctx.container.monitor()`, now also keep the Durable Object running.

Promises passed to `this.ctx.waitUntil()` and pending `setTimeout()` and `setInterval()` timers also receive this protection.

Previously, Cloudflare could shut down an idle Durable Object while one of these operations remained pending without a connected client. This could stop unfinished work.

This change helps you run long-running tasks such as agents. An agent can call tools through service bindings, coordinate with other Durable Objects, or wait for a container process without relying on the original client to remain connected.

Outbound `fetch()` requests to external services, TCP sockets, and outbound WebSockets already keep Durable Objects running.

Each pending operation prevents idle shutdown for up to 15 minutes. Starting another one later can extend the Durable Object's time in memory. The limit applies to each operation, not to the total time in memory.

![Timeline of a service binding fetch, an RPC call, and monitor\(\) each preventing eviction for up to 15 minutes](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=820,height=360,format=svg/_astro/pending-io-keep-alive.vVfDqYTX.svg)

Duration charges continue while an operation prevents eviction.

For more information, refer to [Lifecycle of a Durable Object](https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/).

Sep 25, 2026

## [Subscribe to Browser Run crawl events](https://developers.cloudflare.com/changelog/post/2026-09-25-crawl-event-subscriptions/)

[Browser Run](https://developers.cloudflare.com/browser-run/)[Queues](https://developers.cloudflare.com/queues/)

[Browser Run crawl jobs](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/) can publish lifecycle events to [Cloudflare Queues](https://developers.cloudflare.com/queues/). Subscribe to started, updated, and finished events to track progress or trigger downstream processing without polling.

To create an account-level subscription, run the following command:

npmyarnpnpm
    
    
    npx wrangler queues subscription create <QUEUE_NAME> --source browserRun --events crawl.started,crawl.updated,crawl.finished
    
    
    yarn wrangler queues subscription create <QUEUE_NAME> --source browserRun --events crawl.started,crawl.updated,crawl.finished
    
    
    pnpm wrangler queues subscription create <QUEUE_NAME> --source browserRun --events crawl.started,crawl.updated,crawl.finished

For payload examples, refer to the [Browser Run event schemas](https://developers.cloudflare.com/queues/event-subscriptions/events-schemas/#browser-run).

Sep 24, 2026

## [R2 bandwidth usage metrics](https://developers.cloudflare.com/changelog/post/2026-09-24-r2-bandwidth-metrics/)

[R2](https://developers.cloudflare.com/r2/)

New [R2](https://developers.cloudflare.com/r2/) product-level **Metrics** page in the Cloudflare dashboard shows bandwidth usage. You can view usage across all buckets or per bucket.

[ Go to **R2 Metrics** ↗ ](https://dash.cloudflare.com/?to=/:account/r2/metrics) ![R2 upload and download throughput across all buckets over 24 hours](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1443,height=747,format=webp/_astro/r2-bandwidth-metrics.9lTC-zY2.png)

Bandwidth throughput is split by object upload and download. The [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) exposes the same bandwidth usage metrics that power the dashboard for your queries and analytics.

For more information, refer to [R2 metrics and analytics](https://developers.cloudflare.com/r2/platform/metrics-analytics/).

Sep 23, 2026

## [Durable Object name search now supports 128 characters](https://developers.cloudflare.com/changelog/post/2026-09-24-durable-object-name-search-limit/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Durable Object name searches in the Cloudflare dashboard now accept up to 128 characters, up from 20.

Search results and recent invocation lists show up to 128 characters before being truncated with an ellipsis. This limit applies to the object filter on the **Metrics** tab and object search in **Data Studio**.

For more information, refer to [Metrics and analytics](https://developers.cloudflare.com/durable-objects/observability/metrics-and-analytics/) and [Data Studio](https://developers.cloudflare.com/durable-objects/observability/data-studio/).

Sep 17, 2026

## [Workers traces now automatically include JavaScript RPC session spans](https://developers.cloudflare.com/changelog/post/2026-09-17-javascript-rpc-session-spans/)

[Workers](https://developers.cloudflare.com/workers/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Workers traces can now follow JavaScript RPC calls across Worker boundaries and into Durable Objects. Previously, a trace stopped at the caller's RPC boundary. The dashboard now shows the caller-side session and method calls alongside the callee invocation, nested calls, and callbacks into another Worker.

A session span covers the lifetime of a caller-side session and groups calls that reuse it. Individual call spans show each method invocation. Execution colors distinguish the Workers or Durable Object entrypoints involved, while arrows mark outgoing and incoming calls. Together, these details show where time was spent, which calls reused a session, and how returned stubs and callbacks fit into the request.

![A Workers trace of a Worker-to-Worker RPC session, showing the session span, the caller's getCounter and increment call spans, and the callee's invocation and matching call spans](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2878,height=1576,format=webp/_astro/jsrpc-session-spans.DQuwQrpm.png)

Enable tracing with one setting in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/#observability):
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "observability": {
        "traces": {
          "enabled": true
        }
      }
    }
    
    
    [observability.traces]
    enabled = true

Cloudflare records these spans automatically. You do not need to change your application code or add an observability SDK.

For supported spans and attributes, refer to [Spans and attributes](https://developers.cloudflare.com/workers/observability/traces/spans-and-attributes/).

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

Sep 16, 2026

## [Hyperdrive support for Python Workers](https://developers.cloudflare.com/changelog/post/2026-09-16-hyperdrive-python-workers/)

[Workers](https://developers.cloudflare.com/workers/)[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

[Python Workers](https://developers.cloudflare.com/workers/languages/python/) can now connect to PostgreSQL and MySQL through Hyperdrive.

For setup, code examples, and limitations, refer to [Use Hyperdrive from Python Workers](https://developers.cloudflare.com/hyperdrive/examples/python-workers/).

Sep 4, 2026

## [R2 Data Access Logs](https://developers.cloudflare.com/changelog/post/2026-09-04-r2-data-access-logs/)

[R2](https://developers.cloudflare.com/r2/)

R2 Data Access Logs are now generally available. Turn on logging for a bucket to record object read, write, list, multipart upload, and delete operations with response status codes below `400`.

Data Access Logs cover requests made through the S3-compatible API, Cloudflare API and dashboard, Workers bindings, and public buckets through `r2.dev` or custom domains. Events are available in Workers Observability, where you can filter by bucket, operation, interface, actor, and other request fields.

Log delivery is asynchronous and best effort. Events may be delayed or omitted, so do not rely on Data Access Logs as a complete record of bucket activity.

Data Access Logs are available for non-jurisdictional buckets. For setup instructions, supported operations, and the event field reference, refer to [R2 Data Access Logs](https://developers.cloudflare.com/r2/buckets/data-access-logs/).

Sep 1, 2026

## [D1 enforces free tier daily query limits](https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/)

[D1](https://developers.cloudflare.com/d1/)

Beginning September 1, 2026, D1 queries on the [Workers Free plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) will fail when an account exceeds the daily [row read or row write limits](https://developers.cloudflare.com/d1/platform/pricing/). Queries via the [Workers Binding API](https://developers.cloudflare.com/d1/worker-api/) and the [REST API](https://developers.cloudflare.com/d1/rest-api/) will return errors until the limit resets at midnight UTC. Stored data is not affected.

You will receive email alerts when the daily limit is reached. The following errors indicate that a limit has been exceeded:

Error | Description  
---|---  
Your account has exceeded D1's free tier daily row read limit. Upgrade to a paid plan or wait until tomorrow (midnight UTC) to continue. | The account has reached its daily row read limit.  
Your account has exceeded D1's free tier daily row write limit. Upgrade to a paid plan or wait until tomorrow (midnight UTC) to continue. | The account has reached its daily row write limit.  
  
Inspect database query activity before the enforcement date to identify queries that may exceed these limits. To reduce row reads, add [indexes](https://developers.cloudflare.com/d1/best-practices/use-indexes/) to tables and review queries that perform full table scans. If usage requires higher limits after optimization, upgrade to a [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers).

For more information on D1 errors and how to handle them, refer to the [D1 error list](https://developers.cloudflare.com/d1/observability/debug-d1/#error-list).

Aug 28, 2026

## [Durable Objects can use up to ten Dynamic Workers concurrently](https://developers.cloudflare.com/changelog/post/2026-08-28-durable-objects-dynamic-workers-limit/)

[Workers](https://developers.cloudflare.com/workers/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/) can have up to ten distinct [Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/) with in-flight requests, increased from four. This limit applies across all concurrent requests to the same Durable Object because they share an input/output (I/O) context. Other Workers can have up to four distinct Dynamic Workers with in-flight requests per request.

Multiple in-flight requests to the same Dynamic Worker count as one toward this limit.

For more information, refer to [Dynamic Workers limits](https://developers.cloudflare.com/dynamic-workers/platform/limits/).

Aug 25, 2026

## [Prevent Durable Object alarm retries when using `ctx.abort()`](https://developers.cloudflare.com/changelog/post/2026-08-25-durable-object-alarm-abort-no-retry/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)

By default, an alarm interrupted by `ctx.abort()` retries after the Durable Object resets. Pass `{ retryAlarm: false }` when the alarm should stop instead:

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class CleanupTask extends DurableObject {
    	async alarm() {
    		await this.ctx.storage.deleteAll();
    
    		this.ctx.abort("Cleanup complete", { retryAlarm: false });
    	}
    }

src/index.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class CleanupTask extends DurableObject {
    	async alarm(): Promise<void> {
    		await this.ctx.storage.deleteAll();
    
    		this.ctx.abort("Cleanup complete", { retryAlarm: false });
    	}
    }

For example, an alarm that deletes its storage can use this option to avoid repeating the cleanup or re-running the Durable Object constructor.

Alarms can run concurrently with other requests to the same Durable Object. If another request calls `ctx.abort()` while an alarm is running, the `retryAlarm` option on that call also controls whether the alarm retries.

The default retry prevents an unrelated request from permanently canceling the alarm. Set `retryAlarm: false` on every abort path that should stop an in-progress alarm, not only on calls from the alarm handler. Existing calls to `ctx.abort()` keep retrying alarms.

For local development, `retryAlarm` requires Wrangler 4.126.0 or later.

For more information, refer to [`ctx.abort()`](https://developers.cloudflare.com/durable-objects/api/state/#abort).

Aug 20, 2026

## [View deployments for Durable Objects in the dashboard](https://developers.cloudflare.com/changelog/post/2026-08-20-durable-objects-deployments-tab/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Durable Object namespaces now have a **Deployments** tab in the Cloudflare dashboard, showing the [versions](https://developers.cloudflare.com/workers/versions-and-deployments/#versions) of the backing Worker that are currently live and the traffic split between them.

![The Deployments tab for a Durable Object namespace, showing two versions with their traffic %, requests/sec, error rate, and median wall time](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2508,height=654,format=webp/_astro/durable-objects-deployments-tab.ZJc93gIt.png)[ Go to **Durable Objects** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/durable-objects)

A Durable Object namespace is backed by a Worker script, so its deployments are the same as that Worker's deployments. Previously, checking on a [gradual deployment](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/) in progress for a Durable Object meant navigating to the backing Worker. The new tab surfaces that information directly on the namespace, alongside the metrics that matter for it: requests, error rate, and wall time per version.

The tab is read-only — promoting, rolling back, or splitting traffic on a deployment is still managed from the backing Worker's Deployments tab.

#### Actual vs. configured traffic split

The **Traffic %** column, for both Workers and Durable Objects, now shows the actual, observed traffic share for each version next to the percentage you configured. Previously, this column only showed the configured percentage. If you moved a deployment from 50/50 to 100% on a new version, the configured number updated immediately, but requests take time to catch up, and there was no way to tell how far along that shift was without checking metrics elsewhere.

The configured split assigns Worker versions to individual Durable Objects, not to individual requests. Because [each Durable Object is pinned to the version it started on until you create a new deployment](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/with-durable-objects/) and some objects naturally receive more traffic than others, the observed split can differ from the configured one for as long as multiple versions are active.

Actual traffic share is calculated from the same [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) data that powers other Workers and Durable Objects metrics, so standard ingestion delay and [sampling](https://developers.cloudflare.com/analytics/faq/graphql-api-inconsistent-results/) apply. Durable Objects analytics can lag Workers analytics by several minutes, so a version's actual share may take a little longer to catch up after a change.

To view this, go to **Workers & Pages** > **Durable Objects** , select a namespace, then select the **Deployments** tab. For more on how gradual deployments work, refer to [Gradual deployments](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/).

Aug 17, 2026

## [New `us` jurisdiction for R2](https://developers.cloudflare.com/changelog/post/2026-08-17-r2-us-jurisdiction/)

[R2](https://developers.cloudflare.com/r2/)

R2 now supports a `us` [jurisdiction](https://developers.cloudflare.com/r2/reference/data-location/#jurisdictional-restrictions), which guarantees that bucket data is stored and processed within the United States. Use this jurisdiction when you need explicit US data residency guarantees.

Use the jurisdiction-specific S3 endpoint to create and access buckets in the `us` jurisdiction:

`https://<ACCOUNT_ID>.us.r2.cloudflarestorage.com`

To access a bucket in the `us` jurisdiction from Workers, set `jurisdiction` in your R2 binding:
    
    
    {
    	"r2_buckets": [
    		{
    			"binding": "MY_BUCKET",
    			"bucket_name": "<YOUR_BUCKET_NAME>",
    			"jurisdiction": "us"
    		}
    	]
    }
    
    
    [[r2_buckets]]
    binding = "MY_BUCKET"
    bucket_name = "<YOUR_BUCKET_NAME>"
    jurisdiction = "us"

Once an R2 bucket is created, its jurisdiction cannot be changed.

For setup instructions and the full list of supported jurisdictions, refer to [R2 data location](https://developers.cloudflare.com/r2/reference/data-location/#jurisdictional-restrictions).

Aug 7, 2026

## [MySQL support in Hyperdrive is now generally available](https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-mysql-ga/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Support for MySQL in Hyperdrive is now generally available. You can connect to any MySQL database from your Workers using Hyperdrive.

Hyperdrive makes your regional, MySQL databases fast when connecting from Cloudflare Workers. It eliminates unnecessary network roundtrips during connection setup, pools database connections globally, and can cache query results to provide the fastest possible response times.

You can connect using your existing drivers, ORMs, and query builders with Hyperdrive's secure credentials, with no code changes required. MySQL support is available at the same [pricing](https://developers.cloudflare.com/hyperdrive/platform/pricing/) as Postgres.
    
    
    import { createConnection } from "mysql2/promise";
    
    export default {
    	async fetch(request, env, ctx) {
    		const connection = await createConnection({
    			host: env.HYPERDRIVE.host,
    			user: env.HYPERDRIVE.user,
    			password: env.HYPERDRIVE.password,
    			database: env.HYPERDRIVE.database,
    			port: env.HYPERDRIVE.port,
    			disableEval: true, // Required for Workers compatibility
    		});
    
    		const [results, fields] = await connection.query("SHOW tables;");
    
    		ctx.waitUntil(connection.end());
    
    		return new Response(JSON.stringify({ results, fields }), {
    			headers: {
    				"Content-Type": "application/json",
    				"Access-Control-Allow-Origin": "*",
    			},
    		});
    	},
    };
    
    
    import { createConnection } from "mysql2/promise";
    
    export interface Env {
    	HYPERDRIVE: Hyperdrive;
    }
    
    export default {
    	async fetch(request, env, ctx): Promise<Response> {
    		const connection = await createConnection({
    			host: env.HYPERDRIVE.host,
    			user: env.HYPERDRIVE.user,
    			password: env.HYPERDRIVE.password,
    			database: env.HYPERDRIVE.database,
    			port: env.HYPERDRIVE.port,
    			disableEval: true, // Required for Workers compatibility
    		});
    
    		const [results, fields] = await connection.query("SHOW tables;");
    
    		ctx.waitUntil(connection.end());
    
    		return new Response(JSON.stringify({ results, fields }), {
    			headers: {
    				"Content-Type": "application/json",
    				"Access-Control-Allow-Origin": "*",
    			},
    		});
    	},
    } satisfies ExportedHandler<Env>;

Learn more about [how Hyperdrive works](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/) and [get started building Workers that connect to MySQL with Hyperdrive](https://developers.cloudflare.com/hyperdrive/get-started/).

Aug 7, 2026

## [Restart a Hyperdrive configuration from the dashboard](https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-restart-configuration-dashboard/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

You can now restart a Hyperdrive configuration from the Cloudflare dashboard. Restarting drains the connection pool and forces Hyperdrive to establish new connections to your origin database.

Restarting is a break-glass action. Hyperdrive automatically detects and recovers from most database failovers. Use a manual restart only when you need to force the pool to drain immediately.

To restart, select your Hyperdrive configuration in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com), go to the **Settings** tab, and select **Restart** under **Danger zone**. Restarting requires the [**Hyperdrive Admin** role](https://developers.cloudflare.com/fundamentals/manage-members/roles/). After a restart, the **Settings** tab shows when the configuration was last manually restarted.

![The Danger zone section of the Hyperdrive Settings tab, showing the Restart and Delete actions.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1698,height=468,format=webp/_astro/dashboard-restart-danger-zone.D1h69zVU.png)

Caution

Restarting drops all active connections in the pool and forces them to be re-established. In-flight queries may see brief errors while the pool rebuilds.

For more information, refer to [Connection pooling](https://developers.cloudflare.com/hyperdrive/concepts/connection-pooling/).

Aug 4, 2026

## [Vectorize indexes now support up to 20 million vectors](https://developers.cloudflare.com/changelog/post/2026-08-04-index-capacity-20-million/)

[Vectorize](https://developers.cloudflare.com/vectorize/)

You can now store up to 20 million vectors in a single Vectorize index, doubling the previous limit of 10 million vectors. This enables larger-scale semantic search, recommendation systems, and retrieval-augmented generation (RAG) applications without splitting data across multiple indexes.

Vectorize continues to support indexes with up to 1,536 dimensions per vector at 32-bit precision. Refer to the [Vectorize limits documentation](https://developers.cloudflare.com/vectorize/platform/limits/) for complete details.

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

Jul 31, 2026

## [Inspect Worker startup performance with Wrangler](https://developers.cloudflare.com/changelog/post/2026-07-31-wrangler-startup-profile-summary/)

[Workers](https://developers.cloudflare.com/workers/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)

`wrangler check startup` now reports your Worker's raw and compressed bundle sizes. It also summarizes local CPU activity during startup directly in your terminal.

Large bundles and costly startup work can introduce cold-start latency, so use this command to find code and large dependencies that slow your Worker before it handles requests.

The summary includes sampled, active, garbage collection, and idle time. Wrangler continues to save a `.cpuprofile` file for detailed flamegraph analysis in Chrome DevTools or VS Code.
    
    
    ⛅️ wrangler 4.116.0
    ───────────────────────────────────────────────
    ├ Building your Worker
    │ Worker Built! 🎉
    │
    ├ Analysing
    │ Startup phase analysed
    │
    │ Bundle: 7171.25 KiB / gzip: 2197.00 KiB
    │
    │ Local startup profile:
    │   Profile window: 70.3 ms
    │   Sampled time: 70.3 ms
    │   Active: 38.5 ms (including 3.7 ms garbage collection)
    │   Idle: 31.8 ms
    │   Samples: 36
    │
    │ CPU Profile has been written to worker-startup.cpuprofile. Load it into the Chrome DevTools profiler (or directly in VSCode) to view a flamegraph.
    │
    │ Note that the CPU Profile was measured on your Worker running locally on your machine, which has a different CPU than when your Worker runs on Cloudflare.
    │
    │ As such, CPU Profile can be used to understand where time is spent at startup, but the overall startup time in the profile should not be expected to exactly match what your Worker's startup time will be when deploying to Cloudflare.

The profile runs locally, so its duration will differ from startup time on Cloudflare. For authoritative startup time, deploy your Worker or upload a version.

Available in Wrangler version 4.116.0 or later. For more information, refer to [`wrangler check startup`](https://developers.cloudflare.com/workers/wrangler/commands/workers/#startup).

← Prev

1[2](https://developers.cloudflare.com/changelog/product-group/storage/2/)…[6](https://developers.cloudflare.com/changelog/product-group/storage/6/)

[Next →](https://developers.cloudflare.com/changelog/product-group/storage/2/)
