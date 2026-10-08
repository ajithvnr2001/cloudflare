---
url: https://developers.cloudflare.com/workers-ai/platform/event-subscriptions/
title: Event subscriptions \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:06.956116+00:00
---

# Event subscriptions · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/platform/event-subscriptions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Platform
  4. /Event subscriptions



# Event subscriptions

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/platform/event-subscriptions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailable Workers AI events

[Event subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/) allow you to receive messages when events occur across your Cloudflare account. Cloudflare products (e.g., [KV](https://developers.cloudflare.com/kv/), [Workers AI](https://developers.cloudflare.com/workers-ai/), [Workers](https://developers.cloudflare.com/workers/)) can publish structured events to a [queue](https://developers.cloudflare.com/queues/), which you can then consume with Workers or [HTTP pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers/) to build custom workflows, integrations, or logic.

For more information on [Event Subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/), refer to the [management guide](https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/).

## Available Workers AI events

#### `batch.queued`

Triggered when a batch request is queued.

**Example:**
    
    
    {
      "type": "cf.workersAi.model.batch.queued",
      "source": {
        "type": "workersAi.model",
        "modelName": "@cf/baai/bge-base-en-v1.5"
      },
      "payload": {
        "requestId": "req-12345678-90ab-cdef-1234-567890abcdef"
      },
      "metadata": {
        "accountId": "f9f79265f388666de8122cfb508d7776",
        "eventSubscriptionId": "1830c4bb612e43c3af7f4cada31fbf3f",
        "eventSchemaVersion": 1,
        "eventTimestamp": "2025-05-01T02:48:57.132Z"
      }
    }

#### `batch.succeeded`

Triggered when a batch request has completed.

**Example:**
    
    
    {
      "type": "cf.workersAi.model.batch.succeeded",
      "source": {
        "type": "workersAi.model",
        "modelName": "@cf/baai/bge-base-en-v1.5"
      },
      "payload": {
        "requestId": "req-12345678-90ab-cdef-1234-567890abcdef"
      },
      "metadata": {
        "accountId": "f9f79265f388666de8122cfb508d7776",
        "eventSubscriptionId": "1830c4bb612e43c3af7f4cada31fbf3f",
        "eventSchemaVersion": 1,
        "eventTimestamp": "2025-05-01T02:48:57.132Z"
      }
    }

#### `batch.failed`

Triggered when a batch request has failed.

**Example:**
    
    
    {
      "type": "cf.workersAi.model.batch.failed",
      "source": {
        "type": "workersAi.model",
        "modelName": "@cf/baai/bge-base-en-v1.5"
      },
      "payload": {
        "requestId": "req-12345678-90ab-cdef-1234-567890abcdef",
        "message": "Model execution failed",
        "internalCode": 5001,
        "httpCode": 500
      },
      "metadata": {
        "accountId": "f9f79265f388666de8122cfb508d7776",
        "eventSubscriptionId": "1830c4bb612e43c3af7f4cada31fbf3f",
        "eventSchemaVersion": 1,
        "eventTimestamp": "2025-05-01T02:48:57.132Z"
      }
    }

[PreviousChoose a data or storage product ↗︎](https://developers.cloudflare.com/workers/platform/storage-options/)[NextAgents ↗︎](https://developers.cloudflare.com/agents/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/platform/event-subscriptions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
