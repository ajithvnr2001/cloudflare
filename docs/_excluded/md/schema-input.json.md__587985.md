---
url: https://developers.cloudflare.com/ai/models/bytedance/seedream-4.0/schema-input.json
title: https://developers.cloudflare.com/ai/models/bytedance/seedream-4.0/schema-input.json
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (674 chars), fallback to crawl4ai)
fetched_at: 2026-10-08T07:23:35.483554+00:00
---

# https://developers.cloudflare.com/ai/models/bytedance/seedream-4.0/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/bytedance/seedream-4.0/schema-input.json


```
{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"prompt":{"type":"string"},"size":{"type":"string","enum":["1K","2K","4K","custom"]},"aspect_ratio":{"type":"string","enum":["match_input_image","1:1","4:3","3:4","16:9","9:16","3:2","2:3","21:9"]},"width":{"type":"integer","minimum":1024,"maximum":4096},"height":{"type":"integer","minimum":1024,"maximum":4096},"enhance_prompt":{"type":"boolean"}},"required":["prompt"],"additionalProperties":false}
```

