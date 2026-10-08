---
url: https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3/schema-input.json
title: https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3/schema-input.json
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (725 chars), fallback to crawl4ai)
fetched_at: 2026-10-08T07:23:40.937112+00:00
---

# https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3/schema-input.json


```
{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"prompt":{"type":"string","maxLength":2000},"first_frame_image":{"type":"string"},"prompt_optimizer":{"default":true,"type":"boolean"},"fast_pretreatment":{"default":false,"type":"boolean"},"duration":{"default":6,"anyOf":[{"type":"number","const":6},{"type":"number","const":10}]},"resolution":{"default":"768P","type":"string","enum":["768P","1080P"]}},"required":["prompt_optimizer","fast_pretreatment","duration","resolution"],"additionalProperties":false}
```

