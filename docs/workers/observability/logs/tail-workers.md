---
url: https://developers.cloudflare.com/workers/observability/logs/tail-workers/
title: Tail Workers \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:35.729517+00:00
---

# Tail Workers · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/observability/logs/tail-workers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Observability](https://developers.cloudflare.com/workers/observability/)

  4. /[Logs](https://developers.cloudflare.com/workers/observability/logs/)
  5. /Tail Workers



# Tail Workers

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/observability/logs/tail-workers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure Tail WorkersUse Analytics Engine for aggregated metricsRelated resources

A Tail Worker receives information about the execution of other Workers (known as producer Workers), such as HTTP statuses, data passed to `console.log()` or uncaught exceptions. Tail Workers can process logs for alerts, debugging, or analytics.

Tail Workers are available to all customers on the Workers Paid and Enterprise tiers. Tail Workers are billed by [CPU time](https://developers.cloudflare.com/workers/platform/pricing/#workers), not by the number of requests.

![Tail Worker diagram](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1280,height=532,format=webp/_astro/tail-workers.CaYo-ajt.png)

A Tail Worker is automatically invoked after the invocation of a producer Worker (the Worker the Tail Worker will track) that contains the application logic. It captures events after the producer has finished executing. Events throughout the request lifecycle, including potential sub-requests via [Service Bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) and [Dynamic Dispatch](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/), will be included. You can filter, change the format of the data, and send events to any HTTP endpoint. For quick debugging, Tail Workers can be used to send logs to [KV](https://developers.cloudflare.com/kv/api/) or any database.

Export batches of logs and traces to Sentry, Grafana, Honeycomb and more

If you are using Tail Workers to export logs and errors to observability tools like Sentry, Grafana, Honeycomb and more — you may not need to use Tail Workers.

Instead, you can configure your Worker to [export OpenTelemetry logs and traces](https://developers.cloudflare.com/workers/observability/opentelemetry-export/) to these tools. Unlike Tail Workers, an OpenTelemetry destination receives logs and traces in batches rather than after each Worker invocation.

You should think of Tail Workers as the advanced-mode option, for when you need to do something custom that is not built into the Workers observability platform.

## Configure Tail Workers

To configure a Tail Worker:

  1. [Create a Worker](https://developers.cloudflare.com/workers/get-started/guide) to serve as the Tail Worker.
  2. Add a [`tail()`](https://developers.cloudflare.com/workers/runtime-apis/handlers/tail/) handler to your Worker. The `tail()` handler is invoked every time the producer Worker to which a Tail Worker is connected is invoked. The following Worker code is a Tail Worker that sends its data to an HTTP endpoint:


    
    
    export default {
    	async tail(events) {
    		fetch("https://example.com/endpoint", {
    			method: "POST",
    			body: JSON.stringify(events),
    		});
    	},
    };

The following Worker code is an example of what the `events` object may look like:
    
    
    [
    	{
    		"scriptName": "Example script",
    		"outcome": "exception",
    		"eventTimestamp": 1587058642005,
    		"event": {
    			"request": {
    				"url": "https://example.com/some/requested/url",
    				"method": "GET",
    				"headers": {
    					"cf-ray": "57d55f210d7b95f3",
    					"x-custom-header-name": "my-header-value"
    				},
    				"cf": {
    					"colo": "SJC"
    				}
    			}
    		},
    		"logs": [
    			{
    				"message": ["string passed to console.log()"],
    				"level": "log",
    				"timestamp": 1587058642005
    			}
    		],
    		"exceptions": [
    			{
    				"name": "Error",
    				"message": "Threw a sample exception",
    				"timestamp": 1587058642005
    			}
    		],
    		"diagnosticsChannelEvents": [
    			{
    				"channel": "foo",
    				"message": "The diagnostic channel message",
    				"timestamp": 1587058642005
    			}
    		]
    	}
    ]

  3. Add the following to the Wrangler file of the producer Worker:


    
    
    {
    	"tail_consumers": [
    		{
    			"service": "<TAIL_WORKER_NAME>"
    		}
    	]
    }
    
    
    [[tail_consumers]]
    service = "<TAIL_WORKER_NAME>"

Note

Workers added to the `tail_consumers` array must have a `tail()` handler defined.

## Use Analytics Engine for aggregated metrics

If you need aggregated analytics rather than individual log events, consider writing to [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) from your Tail Worker. Analytics Engine is optimized for high-cardinality, time-series data that you can query with SQL.

For example, you can use a Tail Worker to count errors by endpoint, track response times by customer, or build usage metrics, then write those aggregates to Analytics Engine for querying and visualization.
    
    
    export default {
    	async tail(events, env) {
    		for (const event of events) {
    			env.ANALYTICS.writeDataPoint({
    				blobs: [event.scriptName, event.outcome],
    				doubles: [1],
    				indexes: [event.event?.request?.cf?.colo ?? "unknown"],
    			});
    		}
    	},
    };

Refer to the [Analytics Engine documentation](https://developers.cloudflare.com/analytics/analytics-engine/) for more details on writing and querying data.

## Related resources

  * [`tail()`](https://developers.cloudflare.com/workers/runtime-apis/handlers/tail/) Handler API docs - Learn how to set up a `tail()` handler in your Worker.
  * [Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) \- Write custom analytics from your Worker for high-cardinality, time-series queries.
  * [Errors and exceptions](https://developers.cloudflare.com/workers/observability/errors/) \- Review common Workers errors.
  * [Local development](https://developers.cloudflare.com/workers/local-development/) \- Develop and test your Workers locally.
  * [Source maps and stack traces](https://developers.cloudflare.com/workers/observability/source-maps) \- Learn how to enable source maps and generate stack traces for Workers.



[PreviousReal-time logs](https://developers.cloudflare.com/workers/observability/logs/real-time-logs/)[NextWorkers Logpush](https://developers.cloudflare.com/workers/observability/logs/logpush/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/observability/logs/tail-workers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
