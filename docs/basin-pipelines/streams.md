---
url: https://developers.cloudflare.com/basin-pipelines/streams/
title: Streams \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:27.302844+00:00
---

# Streams · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/streams/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /Streams



# Streams

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/streams/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLearn more

Streams are durable, buffered queues that receive and store events for processing in [Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/). They provide reliable data ingestion via HTTP endpoints and Worker bindings, ensuring no data loss even during downstream processing delays or failures.

A single stream can be read by multiple pipelines, allowing you to route the same data to different destinations or apply different transformations. For example, you might send user events to both a real-time analytics pipeline and a data warehouse pipeline.

Streams currently accept events in JSON format and support both structured events with defined schemas and unstructured JSON. When a schema is provided, streams will validate and enforce it for incoming events.

## Learn more

### [Manage streams](https://developers.cloudflare.com/basin-pipelines/streams/manage-streams/)

Create, configure, and delete streams using Wrangler or the API.

### [Writing to streams](https://developers.cloudflare.com/basin-pipelines/streams/writing-to-streams/)

Send events to streams via HTTP endpoints or Worker bindings.

### [Logpush as a source](https://developers.cloudflare.com/basin-pipelines/streams/logpush/)

Use Cloudflare Logpush to send logs from Cloudflare products to a Basin Pipelines stream.

[PreviousGetting started](https://developers.cloudflare.com/basin-pipelines/getting-started/)[NextManage streams](https://developers.cloudflare.com/basin-pipelines/streams/manage-streams/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/streams/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
