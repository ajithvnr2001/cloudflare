---
url: https://developers.cloudflare.com/ai/models/openai/gpt-5.4/
title: GPT-5.4 (OpenAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:01.675985+00:00
---

# GPT-5.4 (OpenAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/openai/gpt-5.4/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![OpenAI logo](https://developers.cloudflare.com/_astro/openai.BBwNKzBb.svg)

# GPT-5.4

Text Generation • OpenAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/openai/gpt-5.4/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`openai/gpt-5.4`

  * Third-party
  * Zero data retention



GPT-5.4 is OpenAI's flagship model with strong coding, reasoning, and multimodal capabilities.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 1,000,000 tokens  
Terms and License| [link ↗](https://openai.com/policies/)  
More information| [link ↗](https://openai.com/)  
Zero data retention| Yes  
Request formats| Responses, Chat Completions  
Pricing| 

  * Input (per 1M tokens)$2.50
  * Output (per 1M tokens)$15.00
  * Cached input (per 1M tokens)$0.25

  
  
## Usage
    
    
    const response = await env.AI.run(
      'openai/gpt-5.4',
      { messages: [{ content: 'What are the three laws of thermodynamics?', role: 'user' }] },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-5.4",
      "messages": [
        {
          "content": "What are the three laws of thermodynamics?",
          "role": "user"
        }
      ]
    }'
    
    
    The **three laws of thermodynamics** are:
    
    1. **First Law of Thermodynamics** — **Energy is conserved**  
       Energy cannot be created or destroyed, only transferred or transformed.  
       In thermodynamic systems, this is often written as:  
       **ΔU = Q - W**  
       where:
       - **ΔU** = change in internal energy  
       - **Q** = heat added to the system  
       - **W** = work done by the system  
    
    2. **Second Law of Thermodynamics** — **Entropy tends to increase**  
       In any natural process, the total entropy of an isolated system never decreases.  
       This means energy tends to spread out, and no heat engine can be 100% efficient.
    
    3. **Third Law of Thermodynamics** — **Entropy approaches a minimum at absolute zero**  
       As the temperature of a perfect crystal approaches **0 Kelvin**, its entropy approaches **zero**.  
       This also implies that absolute zero cannot be reached in a finite number of steps.
    
    There is also a **Zeroth Law of Thermodynamics**, which is often listed before the first three:
    
    - If two systems are each in thermal equilibrium with a third system, they are in thermal equilibrium with each other.  
    - This is the basis for the concept of **temperature**.
    
    If you want, I can also give a simple everyday explanation of each law.
    
    
    {
      "choices": [
        {
          "finish_reason": "stop",
          "index": 0,
          "message": {
            "annotations": [],
            "content": "The **three laws of thermodynamics** are:\n\n1. **First Law of Thermodynamics** — **Energy is conserved**  \n   Energy cannot be created or destroyed, only transferred or transformed.  \n   In thermodynamic systems, this is often written as:  \n   **ΔU = Q - W**  \n   where:\n   - **ΔU** = change in internal energy  \n   - **Q** = heat added to the system  \n   - **W** = work done by the system  \n\n2. **Second Law of Thermodynamics** — **Entropy tends to increase**  \n   In any natural process, the total entropy of an isolated system never decreases.  \n   This means energy tends to spread out, and no heat engine can be 100% efficient.\n\n3. **Third Law of Thermodynamics** — **Entropy approaches a minimum at absolute zero**  \n   As the temperature of a perfect crystal approaches **0 Kelvin**, its entropy approaches **zero**.  \n   This also implies that absolute zero cannot be reached in a finite number of steps.\n\nThere is also a **Zeroth Law of Thermodynamics**, which is often listed before the first three:\n\n- If two systems are each in thermal equilibrium with a third system, they are in thermal equilibrium with each other.  \n- This is the basis for the concept of **temperature**.\n\nIf you want, I can also give a simple everyday explanation of each law.",
            "refusal": null,
            "role": "assistant"
          }
        }
      ],
      "created": 1776470832,
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "id": "chatcmpl-DVnVIkT2U7hYs4iNW9G9MXRoaNGmZ",
      "model": "gpt-5.4-2026-03-05",
      "object": "chat.completion",
      "service_tier": "default",
      "system_fingerprint": null,
      "usage": {
        "completion_tokens": 292,
        "completion_tokens_details": {
          "accepted_prediction_tokens": 0,
          "audio_tokens": 0,
          "reasoning_tokens": 0,
          "rejected_prediction_tokens": 0
        },
        "prompt_tokens": 15,
        "prompt_tokens_details": {
          "audio_tokens": 0,
          "cached_tokens": 0
        },
        "total_tokens": 307
      }
    }

## Examples

**With System Message** — Using a system message to set context
    
    
    const response = await env.AI.run(
      'openai/gpt-5.4',
      {
        messages: [
          { content: 'You are a helpful coding assistant specializing in Python.', role: 'system' },
          { content: 'How do I read a JSON file in Python?', role: 'user' },
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-5.4",
      "messages": [
        {
          "content": "You are a helpful coding assistant specializing in Python.",
          "role": "system"
        },
        {
          "content": "How do I read a JSON file in Python?",
          "role": "user"
        }
      ]
    }'
    
    
    Use Python’s built-in `json` module.
    
    ### Read a JSON file
    ```python
    import json
    
    with open("data.json", "r") as file:
        data = json.load(file)
    
    print(data)
    ```
    
    ### If the file contains:
    ```json
    {
      "name": "Alice",
      "age": 25
    }
    ```
    
    ### Then `data` becomes:
    ```python
    {'name': 'Alice', 'age': 25}
    ```
    
    ### Notes
    - `json.load(file)` reads JSON from a file and converts it to Python objects.
    - JSON objects become Python dictionaries.
    - JSON arrays become Python lists.
    
    ### Read with UTF-8 encoding
    ```python
    import json
    
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    ```
    
    ### Handle invalid JSON safely
    ```python
    import json
    
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        print(data)
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON.")
    ```
    
    If you want, I can also show:
    - how to read a JSON string
    - how to write JSON to a file
    - how to pretty-print JSON
    
    
    {
      "choices": [
        {
          "finish_reason": "stop",
          "index": 0,
          "message": {
            "annotations": [],
            "content": "Use Python’s built-in `json` module.\n\n### Read a JSON file\n```python\nimport json\n\nwith open(\"data.json\", \"r\") as file:\n    data = json.load(file)\n\nprint(data)\n```\n\n### If the file contains:\n```json\n{\n  \"name\": \"Alice\",\n  \"age\": 25\n}\n```\n\n### Then `data` becomes:\n```python\n{'name': 'Alice', 'age': 25}\n```\n\n### Notes\n- `json.load(file)` reads JSON from a file and converts it to Python objects.\n- JSON objects become Python dictionaries.\n- JSON arrays become Python lists.\n\n### Read with UTF-8 encoding\n```python\nimport json\n\nwith open(\"data.json\", \"r\", encoding=\"utf-8\") as file:\n    data = json.load(file)\n```\n\n### Handle invalid JSON safely\n```python\nimport json\n\ntry:\n    with open(\"data.json\", \"r\", encoding=\"utf-8\") as file:\n        data = json.load(file)\n    print(data)\nexcept FileNotFoundError:\n    print(\"File not found.\")\nexcept json.JSONDecodeError:\n    print(\"Invalid JSON.\")\n```\n\nIf you want, I can also show:\n- how to read a JSON string\n- how to write JSON to a file\n- how to pretty-print JSON",
            "refusal": null,
            "role": "assistant"
          }
        }
      ],
      "created": 1776470834,
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "id": "chatcmpl-DVnVKhkW5dNkb7BVCtXpsT0KQSQPA",
      "model": "gpt-5.4-2026-03-05",
      "object": "chat.completion",
      "service_tier": "default",
      "system_fingerprint": null,
      "usage": {
        "completion_tokens": 279,
        "completion_tokens_details": {
          "accepted_prediction_tokens": 0,
          "audio_tokens": 0,
          "reasoning_tokens": 0,
          "rejected_prediction_tokens": 0
        },
        "prompt_tokens": 30,
        "prompt_tokens_details": {
          "audio_tokens": 0,
          "cached_tokens": 0
        },
        "total_tokens": 309
      }
    }

**Multi-turn Conversation** — Continuing a conversation with context
    
    
    const response = await env.AI.run(
      'openai/gpt-5.4',
      {
        max_completion_tokens: 8192,
        messages: [
          {
            content: 'I need help planning a road trip from San Francisco to Los Angeles.',
            role: 'user',
          },
          {
            content:
              "I'd be happy to help! The drive is about 380 miles and takes roughly 5-6 hours. Would you like suggestions for scenic routes or interesting stops along the way?",
            role: 'assistant',
          },
          { content: 'Yes, what are some good places to stop?', role: 'user' },
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-5.4",
      "max_completion_tokens": 8192,
      "messages": [
        {
          "content": "I need help planning a road trip from San Francisco to Los Angeles.",
          "role": "user"
        },
        {
          "content": "I'\''d be happy to help! The drive is about 380 miles and takes roughly 5-6 hours. Would you like suggestions for scenic routes or interesting stops along the way?",
          "role": "assistant"
        },
        {
          "content": "Yes, what are some good places to stop?",
          "role": "user"
        }
      ]
    }'
    
    
    Here are some popular stops if you take the scenic coastal route (Highway 1 / Pacific Coast Highway), which is much slower than I-5 but far more beautiful:
    
    ### Great stops from San Francisco to Los Angeles
    - **Half Moon Bay** – Nice beaches, coastal views, and a good first stop.
    - **Santa Cruz** – Classic beach town with a boardwalk, pier, and cafes.
    - **Monterey** – Famous for Cannery Row and the Monterey Bay Aquarium.
    - **Carmel-by-the-Sea** – Charming small town with shops, galleries, and a beautiful beach.
    - **Big Sur** – One of the most scenic stretches of the drive, with cliffs, ocean views, and hiking spots.
    - **San Simeon** – Known for Hearst Castle and elephant seals nearby.
    - **Morro Bay** – Relaxed coastal town with the iconic Morro Rock.
    - **San Luis Obispo** – Cute downtown, restaurants, and a good overnight stop.
    - **Pismo Beach** – Good for a beach walk or seafood stop.
    - **Santa Barbara** – Beautiful Spanish-style architecture, beaches, and wine tasting.
    - **Malibu** – Scenic coastline before arriving in Los Angeles.
    
    ### If you want the faster inland route (I-5)
    Stops are less scenic, but you could consider:
    - **Gilroy** – Known for garlic-themed food.
    - **Harris Ranch** – Popular food/rest stop on I-5.
    - **Kettleman City** – Convenient midpoint break.
    - **Grapevine area** – Good place to pause before descending into LA.
    
    If you want, I can also suggest:
    1. a **1-day fast itinerary**,  
    2. a **2-3 day scenic itinerary**, or  
    3. **food-focused stops**.
    
    
    {
      "choices": [
        {
          "finish_reason": "stop",
          "index": 0,
          "message": {
            "annotations": [],
            "content": "Here are some popular stops if you take the scenic coastal route (Highway 1 / Pacific Coast Highway), which is much slower than I-5 but far more beautiful:\n\n### Great stops from San Francisco to Los Angeles\n- **Half Moon Bay** – Nice beaches, coastal views, and a good first stop.\n- **Santa Cruz** – Classic beach town with a boardwalk, pier, and cafes.\n- **Monterey** – Famous for Cannery Row and the Monterey Bay Aquarium.\n- **Carmel-by-the-Sea** – Charming small town with shops, galleries, and a beautiful beach.\n- **Big Sur** – One of the most scenic stretches of the drive, with cliffs, ocean views, and hiking spots.\n- **San Simeon** – Known for Hearst Castle and elephant seals nearby.\n- **Morro Bay** – Relaxed coastal town with the iconic Morro Rock.\n- **San Luis Obispo** – Cute downtown, restaurants, and a good overnight stop.\n- **Pismo Beach** – Good for a beach walk or seafood stop.\n- **Santa Barbara** – Beautiful Spanish-style architecture, beaches, and wine tasting.\n- **Malibu** – Scenic coastline before arriving in Los Angeles.\n\n### If you want the faster inland route (I-5)\nStops are less scenic, but you could consider:\n- **Gilroy** – Known for garlic-themed food.\n- **Harris Ranch** – Popular food/rest stop on I-5.\n- **Kettleman City** – Convenient midpoint break.\n- **Grapevine area** – Good place to pause before descending into LA.\n\nIf you want, I can also suggest:\n1. a **1-day fast itinerary**,  \n2. a **2-3 day scenic itinerary**, or  \n3. **food-focused stops**.",
            "refusal": null,
            "role": "assistant"
          }
        }
      ],
      "created": 1776470837,
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "id": "chatcmpl-DVnVNwByCFYOwLiCFfkIf3ghWHlTf",
      "model": "gpt-5.4-2026-03-05",
      "object": "chat.completion",
      "service_tier": "default",
      "system_fingerprint": null,
      "usage": {
        "completion_tokens": 376,
        "completion_tokens_details": {
          "accepted_prediction_tokens": 0,
          "audio_tokens": 0,
          "reasoning_tokens": 0,
          "rejected_prediction_tokens": 0
        },
        "prompt_tokens": 76,
        "prompt_tokens_details": {
          "audio_tokens": 0,
          "cached_tokens": 0
        },
        "total_tokens": 452
      }
    }

**Creative Writing** — Longer completion for creative output
    
    
    const response = await env.AI.run(
      'openai/gpt-5.4',
      {
        max_completion_tokens: 8192,
        messages: [
          {
            content: 'Write a short story opening about a detective finding an unusual clue.',
            role: 'user',
          },
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-5.4",
      "max_completion_tokens": 8192,
      "messages": [
        {
          "content": "Write a short story opening about a detective finding an unusual clue.",
          "role": "user"
        }
      ]
    }'
    
    
    Detective Mara Voss found the first clue where no clue had any business being.
    
    It was tucked inside the mouth of a stone lion that guarded the steps of Blackwell Hall, a place better known for charity galas than murder. The victim lay inside, under a chandelier bright enough to make everyone look innocent. Guests whispered behind silk gloves. Police boots clicked across marble. But Mara stood outside in the rain, staring at the lion’s weather-dark teeth.
    
    Someone had placed a single peach pit on its tongue.
    
    Not dropped. Placed.
    
    She lifted it carefully with her handkerchief. The pit had been polished until it shone, and carved into its surface was the tiniest image of a key.
    
    Mara looked up at the mansion windows. On the third floor, one curtain moved, though the glass behind it was black.
    
    A dead banker in the ballroom was ordinary, as far as her city was concerned. A carved peach pit hidden in a stone lion’s mouth was not.
    
    That was when she began to suspect the murder had started long before the body hit the floor.
    
    
    {
      "choices": [
        {
          "finish_reason": "stop",
          "index": 0,
          "message": {
            "annotations": [],
            "content": "Detective Mara Voss found the first clue where no clue had any business being.\n\nIt was tucked inside the mouth of a stone lion that guarded the steps of Blackwell Hall, a place better known for charity galas than murder. The victim lay inside, under a chandelier bright enough to make everyone look innocent. Guests whispered behind silk gloves. Police boots clicked across marble. But Mara stood outside in the rain, staring at the lion’s weather-dark teeth.\n\nSomeone had placed a single peach pit on its tongue.\n\nNot dropped. Placed.\n\nShe lifted it carefully with her handkerchief. The pit had been polished until it shone, and carved into its surface was the tiniest image of a key.\n\nMara looked up at the mansion windows. On the third floor, one curtain moved, though the glass behind it was black.\n\nA dead banker in the ballroom was ordinary, as far as her city was concerned. A carved peach pit hidden in a stone lion’s mouth was not.\n\nThat was when she began to suspect the murder had started long before the body hit the floor.",
            "refusal": null,
            "role": "assistant"
          }
        }
      ],
      "created": 1776470838,
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "id": "chatcmpl-DVnVORnUmWsqkuSUZDpx0HiNsT3n6",
      "model": "gpt-5.4-2026-03-05",
      "object": "chat.completion",
      "service_tier": "default",
      "system_fingerprint": null,
      "usage": {
        "completion_tokens": 222,
        "completion_tokens_details": {
          "accepted_prediction_tokens": 0,
          "audio_tokens": 0,
          "reasoning_tokens": 0,
          "rejected_prediction_tokens": 0
        },
        "prompt_tokens": 19,
        "prompt_tokens_details": {
          "audio_tokens": 0,
          "cached_tokens": 0
        },
        "total_tokens": 241
      }
    }

**Streaming Response** — Enable streaming for real-time output
    
    
    const response = await env.AI.run(
      'openai/gpt-5.4',
      {
        messages: [{ content: 'Explain the concept of recursion with a simple example.', role: 'user' }],
        stream: true,
        stream_options: { include_usage: true },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-5.4",
      "messages": [
        {
          "content": "Explain the concept of recursion with a simple example.",
          "role": "user"
        }
      ],
      "stream": true,
      "stream_options": {
        "include_usage": true
      }
    }'
    
    
    Recursion is when a function solves a problem by calling itself on a smaller version of the same problem.
    
    It usually has 2 parts:
    
    1. **Base case** — the condition where the function stops calling itself.
    2. **Recursive case** — the part where the function calls itself with a smaller input.
    
    ### Simple example: factorial
    
    The factorial of a number means:
    
    - `5! = 5 × 4 × 3 × 2 × 1`
    - `1! = 1`
    
    A recursive version looks like this in Python:
    
    ```python
    def factorial(n):
        if n == 1:          # base case
            return 1
        return n * factorial(n - 1)   # recursive case
    
    print(factorial(5))
    ```
    
    ### How it works for `factorial(5)`
    
    - `factorial(5)` → `5 * factorial(4)`
    - `factorial(4)` → `4 * factorial(3)`
    - `factorial(3)` → `3 * factorial(2)`
    - `factorial(2)` → `2 * factorial(1)`
    - `factorial(1)` → `1` ← base case
    
    Then it returns back up:
    
    - `factorial(2)` = `2 * 1 = 2`
    - `factorial(3)` = `3 * 2 = 6`
    - `factorial(4)` = `4 * 6 = 24`
    - `factorial(5)` = `5 * 24 = 120`
    
    ### Key idea
    
    Recursion works by breaking a big problem into smaller, similar problems until it reaches a simple stopping point.
    
    If you want, I can also show a **real-life analogy** or a **non-math recursion example**.
    
    
    [
      {
        "choices": [
          {
            "delta": {
              "content": "",
              "refusal": null,
              "role": "assistant"
            },
            "finish_reason": null,
            "index": 0
          }
        ],
        "created": 1776470844,
        "id": "chatcmpl-DVnVUroKWQ9mKa7IP7mbN9LFrUecN",
        "model": "gpt-5.4-2026-03-05",
        "obfuscation": "Wo9naBca",
        "object": "chat.completion.chunk",
        "service_tier": "default",
        "system_fingerprint": null,
        "usage": null
      },
      {
        "choices": [
          {
            "delta": {
              "content": "Rec"
            },
            "finish_reason": null,
            "index": 0
          }
        ],
        "created": 1776470844,
        "id": "chatcmpl-DVnVUroKWQ9mKa7IP7mbN9LFrUecN",
        "model": "gpt-5.4-2026-03-05",
        "obfuscation": "Eu4D5Wg",
        "object": "chat.completion.chunk",
        "service_tier": "default",
        "system_fingerprint": null,
        "usage": null
      },
      "... 371 more chunks omitted ...",
      {
        "choices": [],
        "created": 1776470844,
        "id": "chatcmpl-DVnVUroKWQ9mKa7IP7mbN9LFrUecN",
        "model": "gpt-5.4-2026-03-05",
        "obfuscation": "quuZy0B",
        "object": "chat.completion.chunk",
        "service_tier": "default",
        "system_fingerprint": null,
        "usage": {
          "completion_tokens": 374,
          "completion_tokens_details": {
            "accepted_prediction_tokens": 0,
            "audio_tokens": 0,
            "reasoning_tokens": 0,
            "rejected_prediction_tokens": 0
          },
          "prompt_tokens": 16,
          "prompt_tokens_details": {
            "audio_tokens": 0,
            "cached_tokens": 0
          },
          "total_tokens": 390
        }
      }
    ]

**Web Search** — Letting the model use OpenAI's built-in web search tool to answer with current information
    
    
    const response = await env.AI.run(
      'openai/gpt-5.4',
      {
        input: 'What were the top news stories about Cloudflare this week? Summarise in three bullets.',
        max_output_tokens: 4096,
        tools: [{ type: 'web_search_preview' }],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-5.4",
      "input": "What were the top news stories about Cloudflare this week? Summarise in three bullets.",
      "max_output_tokens": 4096,
      "tools": [
        {
          "type": "web_search_preview"
        }
      ]
    }'
    
    
    Here are the top Cloudflare stories I found for **this week of June 16–22, 2026**:
    
    - **Cloudflare unveiled a new browser-backed web standard effort on June 22.** It said it is working with **Mozilla, Google, Microsoft, and Shopify** on **Private Access Control Tokens (PACT)**, a privacy-first protocol meant to help websites distinguish legitimate humans and authorized bots from malicious automation without relying as heavily on CAPTCHAs or invasive tracking. ([cloudflare.com](https://www.cloudflare.com/press/press-releases/2026/cloudflare-collaborates-with-leading-browsers-to-develop-a-privacy-first-protocol-for-the-global-internet/))
    
    - **Cloudflare launched a new partner program push around AI and SASE on June 17–18.** The company introduced a **Cloudflare One Design Partner** designation and an **AI-powered deployment toolkit / Cloudflare One Stack** aimed at helping partners migrate customers from legacy security setups to Cloudflare’s SASE platform more quickly. ([cloudflare.com](https://www.cloudflare.com/press/press-releases/))
    
    - **Cloudflare was also in the spotlight for a major outage discussion on June 22.** Community and operator reports pointed to a widespread incident affecting North America, with users debating Cloudflare’s status-page timing and some commenters attributing the disruption to a large **fiber cut in the eastern U.S.** That attribution appears to be community reporting rather than an official Cloudflare statement, so treat it as provisional. ([reddit.com](https://www.reddit.com/r/sysadmin/comments/1ucmhpy/cloudflares_outage_and_the_ethics_of_fudging/))
    
    If you want, I can also turn this into a **more polished “executive brief” version** or include **links to the original articles/press releases**.
    
    
    {
      "id": "resp_07308ed5e73a1a07016a399654b808819bbe73b7cacddeb144",
      "object": "response",
      "created_at": 1782158932,
      "model": "gpt-5.4-2026-03-05",
      "output": [
        {
          "id": "ws_07308ed5e73a1a07016a3996555478819ba0dc680619d5b577",
          "type": "web_search_call",
          "status": "completed",
          "action": {
            "type": "search",
            "queries": [
              "Cloudflare latest news this week June 2026",
              "Cloudflare news June 2026 site:cloudflare.com OR site:reuters.com OR site:theverge.com OR site:techcrunch.com",
              "Cloudflare press release June 2026",
              "Cloudflare Reuters June 2026"
            ],
            "query": "Cloudflare latest news this week June 2026"
          }
        },
        {
          "id": "ws_07308ed5e73a1a07016a399657b250819b993ed21cd98de1b0",
          "type": "web_search_call",
          "status": "completed",
          "action": {
            "type": "open_page",
            "url": "https://www.cloudflare.com/press/press-releases/"
          }
        },
        {
          "id": "ws_07308ed5e73a1a07016a39965a0d04819b8c2ed37555f60460",
          "type": "web_search_call",
          "status": "completed",
          "action": {
            "type": "open_page",
            "url": "https://www.cloudflare.com/press/press-releases/"
          }
        },
        {
          "id": "msg_07308ed5e73a1a07016a39965b2a44819bb530eea4c274d30e",
          "type": "message",
          "status": "completed",
          "content": [
            {
              "type": "output_text",
              "annotations": [
                {
                  "type": "url_citation",
                  "end_index": 643,
                  "start_index": 464,
                  "title": "www.cloudflare.com",
                  "url": "https://www.cloudflare.com/press/press-releases/2026/cloudflare-collaborates-with-leading-browsers-to-develop-a-privacy-first-protocol-for-the-global-internet/"
                },
                {
                  "type": "url_citation",
                  "end_index": 1051,
                  "start_index": 983,
                  "title": "Press Overview | Cloudflare",
                  "url": "https://www.cloudflare.com/press/press-releases/"
                },
                {
                  "type": "url_citation",
                  "end_index": 1608,
                  "start_index": 1496,
                  "title": "Cloudflare's outage and the ethics of fudging status page timestamps : r/sysadmin",
                  "url": "https://www.reddit.com/r/sysadmin/comments/1ucmhpy/cloudflares_outage_and_the_ethics_of_fudging/"
                }
              ],
              "logprobs": [],
              "text": "Here are the top Cloudflare stories I found for **this week of June 16–22, 2026**:\n\n- **Cloudflare unveiled a new browser-backed web standard effort on June 22.** It said it is working with **Mozilla, Google, Microsoft, and Shopify** on **Private Access Control Tokens (PACT)**, a privacy-first protocol meant to help websites distinguish legitimate humans and authorized bots from malicious automation without relying as heavily on CAPTCHAs or invasive tracking. ([cloudflare.com](https://www.cloudflare.com/press/press-releases/2026/cloudflare-collaborates-with-leading-browsers-to-develop-a-privacy-first-protocol-for-the-global-internet/))\n\n- **Cloudflare launched a new partner program push around AI and SASE on June 17–18.** The company introduced a **Cloudflare One Design Partner** designation and an **AI-powered deployment toolkit / Cloudflare One Stack** aimed at helping partners migrate customers from legacy security setups to Cloudflare’s SASE platform more quickly. ([cloudflare.com](https://www.cloudflare.com/press/press-releases/))\n\n- **Cloudflare was also in the spotlight for a major outage discussion on June 22.** Community and operator reports pointed to a widespread incident affecting North America, with users debating Cloudflare’s status-page timing and some commenters attributing the disruption to a large **fiber cut in the eastern U.S.** That attribution appears to be community reporting rather than an official Cloudflare statement, so treat it as provisional. ([reddit.com](https://www.reddit.com/r/sysadmin/comments/1ucmhpy/cloudflares_outage_and_the_ethics_of_fudging/))\n\nIf you want, I can also turn this into a **more polished “executive brief” version** or include **links to the original articles/press releases**."
            }
          ],
          "phase": "final_answer",
          "role": "assistant"
        }
      ],
      "status": "completed",
      "usage": {
        "input_tokens": 19126,
        "output_tokens": 522,
        "total_tokens": 19648,
        "input_tokens_details": {
          "cached_tokens": 0
        },
        "output_tokens_details": {
          "reasoning_tokens": 175
        }
      },
      "background": false,
      "billing": {
        "payer": "developer"
      },
      "completed_at": 1782158944,
      "error": null,
      "frequency_penalty": 0,
      "incomplete_details": null,
      "instructions": null,
      "max_output_tokens": 4096,
      "max_tool_calls": null,
      "moderation": null,
      "parallel_tool_calls": true,
      "presence_penalty": 0,
      "previous_response_id": null,
      "prompt_cache_key": null,
      "prompt_cache_retention": "in_memory",
      "reasoning": {
        "context": "current_turn",
        "effort": "none",
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
      "tools": [
        {
          "type": "web_search_preview",
          "search_content_types": [
            "text"
          ],
          "search_context_size": "medium",
          "user_location": {
            "type": "approximate",
            "city": null,
            "country": "US",
            "region": null,
            "timezone": null
          }
        }
      ],
      "top_logprobs": 0,
      "top_p": 0.98,
      "truncation": "disabled",
      "user": null,
      "metadata": {},
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

Input[](https://developers.cloudflare.com/ai/models/openai/gpt-5.4/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-5.4/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/openai/gpt-5.4/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-5.4/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
