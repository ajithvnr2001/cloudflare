---
url: https://developers.cloudflare.com/ai/models/openai/gpt-6-sol/
title: GPT-6 Sol (OpenAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:09.457097+00:00
---

# GPT-6 Sol (OpenAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/openai/gpt-6-sol/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![OpenAI logo](https://developers.cloudflare.com/_astro/openai.BBwNKzBb.svg)

# GPT-6 Sol

Text Generation • OpenAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`openai/gpt-6-sol`

  * Third-party



GPT-6 Sol is OpenAI's mid-tier GPT-6 model, built to power complex coding and agentic workflows.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 1,050,000 tokens  
Terms and License| [link ↗](https://openai.com/policies/)  
More information| [link ↗](https://developers.openai.com/api/docs/models/gpt-6-sol)  
Request formats| Responses, Chat Completions  
Pricing| 

  * Short-context input (per 1M)$2.00
  * Short-context cached input (per 1M)$0.20
  * Short-context cache write (per 1M)$2.50
  * Short-context output (per 1M)$10.00
  * Long-context input (per 1M)$4.00
  * Long-context cached input (per 1M)$0.40
  * Long-context cache write (per 1M)$5.00
  * Long-context output (per 1M)$15.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'openai/gpt-6-sol',
      {
        input:
          'A service has 99.9% monthly availability and just had 31 minutes of downtime. Has it exceeded the monthly error budget for a 30-day month? Show the calculation briefly.',
        max_output_tokens: 512,
        reasoning: { effort: 'high' },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-6-sol",
      "input": "A service has 99.9% monthly availability and just had 31 minutes of downtime. Has it exceeded the monthly error budget for a 30-day month? Show the calculation briefly.",
      "max_output_tokens": 512,
      "reasoning": {
        "effort": "high"
      }
    }'
    
    
    No. A 30-day month has \(30 \times 24 \times 60 = 43{,}200\) minutes, so the 0.1% downtime budget is **43.2 minutes**. After 31 minutes of downtime, **12.2 minutes remain**.
    
    
    {
      "id": "resp_004a362708bc0a44006ab2cc7bd4c487d1bffa1555dc6c5110",
      "object": "response",
      "created_at": 1790102651,
      "status": "completed",
      "access_programs": {
        "cyber": "daybreak_blue"
      },
      "background": false,
      "billing": {
        "payer": "developer"
      },
      "completed_at": 1790102653,
      "error": null,
      "frequency_penalty": 0,
      "incomplete_details": null,
      "instructions": null,
      "max_output_tokens": 512,
      "max_tool_calls": null,
      "model": "gpt-6-sol",
      "moderation": null,
      "output": [
        {
          "id": "rs_004a362708bc0a44006ab2cc7c78bc87d1b3ac1095e5bbaaae",
          "type": "reasoning",
          "content": [],
          "encrypted_content": "gAAAAABqssx9oBJ5yr_VdmObO4zvyzJEasvjs_4xsaXswQG7TjMqx-6kfx_szw29t29TiMj1CMtiWD8IdaVjgznOab6hu0poxB9ZuvgbmIrkgiYx_oqp8UHjtJd06fhkzNaTp01_BBaBQpcwhC9bd_Y6VR8HlvEB1Go4JL7-RLhwh2nJN5wjRjWOlqWaHZRaz1Wz2eQon9IYI8pJ9jpxvYMQpNBle___KLzlJiCjeDKw5yFf9NAjKDwqi75YR4f2uhsWYIfRNgi3Eyzx-h_5dnIahzx1-26Bj_UcRQvUhqf0-0jGmIS1PLg1uSVlHJ7iQsuLJwtcwJYG7X-FYEx61X9BtqtiUFODxRODCUpq3RMrZKUm6N9BtNwqB1PkLR6Y5gCyhWPAdf77zvcxGJKncLGIduS4Fei5u3lJTg8NlDpFC5sFNUu6wEmBV3Mz3e_uCo3B2bHVFNAFcK8h-nnvj3hM6EYbVTRnXlaFrb2Fb51_TvZBQ1ReAPmz9nQcdb9bIZRBeRIN7PAKChmwgS4gYD_r3IE3k4q8CWBHOPzzxHeQzOSPgameIHzXR13uc9dy-gBD8o2wWChw616xhktHemPEUZG4l2AIBVSJNuFKIoGS_jT_P7ScPZwynxwS3wSGuyCLa3qAPkZWeP7qqfZQmtDKWj0xnjyipbOGoDQh5pAPtkIMdKIsMBj12RY_Ms-sYB7ojN1vOhUWeN-2MXPDkBmxY_L58hUjNVyLbYo1TUQsZVQX5r0tT0o3_9GI7aAa-vgMz_hXFJ4QepBtzc2hlGDT6CKp5tt235fisry5k0xaMAsl9ae6o-yEn0KDeLmpeIICZX6vDgqIZjPny7D_jpmHNZPLYkC56kQL2xaLI695l3GuMkeV6S5kphxK1y-5yyEJ9lasAT2aEwTIFSQ1fjdMwb9QjCpDXL-w-fUMxAfy_u8LapQBH5aV6XH5L2No4VKP-0IDrstrfh38LEEm9sBt55zVBQ2-UpB_DYy-BsG4Qn77cpDVaKC3MHXBbMhYWaNc6vJ1zsLaUhO2AgH7QW8sCRHexDRb1QO9NRXbp9Y-HSOIV8UxFEXjxbUV_dPxYUABNioPutzYq54kqnJc8ekT45AN-CRgviXVG9824m20cjEz1ryvnVNIKmen_ysou2W98MQqIch2Hh4cqgCkBxOyh7iYTqSS8LhGoJqAtGRgK7XlV8sB-q3xEDLEsW5cD_irRuVzh5Bb1ofy4emT2HNeoYUNdA9SLvpZfK9c8jCHr01ia4NzGrjwSBn4fzujX-eCPoYaN2MLQ2N8mp1cfYGH35LDIhmCjA==",
          "summary": []
        },
        {
          "id": "msg_004a362708bc0a44006ab2cc7ca89487d1a80f11a6def484c5",
          "type": "message",
          "status": "completed",
          "content": [
            {
              "type": "output_text",
              "annotations": [],
              "logprobs": [],
              "text": "No. A 30-day month has \\(30 \\times 24 \\times 60 = 43{,}200\\) minutes, so the 0.1% downtime budget is **43.2 minutes**. After 31 minutes of downtime, **12.2 minutes remain**."
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
      "prompt_cache_retention": "24h",
      "reasoning": {
        "context": "all_turns",
        "effort": "high",
        "mode": "standard",
        "summary": null
      },
      "safety_identifier": null,
      "service_tier": "default",
      "store": true,
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
        "input_tokens": 44,
        "input_tokens_details": {
          "cache_write_tokens": 0,
          "cached_tokens": 0
        },
        "output_tokens": 103,
        "output_tokens_details": {
          "reasoning_tokens": 36
        },
        "total_tokens": 147
      },
      "user": null,
      "metadata": {}
    }

## Examples

**Migration Safeguards** — Generate a concise answer through Chat Completions
    
    
    const response = await env.AI.run(
      'openai/gpt-6-sol',
      {
        messages: [
          { role: 'user', content: 'List three practical safeguards for a production API migration.' },
        ],
        max_completion_tokens: 256,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-6-sol",
      "messages": [
        {
          "role": "user",
          "content": "List three practical safeguards for a production API migration."
        }
      ],
      "max_completion_tokens": 256
    }'
    
    
    1. **Preserve compatibility:** Version breaking changes and run contract tests against existing clients.
    2. **Roll out gradually:** Start with a canary or small percentage of traffic, and monitor errors, latency, and key business metrics.
    3. **Prepare a rollback:** Keep the previous API deployable, back up data, and rehearse how to reverse any schema changes.
    
    
    {
      "id": "chatcmpl-EQzlOt1nlzMH6eShi7U8iGaHTJByy",
      "object": "chat.completion",
      "created": 1790102654,
      "model": "gpt-6-sol",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "1. **Preserve compatibility:** Version breaking changes and run contract tests against existing clients.\n2. **Roll out gradually:** Start with a canary or small percentage of traffic, and monitor errors, latency, and key business metrics.\n3. **Prepare a rollback:** Keep the previous API deployable, back up data, and rehearse how to reverse any schema changes.",
            "refusal": null,
            "annotations": []
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 16,
        "completion_tokens": 118,
        "total_tokens": 134,
        "prompt_tokens_details": {
          "cached_tokens": 0,
          "cache_write_tokens": 0,
          "audio_tokens": 0
        },
        "completion_tokens_details": {
          "reasoning_tokens": 34,
          "audio_tokens": 0,
          "accepted_prediction_tokens": 0,
          "rejected_prediction_tokens": 0
        }
      },
      "service_tier": "default",
      "system_fingerprint": null
    }

## Parameters

Schema variant

ResponsesChat Completions

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

▶messages[]

`array`required

temperature

`number`minimum: 0maximum: 2

max_tokens

`number`exclusiveMinimum: 0

max_completion_tokens

`number`exclusiveMinimum: 0

top_p

`number`minimum: 0maximum: 1

frequency_penalty

`number`minimum: -2maximum: 2

presence_penalty

`number`minimum: -2maximum: 2

stream

`boolean`

▶stream_options{}

`object`

▶tools[]

`array`

tool_choice

``

response_format

``

▶modalities[]

`array`

▶audio{}

`object`

reasoning_effort

`string`Optional reasoning control; availability and accepted values are model-dependent.

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

id

`string`

object

`string`

created

`number`

model

`string`

▶choices[]

`array`

▶usage{}

`object`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/openai/gpt-6-sol/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-6-sol/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/openai/gpt-6-sol/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-6-sol/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
