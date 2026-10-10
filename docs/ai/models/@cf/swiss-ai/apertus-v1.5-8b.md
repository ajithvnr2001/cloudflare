---
url: https://developers.cloudflare.com/ai/models/%40cf/swiss-ai/apertus-v1.5-8b/
title: apertus-v1.5-8b (swiss-ai) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:19.915488+00:00
---

# apertus-v1.5-8b (swiss-ai) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/%40cf/swiss-ai/apertus-v1.5-8b/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



s

# apertus-v1.5-8b

Text Generation • swiss-ai

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/swiss-ai/apertus-v1.5-8b`

  * Cloudflare-hosted
  * Function calling
  * Vision



Apertus 1.5 is an 8B parameter language model designed to advance the state of multilingual, multimodal, fully open, and transparent AI. The models support a wide range of languages, handle contexts of up to 262,144 tokens, and it uses only fully open training data whilst delivering performance comparable to other models of similar size. For access, please fill out this form: https://forms.gle/kgvmkr6ucHN3xNuH6

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 262,144 tokens  
Function calling [ ↗](https://developers.cloudflare.com/workers-ai/function-calling/)| Yes  
Vision| Yes  
  
## Playground

Try out this model with Workers AI LLM Playground. It does not require any setup or authentication and is an instant way to preview and test a model directly in the browser.

[ Launch the LLM Playground ](https://playground.ai.cloudflare.com/?model=@cf/swiss-ai/apertus-v1.5-8b)

## Usage
    
    
    export interface Env {
      AI: Ai;
    }
    
    export default {
      async fetch(request, env): Promise<Response> {
    
        const messages = [
          { role: "system", content: "You are a friendly assistant" },
          {
            role: "user",
            content: "What is the origin of the phrase Hello, World",
          },
        ];
    
        const stream = await env.AI.run("@cf/swiss-ai/apertus-v1.5-8b", {
          messages,
          stream: true,
        });
    
        return new Response(stream, {
          headers: { "content-type": "text/event-stream" },
        });
      },
    } satisfies ExportedHandler<Env>;
    
    
    export interface Env {
      AI: Ai;
    }
    
    export default {
      async fetch(request, env): Promise<Response> {
    
        const messages = [
          { role: "system", content: "You are a friendly assistant" },
          {
            role: "user",
            content: "What is the origin of the phrase Hello, World",
          },
        ];
        const response = await env.AI.run("@cf/swiss-ai/apertus-v1.5-8b", { messages });
    
        return Response.json(response);
      },
    } satisfies ExportedHandler<Env>;
    
    
    import os
    import requests
    
    ACCOUNT_ID = "your-account-id"
    AUTH_TOKEN = os.environ.get("CLOUDFLARE_AUTH_TOKEN")
    
    prompt = "Tell me all about PEP-8"
    response = requests.post(
      f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/swiss-ai/apertus-v1.5-8b",
        headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
        json={
          "messages": [
            {"role": "system", "content": "You are a friendly assistant"},
            {"role": "user", "content": prompt}
          ]
        }
    )
    result = response.json()
    print(result)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/swiss-ai/apertus-v1.5-8b \
      -X POST \
      -H "Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN" \
      -d '{ "messages": [{ "role": "system", "content": "You are a friendly assistant" }, { "role": "user", "content": "Why is pizza so good" }]}'

OpenAI compatible endpoints

Workers AI also supports OpenAI compatible API endpoints for `/v1/chat/completions` and `/v1/embeddings`. For more details, refer to [Configurations](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/) . 

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
