---
url: https://developers.cloudflare.com/ai/models/anthropic/claude-sonnet-4.6/schema-output.json
title: https://developers.cloudflare.com/ai/models/anthropic/claude-sonnet-4.6/schema-output.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:31.268440+00:00
---

# https://developers.cloudflare.com/ai/models/anthropic/claude-sonnet-4.6/schema-output.json

> Source: https://developers.cloudflare.com/ai/models/anthropic/claude-sonnet-4.6/schema-output.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"id":{"type":"string"},"type":{"type":"string","const":"message"},"role":{"type":"string","const":"assistant"},"content":{"type":"array","items":{"type":"object","properties":{"type":{"type":"string"},"text":{"type":"string"}},"required":["type"],"additionalProperties":{}}},"model":{"type":"string"},"stop_reason":{"type":["string","null"]},"usage":{"type":"object","properties":{"input_tokens":{"type":"number"},"output_tokens":{"type":"number"}},"required":["input_tokens","output_tokens"],"additionalProperties":false}},"required":["id","type","role","content","model","stop_reason","usage"],"additionalProperties":{}}
