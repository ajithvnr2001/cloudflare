---
url: https://developers.cloudflare.com/ai/models/xai/grok-stt/schema-output.json
title: https://developers.cloudflare.com/ai/models/xai/grok-stt/schema-output.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:49.618242+00:00
---

# https://developers.cloudflare.com/ai/models/xai/grok-stt/schema-output.json

> Source: https://developers.cloudflare.com/ai/models/xai/grok-stt/schema-output.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"text":{"type":"string","description":"Full transcript text."},"language":{"description":"Detected language name (e.g. \"English\", \"French\").","type":"string"},"duration":{"description":"Audio duration in seconds (2 d.p.).","type":"number"},"words":{"description":"Word-level segments. Each entry has text, start, end (seconds). Includes speaker integer when diarize=true.","type":"array","items":{"type":"object","properties":{"text":{"type":"string"},"start":{"type":"number"},"end":{"type":"number"},"speaker":{"type":"number"}},"required":["text","start","end"],"additionalProperties":{}}},"channels":{"description":"Per-channel transcripts when multichannel=true.","type":"array","items":{"type":"object","properties":{"index":{"type":"number"},"text":{"type":"string"},"words":{"type":"array","items":{"type":"object","properties":{"text":{"type":"string"},"start":{"type":"number"},"end":{"type":"number"}},"required":["text","start","end"],"additionalProperties":{}}}},"required":["index","text"],"additionalProperties":{}}}},"required":["text"],"additionalProperties":{}}
