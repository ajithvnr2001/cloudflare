---
url: https://developers.cloudflare.com/ai/models/deepseek/deepseek-v4-pro/
title: DeepSeek V4 Pro (deepseek) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:55.162501+00:00
---

# DeepSeek V4 Pro (deepseek) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/deepseek/deepseek-v4-pro/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



d

# DeepSeek V4 Pro

Text Generation • deepseek

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/deepseek/deepseek-v4-pro/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`deepseek/deepseek-v4-pro`

  * Third-party



DeepSeek V4 Pro is a high-capability reasoning model from DeepSeek, served via Fireworks infrastructure for production-grade inference.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 131,072 tokens  
More information| [link ↗](https://api-docs.deepseek.com)  
Request formats| Chat Completions  
Pricing| 

  * Input (per 1M tokens)$1.74
  * Output (per 1M tokens)$3.48
  * Cached input (per 1M tokens)$0.145

  
  
## Usage
    
    
    const response = await env.AI.run(
      'deepseek/deepseek-v4-pro',
      {
        messages: [{ content: 'What is the capital of France?', role: 'user' }],
        model: 'deepseek/deepseek-v4-pro',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "deepseek/deepseek-v4-pro",
      "messages": [
        {
          "content": "What is the capital of France?",
          "role": "user"
        }
      ]
    }'
    
    
    The capital of France is **Paris**.
    
    
    {
      "id": "chatcmpl-3a08845344c942108c3ab7b29112f012",
      "object": "chat.completion",
      "created": 1781047641,
      "model": "deepseek/deepseek-v4-pro",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "The capital of France is **Paris**.",
            "reasoning_content": "We need to answer the question: \"What is the capital of France?\" This is straightforward. The capital of France is Paris. I should answer concisely."
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 11,
        "completion_tokens": 43,
        "total_tokens": 54,
        "prompt_tokens_details": {
          "cached_tokens": 0
        }
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**With System Message** — Using a system message to set context
    
    
    const response = await env.AI.run(
      'deepseek/deepseek-v4-pro',
      {
        messages: [
          { content: 'You are a helpful coding assistant specializing in Python.', role: 'system' },
          { content: 'How do I read a JSON file in Python?', role: 'user' },
        ],
        model: 'deepseek/deepseek-v4-pro',
        temperature: 0.3,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "deepseek/deepseek-v4-pro",
      "messages": [
        {
          "content": "You are a helpful coding assistant specializing in Python.",
          "role": "system"
        },
        {
          "content": "How do I read a JSON file in Python?",
          "role": "user"
        }
      ],
      "temperature": 0.3
    }'
    
    
    To read a JSON file in Python, you use the built-in `json` module. The most common approach is `json.load()` which reads directly from a file object.
    
    ### Basic example
    ```python
    import json
    
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(data)
    ```
    
    ### Key points
    - **`json.load(file)`** – parses JSON from a file-like object.
    - **`json.loads(string)`** – parses JSON from a string (useful if you already have JSON data in memory).
    - Always open the file in read mode (`'r'`) and specify the correct encoding (usually `'utf-8'`).
    - The result is a Python dictionary (if the JSON is an object) or a list (if it’s an array).
    
    ### Handling errors
    Wrap the loading in a `try`/`except` to catch malformed JSON or file issues:
    ```python
    import json
    
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
    ```
    
    ### Reading from a string
    If you already have a JSON string:
    ```python
    json_string = '{"name": "Alice", "age": 30}'
    data = json.loads(json_string)
    ```
    
    That’s it! Let me know if you need help with writing JSON or more advanced usage.
    
    
    {
      "id": "chatcmpl-1aecff3044dc4e349362b9237f0e63b4",
      "object": "chat.completion",
      "created": 1781047642,
      "model": "deepseek/deepseek-v4-pro",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "To read a JSON file in Python, you use the built-in `json` module. The most common approach is `json.load()` which reads directly from a file object.\n\n### Basic example\n```python\nimport json\n\nwith open('data.json', 'r', encoding='utf-8') as f:\n    data = json.load(f)\n\nprint(data)\n```\n\n### Key points\n- **`json.load(file)`** – parses JSON from a file-like object.\n- **`json.loads(string)`** – parses JSON from a string (useful if you already have JSON data in memory).\n- Always open the file in read mode (`'r'`) and specify the correct encoding (usually `'utf-8'`).\n- The result is a Python dictionary (if the JSON is an object) or a list (if it’s an array).\n\n### Handling errors\nWrap the loading in a `try`/`except` to catch malformed JSON or file issues:\n```python\nimport json\n\ntry:\n    with open('data.json', 'r', encoding='utf-8') as f:\n        data = json.load(f)\nexcept FileNotFoundError:\n    print(\"File not found.\")\nexcept json.JSONDecodeError as e:\n    print(f\"Invalid JSON: {e}\")\n```\n\n### Reading from a string\nIf you already have a JSON string:\n```python\njson_string = '{\"name\": \"Alice\", \"age\": 30}'\ndata = json.loads(json_string)\n```\n\nThat’s it! Let me know if you need help with writing JSON or more advanced usage.",
            "reasoning_content": "We need to provide a clear, concise answer on how to read a JSON file in Python. The user likely wants to know the standard method using the `json` module. We'll explain opening the file, using `json.load()` for file objects, and `json.loads()` for strings. Also mention error handling, encoding, and maybe a simple example. Keep it friendly and informative."
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 24,
        "completion_tokens": 413,
        "total_tokens": 437,
        "prompt_tokens_details": {
          "cached_tokens": 0
        }
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Streaming Response** — Enable streaming for real-time output
    
    
    const response = await env.AI.run(
      'deepseek/deepseek-v4-pro',
      {
        messages: [{ content: 'Explain the concept of recursion with a simple example.', role: 'user' }],
        model: 'deepseek/deepseek-v4-pro',
        stream: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "deepseek/deepseek-v4-pro",
      "messages": [
        {
          "content": "Explain the concept of recursion with a simple example.",
          "role": "user"
        }
      ],
      "stream": true
    }'
    
    
    Recursion is a programming technique where a function calls itself to solve a smaller version of the same problem. Each recursive call works on a simpler input, and there’s always a **base case** that stops the recursion, preventing an infinite loop.
    
    ### The Two Essential Parts
    1. **Base case** – the simplest scenario that can be answered directly (no more recursive calls).
    2. **Recursive case** – the function calls itself with a smaller/simpler argument, moving toward the base case.
    
    ### Simple Example: Factorial
    The factorial of a non-negative integer `n` (written `n!`) is the product of all positive integers up to `n`.  
    Definition:  
    - `0! = 1` (base case)  
    - `n! = n × (n−1)!` for `n > 0` (recursive case)
    
    #### Python implementation
    ```python
    def factorial(n):
        if n == 0:          # base case
            return 1
        else:               # recursive case
            return n * factorial(n - 1)
    ```
    
    #### How it works step-by-step for `factorial(3)`
    ```
    factorial(3)
      → 3 * factorial(2)           # waiting for factorial(2)
            → 2 * factorial(1)     # waiting for factorial(1)
                  → 1 * factorial(0)
                        → 0 == 0? → return 1   # base case reached
                  → 1 * 1 = 1
            → 2 * 1 = 2
      → 3 * 2 = 6
    ```
    The calls "stack up" until the base case is hit, then they resolve in reverse order, multiplying as they go.
    
    ### Key Takeaways
    - Recursion breaks a problem into self-similar subproblems.
    - Every recursive function needs a stopping condition (base case).
    - Without a base case, you get infinite recursion (eventually a stack overflow).
    - It’s especially natural for problems with a recursive structure (trees, sorting, divide-and-conquer, etc.).
    
    
    [
      {
        "id": "chatcmpl-cf0a764075534f728f55b99dacf898ba",
        "object": "chat.completion.chunk",
        "created": 1781047647,
        "model": "accounts/fireworks/models/deepseek-v4-pro",
        "choices": [
          {
            "index": 0,
            "delta": {
              "role": "assistant"
            },
            "finish_reason": null,
            "raw_output": null
          }
        ],
        "usage": null
      },
      {
        "id": "chatcmpl-cf0a764075534f728f55b99dacf898ba",
        "object": "chat.completion.chunk",
        "created": 1781047647,
        "model": "accounts/fireworks/models/deepseek-v4-pro",
        "choices": [
          {
            "index": 0,
            "delta": {
              "reasoning_content": "We"
            },
            "finish_reason": null,
            "raw_output": null
          }
        ],
        "usage": null
      },
      "... 606 more chunks omitted ...",
      {
        "id": "chatcmpl-cf0a764075534f728f55b99dacf898ba",
        "object": "chat.completion.chunk",
        "created": 1781047647,
        "model": "accounts/fireworks/models/deepseek-v4-pro",
        "choices": [],
        "usage": {
          "prompt_tokens": 14,
          "total_tokens": 622,
          "completion_tokens": 608,
          "prompt_tokens_details": {
            "cached_tokens": 0
          }
        }
      }
    ]

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

Input[](https://developers.cloudflare.com/ai/models/deepseek/deepseek-v4-pro/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/deepseek/deepseek-v4-pro/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/deepseek/deepseek-v4-pro/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/deepseek/deepseek-v4-pro/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
