---
url: https://developers.cloudflare.com/workers/examples/analytics-engine/
title: Write to Analytics Engine \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:19.794375+00:00
---

# Write to Analytics Engine · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/examples/analytics-engine/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Examples](https://developers.cloudflare.com/workers/examples/)
  4. /Analytics Engine



# Write to Analytics Engine

Write custom analytics events to Workers Analytics Engine.

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/examples/analytics-engine/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure the bindingWrite data pointsData point structureQuery your dataRelated resources

[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) provides time-series analytics at scale. Use it to track custom metrics, build usage-based billing, or understand service health on a per-customer basis.

Unlike logs, Analytics Engine is designed for aggregated queries over high-cardinality data. Writes are non-blocking and do not impact request latency.

## Configure the binding

Add an Analytics Engine dataset binding to your Wrangler configuration file. The dataset is created automatically when you first write to it.
    
    
    {
    	"analytics_engine_datasets": [
    		{
    			"binding": "ANALYTICS",
    			"dataset": "my_dataset",
    		},
    	],
    }
    
    
    [[analytics_engine_datasets]]
    binding = "ANALYTICS"
    dataset = "my_dataset"

## Write data points
    
    
    export default {
    	async fetch(request, env) {
    		const url = new URL(request.url);
    
    		// Write a page view event
    		env.ANALYTICS.writeDataPoint({
    			blobs: [
    				url.pathname,
    				request.headers.get("cf-connecting-country") ?? "unknown",
    			],
    			doubles: [1], // Count
    			indexes: [url.hostname], // Sampling key
    		});
    
    		// Write a response timing event
    		const start = Date.now();
    		const response = await fetch(request);
    		const duration = Date.now() - start;
    
    		env.ANALYTICS.writeDataPoint({
    			blobs: [url.pathname, response.status.toString()],
    			doubles: [duration],
    			indexes: [url.hostname],
    		});
    
    		// Writes are non-blocking - no need to await or use waitUntil()
    		return response;
    	},
    };
    
    
    interface Env {
    	ANALYTICS: AnalyticsEngineDataset;
    }
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const url = new URL(request.url);
    
    		// Write a page view event
    		env.ANALYTICS.writeDataPoint({
    			blobs: [
    				url.pathname,
    				request.headers.get("cf-connecting-country") ?? "unknown",
    			],
    			doubles: [1], // Count
    			indexes: [url.hostname], // Sampling key
    		});
    
    		// Write a response timing event
    		const start = Date.now();
    		const response = await fetch(request);
    		const duration = Date.now() - start;
    
    		env.ANALYTICS.writeDataPoint({
    			blobs: [url.pathname, response.status.toString()],
    			doubles: [duration],
    			indexes: [url.hostname],
    		});
    
    		// Writes are non-blocking - no need to await or use waitUntil()
    		return response;
    	},
    };

## Data point structure

Each data point consists of:

  * **blobs** (strings) - Dimensions for grouping and filtering. Use for paths, regions, status codes, or customer IDs.
  * **doubles** (numbers) - Numeric values to record, such as counts, durations, or sizes.
  * **indexes** (strings) - A single string used as the [sampling key](https://developers.cloudflare.com/analytics/analytics-engine/sql-api/#sampling). Group related events under the same index.



## Query your data

Query your data using the [SQL API](https://developers.cloudflare.com/analytics/analytics-engine/sql-api/):
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/analytics_engine/sql" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --data "SELECT blob1 AS path, SUM(_sample_interval) AS views FROM my_dataset WHERE timestamp > NOW() - INTERVAL '1' HOUR GROUP BY path ORDER BY views DESC LIMIT 10"

## Related resources

  * [Analytics Engine documentation](https://developers.cloudflare.com/analytics/analytics-engine/) \- Full reference for Workers Analytics Engine.
  * [SQL API reference](https://developers.cloudflare.com/analytics/analytics-engine/sql-api/) \- Query syntax and available functions.
  * [Grafana integration](https://developers.cloudflare.com/analytics/analytics-engine/grafana/) \- Visualize Analytics Engine data in Grafana.



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/examples/analytics-engine.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
