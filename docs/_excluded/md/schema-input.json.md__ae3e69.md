---
url: https://developers.cloudflare.com/ai/models/alibaba/hh1.1-t2v/schema-input.json
title: https://developers.cloudflare.com/ai/models/alibaba/hh1.1-t2v/schema-input.json
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-08T07:23:29.658659+00:00
---

# https://developers.cloudflare.com/ai/models/alibaba/hh1.1-t2v/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/alibaba/hh1.1-t2v/schema-input.json


```
{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"prompt":{"type":"string","minLength":1,"maxLength":2500},"resolution":{"type":"string","enum":["720P","1080P"]},"ratio":{"type":"string","enum":["16:9","9:16","1:1","4:3","3:4"]},"duration":{"type":"integer","minimum":3,"maximum":15},"seed":{"type":"integer","minimum":0,"maximum":2147483647},"watermark":{"type":"boolean"}},"required":["prompt"],"additionalProperties":false}
```

