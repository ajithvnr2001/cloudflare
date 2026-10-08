---
url: https://developers.cloudflare.com/changelog/post/2025-08-19-event-subscriptions/
title: Subscribe to events from Cloudflare services with Queues \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:19.887136+00:00
---

# Subscribe to events from Cloudflare services with Queues · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-19-event-subscriptions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 19, 2025

## Subscribe to events from Cloudflare services with Queues

[Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-19-event-subscriptions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now subscribe to events from other Cloudflare services (for example, [Workers KV](https://developers.cloudflare.com/kv/), [Workers AI](https://developers.cloudflare.com/workers-ai), [Workers](https://developers.cloudflare.com/workers)) and consume those events via [Queues](https://developers.cloudflare.com/queues/), allowing you to build custom workflows, integrations, and logic in response to account activity.

![Event subscriptions architecture](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=924,height=403,format=webp/_astro/queues-event-subscriptions.3aVidnXJ.png)

Event subscriptions allow you to receive messages when events occur across your Cloudflare account. Cloudflare products can publish structured events to a queue, which you can then consume with [Workers](https://developers.cloudflare.com/workers/) or [pull via HTTP from anywhere](https://developers.cloudflare.com/queues/configuration/pull-consumers/).

To create a subscription, use the dashboard or [Wrangler](https://developers.cloudflare.com/workers/wrangler/commands/queues/#queues-subscription-create):
    
    
    npx wrangler queues subscription create my-queue --source r2 --events bucket.created

An event is a structured record of something happening in your Cloudflare account – like a Workers AI batch request being queued, a Worker build completing, or an R2 bucket being created. Events follow a consistent structure:

Example R2 bucket created eventjson
    
    
    {
      "type": "cf.r2.bucket.created",
      "source": {
        "type": "r2"
      },
      "payload": {
        "name": "my-bucket",
        "location": "WNAM"
      },
      "metadata": {
        "accountId": "f9f79265f388666de8122cfb508d7776",
        "eventTimestamp": "2025-07-28T10:30:00Z"
      }
    }

Current [event sources](https://developers.cloudflare.com/queues/event-subscriptions/events-schemas/) include [R2](https://developers.cloudflare.com/r2/), [Workers KV](https://developers.cloudflare.com/kv/), [Workers AI](https://developers.cloudflare.com/workers-ai/), [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/), [Vectorize](https://developers.cloudflare.com/vectorize/), [Super Slurper](https://developers.cloudflare.com/r2/data-migration/super-slurper/), and [Workflows](https://developers.cloudflare.com/workflows/). More sources and events are on the way.

For more information on event subscriptions, available events, and how to get started, refer to our [documentation](https://developers.cloudflare.com/queues/event-subscriptions/).
