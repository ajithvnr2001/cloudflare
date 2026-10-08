---
url: https://developers.cloudflare.com/ai/models/minimax/music-2.6/schema-input.json
title: https://developers.cloudflare.com/ai/models/minimax/music-2.6/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:39.598218+00:00
---

# https://developers.cloudflare.com/ai/models/minimax/music-2.6/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/minimax/music-2.6/schema-input.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"prompt":{"type":"string","maxLength":2000,"description":"Description of the music style, mood, and scenario"},"lyrics":{"description":"Song lyrics, using \\\n to separate lines","type":"string","minLength":1,"maxLength":3500},"sample_rate":{"description":"Audio sample rate","anyOf":[{"type":"number","const":16000},{"type":"number","const":24000},{"type":"number","const":32000},{"type":"number","const":44100}]},"bitrate":{"description":"Audio bitrate","anyOf":[{"type":"number","const":32000},{"type":"number","const":64000},{"type":"number","const":128000},{"type":"number","const":256000}]},"format":{"description":"Audio format","type":"string","enum":["mp3","wav"]},"lyrics_optimizer":{"default":false,"description":"Automatically generate lyrics based on the prompt description","type":"boolean"},"is_instrumental":{"default":false,"description":"Generate instrumental music (no vocals)","type":"boolean"}},"required":["prompt","lyrics_optimizer","is_instrumental"],"additionalProperties":false}
