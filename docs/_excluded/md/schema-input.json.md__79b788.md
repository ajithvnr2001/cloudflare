---
url: https://developers.cloudflare.com/ai/models/minimax/h3-max/schema-input.json
title: https://developers.cloudflare.com/ai/models/minimax/h3-max/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:38.930798+00:00
---

# https://developers.cloudflare.com/ai/models/minimax/h3-max/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/minimax/h3-max/schema-input.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"content":{"minItems":1,"type":"array","items":{"oneOf":[{"type":"object","properties":{"type":{"type":"string","const":"text"},"text":{"type":"string","minLength":1,"maxLength":7000}},"required":["type","text"],"additionalProperties":false},{"type":"object","properties":{"type":{"type":"string","const":"image_url"},"image_url":{"type":"object","properties":{"url":{"type":"string","minLength":1}},"required":["url"],"additionalProperties":false},"role":{"type":"string","enum":["first_frame","last_frame","reference_image"]}},"required":["type","image_url"],"additionalProperties":false},{"type":"object","properties":{"type":{"type":"string","const":"video_url"},"video_url":{"type":"object","properties":{"url":{"type":"string","minLength":1}},"required":["url"],"additionalProperties":false},"role":{"type":"string","const":"reference_video"}},"required":["type","video_url","role"],"additionalProperties":false},{"type":"object","properties":{"type":{"type":"string","const":"audio_url"},"audio_url":{"type":"object","properties":{"url":{"type":"string","minLength":1}},"required":["url"],"additionalProperties":false},"role":{"type":"string","const":"reference_audio"}},"required":["type","audio_url","role"],"additionalProperties":false}]}},"duration":{"type":"integer","minimum":5,"maximum":15},"ratio":{"type":"string","enum":["adaptive","21:9","16:9","4:3","1:1","3:4","9:16"]},"callback_url":{"type":"string","format":"uri"},"resolution":{"type":"string","enum":["480P","768P"]},"extra":{"type":"object","properties":{"prompt_expansion_mode":{"default":"balanced","type":"string","enum":["disabled","balanced","quality"]}},"required":["prompt_expansion_mode"],"additionalProperties":false}},"required":["content","duration","resolution"],"additionalProperties":false}
