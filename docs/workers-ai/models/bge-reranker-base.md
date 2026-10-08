---
url: https://developers.cloudflare.com/workers-ai/models/bge-reranker-base/
title: bge-reranker-base (BAAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:01.710552+00:00
---

# bge-reranker-base (BAAI) · Cloudflare AI docs · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/models/bge-reranker-base/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Models



![BAAI logo](https://developers.cloudflare.com/_astro/baai.BooZR_xF.svg)

# bge-reranker-base

Text Classification • BAAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/models/bge-reranker-base/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/baai/bge-reranker-base`

  * Cloudflare-hosted



Different from embedding model, reranker uses question and document as input and directly output similarity instead of embedding. You can get a relevance score by inputting query and passage to the reranker. And the score can be mapped to a float value in [0,1] by sigmoid function. 

Model Info|   
---|---  
Unit Pricing| $0.00311 per M input tokens  
  
## Usage
    
    
    export interface Env {
    	AI: Ai;
    }
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		const query = 'Which one is cooler?'
    		const contexts = [
    			{
    				text: 'a cyberpunk lizzard'
    			},
    			{
    				text: 'a cyberpunk cat'
    			}
    		];
    
    		const response = await env.AI.run('@cf/baai/bge-reranker-base', { query, contexts });
    
    		return Response.json(response);
    	},
    } satisfies ExportedHandler<Env>;
    
    
    
    import os
    import requests
    
    ACCOUNT_ID = "your-account-id"
    AUTH_TOKEN = os.environ.get("CLOUDFLARE_AUTH_TOKEN")
    
    response = requests.post(
      f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/baai/bge-reranker-base",
        headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
        json={
    	  "query": "Which one is better?",
          "contexts": [
            {"text": "a cyberpunk lizzard"},
    		    {"text": "a cyberpunk car"},
          ]
        }
    )
    result = response.json()
    print(result)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/baai/bge-reranker-base \
      -X POST \
      -H "Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN" \
      -d '{ "query": "Which one is better?", "contexts": [{ "text": "a cyberpunk lizzard" }, {"text": "a cyberpunk cat"}]}'

## Parameters

query

`string`requiredminLength: 1A query you wish to perform against the provided contexts.

top_k

`integer`minimum: 1Number of returned results starting with the best score.

▶contexts[]

`array`requiredList of provided contexts. Note that the index in this array is important, as the response will refer to it.

▶response[]

`array`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/workers-ai/models/bge-reranker-base/schema-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/bge-reranker-base/schema-input.json "Download")

Output[](https://developers.cloudflare.com/workers-ai/models/bge-reranker-base/schema-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/bge-reranker-base/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
