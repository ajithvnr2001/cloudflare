---
url: https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3-fast/schema-input.json
title: https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3-fast/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:39.413002+00:00
---

# https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3-fast/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3-fast/schema-input.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"first_frame_image":{"type":"string","description":"URL or base64 data URI of the first frame image"},"prompt":{"type":"string","maxLength":2000},"prompt_optimizer":{"default":true,"type":"boolean"},"fast_pretreatment":{"default":false,"type":"boolean"},"duration":{"default":6,"anyOf":[{"type":"number","const":6},{"type":"number","const":10}]},"resolution":{"default":"768P","type":"string","enum":["768P","1080P"]}},"required":["first_frame_image","prompt_optimizer","fast_pretreatment","duration","resolution"],"additionalProperties":false}
