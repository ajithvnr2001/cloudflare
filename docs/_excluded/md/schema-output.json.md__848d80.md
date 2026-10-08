---
url: https://developers.cloudflare.com/ai/models/@cf/openai/whisper/schema-output.json
title: https://developers.cloudflare.com/ai/models/@cf/openai/whisper/schema-output.json
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-08T07:23:25.973731+00:00
---

# https://developers.cloudflare.com/ai/models/@cf/openai/whisper/schema-output.json

> Source: https://developers.cloudflare.com/ai/models/@cf/openai/whisper/schema-output.json


```
{"type":"object","contentType":"application/json","properties":{"text":{"type":"string","description":"The transcription"},"word_count":{"type":"number"},"words":{"type":"array","items":{"type":"object","properties":{"word":{"type":"string"},"start":{"type":"number","description":"The second this word begins in the recording"},"end":{"type":"number","description":"The ending second when the word completes"}}}},"vtt":{"type":"string"}},"required":["text"]}
```

