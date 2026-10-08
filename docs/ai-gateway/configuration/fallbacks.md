---
url: https://developers.cloudflare.com/ai-gateway/configuration/fallbacks/
title: Fallbacks \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:28.792325+00:00
---

# Fallbacks · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/configuration/fallbacks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ai Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /[Configuration](https://developers.cloudflare.com/ai-gateway/configuration/)
  4. /Fallbacks



# Fallbacks

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/configuration/fallbacks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRequest failures ExampleResponse header(cf-aig-step)

Specify model or provider fallbacks with your [Universal endpoint](https://developers.cloudflare.com/ai-gateway/usage/universal/) to handle request failures and ensure reliability.

Cloudflare can trigger your fallback provider in response to request errors or [predetermined request timeouts](https://developers.cloudflare.com/ai-gateway/configuration/request-handling#request-timeouts). The response header `cf-aig-step` indicates which step successfully processed the request.

## Request failures

By default, Cloudflare triggers your fallback if a model request returns an error.

### Example

In the following example, a request first goes to the [Workers AI](https://developers.cloudflare.com/workers-ai/) Inference API. If the request fails, it falls back to OpenAI. The response header `cf-aig-step` indicates which provider successfully processed the request.

  1. Sends a request to Workers AI Inference API.
  2. If that request fails, proceeds to OpenAI.


    
    
    graph TD
        A[AI Gateway] --> B[Request to Workers AI Inference API]
        B -->|Success| C[Return Response]
        B -->|Failure| D[Request to OpenAI API]
        D --> E[Return Response]
    

  


You can add as many fallbacks as you need, just by adding another object in the array.

Requestbash
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id} \
      --header 'Content-Type: application/json' \
      --data '[
      {
        "provider": "workers-ai",
        "endpoint": "@cf/meta/llama-3.1-8b-instruct",
        "headers": {
          "Authorization": "Bearer {cloudflare_token}",
          "Content-Type": "application/json"
        },
        "query": {
          "messages": [
            {
              "role": "system",
              "content": "You are a friendly assistant"
            },
            {
              "role": "user",
              "content": "What is Cloudflare?"
            }
          ]
        }
      },
      {
        "provider": "openai",
        "endpoint": "chat/completions",
        "headers": {
          "Authorization": "Bearer {open_ai_token}",
          "Content-Type": "application/json"
        },
        "query": {
          "model": "gpt-4o-mini",
          "stream": true,
          "messages": [
            {
              "role": "user",
              "content": "What is Cloudflare?"
            }
          ]
        }
      }
    ]'

## Response header(cf-aig-step)

When using the [Universal endpoint](https://developers.cloudflare.com/ai-gateway/usage/universal/) with fallbacks, the response header `cf-aig-step` indicates which model successfully processed the request by returning the step number. This header provides visibility into whether a fallback was triggered and which model ultimately processed the response.

  * `cf-aig-step:0` – The first (primary) model was used successfully.
  * `cf-aig-step:1` – The request fell back to the second model.
  * `cf-aig-step:2` – The request fell back to the third model.
  * Subsequent steps – Each fallback increments the step number by 1.



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/configuration/fallbacks.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
