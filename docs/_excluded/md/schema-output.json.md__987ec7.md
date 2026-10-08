---
url: https://developers.cloudflare.com/ai/models/assemblyai/universal-3.5-pro/schema-output.json
title: https://developers.cloudflare.com/ai/models/assemblyai/universal-3.5-pro/schema-output.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:31.885178+00:00
---

# https://developers.cloudflare.com/ai/models/assemblyai/universal-3.5-pro/schema-output.json

> Source: https://developers.cloudflare.com/ai/models/assemblyai/universal-3.5-pro/schema-output.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"text":{"type":"string","description":"The transcribed text."},"words":{"description":"Word-level timestamps and confidence scores.","anyOf":[{"type":"array","items":{"type":"object","properties":{"text":{"type":"string"},"start":{"type":"number"},"end":{"type":"number"},"confidence":{"type":"number"},"speaker":{"type":["string","null"]}},"required":["text","start","end","confidence"],"additionalProperties":false}},{"type":"null"}]},"utterances":{"description":"Speaker-separated utterances (when speaker_labels is enabled).","anyOf":[{"type":"array","items":{"type":"object","properties":{"text":{"type":"string"},"start":{"type":"number"},"end":{"type":"number"},"confidence":{"type":"number"},"speaker":{"type":"string"}},"required":["text","start","end","confidence","speaker"],"additionalProperties":false}},{"type":"null"}]},"confidence":{"description":"Overall confidence score for the transcription.","type":["number","null"]},"language_code":{"description":"Detected or specified language code.","type":["string","null"]},"language_confidence":{"description":"Confidence score for language detection.","type":["number","null"]}},"required":["text"],"additionalProperties":false}
