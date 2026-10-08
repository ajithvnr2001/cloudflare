---
url: https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-vector/schema-input.json
title: https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-vector/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:46.883316+00:00
---

# https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-vector/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-vector/schema-input.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"prompt":{"type":"string"},"size":{"type":"string"},"style":{"type":"string"},"substyle":{"type":"string"},"controls":{"type":"object","properties":{"colors":{"maxItems":5,"type":"array","items":{"type":"object","properties":{"rgb":{"minItems":3,"maxItems":3,"type":"array","items":{"type":"integer","minimum":0,"maximum":255}}},"required":["rgb"],"additionalProperties":false}},"background_color":{"type":"object","properties":{"rgb":{"minItems":3,"maxItems":3,"type":"array","items":{"type":"integer","minimum":0,"maximum":255}}},"required":["rgb"],"additionalProperties":false}},"additionalProperties":false}},"required":["prompt"],"additionalProperties":false}
