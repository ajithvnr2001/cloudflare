---
url: https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/
title: kimi-k2.7-code (Moonshot AI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:04.105381+00:00
---

# kimi-k2.7-code (Moonshot AI) · Cloudflare AI docs · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Models



![Moonshot AI logo](https://developers.cloudflare.com/_astro/moonshotai.DjWMkXUS.svg)

# kimi-k2.7-code

Text Generation • Moonshot AI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/moonshotai/kimi-k2.7-code`

  * Cloudflare-hosted
  * Function calling
  * Reasoning
  * Vision



Kimi K2.7 is a frontier-scale open-source 1T parameter model with a 262.1k context window, multi-turn tool calling, vision inputs, and structured outputs for agentic workloads.

Paid access required

This model is not available through standard Workers Free billing. To use it, upgrade to the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) or use prepaid [AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/).

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 262,144 tokens  
Terms and License| [link ↗](https://huggingface.co/moonshotai/Kimi-K2.7-Code/blob/main/LICENSE)  
Function calling [ ↗](https://developers.cloudflare.com/workers-ai/function-calling/)| Yes  
Reasoning| Always on  
Vision| Yes  
Unit Pricing| $0.95 per M input tokens, $4.00 per M output tokens, $0.19 per M cached input tokens  
  
## Playground

Try out this model with Workers AI LLM Playground. It does not require any setup or authentication and is an instant way to preview and test a model directly in the browser.

[ Launch the LLM Playground ](https://playground.ai.cloudflare.com/?model=@cf/moonshotai/kimi-k2.7-code)

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
    
        const stream = await env.AI.run("@cf/moonshotai/kimi-k2.7-code", {
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
        const response = await env.AI.run("@cf/moonshotai/kimi-k2.7-code", { messages });
    
        return Response.json(response);
      },
    } satisfies ExportedHandler<Env>;
    
    
    import os
    import requests
    
    ACCOUNT_ID = "your-account-id"
    AUTH_TOKEN = os.environ.get("CLOUDFLARE_AUTH_TOKEN")
    
    prompt = "Tell me all about PEP-8"
    response = requests.post(
      f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/moonshotai/kimi-k2.7-code",
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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/moonshotai/kimi-k2.7-code \
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

model

`string`ID of the model to use (e.g. '@cf/zai-org/glm-4.7-flash, etc').

▶audio{}

`object`Parameters for audio output. Required when modalities includes 'audio'.

frequency_penalty

`number | null`Penalizes new tokens based on their existing frequency in the text so far.

logit_bias

`object | null`Modify the likelihood of specified tokens appearing in the completion. Maps token IDs to bias values from -100 to 100.

logprobs

`boolean | null`Whether to return log probabilities of the output tokens.

top_logprobs

`integer | null`How many top log probabilities to return at each token position (0-20). Requires logprobs=true.

max_tokens

`integer | null`Deprecated in favor of max_completion_tokens. The maximum number of tokens to generate.

max_completion_tokens

`integer | null`An upper bound for the number of tokens that can be generated for a completion.

metadata

`object | null`Set of 16 key-value pairs that can be attached to the object.

modalities

`array | null`Output types requested from the model (e.g. ['text'] or ['text', 'audio']).

n

`integer | null`How many chat completion choices to generate for each input message.

parallel_tool_calls

`boolean`default: trueWhether to enable parallel function calling during tool use.

▶prediction{}

`object`

presence_penalty

`number | null`Penalizes new tokens based on whether they appear in the text so far.

▶chat_template_kwargs{}

`object`

▶response_format

`one of`Specifies the format the model must output.

seed

`integer | null`If specified, the system will make a best effort to sample deterministically.

▶stop

`one of`

store

`boolean | null`Whether to store the output for model distillation / evals.

stream

`boolean | null`If true, partial message deltas will be sent as server-sent events.

▶stream_options{}

`object`

temperature

`number | null`Sampling temperature between 0 and 2.

▶tool_choice

`one of`Controls which (if any) tool is called by the model. 'none' = no tools, 'auto' = model decides, 'required' = must call a tool.

▶tools[]

`array`A list of tools the model may call.

top_p

`number | null`Nucleus sampling: considers the results of the tokens with top_p probability mass.

user

`string`A unique identifier representing your end-user, for abuse monitoring.

▶web_search_options{}

`object`Options for the web search tool (when using built-in web search).

▶function_call

`one of`

▶functions[]

`array`minItems: 1maxItems: 128

id

`string`A unique identifier for the chat completion.

object

`string`

created

`integer`Unix timestamp (seconds) of when the completion was created.

model

`string`The model used for the chat completion.

▶choices[]

`array`minItems: 1

▶usage{}

`object`

system_fingerprint

`string | null`

Streaming — Send a request with `stream: true` and receive server-sent events

Input format

Prompt

Simple text input for single-turn interactions

Messages

Structured conversation format with roles (user, assistant, system)

prompt

`string`requiredminLength: 1The input text prompt for the model to generate a response.

model

`string`ID of the model to use (e.g. '@cf/zai-org/glm-4.7-flash, etc').

▶audio{}

`object`Parameters for audio output. Required when modalities includes 'audio'.

frequency_penalty

`number | null`Penalizes new tokens based on their existing frequency in the text so far.

logit_bias

`object | null`Modify the likelihood of specified tokens appearing in the completion. Maps token IDs to bias values from -100 to 100.

logprobs

`boolean | null`Whether to return log probabilities of the output tokens.

top_logprobs

`integer | null`How many top log probabilities to return at each token position (0-20). Requires logprobs=true.

max_tokens

`integer | null`Deprecated in favor of max_completion_tokens. The maximum number of tokens to generate.

max_completion_tokens

`integer | null`An upper bound for the number of tokens that can be generated for a completion.

metadata

`object | null`Set of 16 key-value pairs that can be attached to the object.

modalities

`array | null`Output types requested from the model (e.g. ['text'] or ['text', 'audio']).

n

`integer | null`How many chat completion choices to generate for each input message.

parallel_tool_calls

`boolean`default: trueWhether to enable parallel function calling during tool use.

▶prediction{}

`object`

presence_penalty

`number | null`Penalizes new tokens based on whether they appear in the text so far.

▶chat_template_kwargs{}

`object`

▶response_format

`one of`Specifies the format the model must output.

seed

`integer | null`If specified, the system will make a best effort to sample deterministically.

▶stop

`one of`

store

`boolean | null`Whether to store the output for model distillation / evals.

stream

`boolean | null`If true, partial message deltas will be sent as server-sent events.

▶stream_options{}

`object`

temperature

`number | null`Sampling temperature between 0 and 2.

▶tool_choice

`one of`Controls which (if any) tool is called by the model. 'none' = no tools, 'auto' = model decides, 'required' = must call a tool.

▶tools[]

`array`A list of tools the model may call.

top_p

`number | null`Nucleus sampling: considers the results of the tokens with top_p probability mass.

user

`string`A unique identifier representing your end-user, for abuse monitoring.

▶web_search_options{}

`object`Options for the web search tool (when using built-in web search).

▶function_call

`one of`

▶functions[]

`array`minItems: 1maxItems: 128

type

`string`

contentType

`text/event-stream`

format

`binary`

Batch — Send multiple requests in a single API call

▶requests[]

`array`

id

`string`A unique identifier for the chat completion.

object

`string`

created

`integer`Unix timestamp (seconds) of when the completion was created.

model

`string`The model used for the chat completion.

▶choices[]

`array`minItems: 1

▶usage{}

`object`

system_fingerprint

`string | null`

## API Schemas (Raw)

SynchronousInput[](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/sync-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/sync-input.json "Download")

SynchronousOutput[](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/sync-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/sync-output.json "Download")

StreamingInput[](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/streaming-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/streaming-input.json "Download")

StreamingOutput[](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/streaming-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/streaming-output.json "Download")

BatchInput[](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/batch-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/batch-input.json "Download")

BatchOutput[](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/batch-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/batch-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
