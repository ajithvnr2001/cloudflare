---
url: https://developers.cloudflare.com/ai-gateway/integrations/vercel-ai-sdk/
title: Vercel AI SDK \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:31.783517+00:00
---

# Vercel AI SDK · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/integrations/vercel-ai-sdk/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /Integrations
  4. /Vercel AI SDK



# Vercel AI SDK

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/integrations/vercel-ai-sdk/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstallationExamples AI binding with third-party models Fallback Providers

The [Vercel AI SDK ↗︎](https://sdk.vercel.ai/) is a TypeScript library for building AI applications. The SDK supports many different AI providers, tools for streaming completions, and more. To use Cloudflare AI Gateway with Vercel AI SDK, you will need to use the `ai-gateway-provider` package.

## Installation
    
    
    npm install ai-gateway-provider

## Examples

Make a request to 

![](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48IS0tIFVwbG9hZGVkIHRvOiBTVkcgUmVwbywgd3d3LnN2Z3JlcG8uY29tLCBHZW5lcmF0b3I6IFNWRyBSZXBvIE1peGVyIFRvb2xzIC0tPgo8c3ZnIGZpbGw9IiMwMDAwMDAiIHdpZHRoPSI2NHB4IiBoZWlnaHQ9IjY0cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgcm9sZT0iaW1nIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjx0aXRsZT5PcGVuQUkgaWNvbjwvdGl0bGU+PHBhdGggZD0iTTIyLjI4MTkgOS44MjExYTUuOTg0NyA1Ljk4NDcgMCAwIDAtLjUxNTctNC45MTA4IDYuMDQ2MiA2LjA0NjIgMCAwIDAtNi41MDk4LTIuOUE2LjA2NTEgNi4wNjUxIDAgMCAwIDQuOTgwNyA0LjE4MThhNS45ODQ3IDUuOTg0NyAwIDAgMC0zLjk5NzcgMi45IDYuMDQ2MiA2LjA0NjIgMCAwIDAgLjc0MjcgNy4wOTY2IDUuOTggNS45OCAwIDAgMCAuNTExIDQuOTEwNyA2LjA1MSA2LjA1MSAwIDAgMCA2LjUxNDYgMi45MDAxQTUuOTg0NyA1Ljk4NDcgMCAwIDAgMTMuMjU5OSAyNGE2LjA1NTcgNi4wNTU3IDAgMCAwIDUuNzcxOC00LjIwNTggNS45ODk0IDUuOTg5NCAwIDAgMCAzLjk5NzctMi45MDAxIDYuMDU1NyA2LjA1NTcgMCAwIDAtLjc0NzUtNy4wNzI5em0tOS4wMjIgMTIuNjA4MWE0LjQ3NTUgNC40NzU1IDAgMCAxLTIuODc2NC0xLjA0MDhsLjE0MTktLjA4MDQgNC43NzgzLTIuNzU4MmEuNzk0OC43OTQ4IDAgMCAwIC4zOTI3LS42ODEzdi02LjczNjlsMi4wMiAxLjE2ODZhLjA3MS4wNzEgMCAwIDEgLjAzOC4wNTJ2NS41ODI2YTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0NSA0LjQ5NDR6bS05LjY2MDctNC4xMjU0YTQuNDcwOCA0LjQ3MDggMCAwIDEtLjUzNDYtMy4wMTM3bC4xNDIuMDg1MiA0Ljc4MyAyLjc1ODJhLjc3MTIuNzcxMiAwIDAgMCAuNzgwNiAwbDUuODQyOC0zLjM2ODV2Mi4zMzI0YS4wODA0LjA4MDQgMCAwIDEtLjAzMzIuMDYxNUw5Ljc0IDE5Ljk1MDJhNC40OTkyIDQuNDk5MiAwIDAgMS02LjE0MDgtMS42NDY0ek0yLjM0MDggNy44OTU2YTQuNDg1IDQuNDg1IDAgMCAxIDIuMzY1NS0xLjk3MjhWMTEuNmEuNzY2NC43NjY0IDAgMCAwIC4zODc5LjY3NjVsNS44MTQ0IDMuMzU0My0yLjAyMDEgMS4xNjg1YS4wNzU3LjA3NTcgMCAwIDEtLjA3MSAwbC00LjgzMDMtMi43ODY1QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQwOCA3Ljg3MnptMTYuNTk2MyAzLjg1NThMMTMuMTAzOCA4LjM2NCAxNS4xMTkyIDcuMmEuMDc1Ny4wNzU3IDAgMCAxIC4wNzEgMGw0LjgzMDMgMi43OTEzYTQuNDk0NCA0LjQ5NDQgMCAwIDEtLjY3NjUgOC4xMDQydi01LjY3NzJhLjc5Ljc5IDAgMCAwLS40MDctLjY2N3ptMi4wMTA3LTMuMDIzMWwtLjE0Mi0uMDg1Mi00Ljc3MzUtMi43ODE4YS43NzU5Ljc3NTkgMCAwIDAtLjc4NTQgMEw5LjQwOSA5LjIyOTdWNi44OTc0YS4wNjYyLjA2NjIgMCAwIDEgLjAyODQtLjA2MTVsNC44MzAzLTIuNzg2NmE0LjQ5OTIgNC40OTkyIDAgMCAxIDYuNjgwMiA0LjY2ek04LjMwNjUgMTIuODYzbC0yLjAyLTEuMTYzOGEuMDgwNC4wODA0IDAgMCAxLS4wMzgtLjA1NjdWNi4wNzQyYTQuNDk5MiA0LjQ5OTIgMCAwIDEgNy4zNzU3LTMuNDUzN2wtLjE0Mi4wODA1TDguNzA0IDUuNDU5YS43OTQ4Ljc5NDggMCAwIDAtLjM5MjcuNjgxM3ptMS4wOTc2LTIuMzY1NGwyLjYwMi0xLjQ5OTggMi42MDY5IDEuNDk5OHYyLjk5OTRsLTIuNTk3NCAxLjQ5OTctMi42MDY3LTEuNDk5N1oiLz48L3N2Zz4=)OpenAI

Unified

API with 

Stored Key (BYOK)
    
    
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

### AI binding with third-party models

If you are already using the [`workers-ai-provider` ↗︎](https://www.npmjs.com/package/workers-ai-provider) package, you can route requests through AI Gateway to call third-party models without needing separate provider SDKs. Pass a `gateway` option with your gateway ID to `createWorkersAI`:
    
    
    import { createWorkersAI } from "workers-ai-provider";
    import { streamText } from "ai";
    
    export default {
    	async fetch(request, env) {
    		const workersai = createWorkersAI({
    			binding: env.AI,
    			gateway: { id: "my-gateway" },
    		});
    
    		const result = streamText({
    			model: workersai("openai/gpt-4o"),
    			messages: [{ role: "user", content: "Write a short story" }],
    		});
    
    		return result.toTextStreamResponse();
    	},
    };
    
    
    import { createWorkersAI } from "workers-ai-provider";
    import { streamText } from "ai";
    
    export default {
    	async fetch(request, env) {
    		const workersai = createWorkersAI({
    			binding: env.AI,
    			gateway: { id: "my-gateway" },
    		});
    
    		const result = streamText({
    			model: workersai("openai/gpt-4o"),
    			messages: [{ role: "user", content: "Write a short story" }],
    		});
    
    		return result.toTextStreamResponse();
    	},
    } satisfies ExportedHandler<Env>;

This works with any [supported provider and model](https://developers.cloudflare.com/ai/models/) available through AI Gateway.

### Fallback Providers

To specify model or provider fallbacks to handle request failures and ensure reliability, you can pass an array of models to the `model` option.
    
    
    const { text } = await generateText({
    	model: aigateway([openai.chat("gpt-5.1"), anthropic("claude-sonnet-4-5")]),
    	prompt: "Write a vegetarian lasagna recipe for 4 people.",
    });

[PreviousOpenTelemetry](https://developers.cloudflare.com/ai-gateway/observability/otel-integration/)[NextAgents ↗︎](https://developers.cloudflare.com/agents/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/integrations/vercel-ai-sdk.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
