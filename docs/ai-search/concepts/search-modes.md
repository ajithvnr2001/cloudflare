---
url: https://developers.cloudflare.com/ai-search/concepts/search-modes/
title: Search modes \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:38.809005+00:00
---

# Search modes · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/concepts/search-modes/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /Concepts
  4. /Search modes



# Search modes

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-search/concepts/search-modes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewVector searchKeyword searchHybrid search

AI Search supports three search modes: [vector](https://developers.cloudflare.com/ai-search/configuration/indexing/vector-search/), [keyword](https://developers.cloudflare.com/ai-search/configuration/indexing/keyword-search/), and [hybrid](https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/). New instances use hybrid search by default.

To opt out, set `index_method` to `{ vector: true, keyword: false }`. Refer to [Hybrid search](https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/) for configuration details.

## Vector search

Vector search converts your query into a vector embedding and finds chunks with similar meaning, even when the exact words differ. It knows that "deployment guide" and "how to ship my app" mean similar things. However, it can lose specifics. In a query like "ERR_CONNECTION_REFUSED timeout," vector search captures the broad concept of connection failures but might not surface the page that contains that exact error string.

## Keyword search

Keyword search matches chunks that contain your query terms exactly using BM25 full-text search. When you search "ERR_CONNECTION_REFUSED timeout," BM25 finds documents that actually contain "ERR_CONNECTION_REFUSED" as a term. However, it may miss a page about "troubleshooting network connections" that describes the same problem. Refer to [Keyword search](https://developers.cloudflare.com/ai-search/configuration/indexing/keyword-search/) for setup.

## Hybrid search

Hybrid search runs vector and keyword search in parallel and merges the results using a fusion method. Vector search understands intent, keyword search matches specific terms. Together, a query like "ERR_CONNECTION_REFUSED timeout" finds the exact error page and related troubleshooting content. Refer to [Hybrid search](https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/) for setup.

![Hybrid search](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1381,height=954,format=webp/_astro/hybrid-search.CJ9Cuw7h.png)

[PreviousNamespaces](https://developers.cloudflare.com/ai-search/concepts/namespaces/)[NextWorkers binding](https://developers.cloudflare.com/ai-search/api/instances/workers-binding/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/concepts/search-modes.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
