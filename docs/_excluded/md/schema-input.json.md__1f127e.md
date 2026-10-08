---
url: https://developers.cloudflare.com/ai/models/anthropic/claude-sonnet-5/schema-input.json
title: https://developers.cloudflare.com/ai/models/anthropic/claude-sonnet-5/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:31.527641+00:00
---

# https://developers.cloudflare.com/ai/models/anthropic/claude-sonnet-5/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/anthropic/claude-sonnet-5/schema-input.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"messages":{"type":"array","items":{"type":"object","properties":{"role":{"type":"string","enum":["user","assistant"]},"content":{"anyOf":[{"type":"string"},{"type":"array","items":{"type":"object","properties":{"type":{"type":"string"},"text":{"type":"string"},"source":{},"cache_control":{"type":"object","properties":{"type":{"type":"string","const":"ephemeral"},"ttl":{"type":"string","enum":["5m","1h"]}},"required":["type"],"additionalProperties":false}},"required":["type"],"additionalProperties":{}}}]}},"required":["role","content"],"additionalProperties":false}},"max_tokens":{"type":"number","exclusiveMinimum":0},"system":{"type":"string"},"stream":{"type":"boolean"},"metadata":{"type":"object","propertyNames":{"type":"string"},"additionalProperties":{}}},"required":["messages","max_tokens"],"additionalProperties":{}}
