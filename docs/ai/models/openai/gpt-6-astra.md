---
url: https://developers.cloudflare.com/ai/models/openai/gpt-6-astra/
title: GPT-6 Astra (OpenAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:02.820882+00:00
---

# GPT-6 Astra (OpenAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/openai/gpt-6-astra/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![OpenAI logo](https://developers.cloudflare.com/_astro/openai.BBwNKzBb.svg)

# GPT-6 Astra

Text Generation • OpenAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/openai/gpt-6-astra/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`openai/gpt-6-astra`

  * Third-party



GPT-6 Astra is OpenAI's most capable model, built for complex reasoning, coding, computer use, research, and document creation.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 1,050,000 tokens  
Terms and License| [link ↗](https://openai.com/policies/)  
More information| [link ↗](https://developers.openai.com/api/docs/models/gpt-6-astra)  
Request formats| Responses, Chat Completions  
Pricing| 

  * Short-context input (per 1M)$10.00
  * Short-context cached input (per 1M)$1.00
  * Short-context cache write (per 1M)$12.00
  * Short-context output (per 1M)$50.00
  * Long-context input (per 1M)$20.00
  * Long-context cached input (per 1M)$2.00
  * Long-context cache write (per 1M)$25.00
  * Long-context output (per 1M)$75.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'openai/gpt-6-astra',
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
      "model": "openai/gpt-6-astra",
      "input": "A service has 99.9% monthly availability and just had 31 minutes of downtime. Has it exceeded the monthly error budget for a 30-day month? Show the calculation briefly.",
      "max_output_tokens": 512,
      "reasoning": {
        "effort": "high"
      }
    }'
    
    
    No. For a 30-day month:
    
    - Total time: \(30 \times 24 \times 60 = 43{,}200\) minutes
    - Error budget: \(43{,}200 \times (1 - 0.999) = 43.2\) minutes
    - Remaining budget: \(43.2 - 31 = 12.2\) minutes
    
    Assuming 31 minutes is the total downtime this month, it is **within the error budget**.
    
    
    {
      "id": "resp_0f4dd4f38f19eb60016a99d9b6aaec87d1ab6bb0c344527fbc",
      "object": "response",
      "created_at": 1788467638,
      "model": "gpt-6-astra",
      "output": [
        {
          "id": "rs_0f4dd4f38f19eb60016a99d9b77c6087d1ab41b79ccdf5a833",
          "type": "reasoning",
          "content": [],
          "encrypted_content": "gAAAAABqmdm5bNo3TE240J65AqELJf45m_Forsch1ik0e0iiz5B-XZsvljWjY5PfmKXyel-6WvdoKmKulsRo3PX0fCqdNQFUaSYufMITZh61KSdsWBeeKRAwczgj8ihQBEbSF95MmTwkoQzsHX5SBitcf0n7CrMhXt8-LcE2tXqY309dnpgzAtjeI8H318LR1JyAWKsbver3s30gE1TRh0GC3YisTLrfACSclHB8_cOPA5QvEwKJNljm8R7eVDJx7LTFoB2Av93eaSD7l4fbAJzR_afL8K_Akj5NsjYaZVrsbPPxTYlYpqRhE0c-3C2U0oJ31-4UVa6_nT94QYtnDJ9YNjEdRC8sMkq6DwLhkbIIJGVNJGqHmWP3vQu3JCq9VDUtC3ss3FCkgWwhIV5tAFTFOtppnHenz1Xi2UYwaBNwaHWYJdrTBidNcpEQwPcIdSRAfOHv2r-ueFywhAZmj8Rx_GcJO_5_RWjvglhuNRBTbC92icwLx6wt4LWYBpLW-0itkHNtdy2cqsiKYSxWyMRzaEwyhW3wQo6jC9w9MRUG35wT3drTsuvnMDV5yhtzCtxq57eTRpIpCM9343ITl5DUwS-d7vouI7QH2MAIkZknxTO-_vVPYVQrQ4Th0g6Cb8CrGd-nHQ39xYKnPG7oUmvRobLSaGpKmQREzp-uoQeVK8dypZCl3Xd1uHSUO7w-HKsob-t5whmpE-ziHFaqciWh9YcssC0YE1ztbq0f9tGRy386ZzkkihD23sGR0khZukCdiGSw3Njakpe4AMWujU-t2BtomDJa6pdtLEuvG7p3MbIbHRoXkyK-9h74NgBY2jO7fk0BgItjpmqhcPHelCtMxIhP_OroanM0rCUjfQdqcSBVxwOd_hJ5wcNHmWdyf3gVvKEO83M4cj-sVljJ1afzFfhFsAQH5Zw-JTeBI1udknm3oy5lDwEzRoZpTcQs2Ix8lyUBtZ4MypqRLTnKLXzyij8G8XdgTIqwUkOHhMrm8Zc0_ndcrwPoVjwTq0NugRGJMDAxPKl-aqg6XvEfCYCUF2WYIu8jGo3KK6An8GJ5HFLyidgUslKGJtN2TJmKBOPwc0fXoiW4qyUQdVi2Hz23KBMOQE77jIF0cccZAWDToq67zPLVw9I4j-VKRpti-tOfcg9tz0wr4zJRi49uOqTw038Xn03VXzTolhb3GwwQkMZxWLjam3buEX6SLuS1A7XXZn3aKeLu6KhUin6_aR3jP0s2_Y50Mjv3x0EouaIKQJEINqYRgi9K2SKAxzRSKjGksdNGNcNRGs6cydkHSJF-f60p9HRBbBsN7duP8qm0K2URSJ1DX30=",
          "summary": []
        },
        {
          "id": "msg_0f4dd4f38f19eb60016a99d9b7d7f087d191f17156c41c2f32",
          "type": "message",
          "status": "completed",
          "content": [
            {
              "type": "output_text",
              "annotations": [],
              "logprobs": [],
              "text": "No. For a 30-day month:\n\n- Total time: \\(30 \\times 24 \\times 60 = 43{,}200\\) minutes\n- Error budget: \\(43{,}200 \\times (1 - 0.999) = 43.2\\) minutes\n- Remaining budget: \\(43.2 - 31 = 12.2\\) minutes\n\nAssuming 31 minutes is the total downtime this month, it is **within the error budget**."
            }
          ],
          "phase": "final_answer",
          "role": "assistant"
        }
      ],
      "status": "completed",
      "usage": {
        "input_tokens": 44,
        "output_tokens": 151,
        "total_tokens": 195,
        "input_tokens_details": {
          "cache_write_tokens": 0,
          "cached_tokens": 0
        },
        "output_tokens_details": {
          "reasoning_tokens": 41
        }
      },
      "access_programs": {
        "cyber": "standard"
      },
      "background": false,
      "billing": {
        "payer": "developer"
      },
      "completed_at": 1788467641,
      "error": null,
      "frequency_penalty": 0,
      "incomplete_details": null,
      "instructions": null,
      "max_output_tokens": 512,
      "max_tool_calls": null,
      "moderation": null,
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
      "user": null,
      "metadata": {},
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Migration Safeguards** — Generate a concise answer through Chat Completions
    
    
    const response = await env.AI.run(
      'openai/gpt-6-astra',
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
      "model": "openai/gpt-6-astra",
      "messages": [
        {
          "role": "user",
          "content": "List three practical safeguards for a production API migration."
        }
      ],
      "max_completion_tokens": 256
    }'
    
    
    1. **Validate compatibility before rollout.** Run contract and integration tests against real client behaviors. Keep breaking changes behind a new API version, and verify authentication, error formats, and data schemas.
    
    2. **Roll out gradually with monitoring.** Start with internal traffic or a small canary group. Track error rates, latency, and critical business metrics; pause expansion if predefined thresholds are exceeded.
    
    3. **Prepare and test rollback.** Keep the old API available and use a feature flag or traffic switch to revert quickly. Ensure database changes remain backward-compatible, and rehearse the rollback procedure.
    
    
    {
      "id": "chatcmpl-EK8QDqH1XsfW6m8nEHXxUkrKGcWG5",
      "object": "chat.completion",
      "created": 1788467641,
      "model": "gpt-6-astra",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "1. **Validate compatibility before rollout.** Run contract and integration tests against real client behaviors. Keep breaking changes behind a new API version, and verify authentication, error formats, and data schemas.\n\n2. **Roll out gradually with monitoring.** Start with internal traffic or a small canary group. Track error rates, latency, and critical business metrics; pause expansion if predefined thresholds are exceeded.\n\n3. **Prepare and test rollback.** Keep the old API available and use a feature flag or traffic switch to revert quickly. Ensure database changes remain backward-compatible, and rehearse the rollback procedure.",
            "refusal": null,
            "annotations": []
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 16,
        "completion_tokens": 151,
        "total_tokens": 167,
        "prompt_tokens_details": {
          "cached_tokens": 0,
          "cache_write_tokens": 0,
          "audio_tokens": 0
        },
        "completion_tokens_details": {
          "reasoning_tokens": 23,
          "audio_tokens": 0,
          "accepted_prediction_tokens": 0,
          "rejected_prediction_tokens": 0
        }
      },
      "service_tier": "default",
      "system_fingerprint": null,
      "gatewayMetadata": {
        "keySource": "Unified"
      }
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

Input[](https://developers.cloudflare.com/ai/models/openai/gpt-6-astra/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-6-astra/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/openai/gpt-6-astra/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-6-astra/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
