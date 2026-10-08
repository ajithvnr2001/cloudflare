---
url: https://developers.cloudflare.com/ai-search/configuration/indexing/keyword-search/
title: Keyword search \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:39.552185+00:00
---

# Keyword search · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/configuration/indexing/keyword-search/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /…

[Configuration](https://developers.cloudflare.com/ai-search/configuration/)

  4. /Indexing
  5. /Keyword search



# Keyword search

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-search/configuration/indexing/keyword-search/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable keyword searchKeyword tokenizerKeyword match modeLimits

Enable keyword search to match chunks that contain your query terms exactly. For an overview of search modes, refer to [Search modes](https://developers.cloudflare.com/ai-search/concepts/search-modes/).

## Enable keyword search

Set `index_method.keyword` to `true` when creating or updating an instance. You can use keyword search on its own or alongside vector search for [hybrid search](https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/).

Field | Type | Default | Description  
---|---|---|---  
`vector` | boolean | `true` | Enable vector (semantic) search.  
`keyword` | boolean | `true` | Enable keyword (BM25) search.  
  
At least one of `vector` or `keyword` must be `true`. Changing `index_method` triggers a full reindex of your content.

The `keyword` field defaults to `true`.
    
    
    const instance = await env.AI_SEARCH.create({
    	id: "my-instance",
    	index_method: {
    		vector: false,
    		keyword: true,
    	},
    });

## Keyword tokenizer

The `keyword_tokenizer` field (inside `indexing_options`) controls how text is split into tokens. Changing this triggers a full reindex.

Value | Default | Description  
---|---|---  
`porter` | Yes | Applies Porter stemming. "running" matches "run." Best for natural language.  
`trigram` | No | Overlapping 3-character windows. "config" matches "configuration." Best for code.  
  
## Keyword match mode

The `keyword_match_mode` field (inside `retrieval_options`) controls how multiple query terms are combined.

Value | Default | Description  
---|---|---  
`and` | Yes | All query terms must appear. Higher precision, fewer results.  
`or` | No | Any query term can match. Higher recall, more results.  
  
You can override `keyword_match_mode` per request:
    
    
    const instance = env.AI_SEARCH.get("my-instance");
    
    const results = await instance.search({
    	messages: [{ role: "user", content: "What is Cloudflare?" }],
    	ai_search_options: {
    		retrieval: {
    			keyword_match_mode: "or",
    		},
    	},
    });

## Limits

Instances with keyword search enabled support up to 500,000 files per instance on the Workers Paid tier, compared to 1,000,000 for vector-only instances. Refer to [Limits and pricing](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) for the full list of limits.

[PreviousVector search](https://developers.cloudflare.com/ai-search/configuration/indexing/vector-search/)[NextHybrid search](https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/configuration/indexing/keyword-search.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
