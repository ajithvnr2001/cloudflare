---
url: https://developers.cloudflare.com/ai/models/@cf/baai/bge-reranker-base/schema-input.json
title: https://developers.cloudflare.com/ai/models/@cf/baai/bge-reranker-base/schema-input.json
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (769 chars), fallback to crawl4ai)
fetched_at: 2026-10-08T07:23:29.566325+00:00
---

# https://developers.cloudflare.com/ai/models/@cf/baai/bge-reranker-base/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/@cf/baai/bge-reranker-base/schema-input.json


```
{"type":"object","properties":{"query":{"type":"string","minLength":1,"description":"A query you wish to perform against the provided contexts."},"top_k":{"type":"integer","minimum":1,"description":"Number of returned results starting with the best score."},"contexts":{"type":"array","items":{"type":"object","properties":{"text":{"type":"string","minLength":1,"description":"One of the provided context content"}}},"description":"List of provided contexts. Note that the index in this array is important, as the response will refer to it."}},"required":["query","contexts"]}
```

