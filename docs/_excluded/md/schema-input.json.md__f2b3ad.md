---
url: https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-2.0/schema-input.json
title: https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-2.0/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:48.761427+00:00
---

# https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-2.0/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-2.0/schema-input.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"prompt":{"type":"string"},"aspect_ratio":{"type":"string","enum":["1:1","3:4","4:3","9:16","16:9","2:3","3:2","9:19.5","19.5:9","9:20","20:9","1:2","2:1","auto"]},"quality":{"type":"string","enum":["low","medium"]},"resolution":{"type":"string","enum":["1k","2k"]},"response_format":{"type":"string","enum":["url","b64_json"]},"user":{"type":"string"},"image":{"type":"object","properties":{"url":{"type":"string"},"type":{"type":"string"}},"required":["url"],"additionalProperties":false},"images":{"maxItems":5,"type":"array","items":{"type":"object","properties":{"url":{"type":"string"},"type":{"type":"string"}},"required":["url"],"additionalProperties":false}},"mask":{"type":"object","properties":{"url":{"type":"string"}},"required":["url"],"additionalProperties":false}},"required":["prompt"],"additionalProperties":false}
