---
url: https://developers.cloudflare.com/changelog/post/2026-06-05-spend-limits/
title: Control AI costs with spend limits \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:37.073343+00:00
---

# Control AI costs with spend limits · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-05-spend-limits/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 5, 2026

## Control AI costs with spend limits

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway now supports spend limits — cost-based budgets that track cumulative dollar spend and block requests when the budget is exceeded. Unlike rate limiting, which caps the number of requests, spend limits track actual cost based on token usage and model pricing.

You can scope limits by model, provider, or custom metadata dimensions. For example, give each user a $200/day budget, cap total gateway spend at $10,000/day, or limit a specific model to $50/day per user. Each rule uses a configurable time window with fixed or sliding enforcement.

Spend limits work with both [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) and [BYOK](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/) requests for models with known pricing.

For more details, refer to the [Spend limits documentation](https://developers.cloudflare.com/ai-gateway/features/spend-limits/).
