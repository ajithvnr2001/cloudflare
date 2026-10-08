---
url: https://developers.cloudflare.com/basin-pipelines/sinks/
title: Sinks \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:25.416154+00:00
---

# Sinks · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/sinks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /Sinks



# Sinks

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/sinks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLearn more

Sinks define destinations for your data in Basin Pipelines. They support writing to [Basin Catalog](https://developers.cloudflare.com/basin-catalog/) as Apache Iceberg tables or to [R2](https://developers.cloudflare.com/r2/) as raw JSON or Parquet files.

Sinks provide exactly-once delivery guarantees, ensuring events are never duplicated or dropped. They can be configured to write files frequently for low-latency ingestion or to write larger, less frequent files for better query performance.

## Learn more

### [Manage sinks](https://developers.cloudflare.com/basin-pipelines/sinks/manage-sinks/)

Create, configure, and delete sinks using Wrangler or the API.

### [Available sinks](https://developers.cloudflare.com/basin-pipelines/sinks/available-sinks/)

Learn about supported sink destinations and their configuration options.

[PreviousLogpush as a source](https://developers.cloudflare.com/basin-pipelines/streams/logpush/)[NextManage sinks](https://developers.cloudflare.com/basin-pipelines/sinks/manage-sinks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/sinks/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
