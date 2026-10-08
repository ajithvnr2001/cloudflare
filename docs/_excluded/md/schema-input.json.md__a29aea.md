---
url: https://developers.cloudflare.com/ai/models/@cf/black-forest-labs/flux-1-schnell/schema-input.json
title: https://developers.cloudflare.com/ai/models/@cf/black-forest-labs/flux-1-schnell/schema-input.json
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-08T07:23:15.224157+00:00
---

# https://developers.cloudflare.com/ai/models/@cf/black-forest-labs/flux-1-schnell/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/@cf/black-forest-labs/flux-1-schnell/schema-input.json


```
{"type":"object","properties":{"prompt":{"type":"string","minLength":1,"maxLength":2048,"description":"A text description of the image you want to generate."},"steps":{"type":"integer","maximum":8,"description":"The number of diffusion steps; higher values can improve quality but take longer. Default is 4"}},"required":["prompt"],"additionalProperties":false}
```

