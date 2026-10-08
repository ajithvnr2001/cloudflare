---
url: https://developers.cloudflare.com/queues/reference/delivery-guarantees/
title: Delivery guarantees \u00b7 Cloudflare Queues docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:41.791338+00:00
---

# Delivery guarantees · Cloudflare Queues docs

> Source: https://developers.cloudflare.com/queues/reference/delivery-guarantees/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Queues](https://developers.cloudflare.com/queues/)
  3. /Reference
  4. /Delivery guarantees



# Delivery guarantees

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/queues/reference/delivery-guarantees/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Delivery guarantees define how strongly a messaging system enforces the delivery of messages it processes.

As you make stronger guarantees about message delivery, the system needs to perform more checks and acknowledgments to ensure that messages are delivered, or maintain state to ensure a message is only delivered the specified number of times. This increases the latency of the system and reduces the overall throughput of the system. Each message may require an additional internal acknowledgements, and an equivalent number of additional roundtrips, before it can be considered delivered.

  * **Queues provides _at least once_ delivery by default** in order to optimize for reliability.
  * This means that messages are guaranteed to be delivered at least once, and in rare occasions, may be delivered more than once.
  * For the majority of applications, this is the right balance between not losing any messages and minimizing end-to-end latency, as exactly once delivery incurs additional overheads in any messaging system.



In cases where processing the same message more than once would introduce unintended behaviour, generating a unique ID when writing the message to the queue and using that as the primary key on database inserts and/or as an idempotency key to de-duplicate the message after processing. For example, using this idempotency key as the ID in an upstream email API or payment API will allow those services to reject the duplicate on your behalf, without you having to carry additional state in your application.

[PreviousHow Queues Works](https://developers.cloudflare.com/queues/reference/how-queues-works/)[NextWrangler commands](https://developers.cloudflare.com/queues/reference/wrangler-commands/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/queues/reference/delivery-guarantees.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
