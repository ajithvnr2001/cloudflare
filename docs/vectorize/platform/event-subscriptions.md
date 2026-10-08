---
url: https://developers.cloudflare.com/vectorize/platform/event-subscriptions/
title: Event subscriptions \u00b7 Cloudflare Vectorize docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:13.835482+00:00
---

# Event subscriptions · Cloudflare Vectorize docs

> Source: https://developers.cloudflare.com/vectorize/platform/event-subscriptions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Vectorize](https://developers.cloudflare.com/vectorize/)
  3. /Platform
  4. /Event subscriptions



# Event subscriptions

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/vectorize/platform/event-subscriptions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailable Vectorize events

[Event subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/) allow you to receive messages when events occur across your Cloudflare account. Cloudflare products (e.g., [KV](https://developers.cloudflare.com/kv/), [Workers AI](https://developers.cloudflare.com/workers-ai/), [Workers](https://developers.cloudflare.com/workers/)) can publish structured events to a [queue](https://developers.cloudflare.com/queues/), which you can then consume with Workers or [HTTP pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers/) to build custom workflows, integrations, or logic.

For more information on [Event Subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/), refer to the [management guide](https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/).

## Available Vectorize events

#### `index.created`

Triggered when an index is created.

**Example:**
    
    
    {
      "type": "cf.vectorize.index.created",
      "source": {
        "type": "vectorize"
      },
      "payload": {
        "name": "my-vector-index",
        "description": "Index for embeddings",
        "createdAt": "2025-05-01T02:48:57.132Z",
        "modifiedAt": "2025-05-01T02:48:57.132Z",
        "dimensions": 1536,
        "metric": "cosine"
      },
      "metadata": {
        "accountId": "f9f79265f388666de8122cfb508d7776",
        "eventSubscriptionId": "1830c4bb612e43c3af7f4cada31fbf3f",
        "eventSchemaVersion": 1,
        "eventTimestamp": "2025-05-01T02:48:57.132Z"
      }
    }

#### `index.deleted`

Triggered when an index is deleted.

**Example:**
    
    
    {
      "type": "cf.vectorize.index.deleted",
      "source": {
        "type": "vectorize"
      },
      "payload": {
        "name": "my-vector-index"
      },
      "metadata": {
        "accountId": "f9f79265f388666de8122cfb508d7776",
        "eventSubscriptionId": "1830c4bb612e43c3af7f4cada31fbf3f",
        "eventSchemaVersion": 1,
        "eventTimestamp": "2025-05-01T02:48:57.132Z"
      }
    }

[PreviousChangelog](https://developers.cloudflare.com/vectorize/platform/changelog/)[NextVector databases](https://developers.cloudflare.com/vectorize/reference/what-is-a-vector-database/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/vectorize/platform/event-subscriptions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
