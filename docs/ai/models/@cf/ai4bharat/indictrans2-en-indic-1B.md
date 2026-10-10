---
url: https://developers.cloudflare.com/ai/models/%40cf/ai4bharat/indictrans2-en-indic-1B/
title: indictrans2-en-indic-1B (ai4bharat) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:23.571473+00:00
---

# indictrans2-en-indic-1B (ai4bharat) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/%40cf/ai4bharat/indictrans2-en-indic-1B/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



a

# indictrans2-en-indic-1B

Translation • ai4bharat

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/ai4bharat/indictrans2-en-indic-1B`

  * Cloudflare-hosted



IndicTrans2 is the first open-source transformer-based multilingual NMT model that supports high-quality translations across all the 22 scheduled Indic languages

Model Info|   
---|---  
Unit Pricing| $0.342 per M input tokens, $0.342 per M output tokens  
  
## Usage
    
    
    export interface Env {
      AI: Ai;
    }
    
    export default {
      async fetch(request, env): Promise<Response> {
    
        const response = await env.AI.run(
          "@cf/ai4bharat/indictrans2-en-indic-1B",
          {
            text: "Hello, how are you?",
            target_language: "hin_Deva",
          }
        );
    
        return new Response(JSON.stringify(response));
      },
    } satisfies ExportedHandler<Env>;
    
    
    import requests
    
    API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/"
    headers = {"Authorization": "Bearer {API_TOKEN}"}
    
    def run(model, input):
        response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
        return response.json()
    
    output = run('@cf/ai4bharat/indictrans2-en-indic-1B', {
      "text": "Hello, how are you?",
      "target_language": "hin_Deva"
    })
    
    print(output)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/ai4bharat/indictrans2-en-indic-1B  \
        -X POST  \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"  \
        -d '{ "text": "Hello, how are you?", "target_language": "hin_Deva" }'

## Parameters

▶text

`one of`required

target_language

`string`requireddefault: hin_Devaenum: asm_Beng, awa_Deva, ben_Beng, bho_Deva, brx_Deva, doi_Deva, eng_Latn, gom_Deva, gon_Deva, guj_Gujr, hin_Deva, hne_Deva, kan_Knda, kas_Arab, kas_Deva, kha_Latn, lus_Latn, mag_Deva, mai_Deva, mal_Mlym, mar_Deva, mni_Beng, mni_Mtei, npi_Deva, ory_Orya, pan_Guru, san_Deva, sat_Olck, snd_Arab, snd_Deva, tam_Taml, tel_Telu, urd_Arab, unr_DevaTarget langauge to translate to

▶translations[]

`array`Translated texts

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/@cf/ai4bharat/indictrans2-en-indic-1B/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/ai4bharat/indictrans2-en-indic-1B/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/@cf/ai4bharat/indictrans2-en-indic-1B/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/ai4bharat/indictrans2-en-indic-1B/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
