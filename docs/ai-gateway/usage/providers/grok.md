---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/grok/
title: xAI \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:34.442099+00:00
---

# xAI · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/grok/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /xAI



# xAI

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/grok/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointURL structurePrerequisitesExamples cURL Use OpenAI SDK with JavaScript Use OpenAI SDK with Python Use Anthropic SDK with JavaScript Use Anthropic SDK with PythonOpenAI-Compatible Endpoint

## Endpoint
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/grok

## URL structure

When making requests to [Grok ↗︎](https://docs.x.ai/docs#getting-started), replace `https://api.x.ai/v1` in the URL you are currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/grok`.

## Prerequisites

When making requests to Grok, ensure you have the following:

  * Your AI Gateway Account ID.
  * Your AI Gateway gateway name.
  * An active xAI API token.
  * The name of the xAI model you want to use.



## Examples

### cURL

Requestbash
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/grok/v1/chat/completions \
      --header 'content-type: application/json' \
      --header 'Authorization: Bearer {xai_api_token}' \
      --data '{
        "model": "grok-4",
        "messages": [
            {
                "role": "user",
                "content": "What is Cloudflare?"
            }
        ]
    }'

### Use OpenAI SDK with JavaScript

If you are using the OpenAI SDK with JavaScript, you can set your endpoint like this:

JavaScriptjs
    
    
    import OpenAI from "openai";
    
    const openai = new OpenAI({
    	apiKey: "<api key>",
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/grok",
    });
    
    const completion = await openai.chat.completions.create({
    	model: "grok-4",
    	messages: [
    		{
    			role: "system",
    			content:
    				"You are Grok, a chatbot inspired by the Hitchhiker's Guide to the Galaxy.",
    		},
    		{
    			role: "user",
    			content: "What is the meaning of life, the universe, and everything?",
    		},
    	],
    });
    
    console.log(completion.choices[0].message);

### Use OpenAI SDK with Python

If you are using the OpenAI SDK with Python, you can set your endpoint like this:

Pythonpython
    
    
    import os
    from openai import OpenAI
    
    XAI_API_KEY = os.getenv("XAI_API_KEY")
    client = OpenAI(
        api_key=XAI_API_KEY,
        base_url="https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/grok",
    )
    
    completion = client.chat.completions.create(
        model="grok-4",
        messages=[
            {"role": "system", "content": "You are Grok, a chatbot inspired by the Hitchhiker's Guide to the Galaxy."},
            {"role": "user", "content": "What is the meaning of life, the universe, and everything?"},
        ],
    )
    
    print(completion.choices[0].message)

### Use Anthropic SDK with JavaScript

If you are using the Anthropic SDK with JavaScript, you can set your endpoint like this:

JavaScriptjs
    
    
    import Anthropic from "@anthropic-ai/sdk";
    
    const anthropic = new Anthropic({
    	apiKey: "<api key>",
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/grok",
    });
    
    const msg = await anthropic.messages.create({
    	model: "grok-beta",
    	max_tokens: 128,
    	system:
    		"You are Grok, a chatbot inspired by the Hitchhiker's Guide to the Galaxy.",
    	messages: [
    		{
    			role: "user",
    			content: "What is the meaning of life, the universe, and everything?",
    		},
    	],
    });
    
    console.log(msg);

### Use Anthropic SDK with Python

If you are using the Anthropic SDK with Python, you can set your endpoint like this:

Pythonpython
    
    
    import os
    from anthropic import Anthropic
    
    XAI_API_KEY = os.getenv("XAI_API_KEY")
    client = Anthropic(
        api_key=XAI_API_KEY,
        base_url="https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/grok",
    )
    
    message = client.messages.create(
        model="grok-beta",
        max_tokens=128,
        system="You are Grok, a chatbot inspired by the Hitchhiker's Guide to the Galaxy.",
        messages=[
            {
                "role": "user",
                "content": "What is the meaning of life, the universe, and everything?",
            },
        ],
    )
    
    print(message.content)

## OpenAI-Compatible Endpoint

You can also access Grok models using the OpenAI API schema through the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/). Send your requests to:
    
    
    https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions

Specify:
    
    
    {
    "model": "grok/{model}"
    }

[PreviousReplicate](https://developers.cloudflare.com/ai-gateway/usage/providers/replicate/)[NextWeb Search](https://developers.cloudflare.com/ai-gateway/usage/web-search/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/grok.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
