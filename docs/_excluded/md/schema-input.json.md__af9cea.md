---
url: https://developers.cloudflare.com/ai/models/minimax/h3/schema-input.json
title: https://developers.cloudflare.com/ai/models/minimax/h3/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:39.408052+00:00
---

# https://developers.cloudflare.com/ai/models/minimax/h3/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/minimax/h3/schema-input.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"content":{"minItems":1,"type":"array","items":{"oneOf":[{"type":"object","properties":{"type":{"type":"string","const":"text"},"text":{"type":"string","minLength":1,"maxLength":7000}},"required":["type","text"],"additionalProperties":false},{"type":"object","properties":{"type":{"type":"string","const":"image_url"},"image_url":{"type":"object","properties":{"url":{"type":"string","minLength":1}},"required":["url"],"additionalProperties":false},"role":{"type":"string","enum":["first_frame","last_frame","reference_image"]}},"required":["type","image_url"],"additionalProperties":false},{"type":"object","properties":{"type":{"type":"string","const":"video_url"},"video_url":{"type":"object","properties":{"url":{"type":"string","minLength":1}},"required":["url"],"additionalProperties":false},"role":{"type":"string","const":"reference_video"}},"required":["type","video_url","role"],"additionalProperties":false},{"type":"object","properties":{"type":{"type":"string","const":"audio_url"},"audio_url":{"type":"object","properties":{"url":{"type":"string","minLength":1}},"required":["url"],"additionalProperties":false},"role":{"type":"string","const":"reference_audio"}},"required":["type","audio_url","role"],"additionalProperties":false}]}},"resolution":{"type":"string","enum":["768P","2K"]},"duration":{"type":"integer","minimum":4,"maximum":15},"ratio":{"type":"string","enum":["adaptive","21:9","16:9","4:3","1:1","3:4","9:16"]},"callback_url":{"type":"string","format":"uri"}},"required":["content","resolution","duration"],"additionalProperties":false}
