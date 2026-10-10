---
url: https://developers.cloudflare.com/workers-ai/models/plamo-embedding-1b/
title: plamo-embedding-1b (pfnet) \u00b7 Cloudflare AI docs \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:27:15.616522+00:00
---

# plamo-embedding-1b (pfnet) · Cloudflare AI docs · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/models/plamo-embedding-1b/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Models



p

# plamo-embedding-1b

Text Embeddings • pfnet

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/pfnet/plamo-embedding-1b`

  * Cloudflare-hosted



PLaMo-Embedding-1B is a Japanese text embedding model developed by Preferred Networks, Inc. It can convert Japanese text input into numerical vectors and can be used for a wide range of applications, including information retrieval, text classification, and clustering.

Model Info|   
---|---  
Unit Pricing| $0.0186 per M input tokens  
  
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
          "@cf/pfnet/plamo-embedding-1b",
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
      f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/pfnet/plamo-embedding-1b",
      headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
      json={"text": stories}
    )
    
    print(response.json())
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/pfnet/plamo-embedding-1b  \
      -X POST  \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"  \
      -d '{ "text": ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] }'

OpenAI compatible endpoints

Workers AI also supports OpenAI compatible API endpoints for `/v1/chat/completions` and `/v1/embeddings`. For more details, refer to [Configurations](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/). 

## Parameters

▶text

`one of`required

▶data[]

`array`Embedding vectors, where each vector is a list of floats.

▶shape[]

`array`minItems: 2maxItems: 2Shape of the embedding data as [number_of_embeddings, embedding_dimension].

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/workers-ai/models/plamo-embedding-1b/schema-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/plamo-embedding-1b/schema-input.json "Download")

Output[](https://developers.cloudflare.com/workers-ai/models/plamo-embedding-1b/schema-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/plamo-embedding-1b/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
