---
url: https://developers.cloudflare.com/workers-ai/features/batch-api/
title: Asynchronous Batch API \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:57.081989+00:00
---

# Asynchronous Batch API · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/features/batch-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Features
  4. /Asynchronous Batch API



# Asynchronous Batch API

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/features/batch-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDemo applicationSupported Models

Asynchronous batch processing lets you send a collection (batch) of inference requests in a single call. Instead of expecting immediate responses for every request, the system queues them for processing and returns the results later.

Batch processing is useful for large workloads such as summarization or embeddings when there is no human interaction. Using the batch API will guarantee that your requests are fulfilled eventually, rather than erroring out if Cloudflare does not have enough capacity at a given time.

When you send a batch request, the API immediately acknowledges receipt with a status like `queued` and provides a unique `request_id`. This ID is later used to poll for the final responses once the processing is complete.

You can use the Batch API by either creating and deploying a Cloudflare Worker that leverages the [Batch API with the AI binding](https://developers.cloudflare.com/workers-ai/features/batch-api/workers-binding/), using the [REST API](https://developers.cloudflare.com/workers-ai/features/batch-api/rest-api/) directly or by starting from a [template ↗︎](https://github.com/craigsdennis/batch-please-workers-ai).

Note

Ensure that the total payload is under 10 MB.

## Demo application

If you want to get started quickly, click the button below:

[![Deploy to Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/craigsdennis/batch-please-workers-ai)

This will create a repository in your GitHub account and deploy a ready-to-use Worker that demonstrates how to use Cloudflare's Asynchronous Batch API. The template includes preconfigured AI bindings, and examples for sending and retrieving batch requests with and without external references. Once deployed, you can visit the live Worker and start experimenting with the Batch API immediately.

## Supported Models

Refer to our [model catalog](https://developers.cloudflare.com/workers-ai/models/?capabilities=Batch) for supported models.

[PreviousHugging Face Chat UI](https://developers.cloudflare.com/workers-ai/configuration/hugging-face-chat-ui/)[NextWorkers Binding](https://developers.cloudflare.com/workers-ai/features/batch-api/workers-binding/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/features/batch-api/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
