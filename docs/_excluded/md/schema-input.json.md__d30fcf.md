---
url: https://developers.cloudflare.com/ai/models/alibaba/qwen-image-3.0-pro/schema-input.json
title: https://developers.cloudflare.com/ai/models/alibaba/qwen-image-3.0-pro/schema-input.json
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (729 chars), fallback to crawl4ai)
fetched_at: 2026-10-08T07:23:31.396178+00:00
---

# https://developers.cloudflare.com/ai/models/alibaba/qwen-image-3.0-pro/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/alibaba/qwen-image-3.0-pro/schema-input.json


```
{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"prompt":{"type":"string"},"size":{"default":"1024x1024","type":"string","pattern":"^\\d+x\\d+$"},"negative_prompt":{"type":"string","maxLength":500},"n":{"type":"integer","minimum":1,"maximum":6},"seed":{"type":"integer","minimum":0,"maximum":2147483647},"watermark":{"type":"boolean"},"prompt_extend":{"type":"boolean"},"prompt_extend_mode":{"type":"string","enum":["direct","agent"]}},"required":["prompt","size"],"additionalProperties":false}
```

