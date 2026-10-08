---
url: https://developers.cloudflare.com/ai/models/google/gemini-2.5-flash/schema-output.json
title: https://developers.cloudflare.com/ai/models/google/gemini-2.5-flash/schema-output.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:35.905720+00:00
---

# https://developers.cloudflare.com/ai/models/google/gemini-2.5-flash/schema-output.json

> Source: https://developers.cloudflare.com/ai/models/google/gemini-2.5-flash/schema-output.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","oneOf":[{"type":"object","properties":{"candidates":{"type":"array","items":{}},"usageMetadata":{"type":"object","properties":{"promptTokenCount":{"type":"number"},"candidatesTokenCount":{"type":"number"},"totalTokenCount":{"type":"number"}},"additionalProperties":{}},"modelVersion":{"type":"string"}},"additionalProperties":{},"title":"Generate Content"},{"type":"object","properties":{"id":{"type":"string"},"object":{"type":"string"},"created":{"type":"number"},"model":{"type":"string"},"choices":{"type":"array","items":{"type":"object","properties":{"index":{"type":"number"},"message":{"type":"object","properties":{"role":{"type":"string"},"content":{"type":["string","null"]},"tool_calls":{"anyOf":[{"type":"array","items":{}},{"type":"null"}]},"audio":{"anyOf":[{"type":"object","properties":{"id":{"type":"string"},"data":{"type":"string"},"expires_at":{"type":"number"},"transcript":{"type":"string"}},"additionalProperties":{}},{"type":"null"}]}},"required":["role"],"additionalProperties":{}},"finish_reason":{"type":["string","null"]}},"required":["index","message","finish_reason"],"additionalProperties":{}}},"usage":{"type":"object","properties":{"prompt_tokens":{"type":"number"},"completion_tokens":{"type":"number"},"total_tokens":{"type":"number"}},"required":["prompt_tokens","completion_tokens","total_tokens"],"additionalProperties":{}}},"required":["id","object","created","model","choices"],"additionalProperties":{},"title":"Chat Completions"}]}
