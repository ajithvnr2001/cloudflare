---
url: https://developers.cloudflare.com/ai/models/@cf/microsoft/resnet-50/schema-input.json
title: https://developers.cloudflare.com/ai/models/@cf/microsoft/resnet-50/schema-input.json
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-08T07:23:22.630597+00:00
---

# https://developers.cloudflare.com/ai/models/@cf/microsoft/resnet-50/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/@cf/microsoft/resnet-50/schema-input.json


```
{"oneOf":[{"type":"string","format":"binary","description":"The image to classify"},{"type":"object","properties":{"image":{"type":"array","description":"An array of integers that represent the image data constrained to 8-bit unsigned integer values","items":{"type":"number","description":"A value between 0 and 255 (unsigned 8bit)"}}},"required":["image"]}]}
```

