---
url: https://developers.cloudflare.com/changelog/post/2026-04-16-hybrid-search-and-relevance-boosting/
title: AI Search now has hybrid search and relevance boosting \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:47.804401+00:00
---

# AI Search now has hybrid search and relevance boosting · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-16-hybrid-search-and-relevance-boosting/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 16, 2026

## AI Search now has hybrid search and relevance boosting

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-16-hybrid-search-and-relevance-boosting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports hybrid search and relevance boosting, giving you more control over how results are found and ranked.

#### Hybrid search

Hybrid search combines vector (semantic) search with BM25 keyword search in a single query. Vector search finds chunks with similar meaning, even when the exact words differ. Keyword search matches chunks that contain your query terms exactly. When you enable hybrid search, both run in parallel and the results are fused into a single ranked list.

You can configure the tokenizer (`porter` for natural language, `trigram` for code), keyword match mode (`and` for precision, `or` for recall), and fusion method (`rrf` or `max`) per instance:
    
    
    const instance = await env.AI_SEARCH.create({
    	id: "my-instance",
    	index_method: { vector: true, keyword: true },
    	fusion_method: "rrf",
    	indexing_options: { keyword_tokenizer: "porter" },
    	retrieval_options: { keyword_match_mode: "and" },
    });

Refer to [Search modes](https://developers.cloudflare.com/ai-search/concepts/search-modes/) for an overview and [Hybrid search](https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/) for configuration details.

#### Relevance boosting

Relevance boosting lets you nudge search rankings based on document metadata. For example, you can prioritize recent documents by boosting on `timestamp`, or surface high-priority content by boosting on a custom metadata field like `priority`.

Configure up to 3 boost fields per instance or override them per request:
    
    
    const results = await env.AI_SEARCH.get("my-instance").search({
    	messages: [{ role: "user", content: "deployment guide" }],
    	ai_search_options: {
    		retrieval: {
    			boost_by: [
    				{ field: "timestamp", direction: "desc" },
    				{ field: "priority", direction: "desc" },
    			],
    		},
    	},
    });

Refer to [Relevance boosting](https://developers.cloudflare.com/ai-search/configuration/retrieval/boosting/) for configuration details.
