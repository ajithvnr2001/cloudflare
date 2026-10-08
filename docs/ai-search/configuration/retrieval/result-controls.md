---
url: https://developers.cloudflare.com/ai-search/configuration/retrieval/result-controls/
title: Result controls \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:40.931644+00:00
---

# Result controls · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/configuration/retrieval/result-controls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /…

[Configuration](https://developers.cloudflare.com/ai-search/configuration/)

  4. /Retrieval
  5. /Result controls



# Result controls

Last updated Jun 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-search/configuration/retrieval/result-controls/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMatch thresholdMaximum number of resultsHow they work togetherPer-request override

These settings control how many results are returned and the minimum score required. To filter results by metadata attributes like folder or category, refer to [Filtering](https://developers.cloudflare.com/ai-search/configuration/retrieval/filtering/).

## Match threshold

The `match_threshold` sets the minimum vector similarity score that a chunk must meet to be included in the results. Threshold values range from `0` to `1`. The threshold filters on the vector similarity score, not the fused score returned in the response.

  * A higher threshold means stricter filtering, returning only highly similar matches.
  * A lower threshold allows broader matches, increasing recall but possibly reducing precision.



## Maximum number of results

The `max_num_results` setting controls the number of top-matching chunks returned. The maximum allowed value is 50.

  * Use a higher value if you want to synthesize across multiple documents. However, providing more input to the model can increase latency and cost.
  * Use a lower value if you prefer concise answers with minimal context.



## How they work together

  1. Your query is embedded using the configured embedding model.
  2. The search index is queried. For [hybrid search](https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/), vector and keyword results are fused into a single ranked list.
  3. Chunks with a vector similarity score below `match_threshold` are filtered out.
  4. The filtered results are limited to `max_num_results` and passed into the generation step as context.



If no results meet the threshold, AI Search will not generate a response.

If [reranking](https://developers.cloudflare.com/ai-search/configuration/retrieval/reranking/) is enabled, a separate `reranking.match_threshold` can be configured to filter chunks by their reranking score.

## Per-request override

These values can be configured at the instance level or overridden per request:
    
    
    const instance = env.AI_SEARCH.get("my-instance");
    
    const results = await instance.search({
    	messages: [{ role: "user", content: "What is Cloudflare?" }],
    	ai_search_options: {
    		retrieval: {
    			match_threshold: 0.5,
    			max_num_results: 10,
    		},
    	},
    });

[PreviousRelevance boosting](https://developers.cloudflare.com/ai-search/configuration/retrieval/boosting/)[NextSimilarity cache](https://developers.cloudflare.com/ai-search/configuration/retrieval/cache/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/configuration/retrieval/result-controls.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
