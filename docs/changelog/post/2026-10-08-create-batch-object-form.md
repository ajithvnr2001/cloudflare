---
url: https://developers.cloudflare.com/changelog/post/2026-10-08-create-batch-object-form/
title: Create Workflow instance batches by count or list \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:29.144920+00:00
---

# Create Workflow instance batches by count or list · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-08-create-batch-object-form/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 8, 2026

## Create Workflow instance batches by count or list

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[`createBatch()`](https://developers.cloudflare.com/workflows/build/workers-api/#createbatch) now accepts an options object that creates up to 100 Workflow instances in one call. The result lists the created instances and explains why any others were not created. To use this form in local development and get its types from `wrangler types`, use Wrangler 4.148.0 or later.

To create instances that share the same options, pass `count`. Each instance receives a generated ID:
    
    
    const result = await env.MY_WORKFLOW.createBatch({
    	count: 10,
    	params: { report: "daily" },
    });
    
    
    const result = await env.MY_WORKFLOW.createBatch({
    	count: 10,
    	params: { report: "daily" },
    });

To give each instance its own ID or options, pass `instances`:
    
    
    const { created, errors } = await env.MY_WORKFLOW.createBatch({
    	instances: [
    		{ id: "order-1", params: { orderId: 1 } },
    		{ id: "order-2", params: { orderId: 2 } },
    	],
    });
    
    for (const error of errors) {
    	console.log(error.index, error.id, error.code, error.message);
    }
    
    
    const { created, errors } = await env.MY_WORKFLOW.createBatch({
    	instances: [
    		{ id: "order-1", params: { orderId: 1 } },
    		{ id: "order-2", params: { orderId: 2 } },
    	],
    });
    
    for (const error of errors) {
    	console.log(error.index, error.id, error.code, error.message);
    }

`created` contains the created instances. `errors` contains each entry that was not created, identified by its position in the input. IDs that already exist and IDs repeated within the batch are reported as errors instead of being skipped silently.

Passing an array to `createBatch()` is deprecated. Existing code that uses the array form continues to work.

For more information, refer to [`createBatch`](https://developers.cloudflare.com/workflows/build/workers-api/#createbatch).
