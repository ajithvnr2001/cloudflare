---
url: https://developers.cloudflare.com/changelog/post/2025-05-09-publish-to-queues-via-http/
title: Publish messages to Queues directly via HTTP \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:52.389707+00:00
---

# Publish messages to Queues directly via HTTP · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-09-publish-to-queues-via-http/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 9, 2025

## Publish messages to Queues directly via HTTP

[Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now publish messages to [Cloudflare Queues](https://developers.cloudflare.com/queues/) directly via HTTP from any service or programming language that supports sending HTTP requests. Previously, publishing to queues was only possible from within [Cloudflare Workers](https://developers.cloudflare.com/workers/). You can already consume from queues via Workers or [HTTP pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers/), and now publishing is just as flexible.

Publishing via HTTP requires a [Cloudflare API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with `Queues Edit` permissions for authentication. Here's a simple example:
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/<account_id>/queues/<queue_id>/messages" \
      -X POST \
      -H 'Authorization: Bearer <api_token>' \
      --data '{ "body": { "greeting": "hello", "timestamp":  "2025-07-24T12:00:00Z"} }'

You can also use our [SDKs](https://developers.cloudflare.com/fundamentals/api/reference/sdks/) for TypeScript, Python, and Go.

To get started with HTTP publishing, check out our [step-by-step example](https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/) and the full API documentation in our [API reference](https://developers.cloudflare.com/api/resources/queues/subresources/messages/methods/push/).
