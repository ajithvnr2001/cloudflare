---
url: https://developers.cloudflare.com/ai/models/bria/remove-background/schema-input.json
title: https://developers.cloudflare.com/ai/models/bria/remove-background/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:33.108415+00:00
---

# https://developers.cloudflare.com/ai/models/bria/remove-background/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/bria/remove-background/schema-input.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"image":{"type":"string","minLength":1,"description":"JPEG or PNG image (RGB, RGBA, or CMYK), a public URL or base64-encoded image data (a `data:` URI prefix is accepted)."},"preserve_alpha":{"description":"Keep partial transparency from the input alpha channel. When false, every foreground pixel is fully opaque. Default true.","type":"boolean"},"visual_input_content_moderation":{"description":"Reject the request if the input image fails content moderation. Default false.","type":"boolean"},"visual_output_content_moderation":{"description":"Fail the request if the result fails content moderation. Default false.","type":"boolean"}},"required":["image"],"additionalProperties":false}
