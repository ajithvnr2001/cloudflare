---
url: https://developers.cloudflare.com/web-search/
title: Overview \u00b7 Cloudflare Web Search API docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:53.590571+00:00
---

# Overview · Cloudflare Web Search API docs

> Source: https://developers.cloudflare.com/web-search/

  1. [Home](https://developers.cloudflare.com/)
  2. /Web Search API



# Cloudflare Web Search API

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/web-search/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFeaturesRelated productsMore resources

Give your agents real-time web context with a single API call.

Available in open beta

Web Search API lets your AI agents and applications search the Internet and ground their responses in live information. Instead of guessing URLs or relying on a model's training cutoff, your agent sends a search query and receives structured results — titles, URLs, and descriptions — that you can pass straight into a model's context.

Web Search API runs through [AI Gateway](https://developers.cloudflare.com/ai-gateway/), so every search gets the same logging, analytics, billing, and access controls as your model inference requests. You can call it from any backend with the REST API, or from a Worker with the AI binding.

[How to use](https://developers.cloudflare.com/web-search/how-to-use/) [Browse providers](https://developers.cloudflare.com/web-search/providers/)

* * *

## Features

[Multiple search providers](https://developers.cloudflare.com/web-search/providers/)

Choose between Ceramic.ai, Exa, and Linkup with a single `provider` parameter. All providers return results in the same format, so you can switch without changing your code.

View providers

[Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/)

Pay for searches with your AI Gateway credits at each provider's list API price, with no additional markup. You can also bring your own provider API key.

Learn about Unified Billing

[Observability](https://developers.cloudflare.com/ai-gateway/observability/logging/)

Search requests appear in your AI Gateway logs and analytics alongside your model inference requests.

View logging

[Responsible crawling](https://developers.cloudflare.com/web-search/about/#crawler-standards)

Every provider commits to Cloudflare's [verified bot](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/) requirements and returns a link to the source of every result.

Learn more

* * *

## Related products

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Observe and control your AI applications with analytics, caching, rate limiting, and model fallback.

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Run machine learning models, powered by serverless GPUs, on Cloudflare's global network.

[Agents](https://developers.cloudflare.com/agents/)

Build AI-powered agents that can perform tasks, persist state, browse the web, and communicate in real time.

* * *

## More resources

### [Developer Discord](https://discord.cloudflare.com)

Connect with the Workers community on Discord to ask questions, show what you are building, and discuss the platform with other developers.

### [Use cases](https://developers.cloudflare.com/use-cases/ai/)

Learn how you can build and deploy ambitious AI applications to Cloudflare's global network.

### [@CloudflareDev](https://x.com/cloudflaredev)

Follow @CloudflareDev on Twitter to learn about product announcements, and what is new in Cloudflare Workers.

[NextAbout](https://developers.cloudflare.com/web-search/about/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/web-search/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
