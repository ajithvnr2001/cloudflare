---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/cohere/
title: Cohere \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:33.984175+00:00
---

# Cohere · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/cohere/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /Cohere



# Cohere

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/cohere/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointURL structurePrerequisitesExamples cURL Use Cohere SDK with PythonOpenAI-Compatible Endpoint

[Cohere ↗︎](https://cohere.com/) build AI models designed to solve real-world business challenges.

## Endpoint
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cohere

## URL structure

When making requests to [Cohere ↗︎](https://cohere.com/), replace `https://api.cohere.ai/v1` in the URL you're currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cohere`.

## Prerequisites

When making requests to Cohere, ensure you have the following:

  * Your AI Gateway Account ID.
  * Your AI Gateway gateway name.
  * An active Cohere API token.
  * The name of the Cohere model you want to use.



## Examples

### cURL

Requestbash
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cohere/v1/chat \
      --header 'Authorization: Token {cohere_api_token}' \
      --header 'Content-Type: application/json' \
      --data '{
      "chat_history": [
        {"role": "USER", "message": "Who discovered gravity?"},
        {"role": "CHATBOT", "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton"}
      ],
      "message": "What year was he born?",
      "connectors": [{"id": "web-search"}]
    }'

### Use Cohere SDK with Python

If using the [`cohere-python-sdk` ↗︎](https://github.com/cohere-ai/cohere-python), set your endpoint like this:

Pythonjs
    
    
    import cohere
    import os
    
    api_key = os.getenv('API_KEY')
    account_id = '{account_id}'
    gateway_id = '{gateway_id}'
    base_url = f"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cohere/v1"
    
    co = cohere.Client(
      api_key=api_key,
      base_url=base_url,
    )
    
    message = "hello world!"
    model = "command-r-plus"
    
    chat = co.chat(
      message=message,
      model=model
    )
    
    print(chat)

## OpenAI-Compatible Endpoint

You can also access Cohere models using the OpenAI API schema through the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/). Send your requests to:
    
    
    https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions

Specify:
    
    
    {
    "model": "cohere/{model}"
    }

[PreviousCerebras](https://developers.cloudflare.com/ai-gateway/usage/providers/cerebras/)[NextDeepgram](https://developers.cloudflare.com/ai-gateway/usage/providers/deepgram/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/cohere.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
