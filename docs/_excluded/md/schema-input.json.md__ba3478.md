---
url: https://developers.cloudflare.com/ai/models/@cf/pipecat-ai/smart-turn-v2/schema-input.json
title: https://developers.cloudflare.com/ai/models/@cf/pipecat-ai/smart-turn-v2/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:24.257791+00:00
---

# https://developers.cloudflare.com/ai/models/@cf/pipecat-ai/smart-turn-v2/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/@cf/pipecat-ai/smart-turn-v2/schema-input.json

{"type":"object","oneOf":[{"properties":{"audio":{"type":"object","description":"readable stream with audio data and content-type specified for that data","properties":{"body":{"type":"object"},"contentType":{"type":"string"}},"required":["body","contentType"]},"dtype":{"type":"string","description":"type of data PCM data that's sent to the inference server as raw array","enum":["uint8","float32","float64"]}},"required":["audio"]},{"properties":{"audio":{"type":"string","description":"base64 encoded audio data"},"dtype":{"type":"string","description":"type of data PCM data that's sent to the inference server as raw array","enum":["uint8","float32","float64"]}},"required":["audio"]}]}
