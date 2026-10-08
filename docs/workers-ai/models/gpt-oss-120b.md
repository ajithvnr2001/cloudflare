---
url: https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/
title: gpt-oss-120b (OpenAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:03.969269+00:00
---

# gpt-oss-120b (OpenAI) · Cloudflare AI docs · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Models



![OpenAI logo](https://developers.cloudflare.com/_astro/openai.BBwNKzBb.svg)

# gpt-oss-120b

Text Generation • OpenAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/openai/gpt-oss-120b`

  * Cloudflare-hosted
  * Batch
  * Function calling
  * Reasoning



OpenAI’s open-weight models designed for powerful reasoning, agentic tasks, and versatile developer use cases – gpt-oss-120b is for production, general purpose, high reasoning use-cases.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 128,000 tokens  
Function calling [ ↗](https://developers.cloudflare.com/workers-ai/function-calling/)| Yes  
Reasoning| `low``medium` (default)`high`  
Batch| Yes  
Unit Pricing| $0.35 per M input tokens, $0.75 per M output tokens  
  
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
    
        const stream = await env.AI.run("@cf/openai/gpt-oss-120b", {
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
        const response = await env.AI.run("@cf/openai/gpt-oss-120b", { messages });
    
        return Response.json(response);
      },
    } satisfies ExportedHandler<Env>;
    
    
    import os
    import requests
    
    ACCOUNT_ID = "your-account-id"
    AUTH_TOKEN = os.environ.get("CLOUDFLARE_AUTH_TOKEN")
    
    prompt = "Tell me all about PEP-8"
    response = requests.post(
      f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/openai/gpt-oss-120b",
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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/openai/gpt-oss-120b \
      -X POST \
      -H "Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN" \
      -d '{ "messages": [{ "role": "system", "content": "You are a friendly assistant" }, { "role": "user", "content": "Why is pizza so good" }]}'

OpenAI compatible endpoints

Workers AI also supports OpenAI compatible API endpoints for `/v1/chat/completions` and `/v1/embeddings`. For more details, refer to [Configurations](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/) . 

## Parameters

Synchronous — Send a request and receive a complete response

Input format

Prompt

Simple text input for single-turn interactions

Messages

Structured conversation format with roles (user, assistant, system)

prompt

`string`requiredminLength: 1The input text prompt for the model to generate a response.

lora

`string`Name of the LoRA (Low-Rank Adaptation) model to fine-tune the base model.

▶response_format{}

`object`

raw

`boolean`default: falseIf true, a chat template is not applied and you must adhere to the specific model's expected formatting.

stream

`boolean`default: falseIf true, the response will be streamed back incrementally using SSE, Server Sent Events.

max_tokens

`integer`default: 256The maximum number of tokens to generate in the response.

temperature

`number`default: 0.6minimum: 0maximum: 5Controls the randomness of the output; higher values produce more random results.

top_p

`number`minimum: 0.001maximum: 1Adjusts the creativity of the AI's responses by controlling how many possible words it considers. Lower values make outputs more predictable; higher values allow for more varied and creative responses.

top_k

`integer`minimum: 1maximum: 50Limits the AI to choose from the top 'k' most probable words. Lower values make responses more focused; higher values introduce more variety and potential surprises.

seed

`integer`minimum: 1maximum: 9999999999Random seed for reproducibility of the generation.

repetition_penalty

`number`minimum: 0maximum: 2Penalty for repeated tokens; higher values discourage repetition.

frequency_penalty

`number`minimum: -2maximum: 2Decreases the likelihood of the model repeating the same lines verbatim.

presence_penalty

`number`minimum: -2maximum: 2Increases the likelihood of the model introducing new topics.

type

`object`

contentType

`application/json`

Streaming — Send a request with `stream: true` and receive server-sent events

Input format

Prompt

Simple text input for single-turn interactions

Messages

Structured conversation format with roles (user, assistant, system)

prompt

`string`requiredminLength: 1The input text prompt for the model to generate a response.

lora

`string`Name of the LoRA (Low-Rank Adaptation) model to fine-tune the base model.

▶response_format{}

`object`

raw

`boolean`default: falseIf true, a chat template is not applied and you must adhere to the specific model's expected formatting.

stream

`boolean`default: falseIf true, the response will be streamed back incrementally using SSE, Server Sent Events.

max_tokens

`integer`default: 256The maximum number of tokens to generate in the response.

temperature

`number`default: 0.6minimum: 0maximum: 5Controls the randomness of the output; higher values produce more random results.

top_p

`number`minimum: 0.001maximum: 1Adjusts the creativity of the AI's responses by controlling how many possible words it considers. Lower values make outputs more predictable; higher values allow for more varied and creative responses.

top_k

`integer`minimum: 1maximum: 50Limits the AI to choose from the top 'k' most probable words. Lower values make responses more focused; higher values introduce more variety and potential surprises.

seed

`integer`minimum: 1maximum: 9999999999Random seed for reproducibility of the generation.

repetition_penalty

`number`minimum: 0maximum: 2Penalty for repeated tokens; higher values discourage repetition.

frequency_penalty

`number`minimum: -2maximum: 2Decreases the likelihood of the model repeating the same lines verbatim.

presence_penalty

`number`minimum: -2maximum: 2Increases the likelihood of the model introducing new topics.

type

`string`

contentType

`text/event-stream`

format

`binary`

Batch — Send multiple requests in a single API call

▶requests[]

`array`required

type

`object`

contentType

`application/json`

## API Schemas (Raw)

SynchronousInput[](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/sync-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/sync-input.json "Download")

SynchronousOutput[](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/sync-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/sync-output.json "Download")

StreamingInput[](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/streaming-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/streaming-input.json "Download")

StreamingOutput[](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/streaming-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/streaming-output.json "Download")

BatchInput[](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/batch-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/batch-input.json "Download")

BatchOutput[](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/batch-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/batch-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
