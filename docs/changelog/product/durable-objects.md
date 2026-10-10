---
url: https://developers.cloudflare.com/changelog/product/durable-objects/
title: Durable Objects Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:08.473122+00:00
---

# Durable Objects Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/durable-objects/

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

Jul 24, 2026

## [Filter Durable Object logs and traces by instance ID](https://developers.cloudflare.com/changelog/post/2026-07-24-durable-object-instance-observability/)

[Workers](https://developers.cloudflare.com/workers/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)

[Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) and [OpenTelemetry](https://developers.cloudflare.com/observability/export/opentelemetry/) spans for [Durable Object](https://developers.cloudflare.com/durable-objects/) requests include the Durable Object instance ID.

Use `$workers.durableObjectId` to filter logs for a specific instance. Root and child spans include the same ID in `cloudflare.durable_object.id`.

![Query Builder filtering traces by Durable Object instance ID](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2000,height=666,format=webp/_astro/2026-07-24-durable-object-trace-filter.DW-BwlKL.png)

Use these fields to isolate a specific instance and correlate its logs and traces.

For more information, refer to [Durable Objects metrics and analytics](https://developers.cloudflare.com/durable-objects/observability/metrics-and-analytics/) and [Workers tracing spans and attributes](https://developers.cloudflare.com/workers/observability/traces/spans-and-attributes/).

Jul 20, 2026

## [View total SQLite storage for Durable Object namespaces](https://developers.cloudflare.com/changelog/post/2026-07-20-durable-objects-total-storage-metrics/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

You can now monitor the total SQLite storage used by a Durable Object namespace over time in the Cloudflare dashboard. The new **Total storage** chart shows the maximum storage reported during each hour. This helps you identify storage growth, validate data cleanup, and investigate unexpected usage.

![The Total storage chart showing a Durable Object namespace growing to 260.1 MB of storage over time.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1436,height=846,format=webp/_astro/durable-objects-total-storage.Cr_F72Yz.png)[ Go to **Durable Objects** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/durable-objects)

The chart appears only for SQLite-backed Durable Object namespaces. It does not appear for namespaces that use the legacy key-value storage backend. Viewing storage for individual Durable Objects by ID or name is not supported.

For more information, refer to [Metrics and analytics](https://developers.cloudflare.com/durable-objects/observability/metrics-and-analytics/#total-storage).

Jul 9, 2026

## [New Durable Object namespaces must use the SQLite storage backend](https://developers.cloudflare.com/changelog/post/2026-07-09-restrict-new-kv-backed-namespaces/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

If your account does not already have a key-value (KV) backed Durable Object namespace, you can no longer create new ones. New Durable Object namespaces must use the [SQLite storage backend](https://developers.cloudflare.com/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class), which has been recommended for all new Durable Objects since it became [generally available ↗︎](https://blog.cloudflare.com/sqlite-in-durable-objects/) in 2024.

Create a new class with a `new_sqlite_classes` migration:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "migrations": [
        {
          "tag": "v1",
          "new_sqlite_classes": [
            "MyDurableObject"
          ]
        }
      ]
    }
    
    
    [[migrations]]
    tag = "v1"
    new_sqlite_classes = ["MyDurableObject"]

SQLite-backed Durable Objects have feature parity with the key-value backend — including the [key-value storage API](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/#synchronous-kv-api) — and additionally support relational [SQL queries](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/#sql-api) and [point-in-time recovery](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/#pitr-point-in-time-recovery-api) to restore an object's storage to any point in the past 30 days.

If you attempt to create a new key-value backed namespace (a `new_classes` migration) on an affected account, the deployment fails with the following error:
    
    
    Creating new key-value backed Durable Object namespaces is no longer supported on this account. Please create a namespace using a `new_sqlite_classes` migration instead.

This change only affects accounts that are not already using the key-value storage backend. Accounts with at least one existing key-value backed namespace can still create new ones for now, and the Workers Free plan has only ever supported SQLite-backed Durable Objects. It is part of a broader move toward SQLite as the single storage backend for Durable Objects, ahead of a future migration path for existing key-value backed objects.

For more information, refer to [Durable Objects migrations](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/).

Jul 4, 2026

## [Declare Durable Object class lifecycle with `exports`](https://developers.cloudflare.com/changelog/post/2026-06-30-declarative-do-class-exports/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

A new declarative [`exports`](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/) field in your Wrangler configuration file replaces the imperative [`migrations`](https://developers.cloudflare.com/durable-objects/reference/durable-object-class-migrations-legacy/) array for managing Durable Object class lifecycle. Instead of writing an ordered list of migration steps with unique tags, you declare each Durable Object class your Worker exports and Cloudflare compares that against what's already deployed to determine what Durable Object state needs to be created, renamed, or deleted.

With legacy migrations, renaming `ChatRoom` to `Room` requires retaining both tagged steps:

Before — legacy migrationsjsonc
    
    
    {
    	"migrations": [
    		{ "tag": "v1", "new_sqlite_classes": ["ChatRoom"] },
    		{
    			"tag": "v2",
    			"renamed_classes": [{ "from": "ChatRoom", "to": "Room" }],
    		},
    	],
    }

With `exports`, you instead declare `Room` as the current class and mark `ChatRoom` as renamed:

After — declarative exportsjsonc
    
    
    {
    	"exports": {
    		"ChatRoom": {
    			"type": "durable-object",
    			"state": "renamed",
    			"renamed_to": "Room",
    		},
    		"Room": { "type": "durable-object", "storage": "sqlite" },
    	},
    }

Each entry is keyed by class name. The `state` field carries the lifecycle (`created` by default — a live class — plus tombstone states `deleted`, `renamed`, and `transferred`, and the `expecting-transfer` receiving state for cross-Worker transfers).

Key improvements over the legacy `migrations` array:

  * **No migration tags.** The current `exports` map is the source of truth — there is no historical chain of `v1`, `v2`, `v3` entries to maintain.
  * **Structured deployment output.** Wrangler reports when it creates, updates, deletes, renames, or transfers Durable Object classes. It also identifies stale configuration entries that are safe to remove. Deployments with no changes or notices do not print this output.
  * **Zero-downtime rename and transfer patterns are first-class.** Tombstones may coexist with the source class still in code, enabling a [three-deploy rename](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/#avoid-downtime-during-a-rename) and a [four-deploy cross-Worker transfer](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/#transfer-a-durable-object-class-between-workers) without runtime errors during the rollout window.
  * **Cross-Worker safety.** When you delete or rename a class, Cloudflare lists every other Worker in your account whose bindings still reference the namespace, so you can redeploy them before the change goes live.



Existing Workers using the legacy [`migrations`](https://developers.cloudflare.com/durable-objects/reference/durable-object-class-migrations-legacy/) array continue to work unchanged. To move to `exports`, refer to the [migration guide](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/#migrate-from-the-legacy-migrations-flow). `exports` and `migrations` are mutually exclusive within a single Worker.

For the full reference, refer to [Durable Object class exports](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/).

Jun 30, 2026

## [Track memory usage for Workers and Durable Objects in the dashboard](https://developers.cloudflare.com/changelog/post/2026-06-30-memory-usage-metrics/)

[Workers](https://developers.cloudflare.com/workers/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)

You can now monitor how much memory your [Workers](https://developers.cloudflare.com/workers/) and [Durable Objects](https://developers.cloudflare.com/durable-objects/) consume across invocations with the new **Memory Usage** chart in the Workers Metrics tab, broken down by P50, P90, P99, and P999 percentiles.

![Memory usage chart showing P50, P90, P99, and P999 percentiles with deployment markers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1210,height=782,format=webp/_astro/2026-06-26-memory-usage.B20y2uNp.png)

Memory usage measures the V8 [isolate](https://developers.cloudflare.com/workers/reference/how-workers-works/#isolates) memory at the time of each invocation, subject to the [128 MB per-isolate limit](https://developers.cloudflare.com/workers/platform/limits/#memory) — a single isolate can handle many concurrent requests and shares memory across them.

Use the Memory Usage chart to:

  * **Track memory trends** — Spot gradual increases that may indicate a memory leak before they cause `Exceeded Memory` errors.
  * **Correlate with deployments** — Deployment markers on the chart help you identify whether a new version introduced a memory regression.
  * **Right-size your Worker** — Understand your baseline memory footprint and how much headroom you have before hitting the 128 MB limit.



For Durable Objects, memory usage reflects the in-memory state an object holds (class properties, caches, active WebSocket connections), which persists across invocations until the object is [hibernated or evicted](https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/). This state is not preserved across eviction, hibernation, or a crash, so persist anything important to [storage](https://developers.cloudflare.com/durable-objects/best-practices/access-durable-objects-storage/).

To view memory usage, open the **Metrics** tab for your [Worker ↗︎](https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/metrics) or [Durable Object namespace ↗︎](https://dash.cloudflare.com/?to=/:account/workers/durable-objects). For Durable Objects, you can filter by DO ID or name to drill down into memory usage for a specific object. You can also query memory usage programmatically via the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-workers-metrics/) using the `workersInvocationsAdaptive` dataset — the `quantiles.memoryUsageBytesP50` through `quantiles.memoryUsageBytesP999` fields return percentile values in bytes.

For local memory debugging, you can also [profile memory with DevTools](https://developers.cloudflare.com/workers/observability/dev-tools/memory-usage/) to take heap snapshots and identify specific objects causing high memory usage.

Jun 26, 2026

## [New `us` jurisdiction for Durable Objects](https://developers.cloudflare.com/changelog/post/2026-06-26-durable-objects-us-jurisdiction/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Durable Objects now supports a `us` [jurisdiction](https://developers.cloudflare.com/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction), letting you create Durable Objects that only run and store data within the United States. Use the `us` jurisdiction when you need to keep a Durable Object's compute and storage inside the United States to meet data residency requirements.

Create a namespace restricted to the `us` jurisdiction the same way as any other jurisdiction:
    
    
    // Worker
    export default {
    	async fetch(request, env) {
    		const usSubnamespace = env.MY_DURABLE_OBJECT.jurisdiction("us");
    		const stub = usSubnamespace.getByName("general");
    		return stub.fetch(request);
    	},
    };

Workers may still access Durable Objects constrained to the `us` jurisdiction from anywhere in the world. The jurisdiction constraint only controls where the Durable Object itself runs and persists data.

For the full list of supported jurisdictions, refer to [Data location — Restrict Durable Objects to a jurisdiction](https://developers.cloudflare.com/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction).

Jun 25, 2026

## [Test Durable Object eviction with new cloudflare:test helpers](https://developers.cloudflare.com/changelog/post/2026-06-25-durable-object-eviction-test-helpers/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

The `@cloudflare/vitest-pool-workers` package now includes `evictDurableObject` and `evictAllDurableObjects` test helpers, exported from `cloudflare:test`.

These helpers let you test how a Durable Object behaves across evictions, simulating the production lifecycle where an idle Durable Object can be evicted from memory.

For more context, refer to [Lifecycle of a Durable Object](https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/).
    
    
    import { evictDurableObject, evictAllDurableObjects } from "cloudflare:test";
    import { env } from "cloudflare:workers";
    
    const id = env.COUNTER.idFromName("my-counter");
    const stub = env.COUNTER.get(id);
    
    // Evict the Durable Object instance pointed to by a specific stub
    await evictDurableObject(stub);
    
    // Close WebSockets instead of hibernating them
    await evictDurableObject(stub, { webSockets: "close" });
    
    // Evict all currently-running Durable Objects in evictable namespaces
    await evictAllDurableObjects();

These helpers are available in `@cloudflare/vitest-pool-workers@0.16.20` and later.

Learn more in the [Test APIs reference](https://developers.cloudflare.com/workers/testing/vitest-integration/test-apis/#durable-objects) and the [Testing Durable Objects guide](https://developers.cloudflare.com/durable-objects/examples/testing-with-durable-objects/#testing-eviction).

Jun 19, 2026

## [New Asia-Pacific location hints: apac-ne and apac-se](https://developers.cloudflare.com/changelog/post/2026-06-19-apac-ne-apac-se-location-hints/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Durable Objects now supports two new location hints for Asia-Pacific: `apac-ne` (Northeast Asia-Pacific) and `apac-se` (Southeast Asia-Pacific). Use `apac-ne` or `apac-se` when you want finer-grained placement within Asia-Pacific rather than the broader `apac` hint.

Use the new hints the same way as any other `locationHint`:
    
    
    // Northeast Asia-Pacific (Japan, Korea, etc.)
    const stubNE = env.MY_DURABLE_OBJECT.get(id, { locationHint: "apac-ne" });
    
    // Southeast Asia-Pacific (Singapore, Indonesia, etc.)
    const stubSE = env.MY_DURABLE_OBJECT.get(id, { locationHint: "apac-se" });

If your users are spread across all of Asia-Pacific, the existing `apac` hint remains the right choice. Only reach for `apac-ne` or `apac-se` when your traffic is clearly concentrated in one sub-region and you want to minimize round-trip time to that audience. The default behavior and what we generally recommended is not adding a location hint unless absolutely needed, this will create the Durable Object as close to the initializing request as possible to reduce latency.

As with all location hints, these are best-effort suggestions. Cloudflare will place the Durable Object in a nearby data center, not necessarily the exact hinted location.

For the full list of supported hints, refer to [Data location — Provide a location hint](https://developers.cloudflare.com/durable-objects/reference/data-location/#provide-a-location-hint).

Jun 19, 2026

## [Outbound connections keep Durable Objects alive](https://developers.cloudflare.com/changelog/post/2026-06-19-outbound-connections-keep-dos-alive/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Durable Objects now remain alive for the duration of active outbound connections created via [`connect()`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/) or an outbound WebSocket. Previously, a Durable Object would be evicted after 70-140 seconds of no incoming traffic, even if the object had an open outbound connection, which is a common pattern when streaming responses from a large language model (LLM) over TCP or an outbound WebSocket.

With this change, each active outbound connection prevents eviction. Once all outbound connections close, the standard 70-140 second inactivity window applies before the Durable Object is evicted.

#### Before: streaming connections were cut off by eviction

![Timeline showing a Durable Object evicted 70-140 seconds after the last incoming request, cutting off an in-flight LLM stream while the outbound connection is still open](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=820,height=360,format=svg/_astro/outbound-connection-before.jZgN3tY3.svg)

#### After: active outbound connections keep the Durable Object alive

![Timeline showing the same outbound stream completing because the active connection keeps the Durable Object alive, with the inactivity window starting only after the connection closes](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=820,height=360,format=svg/_astro/outbound-connection-after.CxPT16q0.svg)

If you are [building agents on Cloudflare](https://developers.cloudflare.com/agents/), this is especially relevant. An agent that streams tokens from an LLM while [calling models](https://developers.cloudflare.com/agents/concepts/calling-llms/), or that performs [long-running tasks](https://developers.cloudflare.com/agents/concepts/agentic-patterns/long-running-agents/) over an outbound connection, now stays alive for the duration of that connection instead of being evicted mid-stream.

**Limits:**

  * Each outbound connection keeps the Durable Object alive for a maximum of **15 minutes**. After 15 minutes, the connection stops preventing eviction (the connection itself continues operating), and the [standard eviction rules](https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/) resume.
  * The Durable Object's existing [per-account instance limits](https://developers.cloudflare.com/durable-objects/platform/limits/) still apply.



For more information, refer to [Lifecycle of a Durable Object](https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/).

Jun 12, 2026

## [Filter Durable Objects metrics by object ID or name](https://developers.cloudflare.com/changelog/post/2026-06-12-durable-objects-metrics-filter-by-id-name/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

You can now filter the **Metrics** tab for a Durable Objects namespace by an individual Durable Object's [ID](https://developers.cloudflare.com/durable-objects/api/id/) or [name](https://developers.cloudflare.com/durable-objects/api/id/#name) in the Cloudflare dashboard. Previously, metrics charts only showed aggregate, namespace-level data, making it difficult to isolate the behavior of a specific object.

[ Go to **Durable Objects** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/durable-objects) ![The Durable Objects Metrics tab filtered to a single object by ID, showing per-object requests and errors by invocation status.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2936,height=1482,format=webp/_astro/durable-objects-metrics-dashboard.BFZTyhWU.png)

Start typing an ID or name into the filter and select a match from the autocomplete dropdown. The autocomplete only shows objects with invocations during the selected time range, so an object that does not appear has not been invoked in that window. This does not necessarily mean the object has been deleted. Every chart on the page updates to reflect only the selected object. This makes it easier to identify and investigate a single Durable Object when debugging a high-traffic object, an error spike, or unexpected storage usage. Clear the filter to return to namespace-level metrics.

Metrics are powered by the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/), so standard analytics behavior such as ingestion delay and [sampling](https://developers.cloudflare.com/analytics/faq/graphql-api-inconsistent-results/) applies.

For more information, refer to [Metrics and analytics](https://developers.cloudflare.com/durable-objects/observability/metrics-and-analytics/).

Jun 4, 2026

## [Billable usage and budget alerts now in product sidebars](https://developers.cloudflare.com/changelog/post/2026-06-04-billable-usage-product-sidebar/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Workers](https://developers.cloudflare.com/workers/)[D1](https://developers.cloudflare.com/d1/)[R2](https://developers.cloudflare.com/r2/)[KV](https://developers.cloudflare.com/kv/)[Queues](https://developers.cloudflare.com/queues/)[Vectorize](https://developers.cloudflare.com/vectorize/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Containers](https://developers.cloudflare.com/containers/)

Pay-as-you-go customers can now view billable usage and create [budget alerts](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) directly from the product overview pages for [Workers & Pages](https://developers.cloudflare.com/workers/), [D1](https://developers.cloudflare.com/d1/), [R2](https://developers.cloudflare.com/r2/), [Workers KV](https://developers.cloudflare.com/kv/), [Queues](https://developers.cloudflare.com/queues/), [Vectorize](https://developers.cloudflare.com/vectorize/), [Durable Objects](https://developers.cloudflare.com/durable-objects/), and [Containers](https://developers.cloudflare.com/containers/). A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.

The widget pulls from the same data as the [Billable Usage dashboard](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.

![Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2872,height=1614,format=webp/_astro/2026-06-04-billable-usage-product-sidebar.BUuIokn_.png)

Selecting **Create budget alert** opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.

For more information, refer to the [Usage-based billing documentation](https://developers.cloudflare.com/billing/).

Mar 26, 2026

## [Access Durable Object jurisdiction via `ctx.id.jurisdiction`](https://developers.cloudflare.com/changelog/post/2026-03-26-durable-object-id-jurisdiction/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

`ctx.id.jurisdiction` inside a Durable Object now reports the [jurisdiction](https://developers.cloudflare.com/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction) the object was created in — for example `"eu"` when accessed through `env.MY_DURABLE_OBJECT.jurisdiction("eu")` — so you can make region-aware decisions without passing the jurisdiction through method arguments or persisting it in storage. For the full list of ID-construction paths that preserve `jurisdiction`, refer to the [Durable Object ID documentation](https://developers.cloudflare.com/durable-objects/api/id/#jurisdiction).
    
    
    export class RegionalRoom extends DurableObject {
    	async fetch(request) {
    		// "eu" when accessed through env.MY_DURABLE_OBJECT.jurisdiction("eu")
    		const region = this.ctx.id.jurisdiction;
    		return new Response(`Hello from ${region ?? "the default region"}!`);
    	}
    }
    
    // Worker
    export default {
    	async fetch(request, env) {
    		const stub = env.MY_DURABLE_OBJECT.jurisdiction("eu").getByName("general");
    		return stub.fetch(request);
    	},
    };

`ctx.id.jurisdiction` is `undefined` for Durable Objects that were not created in a jurisdiction-restricted namespace. Alarms scheduled before 2026-03-15 also do not have `jurisdiction` stored; to backfill the value, reschedule the alarm from a `fetch()` or RPC handler.

Mar 15, 2026

## [Access Durable Object name via `ctx.id.name`](https://developers.cloudflare.com/changelog/post/2026-03-15-durable-object-id-name/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

When your Worker accesses a Durable Object via `idFromName()` or `getByName()`, the same name is now available on `ctx.id.name` inside the object — no need to pass it through method arguments or persist it in storage. This brings the runtime behavior in line with the [Workers runtime types](https://developers.cloudflare.com/workers/languages/typescript/).

This is especially useful for [alarms](https://developers.cloudflare.com/durable-objects/api/alarms/), where there is no calling client to pass the name as an argument. When an alarm handler runs, `ctx.id.name` will hold the same name the object was originally accessed with.
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class ChatRoom extends DurableObject {
      async getRoomName() {
        // ctx.id.name returns the name passed to getByName() or idFromName()
        return this.ctx.id.name;
      }
    }
    
    // Worker
    export default {
      async fetch(request, env) {
        const stub = env.CHAT_ROOM.getByName("general");
        const roomName = await stub.getRoomName();
        return new Response(`Welcome to ${roomName}!`);
      },
    };

`ctx.id.name` is `undefined` in the following cases:

  * For Durable Objects created with `newUniqueId()`.
  * When accessed via `idFromString()`, even if the ID was originally created from a name.
  * For [names longer than 1,024 bytes](https://developers.cloudflare.com/durable-objects/api/id/#name).



This works the same way in local development with `wrangler dev` as it does in production. Run `npm update wrangler` to ensure you are on a version with this support.

For more information, refer to the [Durable Object ID documentation](https://developers.cloudflare.com/durable-objects/api/id/#name).

Feb 24, 2026

## [deleteAll() now deletes Durable Object alarm](https://developers.cloudflare.com/changelog/post/2026-02-24-deleteall-deletes-alarms/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

`deleteAll()` now deletes a Durable Object alarm in addition to stored data for Workers with a compatibility date of `2026-02-24` or later. This change simplifies clearing a Durable Object's storage with a single API call.

Previously, `deleteAll()` only deleted user-stored data for an object. Alarm usage stores metadata in an object's storage, which required a separate `deleteAlarm()` call to fully clean up all storage for an object. The `deleteAll()` change applies to both KV-backed and SQLite-backed Durable Objects.
    
    
    // Before: two API calls required to clear all storage
    await this.ctx.storage.deleteAlarm();
    await this.ctx.storage.deleteAll();
    
    // Now: a single call clears both data and the alarm
    await this.ctx.storage.deleteAll();

For more information, refer to the [Storage API documentation](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/#deleteall).

Dec 15, 2025

## [New Best Practices guide for Durable Objects](https://developers.cloudflare.com/changelog/post/2025-12-15-rules-of-durable-objects/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

A new [Rules of Durable Objects](https://developers.cloudflare.com/durable-objects/best-practices/rules-of-durable-objects/) guide is now available, providing opinionated best practices for building effective Durable Objects applications. This guide covers design patterns, storage strategies, concurrency, and common anti-patterns to avoid.

Key guidance includes:

  * **Design around your "atom" of coordination** — Create one Durable Object per logical unit (chat room, game session, user) instead of a global singleton that becomes a bottleneck.
  * **Use SQLite storage with RPC methods** — SQLite-backed Durable Objects with typed RPC methods provide the best developer experience and performance.
  * **Understand input and output gates** — Learn how Cloudflare's runtime prevents data races by default, how write coalescing works, and when to use `blockConcurrencyWhile()`.
  * **Leverage Hibernatable WebSockets** — Reduce costs for real-time applications by allowing Durable Objects to sleep while maintaining WebSocket connections.



The [testing documentation](https://developers.cloudflare.com/durable-objects/examples/testing-with-durable-objects/) has also been updated with modern patterns using `@cloudflare/vitest-pool-workers`, including examples for testing SQLite storage, alarms, and direct instance access:

test/counter.test.jsjs
    
    
    import { env, runDurableObjectAlarm } from "cloudflare:test";
    import { it, expect } from "vitest";
    
    it("can test Durable Objects with isolated storage", async () => {
    	const stub = env.COUNTER.getByName("test");
    
    	// Call RPC methods directly on the stub
    	await stub.increment();
    	expect(await stub.getCount()).toBe(1);
    
    	// Trigger alarms immediately without waiting
    	await runDurableObjectAlarm(stub);
    });

test/counter.test.tsts
    
    
    import { env, runDurableObjectAlarm } from "cloudflare:test";
    import { it, expect } from "vitest";
    
    it("can test Durable Objects with isolated storage", async () => {
    	const stub = env.COUNTER.getByName("test");
    
    	// Call RPC methods directly on the stub
    	await stub.increment();
    	expect(await stub.getCount()).toBe(1);
    
    	// Trigger alarms immediately without waiting
    	await runDurableObjectAlarm(stub);
    });

Dec 12, 2025

## [Billing for SQLite Storage](https://developers.cloudflare.com/changelog/post/2025-12-12-durable-objects-sqlite-storage-billing/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Storage billing for SQLite-backed Durable Objects will be enabled in January 2026, with a target date of January 7, 2026 (no earlier).

To view your SQLite storage usage, go to the **Durable Objects** page

[ Go to **Durable Objects** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/durable-objects)

If you do not want to incur costs, please take action such as optimizing queries or deleting unnecessary stored data in order to reduce your SQLite storage usage ahead of the January 7th target. Only usage on and after the billing target date will incur charges.

Developers on the Workers Paid plan with Durable Object's SQLite storage usage beyond included limits will incur charges according to [SQLite storage pricing](https://developers.cloudflare.com/durable-objects/platform/pricing/#sqlite-storage-backend) announced in September 2024 with the [public beta ↗︎](https://blog.cloudflare.com/sqlite-in-durable-objects/). Developers on the Workers Free plan will not be charged.

Compute billing for SQLite-backed Durable Objects has been enabled since the initial public beta. SQLite-backed Durable Objects currently incur [charges for requests and duration](https://developers.cloudflare.com/durable-objects/platform/pricing/#compute-billing), and no changes are being made to compute billing.

For more information about SQLite storage pricing and limits, refer to the [Durable Objects pricing documentation](https://developers.cloudflare.com/durable-objects/platform/pricing/#sqlite-storage-backend).

Oct 31, 2025

## [Workers WebSocket message size limit increased from 1 MiB to 32 MiB](https://developers.cloudflare.com/changelog/post/2025-10-31-increased-websocket-message-size-limit/)

[Workers](https://developers.cloudflare.com/workers/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Browser Run](https://developers.cloudflare.com/browser-run/)

Workers, including those using [Durable Objects](https://developers.cloudflare.com/durable-objects/) and [Browser Rendering](https://developers.cloudflare.com/browser-run/), may now process WebSocket messages up to 32 MiB in size. Previously, this limit was 1 MiB.

This change allows Workers to handle use cases requiring large message sizes, such as processing Chrome Devtools Protocol messages.

For more information, please see the [Durable Objects startup limits](https://developers.cloudflare.com/durable-objects/platform/limits/#sqlite-backed-durable-objects-general-limits).

Oct 16, 2025

## [View and edit Durable Object data in UI with Data Studio (Beta)](https://developers.cloudflare.com/changelog/post/2025-10-16-durable-objects-data-studio/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

![Screenshot of Durable Objects Data Studio](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1699,height=407,format=webp/_astro/do-data-studio.BfCcgtkq.png)

You can now view and write to each Durable Object's storage using a UI editor on the Cloudflare dashboard. Only Durable Objects using [SQLite storage](https://developers.cloudflare.com/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class) can use Data Studio.

[ Go to **Durable Objects** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/durable-objects)

Data Studio unlocks easier data access with Durable Objects for prototyping application data models to debugging production storage usage. Before, querying your Durable Objects data required deploying a Worker.

To access a Durable Object, you can provide an object's unique name or ID generated by Cloudflare. Data Studio requires you to have at least the `Workers Platform Admin` role, and all queries are captured with audit logging for your security and compliance needs. Queries executed by Data Studio send requests to your remote, deployed objects and incur normal usage billing.

To learn more, visit the Data Studio [documentation](https://developers.cloudflare.com/durable-objects/observability/data-studio/). If you have feedback or suggestions for the new Data Studio, please share your experience on [Discord ↗︎](https://discord.com/channels/595317990191398933/773219443911819284)

← Prev

1[2](https://developers.cloudflare.com/changelog/product/durable-objects/2/)

[Next →](https://developers.cloudflare.com/changelog/product/durable-objects/2/)
