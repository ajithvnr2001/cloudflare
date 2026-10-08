---
url: https://developers.cloudflare.com/ai-search/configuration/data-source/built-in-storage/
title: Built-in storage \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:38.837942+00:00
---

# Built-in storage · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/configuration/data-source/built-in-storage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /…

[Configuration](https://developers.cloudflare.com/ai-search/configuration/)

  4. /[Data source](https://developers.cloudflare.com/ai-search/configuration/data-source/)
  5. /Built-in storage



# Built-in storage

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-search/configuration/data-source/built-in-storage/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUpload and manage filesIndexingExternal data sourcesLimits and pricing

Every AI Search instance comes with built-in storage and a built-in vector index, powered by [R2](https://developers.cloudflare.com/r2/) and [Vectorize](https://developers.cloudflare.com/vectorize/). You can upload files directly to an instance without setting up either service yourself.

## Upload and manage files

Upload files to an instance using the [Items API](https://developers.cloudflare.com/ai-search/api/items/workers-binding/) (Workers binding or REST API) or the **Items** tab in the dashboard (**AI** > **AI Search** > your instance > **Items**). You can also list, view, and delete uploaded files through the Items API or the dashboard.

For supported file types, refer to [Supported file types](https://developers.cloudflare.com/ai-search/configuration/data-source/#supported-file-types).

## Indexing

Files uploaded to built-in storage are indexed immediately. External data sources like websites and R2 buckets are indexed on a [sync schedule](https://developers.cloudflare.com/ai-search/configuration/indexing/syncing/).

## External data sources

An instance can use built-in storage alongside an external data source. The available external data sources are:

  * [Website](https://developers.cloudflare.com/ai-search/configuration/data-source/website/): crawl and index a website that you own
  * [R2 Bucket](https://developers.cloudflare.com/ai-search/configuration/data-source/r2/): index documents stored in a Cloudflare R2 bucket



For example, an instance can be backed by a website for shared documentation while also accepting file uploads through the Items API for additional content.

## Limits and pricing

Storage, vector indexing, Browser Run crawling, and Workers AI embedding and reranking usage are included in AI Search billing. Other usage, such as generation through your AI Gateway, is billed separately. For full details, refer to [Limits and pricing](https://developers.cloudflare.com/ai-search/platform/limits-pricing/).

[PreviousOverview](https://developers.cloudflare.com/ai-search/configuration/data-source/)[NextR2](https://developers.cloudflare.com/ai-search/configuration/data-source/r2/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/configuration/data-source/built-in-storage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
