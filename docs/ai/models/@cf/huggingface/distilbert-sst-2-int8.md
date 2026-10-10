---
url: https://developers.cloudflare.com/ai/models/%40cf/huggingface/distilbert-sst-2-int8/
title: distilbert-sst-2-int8 (HuggingFace) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:22.370082+00:00
---

# distilbert-sst-2-int8 (HuggingFace) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/%40cf/huggingface/distilbert-sst-2-int8/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![HuggingFace logo](https://developers.cloudflare.com/_astro/huggingface.DMS-v5TA.svg)

# distilbert-sst-2-int8

Text Classification • HuggingFace

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/huggingface/distilbert-sst-2-int8`

  * Cloudflare-hosted



Distilled BERT model that was finetuned on SST-2 for sentiment classification

Model Info|   
---|---  
More information| [link ↗](https://huggingface.co/Intel/distilbert-base-uncased-finetuned-sst-2-english-int8-static)  
Unit Pricing| $0.0263 per M input tokens  
  
## Usage
    
    
    export interface Env {
      AI: Ai;
    }
    
    export default {
      async fetch(request, env): Promise<Response> {
    
        const response = await env.AI.run(
          "@cf/huggingface/distilbert-sst-2-int8",
          {
            text: "This pizza is great!",
          }
        );
    
        return Response.json(response);
      },
    } satisfies ExportedHandler<Env>;
    
    
    API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/"
    headers = {"Authorization": "Bearer {API_KEY}"}
    
    def run(model, input):
        response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
        return response.json()
    
    output = run("@cf/huggingface/distilbert-sst-2-int8", { "text": "This pizza is great!" })
    print(output)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/huggingface/distilbert-sst-2-int8  \
      -X POST  \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"  \
      -d '{ "text": "This pizza is great!" }'

## Parameters

text

`string`requiredminLength: 1The text that you want to classify

type

`array`

contentType

`application/json`

description

`An array of classification results for the input text`

items

`[object Object]`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/@cf/huggingface/distilbert-sst-2-int8/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/huggingface/distilbert-sst-2-int8/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/@cf/huggingface/distilbert-sst-2-int8/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/huggingface/distilbert-sst-2-int8/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
