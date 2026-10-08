---
url: https://developers.cloudflare.com/queues/configuration/dead-letter-queues/
title: Dead Letter Queues \u00b7 Cloudflare Queues docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:39.909001+00:00
---

# Dead Letter Queues · Cloudflare Queues docs

> Source: https://developers.cloudflare.com/queues/configuration/dead-letter-queues/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Queues](https://developers.cloudflare.com/queues/)
  3. /[Configuration](https://developers.cloudflare.com/queues/configuration/)
  4. /Dead Letter Queues



# Dead Letter Queues

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/queues/configuration/dead-letter-queues/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A Dead Letter Queue (DLQ) is a common concept in a messaging system, and represents where messages are sent when a delivery failure occurs with a consumer after `max_retries` is reached. A Dead Letter Queue is like any other queue, and can be produced to and consumed from independently.

With Cloudflare Queues, a Dead Letter Queue is defined within your [consumer configuration](https://developers.cloudflare.com/queues/configuration/configure-queues/). Messages are delivered to the DLQ when they reach the configured retry limit for the consumer. Without a DLQ configured, messages that reach the retry limit are deleted permanently.

For example, the following consumer configuration would send messages to our DLQ named `"my-other-queue"` after retrying delivery (by default, 3 times):
    
    
    {
    	"queues": {
    		"consumers": [
    			{
    				"queue": "my-queue",
    				"dead_letter_queue": "my-other-queue"
    			}
    		]
    	}
    }
    
    
    [[queues.consumers]]
    queue = "my-queue"
    dead_letter_queue = "my-other-queue"

You can also configure a DLQ when creating a consumer from the command-line using `wrangler`:
    
    
    wrangler queues consumer add $QUEUE_NAME $SCRIPT_NAME --dead-letter-queue=$NAME_OF_OTHER_QUEUE

To process messages placed on your DLQ, you need to [configure a consumer](https://developers.cloudflare.com/queues/configuration/configure-queues/) for that queue as you would with any other queue.

Messages delivered to a DLQ without an active consumer will persist for four (4) days before being deleted from the queue.

[PreviousPause and Purge](https://developers.cloudflare.com/queues/configuration/pause-purge/)[NextPull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/queues/configuration/dead-letter-queues.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
