---
url: https://developers.cloudflare.com/changelog/post/2025-08-05-openai-open-models/
title: OpenAI open models now available on Workers AI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:18.343517+00:00
---

# OpenAI open models now available on Workers AI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-05-openai-open-models/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 5, 2025

## OpenAI open models now available on Workers AI

[Agents](https://developers.cloudflare.com/agents/)[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-05-openai-open-models/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We're thrilled to be a Day 0 partner with [OpenAI ↗︎](http://openai.com/index/introducing-gpt-oss) to bring their [latest open models ↗︎](https://openai.com/index/gpt-oss-model-card/) to Workers AI, including support for Responses API, Code Interpreter, and Web Search (coming soon).

Get started with the new models at `@cf/openai/gpt-oss-120b` and `@cf/openai/gpt-oss-20b`. Check out the [blog ↗︎](https://blog.cloudflare.com/openai-gpt-oss-on-workers-ai) for more details about the new models, and the [`gpt-oss-120b`](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b) and [`gpt-oss-20b`](https://developers.cloudflare.com/workers-ai/models/gpt-oss-20b) model pages for more information about pricing and context windows.

#### Responses API

If you call the model through:

  * Workers Binding, it will accept/return Responses API – `env.AI.run(“@cf/openai/gpt-oss-120b”)`
  * REST API on `/run` endpoint, it will accept/return Responses API – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/run/@cf/openai/gpt-oss-120b`
  * REST API on new `/responses` endpoint, it will accept/return Responses API – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/v1/responses`
  * REST API for OpenAI Compatible endpoint, it will return Chat Completions (coming soon) – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/v1/chat/completions`


    
    
    curl https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/v1/responses \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $CLOUDFLARE_API_KEY" \
      -d '{
        "model": "@cf/openai/gpt-oss-120b",
        "reasoning": {"effort": "medium"},
        "input": [
          {
            "role": "user",
            "content": "What are the benefits of open-source models?"
          }
        ]
      }'
    

#### Code Interpreter

The model is natively trained to support stateful code execution, and we've implemented support for this feature using our [Sandbox SDK ↗︎](https://github.com/cloudflare/sandbox-sdk) and [Containers ↗︎](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/). Cloudflare's Developer Platform is uniquely positioned to support this feature, so we're very excited to bring our products together to support this new use case.

#### Web Search (coming soon)

We are working to implement Web Search for the model, where users can bring their own Exa API Key so the model can browse the Internet.
