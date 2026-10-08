---
url: https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/
title: Select models now require the Workers Paid plan \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:05.079626+00:00
---

# Select models now require the Workers Paid plan · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 28, 2026

## Select models now require the Workers Paid plan

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We are limiting Workers Free plan access to a few resource-intensive models so we can prioritize capacity for the broader Workers AI user base. This helps everyone get a more reliable inference experience, with fewer `429` and `3040` (Out of Capacity) errors.

The following models now require the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers):

  * [`@cf/moonshotai/kimi-k2.6`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.6/)
  * [`@cf/moonshotai/kimi-k2.7-code`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/)
  * [`@cf/zai-org/glm-5.2`](https://developers.cloudflare.com/workers-ai/models/glm-5.2/)



On the Workers Free plan, requests to these models now return a `403` HTTP error ([internal error `5035`](https://developers.cloudflare.com/workers-ai/platform/errors/)) prompting you to upgrade. The Workers Paid plan starts at $5 per month and still includes the 10,000 free Neurons per day allocation, with usage beyond that billed at each [model's pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Many models remain available on the Workers Free plan, including:

  * [`@cf/zai-org/glm-4.7-flash`](https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/)
  * [`@cf/google/gemma-4-26b-a4b-it`](https://developers.cloudflare.com/workers-ai/models/gemma-4-26b-a4b-it/)
  * [`@cf/nvidia/nemotron-3-120b-a12b`](https://developers.cloudflare.com/workers-ai/models/nemotron-3-120b-a12b/)



For the full list, refer to the [Workers AI model catalog](https://developers.cloudflare.com/workers-ai/models/).
