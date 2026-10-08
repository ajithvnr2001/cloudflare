---
url: https://developers.cloudflare.com/ai/models/alibaba/hh1.1-r2v/schema-input.json
title: https://developers.cloudflare.com/ai/models/alibaba/hh1.1-r2v/schema-input.json
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (768 chars), fallback to crawl4ai)
fetched_at: 2026-10-08T07:23:29.666182+00:00
---

# https://developers.cloudflare.com/ai/models/alibaba/hh1.1-r2v/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/alibaba/hh1.1-r2v/schema-input.json


```
{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"prompt":{"type":"string","minLength":1,"maxLength":2500},"images":{"minItems":1,"maxItems":9,"type":"array","items":{"type":"string","format":"uri"}},"resolution":{"type":"string","enum":["720P","1080P"]},"ratio":{"type":"string","enum":["16:9","9:16","3:4","4:3","1:1","21:9","9:21","5:4","4:5"]},"duration":{"type":"integer","minimum":3,"maximum":15},"seed":{"type":"integer","minimum":0,"maximum":2147483647},"watermark":{"type":"boolean"}},"required":["prompt","images"],"additionalProperties":false}
```

