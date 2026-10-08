---
url: https://developers.cloudflare.com/ai/models/xai/grok-imagine-video-1.5-preview/schema-input.json
title: https://developers.cloudflare.com/ai/models/xai/grok-imagine-video-1.5-preview/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:49.245299+00:00
---

# https://developers.cloudflare.com/ai/models/xai/grok-imagine-video-1.5-preview/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/xai/grok-imagine-video-1.5-preview/schema-input.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"_operation":{"type":"string","enum":["generate","edit","extend"]},"prompt":{"type":"string"},"duration":{"type":"integer","minimum":1,"maximum":15},"aspect_ratio":{"type":"string","enum":["1:1","16:9","9:16","4:3","3:4","3:2","2:3"]},"resolution":{"type":"string","enum":["480p","720p"]},"size":{"type":"string","enum":["848x480","1696x960","1280x720","1920x1080"]},"image":{"type":"object","properties":{"url":{"type":"string"}},"required":["url"],"additionalProperties":false},"video":{"type":"object","properties":{"url":{"type":"string"}},"required":["url"],"additionalProperties":false},"reference_images":{"maxItems":10,"type":"array","items":{"type":"object","properties":{"url":{"type":"string"}},"required":["url"],"additionalProperties":false}},"output":{"type":"object","properties":{"upload_url":{"type":"string"}},"required":["upload_url"],"additionalProperties":false},"user":{"type":"string"}},"additionalProperties":false}
