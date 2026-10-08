---
url: https://developers.cloudflare.com/ai/models/pruna/p-video-animate/schema-input.json
title: https://developers.cloudflare.com/ai/models/pruna/p-video-animate/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:44.482166+00:00
---

# https://developers.cloudflare.com/ai/models/pruna/p-video-animate/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/pruna/p-video-animate/schema-input.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"video":{"type":"string","description":"Source RGB video (.mp4) used as the motion and audio source. HTTP(S) URL or data URI."},"image":{"type":"string","description":"Reference image of the subject to animate. HTTP(S) URL or data URI."},"turbo":{"default":false,"description":"Turbo mode: faster generation for slightly lower quality.","type":"boolean"},"resolution":{"default":"720p","description":"Target resolution.","type":"string","enum":["720p","1080p"]},"save_audio":{"default":true,"description":"Save the video with audio.","type":"boolean"},"ignore_audio":{"default":false,"description":"Ignore source audio during generation.","type":"boolean"},"target_fps":{"default":"original","description":"Target FPS for the working video.","type":"string","enum":["24","48","original"]},"instruction_prompt":{"default":"","description":"Further instruction on how the reference subject should be animated.","type":"string"},"seed":{"description":"Random seed for reproducible generation.","type":"integer","minimum":-9007199254740991,"maximum":9007199254740991},"disable_safety_checker":{"default":false,"description":"Disable safety checker for generated videos.","type":"boolean"}},"required":["video","image","turbo","resolution","save_audio","ignore_audio","target_fps","instruction_prompt","disable_safety_checker"],"additionalProperties":{}}
