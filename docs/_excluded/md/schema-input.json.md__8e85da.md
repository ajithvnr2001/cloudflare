---
url: https://developers.cloudflare.com/ai/models/@cf/ai4bharat/indictrans2-en-indic-1B/schema-input.json
title: https://developers.cloudflare.com/ai/models/@cf/ai4bharat/indictrans2-en-indic-1B/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:10.120738+00:00
---

# https://developers.cloudflare.com/ai/models/@cf/ai4bharat/indictrans2-en-indic-1B/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/@cf/ai4bharat/indictrans2-en-indic-1B/schema-input.json

{"type":"object","properties":{"text":{"oneOf":[{"type":"string"},{"type":"array","items":{"type":"string"}}],"description":"Input text to translate. Can be a single string or a list of strings."},"target_language":{"type":"string","enum":["asm_Beng","awa_Deva","ben_Beng","bho_Deva","brx_Deva","doi_Deva","eng_Latn","gom_Deva","gon_Deva","guj_Gujr","hin_Deva","hne_Deva","kan_Knda","kas_Arab","kas_Deva","kha_Latn","lus_Latn","mag_Deva","mai_Deva","mal_Mlym","mar_Deva","mni_Beng","mni_Mtei","npi_Deva","ory_Orya","pan_Guru","san_Deva","sat_Olck","snd_Arab","snd_Deva","tam_Taml","tel_Telu","urd_Arab","unr_Deva"],"default":"hin_Deva","description":"Target langauge to translate to"}},"required":["text","target_language"]}
