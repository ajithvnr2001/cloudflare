---
url: https://developers.cloudflare.com/ai/models/bytedance/seedream-4.5/schema-input.json
title: https://developers.cloudflare.com/ai/models/bytedance/seedream-4.5/schema-input.json
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (757 chars), fallback to crawl4ai)
fetched_at: 2026-10-08T07:23:35.549796+00:00
---

# https://developers.cloudflare.com/ai/models/bytedance/seedream-4.5/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/bytedance/seedream-4.5/schema-input.json


```
{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"prompt":{"type":"string"},"image_input":{"type":"array","items":{"type":"string","format":"uri"}},"size":{"type":"string","enum":["2K","4K"]},"aspect_ratio":{"type":"string","enum":["match_input_image","1:1","4:3","3:4","16:9","9:16","3:2","2:3","21:9"]},"sequential_image_generation":{"type":"string","enum":["disabled","auto"]},"max_images":{"type":"integer","minimum":1,"maximum":15},"disable_safety_checker":{"type":"boolean"}},"required":["prompt"],"additionalProperties":false}
```

