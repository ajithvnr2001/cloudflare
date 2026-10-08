---
url: https://developers.cloudflare.com/durable-objects/observability/metrics-and-analytics/
title: Metrics and analytics \u00b7 Cloudflare Durable Objects docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:09.430934+00:00
---

# Metrics and analytics · Cloudflare Durable Objects docs

> Source: https://developers.cloudflare.com/durable-objects/observability/metrics-and-analytics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Durable Objects](https://developers.cloudflare.com/durable-objects/)
  3. /Observability
  4. /Metrics and analytics



# Metrics and analytics

Last updated Jun 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/durable-objects/observability/metrics-and-analytics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewView metrics and analyticsMemory usageView logsQuery via the GraphQL API WebSocket metricsExample GraphQL query for Durable ObjectsAdditional resourcesFAQs How can I identify which Durable Object instance generated a log entry?

Durable Objects expose analytics for Durable Object namespace-level and request-level metrics.

The metrics displayed in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) charts are queried from Cloudflare's [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/). You can access the metrics programmatically via GraphQL or HTTP client.

Durable Object namespace

A Durable Object namespace is a set of Durable Objects that can be addressed by name, backed by the same class. There is only one Durable Object namespace per class. A Durable Object namespace can contain any number of Durable Objects.

## View metrics and analytics

Per-namespace analytics for Durable Objects are available in the Cloudflare dashboard. To view current and historical metrics for a namespace:

  1. In the Cloudflare dashboard, go to the **Durable Objects** page.

[ Go to **Durable Objects** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/durable-objects)
  2. View account-level Durable Objects usage.

  3. Select an existing Durable Object namespace.

  4. Select the **Metrics** tab.




You can optionally select a time window to query. This defaults to the last 24 hours.

You can also filter the charts to a single Durable Object by entering its [ID](https://developers.cloudflare.com/durable-objects/api/id/) or [name](https://developers.cloudflare.com/durable-objects/api/id/#name) and selecting a match. Clear the filter to return to namespace-level metrics.

## Memory usage

The **Memory usage** chart on the **Metrics** tab shows V8 [isolate](https://developers.cloudflare.com/workers/reference/how-workers-works/#isolates) memory usage, sampled periodically while your Durable Objects are active, broken down into P50, P90, P99, and P999 percentiles. Each isolate is subject to a [128 MB memory limit](https://developers.cloudflare.com/workers/platform/limits/#memory).

This memory holds the in-memory state your objects accumulate — such as class properties, caches, and active WebSocket connections — which persists across requests until an object is [hibernated or evicted](https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/). This state is not preserved across eviction, hibernation, or a crash, so persist anything important to [storage](https://developers.cloudflare.com/durable-objects/best-practices/access-durable-objects-storage/).

Memory is measured per isolate, not per Durable Object

A single isolate can host multiple Durable Objects of the same class, along with the surrounding Worker code, and they all share that isolate's memory. The chart always reports the memory of the whole isolate, not an individual Durable Object.

What the chart shows depends on whether you filter:

  * **Without a filter (namespace view):** the percentiles are computed across the periodic memory samples of every Durable Object in the namespace, showing the distribution of isolate memory across the namespace.
  * **Filtered by[ID](https://developers.cloudflare.com/durable-objects/api/id/) or [name](https://developers.cloudflare.com/durable-objects/api/id/#name):** the percentiles are computed only from the periodic samples reported for that one Durable Object. Each sample is still the memory of the entire isolate hosting it — which may include other Durable Objects sharing that isolate — so this is not a measurement of that single object's memory in isolation.



Memory usage is powered by the `durableObjectsPeriodicGroups` GraphQL dataset, which exposes the `memoryUsageBytes` metric. Percentile values are available as `quantiles.memoryUsageBytesP50` through `quantiles.memoryUsageBytesP999`, in bytes.

If you see memory usage trending upward over time, this may indicate a memory leak. Use [memory profiling with DevTools](https://developers.cloudflare.com/workers/observability/dev-tools/memory-usage/) locally to take heap snapshots and identify specific objects causing high memory consumption.

## View logs

You can view Durable Object logs from the Cloudflare dashboard. Logs are aggregated by the script name and the Durable Object class name.

To start using Durable Object logging:

  1. Enable Durable Object logging in the Wrangler configuration file of the Worker that defines your Durable Object class:
         
         {
             "observability": {
                 "enabled": true
             }
         }
         
         [observability]
         enabled = true

  2. Deploy the latest version of the Worker with the updated binding.

  3. Go to the **Durable Objects** page.

[ Go to **Durable Objects** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/durable-objects)
  4. Select an existing Durable Object namespace.

  5. Select the **Logs** tab.




Note

For information on log limits (such as maximum log retention period), refer to the [Workers Logs documentation](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#limits).

## Query via the GraphQL API

Durable Object metrics are powered by GraphQL.

The datasets that include Durable Object metrics include:

  * `durableObjectsInvocationsAdaptiveGroups`
  * `durableObjectsPeriodicGroups`
  * `durableObjectsStorageGroups`
  * `durableObjectsSubrequestsAdaptiveGroups`



Use [GraphQL Introspection](https://developers.cloudflare.com/analytics/graphql-api/features/discovery/introspection/) to get information on the fields exposed by each datasets.

### WebSocket metrics

Durable Objects using [WebSockets](https://developers.cloudflare.com/durable-objects/best-practices/websockets/) will see request metrics across several GraphQL datasets because WebSockets have different types of requests.

  * Metrics for a WebSocket connection itself is represented in `durableObjectsInvocationsAdaptiveGroups` once the connection closes. Since WebSocket connections are long-lived, connections often do not terminate until the Durable Object terminates.
  * Metrics for incoming and outgoing WebSocket messages on a WebSocket connection are available in `durableObjectsPeriodicGroups`. If a WebSocket connection uses [WebSocket Hibernation](https://developers.cloudflare.com/durable-objects/best-practices/websockets/#durable-objects-hibernation-websocket-api), incoming WebSocket messages are instead represented in `durableObjectsInvocationsAdaptiveGroups`.



## Example GraphQL query for Durable Objects
    
    
      viewer {
        /*
        Replace with your account tag, the 32 hex character id visible at the beginning of any url
        when logged in to dash.cloudflare.com or under "Account ID" on the sidebar of the Workers & Pages Overview
        */
        accounts(filter: {accountTag: "your account tag here"}) {
          // Replace dates with a recent date
          durableObjectsInvocationsAdaptiveGroups(filter: {date_gt: "2023-05-23"}, limit: 1000) {
            sum {
              // Any other fields found through introspection can be added here
              requests
              responseBodySize
            }
          }
          durableObjectsPeriodicGroups(filter: {date_gt: "2023-05-23"}, limit: 1000) {
            sum {
              cpuTime
            }
          }
          durableObjectsStorageGroups(filter: {date_gt: "2023-05-23"}, limit: 1000) {
            max {
              storedBytes
            }
          }
        }
      }

Refer to the [Querying Workers Metrics with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-workers-metrics/) tutorial for authentication and to learn more about querying Workers datasets.

## Additional resources

  * For instructions on setting up a Grafana dashboard to query Cloudflare's GraphQL Analytics API, refer to [Grafana Dashboard starter for Durable Object metrics ↗︎](https://github.com/TimoWilhelm/grafana-do-dashboard).



## FAQs

### How can I identify which Durable Object instance generated a log entry?

Durable Object request logs include the instance ID in `$workers.durableObjectId`. Filter on this field to isolate a specific instance for debugging.

[PreviousTroubleshooting](https://developers.cloudflare.com/durable-objects/observability/troubleshooting/)[NextData Studio](https://developers.cloudflare.com/durable-objects/observability/data-studio/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/durable-objects/observability/metrics-and-analytics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
