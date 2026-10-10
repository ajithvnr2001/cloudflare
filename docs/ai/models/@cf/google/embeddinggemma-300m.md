---
url: https://developers.cloudflare.com/ai/models/%40cf/google/embeddinggemma-300m/
title: embeddinggemma-300m (Google) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:22.342343+00:00
---

# embeddinggemma-300m (Google) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/%40cf/google/embeddinggemma-300m/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Google logo](https://developers.cloudflare.com/_astro/google.DyXKPTPP.svg)

# embeddinggemma-300m

Beta

Text Embeddings • Google

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/google/embeddinggemma-300m`

  * Cloudflare-hosted



EmbeddingGemma is a 300M parameter, state-of-the-art for its size, open embedding model from Google, built from Gemma 3 (with T5Gemma initialization) and the same research and technology used to create Gemini models. EmbeddingGemma produces vector representations of text, making it well-suited for search and retrieval tasks, including classification, clustering, and semantic similarity search. This model was trained with data in 100+ spoken languages.

Model Info|   
---|---  
Beta| Yes  
  
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
          "@cf/google/embeddinggemma-300m",
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
      f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/google/embeddinggemma-300m",
      headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
      json={"text": stories}
    )
    
    print(response.json())
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/google/embeddinggemma-300m  \
      -X POST  \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"  \
      -d '{ "text": ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] }'

OpenAI compatible endpoints

Workers AI also supports OpenAI compatible API endpoints for `/v1/chat/completions` and `/v1/embeddings`. For more details, refer to [Configurations](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/). 

## Parameters

▶text

`one of`required

▶shape[]

`array`

▶data[]

`array`Embeddings of the requested text values

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/@cf/google/embeddinggemma-300m/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/google/embeddinggemma-300m/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/@cf/google/embeddinggemma-300m/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/google/embeddinggemma-300m/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
