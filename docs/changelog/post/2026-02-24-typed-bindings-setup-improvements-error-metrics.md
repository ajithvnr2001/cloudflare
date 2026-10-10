---
url: https://developers.cloudflare.com/changelog/post/2026-02-24-typed-bindings-setup-improvements-error-metrics/
title: Dropped event metrics, typed Pipelines bindings, and improved setup \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.294569+00:00
---

# Dropped event metrics, typed Pipelines bindings, and improved setup · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-24-typed-bindings-setup-improvements-error-metrics/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 24, 2026

## Dropped event metrics, typed Pipelines bindings, and improved setup

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin](https://developers.cloudflare.com/basin/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
