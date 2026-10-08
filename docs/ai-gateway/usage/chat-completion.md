---
url: https://developers.cloudflare.com/ai-gateway/usage/chat-completion/
title: Unified API (OpenAI compat) \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:33.533595+00:00
---

# Unified API (OpenAI compat) · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/chat-completion/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /Using AI Gateway
  4. /Unified API (OpenAI compat)



# Unified API (OpenAI compat)

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpoint URLParametersExamplesSupported Providers

Deprecated for single-model calls

For standard single-model chat completions, this endpoint is deprecated. Use the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/) instead, which provides OpenAI-compatible endpoints at `api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/v1/chat/completions`. The `/compat/chat/completions` endpoint will continue to work for existing integrations.

Dynamic routing

[Dynamic routes](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/) (`dynamic/{route}`) can be invoked through this `/compat/chat/completions` endpoint, and existing integrations continue to work. For new integrations, use the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/) at `/ai/v1/chat/completions` or the [AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/) instead. See [Using a dynamic route](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/usage/) for examples.

Cloudflare's AI Gateway offers an OpenAI-compatible `/chat/completions` endpoint, enabling integration with multiple AI providers using a single URL. This feature simplifies the integration process, allowing for seamless switching between different models without significant code modifications.

## Endpoint URL
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/default/compat/chat/completions

Replace `{account_id}` with your Cloudflare account ID. The `default` gateway is created automatically on your first request — no setup needed. You can also replace `default` with a specific gateway ID if you have already created one.

## Parameters

Switch providers by changing the `model` and `apiKey` parameters.

Specify the model using `{provider}/{model}` format. For example:

  * `openai/gpt-5-mini`
  * `google-ai-studio/gemini-2.5-flash`
  * `anthropic/claude-sonnet-4-5`



## Examples

Make a request to 

![](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48IS0tIFVwbG9hZGVkIHRvOiBTVkcgUmVwbywgd3d3LnN2Z3JlcG8uY29tLCBHZW5lcmF0b3I6IFNWRyBSZXBvIE1peGVyIFRvb2xzIC0tPgo8c3ZnIGZpbGw9IiMwMDAwMDAiIHdpZHRoPSI2NHB4IiBoZWlnaHQ9IjY0cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgcm9sZT0iaW1nIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjx0aXRsZT5PcGVuQUkgaWNvbjwvdGl0bGU+PHBhdGggZD0iTTIyLjI4MTkgOS44MjExYTUuOTg0NyA1Ljk4NDcgMCAwIDAtLjUxNTctNC45MTA4IDYuMDQ2MiA2LjA0NjIgMCAwIDAtNi41MDk4LTIuOUE2LjA2NTEgNi4wNjUxIDAgMCAwIDQuOTgwNyA0LjE4MThhNS45ODQ3IDUuOTg0NyAwIDAgMC0zLjk5NzcgMi45IDYuMDQ2MiA2LjA0NjIgMCAwIDAgLjc0MjcgNy4wOTY2IDUuOTggNS45OCAwIDAgMCAuNTExIDQuOTEwNyA2LjA1MSA2LjA1MSAwIDAgMCA2LjUxNDYgMi45MDAxQTUuOTg0NyA1Ljk4NDcgMCAwIDAgMTMuMjU5OSAyNGE2LjA1NTcgNi4wNTU3IDAgMCAwIDUuNzcxOC00LjIwNTggNS45ODk0IDUuOTg5NCAwIDAgMCAzLjk5NzctMi45MDAxIDYuMDU1NyA2LjA1NTcgMCAwIDAtLjc0NzUtNy4wNzI5em0tOS4wMjIgMTIuNjA4MWE0LjQ3NTUgNC40NzU1IDAgMCAxLTIuODc2NC0xLjA0MDhsLjE0MTktLjA4MDQgNC43NzgzLTIuNzU4MmEuNzk0OC43OTQ4IDAgMCAwIC4zOTI3LS42ODEzdi02LjczNjlsMi4wMiAxLjE2ODZhLjA3MS4wNzEgMCAwIDEgLjAzOC4wNTJ2NS41ODI2YTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0NSA0LjQ5NDR6bS05LjY2MDctNC4xMjU0YTQuNDcwOCA0LjQ3MDggMCAwIDEtLjUzNDYtMy4wMTM3bC4xNDIuMDg1MiA0Ljc4MyAyLjc1ODJhLjc3MTIuNzcxMiAwIDAgMCAuNzgwNiAwbDUuODQyOC0zLjM2ODV2Mi4zMzI0YS4wODA0LjA4MDQgMCAwIDEtLjAzMzIuMDYxNUw5Ljc0IDE5Ljk1MDJhNC40OTkyIDQuNDk5MiAwIDAgMS02LjE0MDgtMS42NDY0ek0yLjM0MDggNy44OTU2YTQuNDg1IDQuNDg1IDAgMCAxIDIuMzY1NS0xLjk3MjhWMTEuNmEuNzY2NC43NjY0IDAgMCAwIC4zODc5LjY3NjVsNS44MTQ0IDMuMzU0My0yLjAyMDEgMS4xNjg1YS4wNzU3LjA3NTcgMCAwIDEtLjA3MSAwbC00LjgzMDMtMi43ODY1QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQwOCA3Ljg3MnptMTYuNTk2MyAzLjg1NThMMTMuMTAzOCA4LjM2NCAxNS4xMTkyIDcuMmEuMDc1Ny4wNzU3IDAgMCAxIC4wNzEgMGw0LjgzMDMgMi43OTEzYTQuNDk0NCA0LjQ5NDQgMCAwIDEtLjY3NjUgOC4xMDQydi01LjY3NzJhLjc5Ljc5IDAgMCAwLS40MDctLjY2N3ptMi4wMTA3LTMuMDIzMWwtLjE0Mi0uMDg1Mi00Ljc3MzUtMi43ODE4YS43NzU5Ljc3NTkgMCAwIDAtLjc4NTQgMEw5LjQwOSA5LjIyOTdWNi44OTc0YS4wNjYyLjA2NjIgMCAwIDEgLjAyODQtLjA2MTVsNC44MzAzLTIuNzg2NmE0LjQ5OTIgNC40OTkyIDAgMCAxIDYuNjgwMiA0LjY2ek04LjMwNjUgMTIuODYzbC0yLjAyLTEuMTYzOGEuMDgwNC4wODA0IDAgMCAxLS4wMzgtLjA1NjdWNi4wNzQyYTQuNDk5MiA0LjQ5OTIgMCAwIDEgNy4zNzU3LTMuNDUzN2wtLjE0Mi4wODA1TDguNzA0IDUuNDU5YS43OTQ4Ljc5NDggMCAwIDAtLjM5MjcuNjgxM3ptMS4wOTc2LTIuMzY1NGwyLjYwMi0xLjQ5OTggMi42MDY5IDEuNDk5OHYyLjk5OTRsLTIuNTk3NCAxLjQ5OTctMi42MDY3LTEuNDk5N1oiLz48L3N2Zz4=)OpenAI

using 

OpenAI JS SDK

with 

Stored Key (BYOK)
    
    
    import OpenAI from "openai";
    
    const client = new OpenAI({
    	apiKey: "{cf_api_token}",
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat",
    });
    
    const response = await client.chat.completions.create({
    	model: "openai/gpt-5.2",
    	messages: [{ role: "user", content: "Hello, world!" }],
    });
    
    
    import OpenAI from "openai";
    
    const client = new OpenAI({
    	apiKey: "{cf_api_token}",
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat",
    });
    
    const response = await client.chat.completions.create({
    	model: "anthropic/claude-4-5-sonnet",
    	messages: [{ role: "user", content: "Hello, world!" }],
    });
    
    
    import OpenAI from "openai";
    
    const client = new OpenAI({
    	apiKey: "{cf_api_token}",
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat",
    });
    
    const response = await client.chat.completions.create({
    	model: "google/gemini-2.5-pro",
    	messages: [{ role: "user", content: "Hello, world!" }],
    });
    
    
    import OpenAI from "openai";
    
    const client = new OpenAI({
    	apiKey: "{cf_api_token}",
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat",
    });
    
    const response = await client.chat.completions.create({
    	model: "grok/grok-4",
    	messages: [{ role: "user", content: "Hello, world!" }],
    });
    
    
    import OpenAI from "openai";
    
    const client = new OpenAI({
    	apiKey: "{cf_api_token}",
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat",
    });
    
    const response = await client.chat.completions.create({
    	model: "dynamic/customer-support",
    	messages: [{ role: "user", content: "Hello, world!" }],
    });
    
    
    import OpenAI from "openai";
    
    const client = new OpenAI({
    	apiKey: "{cf_api_token}",
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat",
    });
    
    const response = await client.chat.completions.create({
    	model: "workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast",
    	messages: [{ role: "user", content: "Hello, world!" }],
    });
    
    
    import OpenAI from "openai";
    
    const client = new OpenAI({
    	apiKey: "{openai_api_token}",
      defaultHeaders: {
          // if gateway is authenticated
          "cf-aig-authorization": `Bearer {cf_api_token}`, 
      },
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat",
    });
    
    const response = await client.chat.completions.create({
    	model: "openai/gpt-5.2",
    	messages: [{ role: "user", content: "Hello, world!" }],
    });
    
    
    import OpenAI from "openai";
    
    const client = new OpenAI({
    	apiKey: "{anthropic_api_token}",
      defaultHeaders: {
          // if gateway is authenticated
          "cf-aig-authorization": `Bearer {cf_api_token}`, 
      },
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat",
    });
    
    const response = await client.chat.completions.create({
    	model: "anthropic/claude-4-5-sonnet",
    	messages: [{ role: "user", content: "Hello, world!" }],
    });
    
    
    import OpenAI from "openai";
    
    const client = new OpenAI({
    	apiKey: "{google_api_token}",
      defaultHeaders: {
          // if gateway is authenticated
          "cf-aig-authorization": `Bearer {cf_api_token}`, 
      },
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat",
    });
    
    const response = await client.chat.completions.create({
    	model: "google/gemini-2.5-pro",
    	messages: [{ role: "user", content: "Hello, world!" }],
    });
    
    
    import OpenAI from "openai";
    
    const client = new OpenAI({
    	apiKey: "{grok_api_token}",
      defaultHeaders: {
          // if gateway is authenticated
          "cf-aig-authorization": `Bearer {cf_api_token}`, 
      },
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat",
    });
    
    const response = await client.chat.completions.create({
    	model: "grok/grok-4",
    	messages: [{ role: "user", content: "Hello, world!" }],
    });
    
    
    import OpenAI from "openai";
    
    const client = new OpenAI({
    	apiKey: "{dynamic_api_token}",
      defaultHeaders: {
          // if gateway is authenticated
          "cf-aig-authorization": `Bearer {cf_api_token}`, 
      },
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat",
    });
    
    const response = await client.chat.completions.create({
    	model: "dynamic/customer-support",
    	messages: [{ role: "user", content: "Hello, world!" }],
    });
    
    
    import OpenAI from "openai";
    
    const client = new OpenAI({
    	apiKey: "{workers-ai_api_token}",
      defaultHeaders: {
          // if gateway is authenticated
          "cf-aig-authorization": `Bearer {cf_api_token}`, 
      },
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat",
    });
    
    const response = await client.chat.completions.create({
    	model: "workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast",
    	messages: [{ role: "user", content: "Hello, world!" }],
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createUnified } from 'ai-gateway-provider/providers/unified';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const unified = createUnified();
    
    const { text } = await generateText({
      model: aigateway(unified('openai/gpt-5.2')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createUnified } from 'ai-gateway-provider/providers/unified';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const unified = createUnified();
    
    const { text } = await generateText({
      model: aigateway(unified('anthropic/claude-4-5-sonnet')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createUnified } from 'ai-gateway-provider/providers/unified';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const unified = createUnified();
    
    const { text } = await generateText({
      model: aigateway(unified('google/gemini-2.5-pro')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createUnified } from 'ai-gateway-provider/providers/unified';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const unified = createUnified();
    
    const { text } = await generateText({
      model: aigateway(unified('grok/grok-4')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createUnified } from 'ai-gateway-provider/providers/unified';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const unified = createUnified();
    
    const { text } = await generateText({
      model: aigateway(unified('dynamic/customer-support')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createUnified } from 'ai-gateway-provider/providers/unified';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const unified = createUnified();
    
    const { text } = await generateText({
      model: aigateway(unified('workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createUnified } from 'ai-gateway-provider/providers/unified';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const unified = createUnified({ apiKey: '{API_KEY}' });
    
    const { text } = await generateText({
      model: aigateway(unified('openai/gpt-5.2')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createUnified } from 'ai-gateway-provider/providers/unified';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const unified = createUnified({ apiKey: '{API_KEY}' });
    
    const { text } = await generateText({
      model: aigateway(unified('anthropic/claude-4-5-sonnet')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createUnified } from 'ai-gateway-provider/providers/unified';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const unified = createUnified({ apiKey: '{API_KEY}' });
    
    const { text } = await generateText({
      model: aigateway(unified('google/gemini-2.5-pro')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createUnified } from 'ai-gateway-provider/providers/unified';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const unified = createUnified({ apiKey: '{API_KEY}' });
    
    const { text } = await generateText({
      model: aigateway(unified('grok/grok-4')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createUnified } from 'ai-gateway-provider/providers/unified';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const unified = createUnified({ apiKey: '{API_KEY}' });
    
    const { text } = await generateText({
      model: aigateway(unified('dynamic/customer-support')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createUnified } from 'ai-gateway-provider/providers/unified';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const unified = createUnified({ apiKey: '{API_KEY}' });
    
    const { text } = await generateText({
      model: aigateway(unified('workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createOpenAI } from 'ai-gateway-provider/providers/openai';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const openai = createOpenAI();
    
    const { text } = await generateText({
      model: aigateway(openai.chat('gpt-5.2')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createAnthropic } from 'ai-gateway-provider/providers/anthropic';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const anthropic = createAnthropic();
    
    const { text } = await generateText({
      model: aigateway(anthropic('claude-4-5-sonnet')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createGoogle } from 'ai-gateway-provider/providers/google';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const google = createGoogle();
    
    const { text } = await generateText({
      model: aigateway(google('gemini-2.5-pro')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createXai } from 'ai-gateway-provider/providers/xai';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const xai = createXai();
    
    const { text } = await generateText({
      model: aigateway(xai('grok-4')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createUnified } from 'ai-gateway-provider/providers/unified';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const unified = createUnified();
    
    const { text } = await generateText({
      model: aigateway(unified('customer-support')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createUnified } from 'ai-gateway-provider/providers/unified';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const unified = createUnified();
    
    const { text } = await generateText({
      model: aigateway(unified('@cf/meta/llama-3.3-70b-instruct-fp8-fast')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createOpenAI } from 'ai-gateway-provider/providers/openai';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const openai = createOpenAI({ apiKey: '{API_KEY}' });
    
    const { text } = await generateText({
      model: aigateway(openai.chat('gpt-5.2')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createAnthropic } from 'ai-gateway-provider/providers/anthropic';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const anthropic = createAnthropic({ apiKey: '{API_KEY}' });
    
    const { text } = await generateText({
      model: aigateway(anthropic('claude-4-5-sonnet')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createGoogle } from 'ai-gateway-provider/providers/google';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const google = createGoogle({ apiKey: '{API_KEY}' });
    
    const { text } = await generateText({
      model: aigateway(google('gemini-2.5-pro')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createXai } from 'ai-gateway-provider/providers/xai';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const xai = createXai({ apiKey: '{API_KEY}' });
    
    const { text } = await generateText({
      model: aigateway(xai('grok-4')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createUnified } from 'ai-gateway-provider/providers/unified';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const unified = createUnified({ apiKey: '{API_KEY}' });
    
    const { text } = await generateText({
      model: aigateway(unified('customer-support')),
      prompt: 'What is Cloudflare?',
    });
    
    
    import { createAiGateway } from 'ai-gateway-provider';
    import { createUnified } from 'ai-gateway-provider/providers/unified';
    import { generateText } from "ai";
    
    const aigateway = createAiGateway({
      accountId: "{CLOUDFLARE_ACCOUNT_ID}",
      gateway: '{GATEWAY_NAME}',
      apiKey: '{CF_AIG_TOKEN}',
    });
    
    const unified = createUnified({ apiKey: '{API_KEY}' });
    
    const { text } = await generateText({
      model: aigateway(unified('@cf/meta/llama-3.3-70b-instruct-fp8-fast')),
      prompt: 'What is Cloudflare?',
    });
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions \
      --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
      --header 'Content-Type: application/json' \
      --data '{
        "model": "openai/gpt-5.2",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions \
      --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
      --header 'Content-Type: application/json' \
      --data '{
        "model": "anthropic/claude-4-5-sonnet",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions \
      --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
      --header 'Content-Type: application/json' \
      --data '{
        "model": "google/gemini-2.5-pro",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions \
      --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
      --header 'Content-Type: application/json' \
      --data '{
        "model": "grok/grok-4",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions \
      --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
      --header 'Content-Type: application/json' \
      --data '{
        "model": "dynamic/customer-support",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions \
      --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
      --header 'Content-Type: application/json' \
      --data '{
        "model": "workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions \
      --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
      --header 'Authorization: Bearer {openai_api_token}' \
      --header 'Content-Type: application/json' \
      --data '{
        "model": "openai/gpt-5.2",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions \
      --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
      --header 'Authorization: Bearer {anthropic_api_token}' \
      --header 'Content-Type: application/json' \
      --data '{
        "model": "anthropic/claude-4-5-sonnet",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions \
      --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
      --header 'Authorization: Bearer {google_api_token}' \
      --header 'Content-Type: application/json' \
      --data '{
        "model": "google/gemini-2.5-pro",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions \
      --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
      --header 'Authorization: Bearer {grok_api_token}' \
      --header 'Content-Type: application/json' \
      --data '{
        "model": "grok/grok-4",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions \
      --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
      --header 'Authorization: Bearer {dynamic_api_token}' \
      --header 'Content-Type: application/json' \
      --data '{
        "model": "dynamic/customer-support",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions \
      --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
      --header 'Authorization: Bearer {workers-ai_api_token}' \
      --header 'Content-Type: application/json' \
      --data '{
        "model": "workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'

## Supported Providers

The OpenAI-compatible endpoint supports models from the following providers:

  * [Anthropic](https://developers.cloudflare.com/ai-gateway/usage/providers/anthropic/)
  * [OpenAI](https://developers.cloudflare.com/ai-gateway/usage/providers/openai/)
  * [Groq](https://developers.cloudflare.com/ai-gateway/usage/providers/groq/)
  * [Mistral](https://developers.cloudflare.com/ai-gateway/usage/providers/mistral/)
  * [Cohere](https://developers.cloudflare.com/ai-gateway/usage/providers/cohere/)
  * [Perplexity](https://developers.cloudflare.com/ai-gateway/usage/providers/perplexity/)
  * [Workers AI](https://developers.cloudflare.com/ai-gateway/usage/providers/workersai/)
  * [Google-AI-Studio](https://developers.cloudflare.com/ai-gateway/usage/providers/google-ai-studio/)
  * [Google Vertex AI](https://developers.cloudflare.com/ai-gateway/usage/providers/vertex/)
  * [xAI](https://developers.cloudflare.com/ai-gateway/usage/providers/grok/)
  * [DeepSeek](https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/)
  * [Cerebras](https://developers.cloudflare.com/ai-gateway/usage/providers/cerebras/)
  * [Baseten](https://developers.cloudflare.com/ai-gateway/usage/providers/baseten/)
  * [Parallel](https://developers.cloudflare.com/ai-gateway/usage/providers/parallel/)



[PreviousWorkers Bindings](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/)[NextWorkers AI](https://developers.cloudflare.com/ai-gateway/usage/providers/workersai/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/chat-completion.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
