---
url: https://developers.cloudflare.com/ai-search/configuration/indexing/chunking/
title: Chunking \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:39.398234+00:00
---

# Chunking · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/configuration/indexing/chunking/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /…

[Configuration](https://developers.cloudflare.com/ai-search/configuration/)

  4. /Indexing
  5. /Chunking



# Chunking

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-search/configuration/indexing/chunking/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat is recursive chunkingChunking controlsChoosing chunk size and overlap Additional considerations:

Chunking is the process of splitting large data into smaller segments before embedding them for search. AI Search uses **recursive chunking** , which breaks your content at natural boundaries (like paragraphs or sentences), and then further splits it if the chunks are too large.

## What is recursive chunking

Recursive chunking tries to keep chunks meaningful by:

  * **Splitting at natural boundaries:** like paragraphs, then sentences.
  * **Checking the size:** if a chunk is too long (based on token count), it’s split again into smaller parts.



This way, chunks are easy to embed and retrieve, without cutting off thoughts mid-sentence.

## Chunking controls

AI Search exposes two parameters to help you control chunking behavior:

  * **Chunk size** : The number of tokens per chunk. The option range may vary depending on the model.
  * **Chunk overlap** : The percentage of overlapping tokens between adjacent chunks. 
    * Minimum: `0%`
    * Maximum: `30%`



These settings apply during the indexing step, before your data is embedded and stored in your search index.

## Choosing chunk size and overlap

Chunking affects both how your content is retrieved and how much context is passed into the generation model. Try out this external [chunk visualizer tool ↗︎](https://huggingface.co/spaces/m-ric/chunk_visualizer) to help understand how different chunk settings could look.

### Additional considerations:

  * **Index size:** Smaller chunk sizes produce more chunks and more total vectors. Refer to the [AI Search limits](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) to ensure your configuration stays within instance limits.
  * **Generation model context window:** Generation models have a limited context window that must fit all retrieved chunks (`max_num_results` × `chunk size`), the user query, and the model's output. Be careful with large chunks or high `max_num_results` values to avoid context overflows.
  * **Ingestion cost:** Overlapping text is counted in every chunk it appears in, so a higher chunk overlap can increase billable ingestion tokens. Refer to [How ingestion tokens are counted](https://developers.cloudflare.com/ai-search/platform/limits-pricing/#how-ingestion-tokens-are-counted).
  * **Cost and performance:** Larger chunks and higher `max_num_results` settings result in more tokens passed to the model, which can increase latency and cost. You can monitor this usage in [AI Gateway](https://developers.cloudflare.com/ai-gateway/).



[PreviousPath filtering](https://developers.cloudflare.com/ai-search/configuration/indexing/path-filtering/)[NextMetadata attributes](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/configuration/indexing/chunking.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
