---
url: https://developers.cloudflare.com/ai/models/bria/fibo-generate-1.5/schema-output.json
title: https://developers.cloudflare.com/ai/models/bria/fibo-generate-1.5/schema-output.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:32.884342+00:00
---

# https://developers.cloudflare.com/ai/models/bria/fibo-generate-1.5/schema-output.json

> Source: https://developers.cloudflare.com/ai/models/bria/fibo-generate-1.5/schema-output.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"image":{"type":"string","format":"uri","description":"URL of the generated image. Bria hosts it for a limited time (3 days by default); download it to keep it."},"seed":{"description":"Seed used for this image.","type":"integer","minimum":-9007199254740991,"maximum":9007199254740991},"structured_prompt":{"description":"Structured (VGL) prompt used for this image, as a JSON string. Pass it back with `seed` to recreate or refine the image.","type":"string"},"warning":{"description":"Present when `ip_signal` flagged the prompt as possibly IP-protected.","type":"string"}},"required":["image"],"additionalProperties":false}
