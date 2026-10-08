---
url: https://developers.cloudflare.com/queues/observability/metrics/
title: Metrics \u00b7 Cloudflare Queues docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:41.323823+00:00
---

# Metrics · Cloudflare Queues docs

> Source: https://developers.cloudflare.com/queues/observability/metrics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Queues](https://developers.cloudflare.com/queues/)
  3. /Observability
  4. /Metrics



# Metrics

Last updated Apr 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/queues/observability/metrics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMetrics Backlog Consumer concurrency Message operations Realtime backlogExample GraphQL Queries Get average queue backlog over time period Get average consumer concurrency by hour Get message operations by minute

Queues expose metrics which allow you to measure the queue backlog, consumer concurrency, and message operations.

The metrics displayed in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) are queried from Cloudflare’s [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/). You can access the metrics programmatically via GraphQL or HTTP client.

## Metrics

### Backlog

Queues export the below metrics within the `queuesBacklogAdaptiveGroups` dataset.

Metric | GraphQL Field Name | Description  
---|---|---  
Backlog bytes | `bytes` | Average size of the backlog, in bytes  
Backlog messages | `messages` | Average size of the backlog, in number of messages  
  
The `queuesBacklogAdaptiveGroups` dataset provides the following dimensions for filtering and grouping queries:

  * `queueID` \- ID of the queue
  * `datetime` \- Timestamp for when the message was sent
  * `date` \- Timestamp for when the message was sent, truncated to the start of a day
  * `datetimeHour` \- Timestamp for when the message was sent, truncated to the start of an hour
  * `datetimeMinute` \- Timestamp for when the message was sent, truncated to the start of a minute



### Consumer concurrency

Queues export the below metrics within the `queueConsumerMetricsAdaptiveGroups` dataset.

Metric | GraphQL Field Name | Description  
---|---|---  
Avg. Consumer Concurrency | `concurrency` | Average number of concurrent consumers over the period  
  
The `queueConsumerMetricsAdaptiveGroups` dataset provides the following dimensions for filtering and grouping queries:

  * `queueID` \- ID of the queue
  * `datetime` \- Timestamp for the consumer metrics
  * `date` \- Timestamp for the consumer metrics, truncated to the start of a day
  * `datetimeHour` \- Timestamp for the consumer metrics, truncated to the start of an hour
  * `datetimeMinute` \- Timestamp for the consumer metrics, truncated to the start of a minute



### Message operations

Queues export the below metrics within the `queueMessageOperationsAdaptiveGroups` dataset.

Metric | GraphQL Field Name | Description  
---|---|---  
Total billable operations | `billableOperations` | Sum of billable operations (writes, reads, and deletes) over the time period  
Total Bytes | `bytes` | Sum of bytes read, written, and deleted from the queue  
Lag | `lagTime` | Average lag time in milliseconds between when the message was written and the operation to consume the message.  
Retries | `retryCount` | Average number of retries per message  
Message Size | `messageSize` | Maximum message size over the specified period  
  
The `queueMessageOperationsAdaptiveGroups` dataset provides the following dimensions for filtering and grouping queries:

  * `queueID` \- ID of the queue
  * `actionType` \- The type of message operation. Can be `WriteMessage`, `ReadMessage` or `DeleteMessage`
  * `consumerType` \- The queue consumer type. Can be `worker` or `http`. Only applicable for `ReadMessage` and `DeleteMessage` action types
  * `outcome` \- The outcome of the message operation. Only applicable for `DeleteMessage` action types. Can be `success`, `dlq` or `fail`.
  * `datetime` \- Timestamp for the message operation
  * `date` \- Timestamp for the message operation, truncated to the start of a day
  * `datetimeHour` \- Timestamp for the message operation, truncated to the start of an hour
  * `datetimeMinute` \- Timestamp for the message operation, truncated to the start of a minute



### Realtime backlog

You can access realtime backlog metrics via the [Queues REST API](https://developers.cloudflare.com/api/resources/queues/) and [JavaScript API](https://developers.cloudflare.com/queues/configuration/javascript-apis/). These metrics provide point-in-time values rather than aggregated data.

Metric | Field Name | Description  
---|---|---  
Backlog count | `backlog_count` | Number of messages currently in the queue  
Backlog bytes | `backlog_bytes` | Total size of messages in the queue, in bytes  
Oldest message timestamp | `oldest_message_timestamp_ms` | Timestamp (in milliseconds) of the oldest message in the queue  
  
To retrieve these metrics via the REST API, use the metrics endpoint (`/accounts/{account_id}/queues/{queue_id}/metrics`).

These fields are also included in `metadata.metrics` when calling `send()`, `sendBatch()`, or `metrics()` via the JavaScript API.

## Example GraphQL Queries

### Get average queue backlog over time period
    
    
    query QueueBacklog(
    	$accountTag: string!
    	$queueId: string!
    	$datetimeStart: Time!
    	$datetimeEnd: Time!
    ) {
    	viewer {
    		accounts(filter: { accountTag: $accountTag }) {
    			queueBacklogAdaptiveGroups(
    				limit: 10000
    				filter: {
    					queueId: $queueId
    					datetime_geq: $datetimeStart
    					datetime_leq: $datetimeEnd
    				}
    			) {
    				avg {
    					messages
    					bytes
    				}
    			}
    		}
    	}
    }

### Get average consumer concurrency by hour
    
    
    query QueueConcurrencyByHour(
    	$accountTag: string!
    	$queueId: string!
    	$datetimeStart: Time!
    	$datetimeEnd: Time!
    ) {
    	viewer {
    		accounts(filter: { accountTag: $accountTag }) {
    			queueConsumerMetricsAdaptiveGroups(
    				limit: 10000
    				filter: {
    					queueId: $queueId
    					datetime_geq: $datetimeStart
    					datetime_leq: $datetimeEnd
    				}
    				orderBy: [datetimeHour_DESC]
    			) {
    				avg {
    					concurrency
    				}
    				dimensions {
    					datetimeHour
    				}
    			}
    		}
    	}
    }

### Get message operations by minute
    
    
    query QueueMessageOperationsByMinute(
    	$accountTag: string!
    	$queueId: string!
    	$datetimeStart: Date!
    	$datetimeEnd: Date!
    ) {
    	viewer {
    		accounts(filter: { accountTag: $accountTag }) {
    			queueMessageOperationsAdaptiveGroups(
    				limit: 10000
    				filter: {
    					queueId: $queueId
    					datetime_geq: $datetimeStart
    					datetime_leq: $datetimeEnd
    				}
    				orderBy: [datetimeMinute_DESC]
    			) {
    				count
    				sum {
    					bytes
    				}
    				dimensions {
    					datetimeMinute
    				}
    			}
    		}
    	}
    }

[PreviousEvents & schemas](https://developers.cloudflare.com/queues/event-subscriptions/events-schemas/)[NextOverview](https://developers.cloudflare.com/queues/examples/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/queues/observability/metrics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
