---
url: https://developers.cloudflare.com/workers-ai/configuration/hugging-face-chat-ui/
title: Hugging Face Chat UI \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:56.714929+00:00
---

# Hugging Face Chat UI · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/configuration/hugging-face-chat-ui/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Configuration
  4. /Hugging Face Chat UI



# Hugging Face Chat UI

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/configuration/hugging-face-chat-ui/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesSetupSupported models

Use Workers AI with [Chat UI ↗︎](https://github.com/huggingface/chat-ui?tab=readme-ov-file#text-embedding-models), an open-source chat interface offered by Hugging Face.

## Prerequisites

You will need the following:

  * A [Cloudflare account ↗︎](https://dash.cloudflare.com)
  * Your [Account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/)
  * An [API token](https://developers.cloudflare.com/workers-ai/get-started/rest-api/#1-get-api-token-and-account-id) for Workers AI



## Setup

First, decide how to reference your Account ID and API token (either directly in your `.env.local` using the `CLOUDFLARE_ACCOUNT_ID` and `CLOUDFLARE_API_TOKEN` variables or in the endpoint configuration).

Then, follow the rest of the setup instructions in the [Chat UI GitHub repository ↗︎](https://github.com/huggingface/chat-ui?tab=readme-ov-file#text-embedding-models).

When setting up your models, specify the `cloudflare` endpoint.
    
    
    {
      "name" : "nousresearch/hermes-2-pro-mistral-7b",
      "tokenizer": "nousresearch/hermes-2-pro-mistral-7b",
      "parameters": {
        "stop": ["<|im_end|>"]
      },
      "endpoints" : [
        {
          "type": "cloudflare",
          // optionally specify these if not included in .env.local
          "accountId": "your-account-id",
          "apiToken": "your-api-token"
          //
        }
      ]
    }

## Supported models

This template works with any [text generation models](https://developers.cloudflare.com/workers-ai/models/) that begin with the `@hf` parameter.

[PreviousVercel AI SDK](https://developers.cloudflare.com/workers-ai/configuration/ai-sdk/)[NextOverview](https://developers.cloudflare.com/workers-ai/features/batch-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/configuration/hugging-face-chat-ui.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
