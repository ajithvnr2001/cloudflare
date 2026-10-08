---
url: https://developers.cloudflare.com/ai/models/alibaba/wan-3.0-prime/schema-input.json
title: https://developers.cloudflare.com/ai/models/alibaba/wan-3.0-prime/schema-input.json
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-08T07:23:31.449074+00:00
---

# https://developers.cloudflare.com/ai/models/alibaba/wan-3.0-prime/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/alibaba/wan-3.0-prime/schema-input.json


```
{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"prompt":{"type":"string","minLength":1,"maxLength":2500},"resolution":{"type":"string","enum":["480P","720P","1080P"]},"ratio":{"type":"string","enum":["adaptive","16:9","9:16","1:1","4:3","3:4"]},"duration":{"type":"integer","minimum":1,"maximum":15}},"required":["prompt"],"additionalProperties":false}
```

