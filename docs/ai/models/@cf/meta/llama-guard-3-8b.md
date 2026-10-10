---
url: https://developers.cloudflare.com/ai/models/%40cf/meta/llama-guard-3-8b/
title: llama-guard-3-8b (Meta) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:21.728504+00:00
---

# llama-guard-3-8b (Meta) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/%40cf/meta/llama-guard-3-8b/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Meta logo](https://developers.cloudflare.com/_astro/meta.CTzB_ysm.svg)

# llama-guard-3-8b

Text Generation • Meta

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/meta/llama-guard-3-8b`

  * Cloudflare-hosted
  * LoRA



Llama Guard 3 is a Llama-3.1-8B pretrained model, fine-tuned for content safety classification. Similar to previous versions, it can be used to classify content in both LLM inputs (prompt classification) and in LLM responses (response classification). It acts as an LLM – it generates text in its output that indicates whether a given prompt or response is safe or unsafe, and if unsafe, it also lists the content categories violated.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 131,072 tokens  
LoRA| Yes  
Unit Pricing| $0.484 per M input tokens, $0.03 per M output tokens  
  
## Playground

Try out this model with Workers AI LLM Playground. It does not require any setup or authentication and is an instant way to preview and test a model directly in the browser.

[ Launch the LLM Playground ](https://playground.ai.cloudflare.com/?model=@cf/meta/llama-guard-3-8b)

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
    
        const stream = await env.AI.run("@cf/meta/llama-guard-3-8b", {
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
        const response = await env.AI.run("@cf/meta/llama-guard-3-8b", { messages });
    
        return Response.json(response);
      },
    } satisfies ExportedHandler<Env>;
    
    
    import os
    import requests
    
    ACCOUNT_ID = "your-account-id"
    AUTH_TOKEN = os.environ.get("CLOUDFLARE_AUTH_TOKEN")
    
    prompt = "Tell me all about PEP-8"
    response = requests.post(
      f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/meta/llama-guard-3-8b",
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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/meta/llama-guard-3-8b \
      -X POST \
      -H "Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN" \
      -d '{ "messages": [{ "role": "system", "content": "You are a friendly assistant" }, { "role": "user", "content": "Why is pizza so good" }]}'

OpenAI compatible endpoints

Workers AI also supports OpenAI compatible API endpoints for `/v1/chat/completions` and `/v1/embeddings`. For more details, refer to [Configurations](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/) . 

## Parameters

▶messages[]

`array`requiredAn array of message objects representing the conversation history.

max_tokens

`integer`default: 256The maximum number of tokens to generate in the response.

temperature

`number`default: 0.6minimum: 0maximum: 5Controls the randomness of the output; higher values produce more random results.

▶response_format{}

`object`Dictate the output format of the generated response.

▶response

`one of`

▶usage{}

`object`Usage statistics for the inference request

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/@cf/meta/llama-guard-3-8b/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/meta/llama-guard-3-8b/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/@cf/meta/llama-guard-3-8b/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/meta/llama-guard-3-8b/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
