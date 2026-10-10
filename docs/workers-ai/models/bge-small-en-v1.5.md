---
url: https://developers.cloudflare.com/workers-ai/models/bge-small-en-v1.5/
title: bge-small-en-v1.5 (BAAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:24.003906+00:00
---

# bge-small-en-v1.5 (BAAI) · Cloudflare AI docs · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/models/bge-small-en-v1.5/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Models



![BAAI logo](https://developers.cloudflare.com/_astro/baai.BooZR_xF.svg)

# bge-small-en-v1.5

Text Embeddings • BAAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/baai/bge-small-en-v1.5`

  * Cloudflare-hosted
  * Batch



BAAI general embedding (Small) model that transforms any given text into a 384-dimensional vector

Model Info|   
---|---  
More information| [link ↗](https://huggingface.co/BAAI/bge-small-en-v1.5)  
Maximum Input Tokens| 512  
Output Dimensions| 384  
Batch| Yes  
Unit Pricing| $0.0202 per M input tokens  
  
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
          "@cf/baai/bge-small-en-v1.5",
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
      f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/baai/bge-small-en-v1.5",
      headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
      json={"text": stories}
    )
    
    print(response.json())
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/baai/bge-small-en-v1.5  \
      -X POST  \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"  \
      -d '{ "text": ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] }'

OpenAI compatible endpoints

Workers AI also supports OpenAI compatible API endpoints for `/v1/chat/completions` and `/v1/embeddings`. For more details, refer to [Configurations](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/). 

## Parameters

Synchronous — Send a request and receive a complete response

▶text

`one of`required

pooling

`string`default: meanenum: mean, clsThe pooling method used in the embedding process. `cls` pooling will generate more accurate embeddings on larger inputs - however, embeddings created with cls pooling are not compatible with embeddings generated with mean pooling. The default pooling method is `mean` in order for this to not be a breaking change, but we highly suggest using the new `cls` pooling for better accuracy.

▶shape[]

`array`

▶data[]

`array`Embeddings of the requested text values

pooling

`string`enum: mean, clsThe pooling method used in the embedding process.

Batch — Send multiple requests in a single API call

▶requests[]

`array`requiredBatch of the embeddings requests to run using async-queue

▶shape[]

`array`

▶data[]

`array`Embeddings of the requested text values

pooling

`string`enum: mean, clsThe pooling method used in the embedding process.

## API Schemas (Raw)

SynchronousInput[](https://developers.cloudflare.com/workers-ai/models/bge-small-en-v1.5/sync-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/bge-small-en-v1.5/sync-input.json "Download")

SynchronousOutput[](https://developers.cloudflare.com/workers-ai/models/bge-small-en-v1.5/sync-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/bge-small-en-v1.5/sync-output.json "Download")

BatchInput[](https://developers.cloudflare.com/workers-ai/models/bge-small-en-v1.5/batch-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/bge-small-en-v1.5/batch-input.json "Download")

BatchOutput[](https://developers.cloudflare.com/workers-ai/models/bge-small-en-v1.5/batch-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/bge-small-en-v1.5/batch-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
