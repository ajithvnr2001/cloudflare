---
url: https://developers.cloudflare.com/ai/models/google/veo-3.1-fast/schema-input.json
title: https://developers.cloudflare.com/ai/models/google/veo-3.1-fast/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:37.580582+00:00
---

# https://developers.cloudflare.com/ai/models/google/veo-3.1-fast/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/google/veo-3.1-fast/schema-input.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"prompt":{"type":"string","description":"Text prompt describing the video to generate"},"image_input":{"description":"Base64-encoded reference image for i2v","type":"string"},"duration":{"default":"6s","description":"Video duration","type":"string","enum":["4s","6s","8s"]},"aspect_ratio":{"default":"16:9","description":"Video aspect ratio","type":"string","enum":["16:9","9:16","1:1"]},"resolution":{"default":"720p","description":"Video resolution","type":"string","enum":["720p","1080p"]},"generate_audio":{"default":true,"description":"Whether to generate audio with the video","type":"boolean"}},"required":["prompt","duration","aspect_ratio","resolution","generate_audio"],"additionalProperties":false}
