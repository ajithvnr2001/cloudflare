---
url: https://developers.cloudflare.com/ai/models/%40cf/qwen/qwq-32b/
title: qwq-32b (Qwen) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:20.454712+00:00
---

# qwq-32b (Qwen) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/%40cf/qwen/qwq-32b/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Qwen logo](https://developers.cloudflare.com/_astro/qwen.ByCZjtXU.svg)

# qwq-32b

Text Generation • Qwen

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/qwen/qwq-32b`

  * Cloudflare-hosted
  * LoRA
  * Reasoning



QwQ is the reasoning model of the Qwen series. Compared with conventional instruction-tuned models, QwQ, which is capable of thinking and reasoning, can achieve significantly enhanced performance in downstream tasks, especially hard problems. QwQ-32B is the medium-sized reasoning model, which is capable of achieving competitive performance against state-of-the-art reasoning models, e.g., DeepSeek-R1, o1-mini.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 24,000 tokens  
Reasoning| Yes  
LoRA| Yes  
Unit Pricing| $0.66 per M input tokens, $1.00 per M output tokens  
  
## Playground

Try out this model with Workers AI LLM Playground. It does not require any setup or authentication and is an instant way to preview and test a model directly in the browser.

[ Launch the LLM Playground ](https://playground.ai.cloudflare.com/?model=@cf/qwen/qwq-32b)

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
    
        const stream = await env.AI.run("@cf/qwen/qwq-32b", {
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
        const response = await env.AI.run("@cf/qwen/qwq-32b", { messages });
    
        return Response.json(response);
      },
    } satisfies ExportedHandler<Env>;
    
    
    import os
    import requests
    
    ACCOUNT_ID = "your-account-id"
    AUTH_TOKEN = os.environ.get("CLOUDFLARE_AUTH_TOKEN")
    
    prompt = "Tell me all about PEP-8"
    response = requests.post(
      f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/qwen/qwq-32b",
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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/qwen/qwq-32b \
      -X POST \
      -H "Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN" \
      -d '{ "messages": [{ "role": "system", "content": "You are a friendly assistant" }, { "role": "user", "content": "Why is pizza so good" }]}'

OpenAI compatible endpoints

Workers AI also supports OpenAI compatible API endpoints for `/v1/chat/completions` and `/v1/embeddings`. For more details, refer to [Configurations](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/) . 

## Parameters

### Input

prompt

`string`requiredminLength: 1The input text prompt for the model to generate a response.

guided_json{}

`object`JSON schema that should be fulfilled for the response.

raw

`boolean`default: falseIf true, a chat template is not applied and you must adhere to the specific model's expected formatting.

stream

`boolean`default: falseIf true, the response will be streamed back incrementally using SSE, Server Sent Events.

max_tokens

`integer`default: 256The maximum number of tokens to generate in the response.

temperature

`number`default: 0.15minimum: 0maximum: 5Controls the randomness of the output; higher values produce more random results.

top_p

`number`minimum: 0maximum: 2Adjusts the creativity of the AI's responses by controlling how many possible words it considers. Lower values make outputs more predictable; higher values allow for more varied and creative responses.

top_k

`integer`minimum: 1maximum: 50Limits the AI to choose from the top 'k' most probable words. Lower values make responses more focused; higher values introduce more variety and potential surprises.

seed

`integer`minimum: 1maximum: 9999999999Random seed for reproducibility of the generation.

repetition_penalty

`number`minimum: 0maximum: 2Penalty for repeated tokens; higher values discourage repetition.

frequency_penalty

`number`minimum: 0maximum: 2Decreases the likelihood of the model repeating the same lines verbatim.

presence_penalty

`number`minimum: 0maximum: 2Increases the likelihood of the model introducing new topics.

### Output

Synchronous — Send a request and receive a complete response

response

`string`The generated text response from the model

▶usage{}

`object`Usage statistics for the inference request

▶tool_calls[]

`array`An array of tool calls requests made during the response generation

Streaming — Send a request with `stream: true` and receive server-sent events

type

`string`

contentType

`text/event-stream`

format

`binary`

## API Schemas (Raw)

SynchronousInput[](https://developers.cloudflare.com/ai/models/@cf/qwen/qwq-32b/sync-input.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/qwen/qwq-32b/sync-input.json "Download")

SynchronousOutput[](https://developers.cloudflare.com/ai/models/@cf/qwen/qwq-32b/sync-output.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/qwen/qwq-32b/sync-output.json "Download")

StreamingInput[](https://developers.cloudflare.com/ai/models/@cf/qwen/qwq-32b/streaming-input.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/qwen/qwq-32b/streaming-input.json "Download")

StreamingOutput[](https://developers.cloudflare.com/ai/models/@cf/qwen/qwq-32b/streaming-output.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/qwen/qwq-32b/streaming-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
