---
url: https://developers.cloudflare.com/ai/models/minimax/h3-max/schema-output.json
title: https://developers.cloudflare.com/ai/models/minimax/h3-max/schema-output.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:39.002136+00:00
---

# https://developers.cloudflare.com/ai/models/minimax/h3-max/schema-output.json

> Source: https://developers.cloudflare.com/ai/models/minimax/h3-max/schema-output.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"task":{"type":"object","properties":{"id":{"type":"string"},"model":{"type":"string"},"status":{"type":"string","enum":["queued","running","succeeded","failed","cancelled"]},"error":{"type":"object","properties":{"code":{"type":"string"},"message":{"type":"string"}},"required":["code","message"],"additionalProperties":false},"created_at":{"type":"integer","minimum":-9007199254740991,"maximum":9007199254740991},"updated_at":{"type":"integer","minimum":-9007199254740991,"maximum":9007199254740991},"content":{"type":"object","properties":{"url":{"type":"string","format":"uri"},"prompt":{"type":"string"}},"additionalProperties":false},"resolution":{"type":"string"},"duration":{"type":"integer","minimum":-9007199254740991,"maximum":9007199254740991},"usage":{"type":"object","properties":{"total_seconds":{"type":"integer","minimum":-9007199254740991,"maximum":9007199254740991},"input_seconds":{"type":"integer","minimum":-9007199254740991,"maximum":9007199254740991},"output_seconds":{"type":"integer","minimum":-9007199254740991,"maximum":9007199254740991},"input_image_count":{"type":"integer","minimum":-9007199254740991,"maximum":9007199254740991},"input_audio_seconds":{"type":"integer","minimum":-9007199254740991,"maximum":9007199254740991},"total_tokens":{"type":"integer","minimum":-9007199254740991,"maximum":9007199254740991},"prompt_tokens":{"type":"integer","minimum":-9007199254740991,"maximum":9007199254740991},"completion_tokens":{"type":"integer","minimum":-9007199254740991,"maximum":9007199254740991}},"additionalProperties":false},"ratio":{"type":"string"},"task_type":{"type":"string","enum":["generation","regeneration","h3_context_ir"]},"modality":{"type":"string","enum":["video","text"]}},"required":["id","model","status","created_at","updated_at"],"additionalProperties":{}}},"required":["task"],"additionalProperties":false}
