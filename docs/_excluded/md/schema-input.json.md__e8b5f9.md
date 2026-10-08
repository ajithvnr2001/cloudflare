---
url: https://developers.cloudflare.com/ai/models/bytedance/seedream-5-pro/schema-input.json
title: https://developers.cloudflare.com/ai/models/bytedance/seedream-5-pro/schema-input.json
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-08T07:23:35.572140+00:00
---

# https://developers.cloudflare.com/ai/models/bytedance/seedream-5-pro/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/bytedance/seedream-5-pro/schema-input.json


```
{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"prompt":{"type":"string"},"image":{"anyOf":[{"type":"string"},{"minItems":1,"maxItems":10,"type":"array","items":{"type":"string"}}]},"size":{"type":"string"},"watermark":{"default":false,"description":"Whether to add an AI-generated watermark to the output image","type":"boolean"}},"required":["prompt","watermark"],"additionalProperties":false}
```

