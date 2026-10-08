---
url: https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-workers/
title: Queues - Publish Directly via a Worker \u00b7 Cloudflare Queues docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:40.933407+00:00
---

# Queues - Publish Directly via a Worker · Cloudflare Queues docs

> Source: https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-workers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Queues](https://developers.cloudflare.com/queues/)
  3. /[Examples](https://developers.cloudflare.com/queues/examples/)
  4. /Publish to a Queue via Workers



# Publish to a Queue via Workers

Publish to a Queue directly from your Worker.

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-workers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites 1\. Create the Worker 2\. Send a test message

The following example shows you how to publish messages to a Queue from a Worker. The example uses a Worker that receives a JSON payload from the request body and writes it as-is to the Queue, but in a real application you might have more logic before you queue a message.

## Prerequisites

  * A [queue created](https://developers.cloudflare.com/queues/get-started/#3-create-a-queue) via the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) or the [wrangler CLI](https://developers.cloudflare.com/workers/wrangler/install-and-update/).
  * A [configured **producer** binding](https://developers.cloudflare.com/queues/configuration/configure-queues/#producer-worker-configuration) in the Cloudflare dashboard or Wrangler file.



Configure your Wrangler file as follows:
    
    
    {
    	"$schema": "./node_modules/wrangler/config-schema.json",
    	"name": "my-worker",
    	"queues": {
    		"producers": [
    			{
    				"queue": "my-queue",
    				"binding": "YOUR_QUEUE"
    			}
    		]
    	}
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "my-worker"
    
    [[queues.producers]]
    queue = "my-queue"
    binding = "YOUR_QUEUE"

### 1\. Create the Worker

The following Worker script:

  1. Validates that the request body is valid JSON.
  2. Publishes the payload to the queue.


    
    
    interface Env {
    	YOUR_QUEUE: Queue;
    }
    
    export default {
    	async fetch(req, env, ctx): Promise<Response> {
    		// Validate the payload is JSON
    		// In a production application, we may more robustly validate the payload
    		// against a schema using a library like 'zod'
    		let messages;
    		try {
    			messages = await req.json();
    		} catch {
    			// Return a HTTP 400 (Bad Request) if the payload isn't JSON
    			return Response.json({ error: "payload not valid JSON" }, { status: 400 });
    		}
    
    		// Publish to the Queue
    		try {
    			await env.YOUR_QUEUE.send(messages);
    		} catch (e) {
    			const message = e instanceof Error ? e.message : "Unknown error";
    			console.error(`failed to send to the queue: ${message}`);
    			// Return a HTTP 500 (Internal Error) if our publish operation fails
    			return Response.json({ error: message }, { status: 500 });
    		}
    
    		// Return a HTTP 200 if the send succeeded!
    		return Response.json({ success: true });
    	},
    } satisfies ExportedHandler<Env>;

To deploy this Worker:
    
    
    npx wrangler deploy

### 2\. Send a test message

To make sure you successfully write a message to your queue, use `curl` on the command line:
    
    
    # Make sure to replace the placeholder with your shared secret
    curl -XPOST "https://YOUR_WORKER.YOUR_ACCOUNT.workers.dev" --data '{"messages": [{"msg":"hello world"}]}'
    
    
    {"success":true}

This will issue a HTTP POST request, and if successful, return a HTTP 200 with a `success: true` response body.

  * If you receive a HTTP 400, this is because you attempted to send malformed JSON to your queue.
  * If you receive a HTTP 500, this is because the message was not written to your Queue successfully.



You can use [`wrangler tail`](https://developers.cloudflare.com/workers/observability/logs/real-time-logs/) to debug the output of `console.log`.

[PreviousUse Queues from Durable Objects](https://developers.cloudflare.com/queues/examples/use-queues-with-durable-objects/)[NextPublish to a Queue via HTTP](https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/queues/examples/publish-to-a-queue-via-workers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
