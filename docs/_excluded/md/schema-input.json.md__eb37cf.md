---
url: https://developers.cloudflare.com/ai/models/google/nano-banana-2-lite/schema-input.json
title: https://developers.cloudflare.com/ai/models/google/nano-banana-2-lite/schema-input.json
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-08T07:23:38.254717+00:00
---

# https://developers.cloudflare.com/ai/models/google/nano-banana-2-lite/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/google/nano-banana-2-lite/schema-input.json


```
{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"prompt":{"type":"string"},"image_input":{"maxItems":3,"type":"array","items":{"type":"string"}},"aspect_ratio":{"type":"string","enum":["match_input_image","1:1","2:3","3:2","3:4","4:3","4:5","5:4","9:16","16:9","21:9"]},"output_format":{"type":"string","enum":["jpg","png"]},"resolution":{"type":"string","enum":["1K","2K","4K"]}},"required":["prompt"],"additionalProperties":false}
```

