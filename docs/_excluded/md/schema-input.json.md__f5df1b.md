---
url: https://developers.cloudflare.com/ai/models/openai/gpt-5.5-pro/schema-input.json
title: https://developers.cloudflare.com/ai/models/openai/gpt-5.5-pro/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:41.738118+00:00
---

# https://developers.cloudflare.com/ai/models/openai/gpt-5.5-pro/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/openai/gpt-5.5-pro/schema-input.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"input":{"anyOf":[{"type":"string"},{"type":"array","items":{}}]},"instructions":{"type":"string"},"temperature":{"type":"number","minimum":0,"maximum":2},"max_output_tokens":{"type":"number","exclusiveMinimum":0},"top_p":{"type":"number","minimum":0,"maximum":1},"stream":{"type":"boolean"},"tools":{"type":"array","items":{}},"tool_choice":{},"text":{"type":"object","properties":{"format":{}},"additionalProperties":{}},"reasoning":{"type":"object","properties":{"effort":{"type":"string","enum":["none","low","medium","high"]}},"additionalProperties":{}}},"required":["input"],"additionalProperties":{}}
