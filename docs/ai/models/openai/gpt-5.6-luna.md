---
url: https://developers.cloudflare.com/ai/models/openai/gpt-5.6-luna/
title: GPT-5.6 Luna (OpenAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:02.178434+00:00
---

# GPT-5.6 Luna (OpenAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/openai/gpt-5.6-luna/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![OpenAI logo](https://developers.cloudflare.com/_astro/openai.BBwNKzBb.svg)

# GPT-5.6 Luna

Text Generation • OpenAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/openai/gpt-5.6-luna/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`openai/gpt-5.6-luna`

  * Third-party



GPT-5.6 Luna is an OpenAI GPT-5.6 model optimized for cost-sensitive workloads, using the Responses API for efficient text generation.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 1,050,000 tokens  
Terms and License| [link ↗](https://openai.com/policies/)  
More information| [link ↗](https://openai.com/)  
Request formats| Responses  
Pricing| 

  * Input (per 1M tokens)$0.20
  * Output (per 1M tokens)$1.20
  * Cached input (per 1M tokens)$0.02
  * Cache creation (per 1M tokens)$0.25

  
  
## Usage
    
    
    const response = await env.AI.run(
      'openai/gpt-5.6-luna',
      {
        input: 'Summarize the benefits of API rate limiting in three bullets.',
        max_output_tokens: 256,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-5.6-luna",
      "input": "Summarize the benefits of API rate limiting in three bullets.",
      "max_output_tokens": 256
    }'
    
    
    - **Protects system stability:** Prevents overload, reduces outages, and ensures predictable performance during traffic spikes.
    - **Ensures fair access:** Stops individual users or applications from consuming disproportionate resources.
    - **Improves security and cost control:** Helps mitigate abuse, brute-force attacks, and unexpected infrastructure usage.
    
    
    {
      "id": "resp_0e481f0cb46bf357016a4fe99bd5fc8194b6ce2049aa65ab08",
      "object": "response",
      "created_at": 1783622043,
      "status": "completed",
      "background": false,
      "billing": {
        "payer": "developer"
      },
      "completed_at": 1783622044,
      "error": null,
      "frequency_penalty": 0,
      "incomplete_details": null,
      "instructions": null,
      "max_output_tokens": 256,
      "max_tool_calls": null,
      "model": "gpt-5.6-luna",
      "moderation": null,
      "output": [
        {
          "id": "msg_0e481f0cb46bf357016a4fe99c2e288194a6fd0ce3f5f88786",
          "type": "message",
          "status": "completed",
          "content": [
            {
              "type": "output_text",
              "annotations": [],
              "logprobs": [],
              "text": "- **Protects system stability:** Prevents overload, reduces outages, and ensures predictable performance during traffic spikes.\n- **Ensures fair access:** Stops individual users or applications from consuming disproportionate resources.\n- **Improves security and cost control:** Helps mitigate abuse, brute-force attacks, and unexpected infrastructure usage."
            }
          ],
          "phase": "final_answer",
          "role": "assistant"
        }
      ],
      "parallel_tool_calls": true,
      "presence_penalty": 0,
      "previous_response_id": null,
      "prompt_cache_key": null,
      "prompt_cache_retention": "in_memory",
      "reasoning": {
        "context": "all_turns",
        "effort": "medium",
        "mode": "standard",
        "summary": null
      },
      "safety_identifier": null,
      "service_tier": "default",
      "store": false,
      "temperature": 1,
      "text": {
        "format": {
          "type": "text"
        },
        "verbosity": "medium"
      },
      "tool_choice": "auto",
      "tool_usage": {
        "image_gen": {
          "input_tokens": 0,
          "input_tokens_details": {
            "image_tokens": 0,
            "text_tokens": 0
          },
          "output_tokens": 0,
          "output_tokens_details": {
            "image_tokens": 0,
            "text_tokens": 0
          },
          "total_tokens": 0
        },
        "web_search": {
          "num_requests": 0
        }
      },
      "tools": [],
      "top_logprobs": 0,
      "top_p": 0.98,
      "truncation": "disabled",
      "usage": {
        "input_tokens": 19,
        "input_tokens_details": {
          "cache_write_tokens": 0,
          "cached_tokens": 0
        },
        "output_tokens": 66,
        "output_tokens_details": {
          "reasoning_tokens": 0
        },
        "total_tokens": 85
      },
      "user": null,
      "metadata": {}
    }

## Examples

**Pull Request Description** — Using instructions for a cost-sensitive drafting task
    
    
    const response = await env.AI.run(
      'openai/gpt-5.6-luna',
      {
        input:
          'Write a brief pull request description for a bug fix that prevents duplicate webhook deliveries.',
        instructions: 'Keep it under 100 words.',
        max_output_tokens: 256,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-5.6-luna",
      "input": "Write a brief pull request description for a bug fix that prevents duplicate webhook deliveries.",
      "instructions": "Keep it under 100 words.",
      "max_output_tokens": 256
    }'
    
    
    ## Summary
    Prevents duplicate webhook deliveries by ensuring each event is processed only once, even when retries or concurrent requests occur.
    
    ## Changes
    - Added idempotency checks for webhook events.
    - Prevented duplicate delivery attempts.
    - Added regression tests covering retries and concurrent processing.
    
    ## Testing
    All existing and new tests pass.
    
    
    {
      "id": "resp_0bed05adeda548a1016a4fe99d1e408194bb0375bad96ab71a",
      "object": "response",
      "created_at": 1783622045,
      "status": "completed",
      "background": false,
      "billing": {
        "payer": "developer"
      },
      "completed_at": 1783622046,
      "error": null,
      "frequency_penalty": 0,
      "incomplete_details": null,
      "instructions": "Keep it under 100 words.",
      "max_output_tokens": 256,
      "max_tool_calls": null,
      "model": "gpt-5.6-luna",
      "moderation": null,
      "output": [
        {
          "id": "msg_0bed05adeda548a1016a4fe99daa748194992854423ba08e72",
          "type": "message",
          "status": "completed",
          "content": [
            {
              "type": "output_text",
              "annotations": [],
              "logprobs": [],
              "text": "## Summary\nPrevents duplicate webhook deliveries by ensuring each event is processed only once, even when retries or concurrent requests occur.\n\n## Changes\n- Added idempotency checks for webhook events.\n- Prevented duplicate delivery attempts.\n- Added regression tests covering retries and concurrent processing.\n\n## Testing\nAll existing and new tests pass."
            }
          ],
          "phase": "final_answer",
          "role": "assistant"
        }
      ],
      "parallel_tool_calls": true,
      "presence_penalty": 0,
      "previous_response_id": null,
      "prompt_cache_key": null,
      "prompt_cache_retention": "in_memory",
      "reasoning": {
        "context": "all_turns",
        "effort": "medium",
        "mode": "standard",
        "summary": null
      },
      "safety_identifier": null,
      "service_tier": "default",
      "store": false,
      "temperature": 1,
      "text": {
        "format": {
          "type": "text"
        },
        "verbosity": "medium"
      },
      "tool_choice": "auto",
      "tool_usage": {
        "image_gen": {
          "input_tokens": 0,
          "input_tokens_details": {
            "image_tokens": 0,
            "text_tokens": 0
          },
          "output_tokens": 0,
          "output_tokens_details": {
            "image_tokens": 0,
            "text_tokens": 0
          },
          "total_tokens": 0
        },
        "web_search": {
          "num_requests": 0
        }
      },
      "tools": [],
      "top_logprobs": 0,
      "top_p": 0.98,
      "truncation": "disabled",
      "usage": {
        "input_tokens": 33,
        "input_tokens_details": {
          "cache_write_tokens": 0,
          "cached_tokens": 0
        },
        "output_tokens": 69,
        "output_tokens_details": {
          "reasoning_tokens": 0
        },
        "total_tokens": 102
      },
      "user": null,
      "metadata": {}
    }

## Parameters

▶input

`one of`required

instructions

`string`

temperature

`number`minimum: 0maximum: 2

max_output_tokens

`number`exclusiveMinimum: 0

top_p

`number`minimum: 0maximum: 1

stream

`boolean`

▶tools[]

`array`

tool_choice

``

▶text{}

`object`

▶reasoning{}

`object`

id

`string`

object

`string`const: response

created_at

`number`

model

`string`

▶output[]

`array`

output_text

`string`

status

`string`enum: in_progress, completed, failed, incomplete

▶usage{}

`object`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/openai/gpt-5.6-luna/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-5.6-luna/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/openai/gpt-5.6-luna/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-5.6-luna/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
