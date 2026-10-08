---
url: https://developers.cloudflare.com/ai/models/@cf/deepgram/aura-2-en/schema-input.json
title: https://developers.cloudflare.com/ai/models/@cf/deepgram/aura-2-en/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:15.661019+00:00
---

# https://developers.cloudflare.com/ai/models/@cf/deepgram/aura-2-en/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/@cf/deepgram/aura-2-en/schema-input.json

{"type":"object","properties":{"speaker":{"type":"string","enum":["amalthea","andromeda","apollo","arcas","aries","asteria","athena","atlas","aurora","callista","cora","cordelia","delia","draco","electra","harmonia","helena","hera","hermes","hyperion","iris","janus","juno","jupiter","luna","mars","minerva","neptune","odysseus","ophelia","orion","orpheus","pandora","phoebe","pluto","saturn","thalia","theia","vesta","zeus"],"default":"luna","description":"Speaker used to produce the audio."},"encoding":{"type":"string","enum":["linear16","flac","mulaw","alaw","mp3","opus","aac"],"description":"Encoding of the output audio."},"container":{"type":"string","enum":["none","wav","ogg"],"description":"Container specifies the file format wrapper for the output audio. The available options depend on the encoding type.."},"text":{"type":"string","description":"The text content to be converted to speech"},"sample_rate":{"type":"number","description":"Sample Rate specifies the sample rate for the output audio. Based on the encoding, different sample rates are supported. For some encodings, the sample rate is not configurable"},"bit_rate":{"type":"number","description":"The bitrate of the audio in bits per second. Choose from predefined ranges or specific values based on the encoding type."}}}
