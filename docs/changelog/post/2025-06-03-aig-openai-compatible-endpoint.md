---
url: https://developers.cloudflare.com/changelog/post/2025-06-03-aig-openai-compatible-endpoint/
title: AI Gateway adds OpenAI compatible endpoint \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:51.910869+00:00
---

# AI Gateway adds OpenAI compatible endpoint · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-03-aig-openai-compatible-endpoint/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 3, 2025

## AI Gateway adds OpenAI compatible endpoint

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Users can now use an [OpenAI Compatible endpoint](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) in AI Gateway to easily switch between providers, while keeping the exact same request and response formats. We're launching now with the chat completions endpoint, with the embeddings endpoint coming up next.

To get started, use the OpenAI compatible chat completions endpoint URL with your own account id and gateway id and switch between providers by changing the `model` and `apiKey` parameters.

OpenAI SDK Examplejs
    
    
    import OpenAI from "openai";
    const client = new OpenAI({
    	apiKey: "YOUR_PROVIDER_API_KEY", // Provider API key
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat",
    });
    
    const response = await client.chat.completions.create({
    	model: "google-ai-studio/gemini-2.0-flash",
    	messages: [{ role: "user", content: "What is Cloudflare?" }],
    });
    
    console.log(response.choices[0].message.content);

Additionally, the [OpenAI Compatible endpoint](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) can be combined with our [Universal Endpoint](https://developers.cloudflare.com/ai-gateway/usage/universal/) to add fallbacks across multiple providers. That means AI Gateway will return every response in the same standardized format, no extra parsing logic required!

Learn more in the [OpenAI Compatibility](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) documentation.
