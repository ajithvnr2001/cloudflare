---
url: https://developers.cloudflare.com/ai/models/bria/fibo-edit-1.5/schema-output.json
title: https://developers.cloudflare.com/ai/models/bria/fibo-edit-1.5/schema-output.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:32.845343+00:00
---

# https://developers.cloudflare.com/ai/models/bria/fibo-edit-1.5/schema-output.json

> Source: https://developers.cloudflare.com/ai/models/bria/fibo-edit-1.5/schema-output.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"image":{"type":"string","format":"uri","description":"URL of the edited image. Bria hosts it for a limited time (3 days by default); download it to keep it."},"seed":{"description":"Seed used for this image.","type":"integer","minimum":-9007199254740991,"maximum":9007199254740991},"structured_instruction":{"description":"Structured (VGL) edit instruction used for this image, as a JSON string.","type":"string"},"warning":{"description":"Present when `ip_signal` flagged the instruction as possibly IP-protected.","type":"string"}},"required":["image"],"additionalProperties":false}
