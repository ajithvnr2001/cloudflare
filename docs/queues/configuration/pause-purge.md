---
url: https://developers.cloudflare.com/queues/configuration/pause-purge/
title: Pause and Purge \u00b7 Cloudflare Queues docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:40.351599+00:00
---

# Pause and Purge · Cloudflare Queues docs

> Source: https://developers.cloudflare.com/queues/configuration/pause-purge/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Queues](https://developers.cloudflare.com/queues/)
  3. /[Configuration](https://developers.cloudflare.com/queues/configuration/)
  4. /Pause and Purge



# Pause and Purge

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/queues/configuration/pause-purge/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPause Delivery Pause and resume delivery using Wrangler What happens to HTTP Pull consumers with a paused queue?Purge queue Purge queue using Wrangler Does purging a Queue affect my bill?

## Pause Delivery

You can pause delivery of messages from your queue to any connected consumers. Pausing a queue is useful when managing downtime (for example, if your consumer Worker is unhealthy) without losing any messages.

Queues continue to receive and store messages even while delivery is paused. Messages in a paused queue are still subject to expiry, if the messages become older than the queue message retention period.

Pausing affects both [push-based consumer Workers](https://developers.cloudflare.com/queues/reference/how-queues-works#consumers) and [pull based consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers).

### Pause and resume delivery using Wrangler

The following command will pause message delivery from your queue:
    
    
    $ npx wrangler queues pause-delivery <QUEUE-NAME>

  * `queue-name` `string` required
    * The name of the queue for which delivery should be paused.



The following command will resume message delivery:
    
    
    $ npx wrangler queues resume-delivery <QUEUE-NAME>

  * `queue-name` `string` required
    * The name of the queue for which delivery should be resumed.



### What happens to HTTP Pull consumers with a paused queue?

When a queue is paused, messages cannot be pulled by an [HTTP pull based consumer](https://developers.cloudflare.com/queues/configuration/pull-consumers). Requests to pull messages will receive a `409` response, along with an error message stating `queue_delivery_paused`.

## Purge queue

Purging a queue permanently deletes any messages currently stored in the Queue. Purging is useful while developing a new application, especially to clear out any test data. It can also be useful in production to handle scenarios when a batch of bad messages have been sent to a Queue.

Note that any in flight messages, which are currently being processed by consumers, might still be processed. Messages sent to a queue during a purge operation might not be purged. Any delayed messages will also be deleted from the queue.

Caution

Purging a queue is an irreversible operation. Make sure to use this operation carefully.

### Purge queue using Wrangler

The following command will purge messages from your queue. You will be prompted to enter the queue name to confirm the operation.
    
    
    $ npx wrangler queues purge <QUEUE-NAME>
    
    This operation will permanently delete all the messages in Queue <QUEUE-NAME>. Type <QUEUE-NAME> to proceed.

### Does purging a Queue affect my bill?

Purging a queue counts as a single billable operation, regardless of how many messages are deleted. For example, if you purge a queue which has 100 messages, all 100 messages will be permanently deleted, and you will be billed for 1 billable operation. Refer to the [pricing](https://developers.cloudflare.com/queues/platform/pricing) page for more information about how Queues is billed.

[PreviousBatching, Retries and Delays](https://developers.cloudflare.com/queues/configuration/batching-retries/)[NextDead Letter Queues](https://developers.cloudflare.com/queues/configuration/dead-letter-queues/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/queues/configuration/pause-purge.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
