---
url: https://developers.cloudflare.com/ai/models/google/nano-banana-2/schema-input.json
title: https://developers.cloudflare.com/ai/models/google/nano-banana-2/schema-input.json
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (722 chars), fallback to crawl4ai)
fetched_at: 2026-10-08T07:23:38.696559+00:00
---

# https://developers.cloudflare.com/ai/models/google/nano-banana-2/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/google/nano-banana-2/schema-input.json


```
{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"prompt":{"type":"string"},"image_input":{"maxItems":3,"type":"array","items":{"type":"string"}},"aspect_ratio":{"type":"string","enum":["match_input_image","1:1","2:3","3:2","3:4","4:3","4:5","5:4","9:16","16:9","21:9"]},"output_format":{"type":"string","enum":["jpg","png"]},"resolution":{"type":"string","enum":["1K","2K","4K"]},"google_search":{"type":"boolean"},"image_search":{"type":"boolean"}},"required":["prompt"],"additionalProperties":false}
```

