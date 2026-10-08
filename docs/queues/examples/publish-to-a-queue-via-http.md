---
url: https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/
title: Queues - Publish Directly via HTTP \u00b7 Cloudflare Queues docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:40.967126+00:00
---

# Queues - Publish Directly via HTTP · Cloudflare Queues docs

> Source: https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Queues](https://developers.cloudflare.com/queues/)
  3. /[Examples](https://developers.cloudflare.com/queues/examples/)
  4. /Publish to a Queue via HTTP



# Publish to a Queue via HTTP

Publish to a Queue directly via HTTP.

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites 1\. Send a test message

The following example shows you how to publish messages to a Queue from any HTTP client, using a Cloudflare API token to authenticate.

This allows you to write to a Queue from any service or programming language that supports HTTP, including Go, Rust, Python or even a Bash script.

## Prerequisites

  * A [queue created](https://developers.cloudflare.com/queues/get-started/#3-create-a-queue) via the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) or the [wrangler CLI](https://developers.cloudflare.com/workers/wrangler/install-and-update/).
  * A Cloudflare API token with the `Queues Edit` permission.



### 1\. Send a test message

To make sure you successfully authenticate and write a message to your queue, use `curl` on the command line:
    
    
    # Make sure to replace the placeholder with your shared secret
    curl -XPOST -H "Authorization: Bearer <paste-your-api-token-here>" "https://api.cloudflare.com/client/v4/accounts/<paste-your-account-id-here>/queues/<paste-your-queue-id-here>/messages" --data '{ "body": { "greeting": "hello" } }'
    
    
    {"success":true}

This will issue a HTTP POST request, and if successful, return a HTTP 200 with a `success: true` response body.

  * If you receive a HTTP 403, this is because your API token is invalid or does not have the `Queues Edit` permission.



For full documentation about the HTTP Push API, refer to the [Cloudflare API documentation ↗︎](https://developers.cloudflare.com/api/resources/queues/subresources/messages/).

[PreviousPublish to a Queue via Workers](https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-workers/)[NextUse Queues to store data in R2](https://developers.cloudflare.com/queues/examples/send-errors-to-r2/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/queues/examples/publish-to-a-queue-via-http.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
