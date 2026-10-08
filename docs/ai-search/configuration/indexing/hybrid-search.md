---
url: https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/
title: Hybrid search \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:39.454216+00:00
---

# Hybrid search · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /…

[Configuration](https://developers.cloudflare.com/ai-search/configuration/)

  4. /Indexing
  5. /Hybrid search



# Hybrid search

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable hybrid searchFusion methodRerankingPer-request overridesScoring detailsLimits

Hybrid search runs vector and keyword search in parallel and merges the results. It requires [keyword search](https://developers.cloudflare.com/ai-search/configuration/indexing/keyword-search/) to be enabled. For an overview of search modes, refer to [Search modes](https://developers.cloudflare.com/ai-search/concepts/search-modes/).

Hybrid search is enabled by default.

## Enable hybrid search

Set both `index_method.vector` and `index_method.keyword` to `true`:
    
    
    const instance = await env.AI_SEARCH.create({
    	id: "my-instance",
    	index_method: {
    		vector: true,
    		keyword: true,
    	},
    	fusion_method: "rrf",
    });

To opt out of hybrid search, set `index_method.keyword` to `false`. The keyword index is deleted.

For each search method, you can configure the following to adjust retrieval behavior:

  * **Vector search** : Configure the [embedding model](https://developers.cloudflare.com/ai-search/configuration/models/).
  * **Keyword search** : Configure the [tokenizer and match mode](https://developers.cloudflare.com/ai-search/configuration/indexing/keyword-search/).



## Fusion method

The `fusion_method` field controls how vector and keyword results are merged.

Value | Default | Description  
---|---|---  
`rrf` | Yes | Reciprocal Rank Fusion. Scores results based on rank position across both search methods. Recommended for most use cases.  
`max` | No | Takes the higher of the normalized vector and keyword scores. Use when one search method is consistently more relevant.  
  
## Reranking

After fusion, you can optionally apply reranking to further reorder results by semantic relevance. Reranking uses a cross-encoder model that evaluates the query and each chunk together, which can improve precision beyond what fusion alone provides.

Reranking is disabled by default. Refer to [Reranking](https://developers.cloudflare.com/ai-search/configuration/retrieval/reranking/) to enable and configure it.

## Per-request overrides

Override search settings on individual requests using `ai_search_options.retrieval`.

Field | Type | Description  
---|---|---  
`retrieval_type` | `"vector"`, `"keyword"`, or `"hybrid"` | Force a specific search mode. Must be compatible with `index_method`.  
`fusion_method` | `"rrf"` or `"max"` | Override the fusion method.  
      
    
    const instance = env.AI_SEARCH.get("my-instance");
    
    const results = await instance.search({
    	messages: [{ role: "user", content: "What is Cloudflare?" }],
    	ai_search_options: {
    		retrieval: {
    			retrieval_type: "hybrid",
    			fusion_method: "rrf",
    		},
    	},
    });

Note

Requesting a `retrieval_type` that is not compatible with the instance `index_method` returns an error.

## Scoring details

When hybrid search is active, each chunk includes a `scoring_details` object:

Field | Type | Description  
---|---|---  
`vector_score` | number | Vector similarity score (0 to 1).  
`keyword_score` | number | Raw BM25 keyword score.  
`vector_rank` | number | Rank position in the vector result set.  
`keyword_rank` | number | Rank position in the keyword result set.  
`fusion_method` | string | Fusion method used (`rrf` or `max`).  
`reranking_score` | number | Score from the reranking model, if enabled.  
  
## Limits

Instances with keyword search enabled support up to 500,000 files per instance on the Workers Paid tier, compared to 1,000,000 for vector-only instances. Refer to [Limits and pricing](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) for the full list of limits.

[PreviousKeyword search](https://developers.cloudflare.com/ai-search/configuration/indexing/keyword-search/)[NextSyncing](https://developers.cloudflare.com/ai-search/configuration/indexing/syncing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/configuration/indexing/hybrid-search.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
