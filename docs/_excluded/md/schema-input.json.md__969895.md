---
url: https://developers.cloudflare.com/ai/models/bria/v-rmbg-3.0/schema-input.json
title: https://developers.cloudflare.com/ai/models/bria/v-rmbg-3.0/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:33.105980+00:00
---

# https://developers.cloudflare.com/ai/models/bria/v-rmbg-3.0/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/bria/v-rmbg-3.0/schema-input.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"video":{"type":"string","format":"uri","description":"Public URL of the input video: MP4, MOV, WEBM, AVI, or GIF, up to 60 seconds and 16000x16000."},"background_color":{"description":"Color that replaces the removed background; set it explicitly. Transparent needs the mov_proresks preset: with any other preset Bria uses Black and returns a `warning`.","type":"string","enum":["Transparent","Black","White","Gray","Red","Green","Blue","Yellow","Cyan","Magenta","Orange"]},"output_container_and_codec":{"description":"Output container and codec. Default mp4_h264. mov_proresks (ProRes) is the preset that keeps transparency.","type":"string","enum":["mp4_h264","mp4_h265","mov_h265","mov_proresks"]},"auto_zoom":{"description":"Crop once to the subject for the whole video. Output resolution and aspect ratio may change, and processing is slower. Default false.","type":"boolean"},"preserve_audio":{"description":"Keep the input audio track. Default true.","type":"boolean"},"spill_suppression":{"description":"Strength of green-fringe removal for green-screen footage, from 0 (off) to 1. Default 0.","type":"number","minimum":0,"maximum":1}},"required":["video"],"additionalProperties":false}
