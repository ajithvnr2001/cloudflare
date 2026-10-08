---
url: https://developers.cloudflare.com/ai/models/%40cf/baai/bge-m3/
title: bge-m3 (BAAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:44.472348+00:00
---

# bge-m3 (BAAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/%40cf/baai/bge-m3/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![BAAI logo](https://developers.cloudflare.com/_astro/baai.BooZR_xF.svg)

# bge-m3

Text Embeddings • BAAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/%40cf/baai/bge-m3/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/baai/bge-m3`

  * Cloudflare-hosted



Multi-Functionality, Multi-Linguality, and Multi-Granularity embeddings model.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 60,000 tokens  
Unit Pricing| $0.0118 per M input tokens  
  
## Usage
    
    
    export interface Env {
      AI: Ai;
    }
    
    export default {
      async fetch(request, env): Promise<Response> {
    
        // Can be a string or array of strings]
        const stories = [
          "This is a story about an orange cloud",
          "This is a story about a llama",
          "This is a story about a hugging emoji",
        ];
    
        const embeddings = await env.AI.run(
          "@cf/baai/bge-m3",
          {
            text: stories,
          }
        );
    
        return Response.json(embeddings);
      },
    } satisfies ExportedHandler<Env>;
    
    
    import os
    import requests
    
    
    ACCOUNT_ID = "your-account-id"
    AUTH_TOKEN = os.environ.get("CLOUDFLARE_AUTH_TOKEN")
    
    stories = [
      'This is a story about an orange cloud',
      'This is a story about a llama',
      'This is a story about a hugging emoji'
    ]
    
    response = requests.post(
      f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/baai/bge-m3",
      headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
      json={"text": stories}
    )
    
    print(response.json())
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/baai/bge-m3  \
      -X POST  \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"  \
      -d '{ "text": ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] }'

OpenAI compatible endpoints

Workers AI also supports OpenAI compatible API endpoints for `/v1/chat/completions` and `/v1/embeddings`. For more details, refer to [Configurations](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/). 

## Parameters

Synchronous — Send a request and receive a complete response

query

`string`minLength: 1A query you wish to perform against the provided contexts. If no query is provided the model with respond with embeddings for contexts

▶contexts[]

`array`requiredList of provided contexts. Note that the index in this array is important, as the response will refer to it.

truncate_inputs

`boolean`default: falseWhen provided with too long context should the model error out or truncate the context to fit?

request_id

`string`The async request id that can be used to obtain the results.

Batch — Send multiple requests in a single API call

▶requests[]

`array`requiredBatch of the embeddings requests to run using async-queue

request_id

`string`The async request id that can be used to obtain the results.

## API Schemas (Raw)

SynchronousInput[](https://developers.cloudflare.com/ai/models/@cf/baai/bge-m3/sync-input.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/baai/bge-m3/sync-input.json "Download")

SynchronousOutput[](https://developers.cloudflare.com/ai/models/@cf/baai/bge-m3/sync-output.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/baai/bge-m3/sync-output.json "Download")

BatchInput[](https://developers.cloudflare.com/ai/models/@cf/baai/bge-m3/batch-input.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/baai/bge-m3/batch-input.json "Download")

BatchOutput[](https://developers.cloudflare.com/ai/models/@cf/baai/bge-m3/batch-output.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/baai/bge-m3/batch-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
