---
url: https://developers.cloudflare.com/ai/models/openai/gpt-6-luna/
title: GPT-6 Luna (OpenAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:03.178993+00:00
---

# GPT-6 Luna (OpenAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/openai/gpt-6-luna/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![OpenAI logo](https://developers.cloudflare.com/_astro/openai.BBwNKzBb.svg)

# GPT-6 Luna

Text Generation • OpenAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/openai/gpt-6-luna/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`openai/gpt-6-luna`

  * Third-party



GPT-6 Luna is OpenAI's most efficient GPT-6 model, built for focused, high-volume tasks.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 1,050,000 tokens  
Terms and License| [link ↗](https://openai.com/policies/)  
More information| [link ↗](https://developers.openai.com/api/docs/models/gpt-6-luna)  
Request formats| Responses, Chat Completions  
Pricing| 

  * Short-context input (per 1M)$0.10
  * Short-context cached input (per 1M)$0.01
  * Short-context cache write (per 1M)$0.125
  * Short-context output (per 1M)$0.50
  * Long-context input (per 1M)$0.20
  * Long-context cached input (per 1M)$0.02
  * Long-context cache write (per 1M)$0.25
  * Long-context output (per 1M)$0.75

  
  
## Usage
    
    
    const response = await env.AI.run(
      'openai/gpt-6-luna',
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
      "model": "openai/gpt-6-luna",
      "input": "A service has 99.9% monthly availability and just had 31 minutes of downtime. Has it exceeded the monthly error budget for a 30-day month? Show the calculation briefly.",
      "max_output_tokens": 512,
      "reasoning": {
        "effort": "high"
      }
    }'
    
    
    No. A 30-day month has 43,200 minutes, so a 99.9% availability target allows **43.2 minutes** of downtime.
    
    **31 minutes < 43.2 minutes** — the service is within its error budget, with **12.2 minutes** remaining.
    
    
    {
      "id": "resp_0834f111f7f68c6e006ab2cf91391887d1b9ed77f9003d8001",
      "object": "response",
      "created_at": 1790103441,
      "status": "completed",
      "access_programs": {
        "cyber": "daybreak_blue"
      },
      "background": false,
      "billing": {
        "payer": "developer"
      },
      "completed_at": 1790103442,
      "error": null,
      "frequency_penalty": 0,
      "incomplete_details": null,
      "instructions": null,
      "max_output_tokens": 512,
      "max_tool_calls": null,
      "model": "gpt-6-luna",
      "moderation": null,
      "output": [
        {
          "id": "rs_0834f111f7f68c6e006ab2cf91a3dc87d194f310e59b05b545",
          "type": "reasoning",
          "content": [],
          "encrypted_content": "gAAAAABqss-TspJODH9IZcFL8SzWTp9z3qvEH482IoLj1OmrPlxluS5KGNZRrU1yGjrek9eQ7K6QzWND5RagCGsxWPN3ZK7lFfa8HWjztExHY-locYCrFDRWniTGdOmjF0dAUcm_5L5laGAhFa5qiRByPmSSapXvxyhbYx1Qs-_SjUxRF7rvxFIisGHm4XeHSuTMLUaVGk3okdDMWwxJDZrPjOk66JLwvZ_D8n345Iw6WG7L6iS30KsEhOuKVxkdkl0H_T_2fDaGxaJfOIr0WCSFjM62vvZNw6Gi9-zf8tzupmjORta_cLu9YDNSklYSNio-rUS-2RMlfJA1RvFQPKIx8347HtpYUYqHBNFRlNA-Az99fWBdGffyNtYL2vuItF4X0UJ1tDN_KtuFil7qLPJMGHTdXI7_-2YzNw9u-rmeeR9tnp3zbCertjlHMsTAcT0fbuLh_ob-GCDSg0pR8Ac5fsJv75nRqIMVixC_e7sL_5sGDAsJDi-24_nUAtU84zCPinglfdiYNvwBoEOgZQ-bYT8K3DZ-Z6dJaupCz_ncOtsFIvvEehM2JzcVdKkhUv6ilUst-J-RoMEzb3HzpKZE2Y6Ry3R-VDvLOda2HL-DrmbK4zW_o8X5-Yp5I-XXIomnt3yxMRYyH5WI66HkMQAFQtiP7ukmQEpI-_ItySu48cro2tpY3tBnRBJAvAU45yGDm9EhG6F_jThXyEav90yADc4GfJw82gZDzrnmQ0Oki8U0jEfPUipKztlsstiLw06Da5IF6cBxhOMiNq2TbB4j5o3bG48HSxAzwgu8xHHSR00_IWMEFO49l6lWpO9W0FWN9OdeaMKkRFQ8cGNIZCqDgYvkw3x0NlbOtjm_TqIQMRVM7vfsdujWSwb1iidy6BEYde7TVAmEg_D0jk7tq9JPIQIngvbxeWXpE2zmvEGrgDqD9y8d-dF2svsxMegzFpZjVowcWRPhJXcySYsMnPrIYqM8bCmXPhSXoBgmTqvWO8BCBJUPvRLPAkJSUU4JTI3GAsN4XAKVm-NaQghf4t5ofeZkIRx9sc1jkz1KfEZ_hH02_89s_A8u2GaiCREYGisKBd9ZuvtDu2WxzIsqud1YKqn9epw-ZC5zCkS0MfZW5rZGmBmu2K6Zia2swsBgs3mypZPh4ihYkkeuAxs_eX1nFtCW-tdYGFcCKVRBf3tvbA2XRgcfgNr9LH6kmbWSBM53kjxLI5L6hR-CDBJ9lWuWoal1R3GzWL9-uIbU4i4ailowQwcgQ2o8Lnnq_jZTs-yurDDyThIVKeo_ZkrmniqyReoVlwYZYRWKaKsSV6i95J-GosOjqM4BoVZGB0tvebNbEOz4tGzKPmoDFI6ckl4Jede1l3dYWAobbPgGab7pp4QgmerdWhiIyK2-kRrDsocrazxjIv0hEqOZha1jwN_cWqmfPTgfmv7jIHZ9Be0S8xrQdd11Qwwyik1OPyJlYte3Ru1IO6FDcCRNbAE3yFBE9pSU8kOKIg==",
          "summary": []
        },
        {
          "id": "msg_0834f111f7f68c6e006ab2cf925fd487d1b67ccd2ee1e2dfe5",
          "type": "message",
          "status": "completed",
          "content": [
            {
              "type": "output_text",
              "annotations": [],
              "logprobs": [],
              "text": "No. A 30-day month has 43,200 minutes, so a 99.9% availability target allows **43.2 minutes** of downtime.\n\n**31 minutes < 43.2 minutes** — the service is within its error budget, with **12.2 minutes** remaining."
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
        "output_tokens": 151,
        "output_tokens_details": {
          "reasoning_tokens": 84
        },
        "total_tokens": 195
      },
      "user": null,
      "metadata": {}
    }

## Examples

**Migration Safeguards** — Generate a concise answer through Chat Completions
    
    
    const response = await env.AI.run(
      'openai/gpt-6-luna',
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
      "model": "openai/gpt-6-luna",
      "messages": [
        {
          "role": "user",
          "content": "List three practical safeguards for a production API migration."
        }
      ],
      "max_completion_tokens": 256
    }'
    
    
    1. **Preserve compatibility:** Version the API or support old and new contracts during the transition; document breaking changes and give clients a migration window.
    2. **Roll out gradually:** Test in staging, then use a canary or percentage-based rollout with monitoring for errors, latency, and client failures.
    3. **Plan validation and rollback:** Verify key workflows and data before and after cutover, keep backups or a reversible migration path, and define clear rollback triggers.
    
    
    {
      "id": "chatcmpl-EQzy7Or5tZ9ZdoXfjhVAYfwDEj28S",
      "object": "chat.completion",
      "created": 1790103443,
      "model": "gpt-6-luna",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "1. **Preserve compatibility:** Version the API or support old and new contracts during the transition; document breaking changes and give clients a migration window.\n2. **Roll out gradually:** Test in staging, then use a canary or percentage-based rollout with monitoring for errors, latency, and client failures.\n3. **Plan validation and rollback:** Verify key workflows and data before and after cutover, keep backups or a reversible migration path, and define clear rollback triggers.",
            "refusal": null,
            "annotations": []
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 16,
        "completion_tokens": 128,
        "total_tokens": 144,
        "prompt_tokens_details": {
          "cached_tokens": 0,
          "cache_write_tokens": 0,
          "audio_tokens": 0
        },
        "completion_tokens_details": {
          "reasoning_tokens": 25,
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

Input[](https://developers.cloudflare.com/ai/models/openai/gpt-6-luna/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-6-luna/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/openai/gpt-6-luna/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-6-luna/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
