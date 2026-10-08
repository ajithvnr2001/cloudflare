---
url: https://developers.cloudflare.com/ai/models/openai/gpt-5.6-terra/schema-output.json
title: https://developers.cloudflare.com/ai/models/openai/gpt-5.6-terra/schema-output.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:42.428545+00:00
---

# https://developers.cloudflare.com/ai/models/openai/gpt-5.6-terra/schema-output.json

> Source: https://developers.cloudflare.com/ai/models/openai/gpt-5.6-terra/schema-output.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"id":{"type":"string"},"object":{"type":"string","const":"response"},"created_at":{"type":"number"},"model":{"type":"string"},"output":{"type":"array","items":{}},"output_text":{"type":"string"},"status":{"type":"string","enum":["in_progress","completed","failed","incomplete"]},"usage":{"type":"object","properties":{"input_tokens":{"type":"number"},"output_tokens":{"type":"number"},"total_tokens":{"type":"number"}},"required":["input_tokens","output_tokens","total_tokens"],"additionalProperties":{}}},"required":["id","object","created_at","model","output"],"additionalProperties":{}}
