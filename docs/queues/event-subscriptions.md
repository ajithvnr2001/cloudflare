---
url: https://developers.cloudflare.com/queues/event-subscriptions/
title: Event subscriptions overview \u00b7 Cloudflare Queues docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:40.256159+00:00
---

# Event subscriptions overview · Cloudflare Queues docs

> Source: https://developers.cloudflare.com/queues/event-subscriptions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Queues](https://developers.cloudflare.com/queues/)
  3. /Event subscriptions



# Event subscriptions

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/queues/event-subscriptions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat is an event?Learn more

Event subscriptions allow you to receive messages when events occur across your Cloudflare account. Cloudflare products (e.g., [KV](https://developers.cloudflare.com/kv/), [Workers AI](https://developers.cloudflare.com/workers-ai), [Workers](https://developers.cloudflare.com/workers)) can publish structured events to a queue, which you can then consume with Workers or [HTTP pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers/) to build custom workflows, integrations, or logic.

![Event subscriptions architecture](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=924,height=403,format=webp/_astro/queues-event-subscriptions.3aVidnXJ.png)

## What is an event?

An event is a structured record of something happening in your Cloudflare account – like a Workers AI batch request being queued, a Worker build completing, or an R2 bucket being created. When you subscribe to these events, your queue will automatically start receiving messages when the events occur.

## Learn more

### [Manage event subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/)

Learn how to create, configure, and manage event subscriptions for your queues.

### [Events & schemas](https://developers.cloudflare.com/queues/event-subscriptions/events-schemas/)

Explore available event types and their corresponding data schemas.

[PreviousR2 Event Notifications ↗︎](https://developers.cloudflare.com/r2/buckets/event-notifications/)[NextManage event subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/queues/event-subscriptions/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
