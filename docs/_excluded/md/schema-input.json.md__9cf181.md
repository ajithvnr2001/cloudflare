---
url: https://developers.cloudflare.com/ai/models/runwayml/gen-4.5/schema-input.json
title: https://developers.cloudflare.com/ai/models/runwayml/gen-4.5/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:46.603504+00:00
---

# https://developers.cloudflare.com/ai/models/runwayml/gen-4.5/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/runwayml/gen-4.5/schema-input.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"prompt":{"type":"string","minLength":1,"maxLength":1000,"description":"Text prompt describing what should appear in the video"},"image_input":{"description":"HTTPS URL, Runway URI, or data URI containing an image for image-to-video","type":"string"},"ratio":{"default":"1280:720","description":"Resolution/aspect ratio of the output video","type":"string","enum":["1280:720","720:1280","1104:832","960:960","832:1104","1584:672"]},"duration":{"default":5,"description":"Video duration in seconds","type":"integer","minimum":2,"maximum":10},"seed":{"description":"Random seed for reproducible results","type":"integer","minimum":0,"maximum":4294967295},"content_moderation":{"description":"Content moderation settings","type":"object","properties":{"public_figure_threshold":{"description":"Content moderation strictness for public figures","type":"string","enum":["auto","low"]}},"additionalProperties":false}},"required":["prompt","ratio","duration"],"additionalProperties":false}
