---
url: https://developers.cloudflare.com/use-cases/ai/build-and-run/
title: Build and run AI applications \u00b7 Cloudflare use cases
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:09.079459+00:00
---

# Build and run AI applications · Cloudflare use cases

> Source: https://developers.cloudflare.com/use-cases/ai/build-and-run/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Use cases](https://developers.cloudflare.com/use-cases/)
  3. /[AI applications](https://developers.cloudflare.com/use-cases/ai/)
  4. /Build and run AI applications



# Build and run AI applications

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/use-cases/ai/build-and-run/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSolutions Workers Workers AI AI Gateway Durable ObjectsGet started

To build and deploy an AI application, you need compute for application logic, a way to run inference, and a gateway to manage costs across providers. Cloudflare Workers hosts your application logic and serves your frontend. Workers AI runs inference at the edge with pay-per-use pricing. AI Gateway adds caching, rate limiting, and observability across OpenAI, Anthropic, and other providers. Durable Objects coordinate stateful workflows and multi-turn conversations.

## Solutions

### Workers

Build and deploy serverless applications on Cloudflare's global network. [Learn more about Workers](https://developers.cloudflare.com/workers/).

  * **Streaming responses** \- Stream AI responses token-by-token as they generate, without buffering the full reply
  * **Full-stack deployment** \- Serve frontend and backend from a single deployment without managing separate infrastructure



### Workers AI

Run inference on Cloudflare's global network via a Workers binding, with pay-per-use pricing. [Learn more about Workers AI](https://developers.cloudflare.com/workers-ai/).

  * **Global inference** \- Run models at the Cloudflare location nearest to the user, reducing round-trip latency
  * **Pay-per-use pricing** \- No GPU reservations or idle costs; pay only for tokens processed



### AI Gateway

Proxy requests to any AI provider with caching, rate limiting, and unified analytics. [Learn more about AI Gateway](https://developers.cloudflare.com/ai-gateway/).

  * **Provider flexibility** \- Route requests to OpenAI, Anthropic, Workers AI, or any other provider through a single endpoint
  * **Unified observability** \- Track request volume, latency, costs, and errors across all providers in one place



### Durable Objects

Stateful objects with strongly consistent storage and coordination. [Learn more about Durable Objects](https://developers.cloudflare.com/durable-objects/).

  * **Stateful workflows** \- Coordinate multi-step AI pipelines and maintain conversation state across requests



## Get started

  1. [Workers AI get started](https://developers.cloudflare.com/workers-ai/get-started/)
  2. [AI Gateway get started](https://developers.cloudflare.com/ai-gateway/get-started/)
  3. [Durable Objects get started](https://developers.cloudflare.com/durable-objects/get-started/)



[PreviousOverview](https://developers.cloudflare.com/use-cases/ai/)[NextStore and retrieve context](https://developers.cloudflare.com/use-cases/ai/store-and-retrieve-context/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/use-cases/ai/build-and-run.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
