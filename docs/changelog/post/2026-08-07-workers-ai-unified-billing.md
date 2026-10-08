---
url: https://developers.cloudflare.com/changelog/post/2026-08-07-workers-ai-unified-billing/
title: Workers AI and AI Gateway unify model access and billing \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:07.457452+00:00
---

# Workers AI and AI Gateway unify model access and billing · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-07-workers-ai-unified-billing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 7, 2026

## Workers AI and AI Gateway unify model access and billing

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-07-workers-ai-unified-billing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers AI and AI Gateway now provide a unified path for accessing models and managing inference traffic. Use the same AI binding and REST API to call models hosted on Workers AI or by supported third-party providers, with AI Gateway providing observability, logging, caching, security, and billing controls.

#### Unified entrypoints and observability

The [AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/) supports both Workers AI and third-party models through `env.AI.run()`. The [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/) provides shared `/ai/` endpoints with Cloudflare authentication across providers.

Route a Workers AI request through AI Gateway by specifying a gateway ID. Use `default` to automatically create a gateway on the first authenticated request, or specify an existing gateway to separate applications and workloads:
    
    
    const response = await env.AI.run(
    	"@cf/zai-org/glm-5.2",
    	{
    		messages: [{ role: "user", content: "What is the capital of France?" }],
    	},
    	{
    		gateway: { id: "default" },
    	},
    );
    
    
    const response = await env.AI.run(
    	"@cf/zai-org/glm-5.2",
    	{
    		messages: [{ role: "user", content: "What is the capital of France?" }],
    	},
    	{
    		gateway: { id: "default" },
    	},
    );

Requests routed through AI Gateway can be logged and included in analytics for request volume, errors, latency, token usage, and costs. You can also configure controls such as caching, rate limiting, and request retries on the gateway.

#### Unified billing and higher rate limits

You can now use prepaid [AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) to pay for Workers AI inference. This provides one credit balance for Workers AI and supported third-party model providers. To use credits for Workers AI, set the gateway's [Workers AI billing setting](https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing) to **Unified billing**. Workers AI requests routed through that gateway deduct from your credit balance in real time.

Prepaid credits also provide access to the following Workers AI frontier models without requiring the Workers Paid plan. Each frontier Workers AI model has a rate limit of 50 requests per minute per account, per model when billed with AI Gateway credits, compared to 20 requests per minute through standard Workers AI billing:

  * [`@cf/moonshotai/kimi-k2.6`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.6/)
  * [`@cf/moonshotai/kimi-k2.7-code`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/)
  * [`@cf/zai-org/glm-5.2`](https://developers.cloudflare.com/workers-ai/models/glm-5.2/)



These limits are designed for typical agentic and coding workloads, where requests to frontier models can take longer to complete.

For details, refer to [Workers AI limits](https://developers.cloudflare.com/workers-ai/platform/limits/), [Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/), [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/), and the [AI Gateway model catalog](https://developers.cloudflare.com/ai/models/).
