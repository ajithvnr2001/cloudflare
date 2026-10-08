---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/event-subscriptions/
title: Event subscriptions \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:22.449894+00:00
---

# Event subscriptions · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/event-subscriptions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)
  4. /Event subscriptions



# Event subscriptions

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/event-subscriptions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailable Access events

[Event subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/) allow you to receive messages when events occur across your Cloudflare account. Cloudflare products (e.g., [KV](https://developers.cloudflare.com/kv/), [Workers AI](https://developers.cloudflare.com/workers-ai/), [Workers](https://developers.cloudflare.com/workers/)) can publish structured events to a [queue](https://developers.cloudflare.com/queues/), which you can then consume with Workers or [HTTP pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers/) to build custom workflows, integrations, or logic.

For more information on [Event Subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/), refer to the [management guide](https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/).

## Available Access events

#### `application.created`

Triggered when an application is created.

**Example:**
    
    
    {
      "type": "cf.access.application.created",
      "source": {
        "type": "access"
      },
      "payload": {
        "id": "app-12345678-90ab-cdef-1234-567890abcdef",
        "name": "My Application"
      },
      "metadata": {
        "accountId": "f9f79265f388666de8122cfb508d7776",
        "eventSubscriptionId": "1830c4bb612e43c3af7f4cada31fbf3f",
        "eventSchemaVersion": 1,
        "eventTimestamp": "2025-05-01T02:48:57.132Z"
      }
    }

#### `application.deleted`

Triggered when an application is deleted.

**Example:**
    
    
    {
      "type": "cf.access.application.deleted",
      "source": {
        "type": "access"
      },
      "payload": {
        "id": "app-12345678-90ab-cdef-1234-567890abcdef",
        "name": "My Application"
      },
      "metadata": {
        "accountId": "f9f79265f388666de8122cfb508d7776",
        "eventSubscriptionId": "1830c4bb612e43c3af7f4cada31fbf3f",
        "eventSchemaVersion": 1,
        "eventTimestamp": "2025-05-01T02:48:57.132Z"
      }
    }

[PreviousAuthenticate coding agents](https://developers.cloudflare.com/cloudflare-one/access-controls/authenticate-agents/)[NextTroubleshoot Access](https://developers.cloudflare.com/cloudflare-one/access-controls/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/event-subscriptions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
