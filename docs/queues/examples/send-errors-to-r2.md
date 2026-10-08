---
url: https://developers.cloudflare.com/queues/examples/send-errors-to-r2/
title: Cloudflare Queues - Queues & R2 \u00b7 Cloudflare Queues docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:41.059360+00:00
---

# Cloudflare Queues - Queues & R2 · Cloudflare Queues docs

> Source: https://developers.cloudflare.com/queues/examples/send-errors-to-r2/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Queues](https://developers.cloudflare.com/queues/)
  3. /[Examples](https://developers.cloudflare.com/queues/examples/)
  4. /Use Queues to store data in R2



# Use Queues to store data in R2

Example of how to use Queues to batch data and store it in an R2 bucket.

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/queues/examples/send-errors-to-r2/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following Worker will catch JavaScript errors and send them to a queue. The same Worker will receive those errors in batches and store them to a log file in an R2 bucket.
    
    
    {
    	"$schema": "./node_modules/wrangler/config-schema.json",
    	"name": "my-worker",
    	"queues": {
    		"producers": [
    			{
    				"queue": "my-queue",
    				"binding": "ERROR_QUEUE"
    			}
    		],
    		"consumers": [
    			{
    				"queue": "my-queue",
    				"max_batch_size": 100,
    				"max_batch_timeout": 30
    			}
    		]
    	},
    	"r2_buckets": [
    		{
    			"bucket_name": "my-bucket",
    			"binding": "ERROR_BUCKET"
    		}
    	]
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "my-worker"
    
    [[queues.producers]]
    queue = "my-queue"
    binding = "ERROR_QUEUE"
    
    [[queues.consumers]]
    queue = "my-queue"
    max_batch_size = 100
    max_batch_timeout = 30
    
    [[r2_buckets]]
    bucket_name = "my-bucket"
    binding = "ERROR_BUCKET"
    
    
    interface ErrorMessage {
    	message: string;
    	stack?: string;
    }
    
    interface Env {
    	readonly ERROR_QUEUE: Queue<ErrorMessage>;
    	readonly ERROR_BUCKET: R2Bucket;
    }
    
    export default {
      async fetch(req, env, ctx): Promise<Response> {
        try {
          return doRequest(req);
        } catch (e) {
          const error: ErrorMessage = {
            message: e instanceof Error ? e.message : String(e),
            stack: e instanceof Error ? e.stack : undefined,
          };
          await env.ERROR_QUEUE.send(error);
          return new Response(error.message, { status: 500 });
        }
      },
      async queue(batch, env, ctx): Promise<void> {
        let file = "";
        for (const message of batch.messages) {
          const error = message.body;
          file += error.stack ?? error.message;
          file += "\r\n";
        }
        await env.ERROR_BUCKET.put(`errors/${Date.now()}.log`, file);
      },
    } satisfies ExportedHandler<Env, ErrorMessage>;
    
    function doRequest(request: Request): Response {
      if (Math.random() > 0.5) {
        return new Response("Success!");
      }
      throw new Error("Failed!");
    }

[PreviousPublish to a Queue via HTTP](https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/)[NextSend messages from the dashboard](https://developers.cloudflare.com/queues/examples/send-messages-from-dash/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/queues/examples/send-errors-to-r2.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
