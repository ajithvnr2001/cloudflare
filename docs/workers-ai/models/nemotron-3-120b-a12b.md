---
url: https://developers.cloudflare.com/workers-ai/models/nemotron-3-120b-a12b/
title: nemotron-3-120b-a12b (NVIDIA) \u00b7 Cloudflare AI docs \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:27:15.999684+00:00
---

# nemotron-3-120b-a12b (NVIDIA) · Cloudflare AI docs · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/models/nemotron-3-120b-a12b/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Models



![NVIDIA logo](https://developers.cloudflare.com/_astro/nvidia.DI1bb8hH.svg)

# nemotron-3-120b-a12b

Text Generation • NVIDIA

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/nvidia/nemotron-3-120b-a12b`

  * Cloudflare-hosted
  * Function calling
  * Reasoning



NVIDIA Nemotron 3 Super is a hybrid MoE model with leading accuracy for multi-agent applications and specialized agentic AI systems.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 256,000 tokens  
Terms and License| [link ↗](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license/)  
Function calling [ ↗](https://developers.cloudflare.com/workers-ai/function-calling/)| Yes  
Reasoning| Yes  
Unit Pricing| $0.50 per M input tokens, $1.50 per M output tokens  
  
## Reasoning effort

Nemotron supports normal reasoning, low reasoning, and reasoning turned off. It does not currently select these modes from the top-level`reasoning_effort` field. Pass the corresponding options through `chat_template_kwargs` instead.

To use low reasoning, set both `enable_thinking` and`low_effort`:
    
    
    response = client.chat.completions.create(
        model="@cf/nvidia/nemotron-3-120b-a12b",
        messages=[{"role": "user", "content": "What is the capital of Japan?"}],
        max_tokens=16000,
        temperature=1.0,
        top_p=0.95,
        extra_body={
            "chat_template_kwargs": {
                "enable_thinking": True,
                "low_effort": True,
            }
        },
    )

The low-effort option appends `{reasoning effort: low}` to the latest user message. To turn reasoning off, set`enable_thinking` to `False`. For coding agents, set`force_nonempty_content` to `True` in the same`chat_template_kwargs` object.

For more information, refer to [NVIDIA's Nemotron API client example](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8#api-client).

## Playground

Try out this model with Workers AI LLM Playground. It does not require any setup or authentication and is an instant way to preview and test a model directly in the browser.

[ Launch the LLM Playground ](https://playground.ai.cloudflare.com/?model=@cf/nvidia/nemotron-3-120b-a12b)

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
    
        const stream = await env.AI.run("@cf/nvidia/nemotron-3-120b-a12b", {
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
        const response = await env.AI.run("@cf/nvidia/nemotron-3-120b-a12b", { messages });
    
        return Response.json(response);
      },
    } satisfies ExportedHandler<Env>;
    
    
    import os
    import requests
    
    ACCOUNT_ID = "your-account-id"
    AUTH_TOKEN = os.environ.get("CLOUDFLARE_AUTH_TOKEN")
    
    prompt = "Tell me all about PEP-8"
    response = requests.post(
      f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/nvidia/nemotron-3-120b-a12b",
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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/nvidia/nemotron-3-120b-a12b \
      -X POST \
      -H "Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN" \
      -d '{ "messages": [{ "role": "system", "content": "You are a friendly assistant" }, { "role": "user", "content": "Why is pizza so good" }]}'

OpenAI compatible endpoints

Workers AI also supports OpenAI compatible API endpoints for `/v1/chat/completions` and `/v1/embeddings`. For more details, refer to [Configurations](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/) . 

## Parameters

### Input

model

`string`ID of the model to use (for example, '@cf/nvidia/nemotron-3-120b-a12b').

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

`integer | null`The maximum number of tokens to generate.

max_completion_tokens

`integer | null`An upper bound for the number of tokens that can be generated for a completion.

metadata

`object | null`Set of key-value pairs that can be attached to the object.

modalities

`array | null`Output types requested from the model.

n

`integer | null`How many chat completion choices to generate for each input message.

parallel_tool_calls

`boolean`default: trueWhether to enable parallel function calling during tool use.

▶prediction{}

`object`

presence_penalty

`number | null`Penalizes new tokens based on whether they appear in the text so far.

▶chat_template_kwargs{}

`object`Nemotron chat-template controls for normal reasoning, low-effort reasoning, and non-reasoning responses.

▶response_format

`one of`Specifies the format the model must output.

seed

`integer | null`If specified, the system will make a best effort to sample deterministically.

▶stop

`one of`

store

`boolean | null`Whether to store the output for model distillation or evaluation.

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

prompt

`string`requiredminLength: 1The input text prompt for the model to generate a response.

### Output

Synchronous — Send a request and receive a complete response

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

type

`string`

contentType

`text/event-stream`

format

`binary`

## API Schemas (Raw)

SynchronousInput[](https://developers.cloudflare.com/workers-ai/models/nemotron-3-120b-a12b/sync-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/nemotron-3-120b-a12b/sync-input.json "Download")

SynchronousOutput[](https://developers.cloudflare.com/workers-ai/models/nemotron-3-120b-a12b/sync-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/nemotron-3-120b-a12b/sync-output.json "Download")

StreamingInput[](https://developers.cloudflare.com/workers-ai/models/nemotron-3-120b-a12b/streaming-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/nemotron-3-120b-a12b/streaming-input.json "Download")

StreamingOutput[](https://developers.cloudflare.com/workers-ai/models/nemotron-3-120b-a12b/streaming-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/nemotron-3-120b-a12b/streaming-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
