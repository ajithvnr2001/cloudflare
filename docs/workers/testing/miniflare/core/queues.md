---
url: https://developers.cloudflare.com/workers/testing/miniflare/core/queues/
title: Queues \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:54.796797+00:00
---

# Queues · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/miniflare/core/queues/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)[Miniflare](https://developers.cloudflare.com/workers/testing/miniflare/)

  4. /Core
  5. /Queues



# Queues

Last updated Jan 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/miniflare/core/queues/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewProducersConsumersManipulating Outside Workers

  * [Queues Reference](https://developers.cloudflare.com/queues/)



## Producers

Specify Queue producers to add to your environment as follows:
    
    
    const mf = new Miniflare({
    	queueProducers: { MY_QUEUE: "my-queue" },
    	queueProducers: ["MY_QUEUE"], // If binding and queue names are the same
    });

## Consumers

Specify Workers to consume messages from your Queues as follows:
    
    
    const mf = new Miniflare({
    	queueConsumers: {
    		"my-queue": {
    			maxBatchSize: 5, // default: 5
    			maxBatchTimeout: 1 /* second(s) */, // default: 1
    			maxRetries: 2, // default: 2
    			deadLetterQueue: "my-dead-letter-queue", // default: none
    		},
    	},
    	queueConsumers: ["my-queue"], // If using default consumer options
    });

## Manipulating Outside Workers

For testing, it can be valuable to interact with Queues outside a Worker. You can do this by using the `workers` option to run multiple Workers in the same instance:
    
    
    const mf = new Miniflare({
    	workers: [
    		{
    			name: "a",
    			modules: true,
    			script: `
    			export default {
    				async fetch(request, env, ctx) {
    					await env.QUEUE.send(await request.text());
    				}
    			}
    			`,
    			queueProducers: { QUEUE: "my-queue" },
    		},
    		{
    			name: "b",
    			modules: true,
    			script: `
    			export default {
    				async queue(batch, env, ctx) {
    					console.log(batch);
    				}
    			}
    			`,
    			queueConsumers: { "my-queue": { maxBatchTimeout: 1 } },
    		},
    	],
    });
    
    const queue = await mf.getQueueProducer("QUEUE", "a"); // Get from worker "a"
    await queue.send("message"); // Logs "message" 1 second later

[PreviousMultiple Workers](https://developers.cloudflare.com/workers/testing/miniflare/core/multiple-workers/)[NextScheduled Events](https://developers.cloudflare.com/workers/testing/miniflare/core/scheduled/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/miniflare/core/queues.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
