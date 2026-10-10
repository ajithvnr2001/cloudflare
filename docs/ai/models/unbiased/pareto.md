---
url: https://developers.cloudflare.com/ai/models/unbiased/pareto/
title: Pareto (unbiased) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:06.162074+00:00
---

# Pareto (unbiased) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/unbiased/pareto/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



u

# Pareto

Text Generation • unbiased

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`unbiased/pareto`

  * Third-party
  * Zero data retention



Pareto is Unbiased's blended AI model. It engages multiple language models in parallel for each request, synthesizes one answer, and supports text and vision inputs through a single API response.

Model Info|   
---|---  
Terms and License| [link ↗](https://unbiased.ai/terms/)  
More information| [link ↗](https://unbiased.ai/model-card/)  
Zero data retention| Yes  
Request formats| Chat Completions  
Pricing| 

  * Input (per 1M tokens)$2.50
  * Output (per 1M tokens)$7.50
  * Cached input (per 1M tokens)$0.25

  
  
## Usage
    
    
    const response = await env.AI.run(
      'unbiased/pareto',
      {
        messages: [{ content: 'What is the capital of France? Answer in one word.', role: 'user' }],
        max_tokens: 16,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "unbiased/pareto",
      "messages": [
        {
          "content": "What is the capital of France? Answer in one word.",
          "role": "user"
        }
      ],
      "max_tokens": 16
    }'
    
    
    Paris
    
    
    {
      "id": "chatcmpl-mu5ww8tss0mj6ofw",
      "object": "chat.completion",
      "model": "unbiased/pareto",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "Paris"
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 11,
        "completion_tokens": 5,
        "total_tokens": 16,
        "prompt_tokens_details": {
          "cached_tokens": 0
        },
        "cost": 0.000045
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**System Guidance** — Set a helpful system role before asking a question.
    
    
    const response = await env.AI.run(
      'unbiased/pareto',
      {
        messages: [
          { content: 'You explain technical topics in plain language.', role: 'system' },
          { content: 'What is an API? Explain it in two sentences.', role: 'user' },
        ],
        max_tokens: 64,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "unbiased/pareto",
      "messages": [
        {
          "content": "You explain technical topics in plain language.",
          "role": "system"
        },
        {
          "content": "What is an API? Explain it in two sentences.",
          "role": "user"
        }
      ],
      "max_tokens": 64
    }'
    
    
    An API (Application Programming Interface) is a set of rules that lets one software program request information or actions from another. For example, a weather app uses an API to get forecasts from a weather service.
    
    
    {
      "id": "chatcmpl-mu5wwcpm6hxi7lsb",
      "object": "chat.completion",
      "model": "unbiased/pareto",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "An API (Application Programming Interface) is a set of rules that lets one software program request information or actions from another. For example, a weather app uses an API to get forecasts from a weather service."
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 19,
        "completion_tokens": 45,
        "total_tokens": 64,
        "prompt_tokens_details": {
          "cached_tokens": 0
        },
        "cost": 0.000305
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Coding Example** — Ask for a short coding example.
    
    
    const response = await env.AI.run(
      'unbiased/pareto',
      {
        messages: [
          {
            content: 'Write a JavaScript function that reverses a string. Include one example call.',
            role: 'user',
          },
        ],
        max_tokens: 128,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "unbiased/pareto",
      "messages": [
        {
          "content": "Write a JavaScript function that reverses a string. Include one example call.",
          "role": "user"
        }
      ],
      "max_tokens": 128
    }'
    
    
    ```javascript
    function reverseString(str) {
      return Array.from(str).reverse().join("");
    }
    
    console.log(reverseString("Hello")); // "olleH"
    ```
    
    
    {
      "id": "chatcmpl-mu5wwj1mqcjfe7xb",
      "object": "chat.completion",
      "model": "unbiased/pareto",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "```javascript\nfunction reverseString(str) {\n  return Array.from(str).reverse().join(\"\");\n}\n\nconsole.log(reverseString(\"Hello\")); // \"olleH\"\n```"
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 14,
        "completion_tokens": 37,
        "total_tokens": 51,
        "prompt_tokens_details": {
          "cached_tokens": 0
        },
        "cost": 0.00024875
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Follow-up Conversation** — Continue a short conversation with prior assistant context.
    
    
    const response = await env.AI.run(
      'unbiased/pareto',
      {
        messages: [
          { content: 'I am planning a weekend trip to a coastal city.', role: 'user' },
          {
            content: 'Consider walkable neighborhoods, local food, and a nearby beach.',
            role: 'assistant',
          },
          { content: 'What should I prioritize when choosing where to stay?', role: 'user' },
        ],
        max_tokens: 96,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "unbiased/pareto",
      "messages": [
        {
          "content": "I am planning a weekend trip to a coastal city.",
          "role": "user"
        },
        {
          "content": "Consider walkable neighborhoods, local food, and a nearby beach.",
          "role": "assistant"
        },
        {
          "content": "What should I prioritize when choosing where to stay?",
          "role": "user"
        }
      ],
      "max_tokens": 96
    }'
    
    
    For a weekend trip, **prioritize location over extra amenities**—less time in transit means more time enjoying the city.
    
    - **Close to your main plans:** Stay near the beach for a beach-focused trip, or near restaurants and sights if you’re more interested in exploring.
    - **Easy transportation:** Check airport or station connections, public transit, and parking costs if you’re driving.
    - **Comfort and quiet:** Recent reviews can reveal street noise, cleanliness issues
    
    
    {
      "id": "chatcmpl-mu5wwqlruoazrxij",
      "object": "chat.completion",
      "model": "unbiased/pareto",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "For a weekend trip, **prioritize location over extra amenities**—less time in transit means more time enjoying the city.\n\n- **Close to your main plans:** Stay near the beach for a beach-focused trip, or near restaurants and sights if you’re more interested in exploring.\n- **Easy transportation:** Check airport or station connections, public transit, and parking costs if you’re driving.\n- **Comfort and quiet:** Recent reviews can reveal street noise, cleanliness issues"
          },
          "finish_reason": "length"
        }
      ],
      "usage": {
        "prompt_tokens": 43,
        "completion_tokens": 96,
        "total_tokens": 139,
        "prompt_tokens_details": {
          "cached_tokens": 0
        },
        "cost": 0.00065375
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Creative Writing** — Generate a compact piece of creative writing.
    
    
    const response = await env.AI.run(
      'unbiased/pareto',
      {
        messages: [
          { content: 'Write a four-line poem about finding light after a difficult day.', role: 'user' },
        ],
        max_tokens: 96,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "unbiased/pareto",
      "messages": [
        {
          "content": "Write a four-line poem about finding light after a difficult day.",
          "role": "user"
        }
      ],
      "max_tokens": 96
    }'
    
    
    The day lay heavy, stitched with shades of gray,
    Until one star shone through the frayed dusk’s seam.
    I set my burdens down beside the way,
    And let its little light rekindle dream.
    
    
    {
      "id": "chatcmpl-mu5wx6hq2jpgslxe",
      "object": "chat.completion",
      "model": "unbiased/pareto",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "The day lay heavy, stitched with shades of gray,\nUntil one star shone through the frayed dusk’s seam.\nI set my burdens down beside the way,\nAnd let its little light rekindle dream."
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 12,
        "completion_tokens": 46,
        "total_tokens": 58,
        "prompt_tokens_details": {
          "cached_tokens": 0
        },
        "cost": 0.0003025
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

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

Input[](https://developers.cloudflare.com/ai/models/unbiased/pareto/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/unbiased/pareto/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/unbiased/pareto/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/unbiased/pareto/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
