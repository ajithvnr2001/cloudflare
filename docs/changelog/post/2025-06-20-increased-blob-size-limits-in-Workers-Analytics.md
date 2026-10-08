---
url: https://developers.cloudflare.com/changelog/post/2025-06-20-increased-blob-size-limits-in-Workers-Analytics/
title: Increased blob size limits in Workers Analytics Engine \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:14.905517+00:00
---

# Increased blob size limits in Workers Analytics Engine · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-20-increased-blob-size-limits-in-Workers-Analytics/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 20, 2025

## Increased blob size limits in Workers Analytics Engine

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-20-increased-blob-size-limits-in-Workers-Analytics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We’ve increased the total allowed size of [`blob`](https://developers.cloudflare.com/analytics/analytics-engine/get-started/#2-write-data-points-from-your-worker) fields on data points written to [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) from **5 KB to 16 KB**.

This change gives you more flexibility when logging rich observability data — such as base64-encoded payloads, AI inference traces, or custom metadata — without hitting request size limits.

You can find full details on limits for queries, filters, payloads, and more [here in the Workers Analytics Engine limits documentation](https://developers.cloudflare.com/analytics/analytics-engine/limits/).
    
    
    export default {
    	async fetch(request, env) {
    		env.analyticsDataset.writeDataPoint({
    			// The sum of all of the blob's sizes can now be 16 KB
    			blobs: [
    				// The URL of the request to the Worker
    				request.url,
    				// Some metadata about your application you'd like to store
    				JSON.stringify(metadata),
    				// The version of your Worker this datapoint was collected from
    				env.versionMetadata.tag,
    			],
    			indexes: ["sample-index"],
    		});
    	},
    };

worker.tsts
    
    
    export default {
    	async fetch(request, env) {
    		env.analyticsDataset.writeDataPoint({
    			// The sum of all of the blob's sizes can now be 16 KB
    			blobs: [
    				// The URL of the request to the Worker
    				request.url,
    				// Some metadata about your application you'd like to store
    				JSON.stringify(metadata),
    				// The version of your Worker this datapoint was collected from
    				env.versionMetadata.tag,
    			],
    			indexes: ["sample-index"],
    		});
    	}
    };
