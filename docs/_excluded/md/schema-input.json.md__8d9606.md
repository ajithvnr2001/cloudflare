---
url: https://developers.cloudflare.com/ai/models/@cf/google/embeddinggemma-300m/schema-input.json
title: https://developers.cloudflare.com/ai/models/@cf/google/embeddinggemma-300m/schema-input.json
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-08T07:23:17.229550+00:00
---

# https://developers.cloudflare.com/ai/models/@cf/google/embeddinggemma-300m/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/@cf/google/embeddinggemma-300m/schema-input.json


```
{"type":"object","properties":{"text":{"oneOf":[{"type":"string","description":"The text to embed","minLength":1},{"type":"array","description":"Batch of text values to embed","items":{"type":"string","description":"The text to embed","minLength":1},"maxItems":100}]}},"required":["text"]}
```

