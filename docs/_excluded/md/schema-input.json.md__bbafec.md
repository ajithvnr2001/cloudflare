---
url: https://developers.cloudflare.com/ai/models/alibaba/hh1-i2v/schema-input.json
title: https://developers.cloudflare.com/ai/models/alibaba/hh1-i2v/schema-input.json
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-08T07:23:29.155544+00:00
---

# https://developers.cloudflare.com/ai/models/alibaba/hh1-i2v/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/alibaba/hh1-i2v/schema-input.json


```
{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"image":{"type":"string","format":"uri"},"prompt":{"type":"string"},"negative_prompt":{"type":"string"},"resolution":{"type":"string","enum":["720P","1080P"]},"duration":{"type":"integer","minimum":3,"maximum":15},"seed":{"type":"integer","minimum":0,"maximum":2147483647},"watermark":{"type":"boolean"}},"required":["image"],"additionalProperties":false}
```

