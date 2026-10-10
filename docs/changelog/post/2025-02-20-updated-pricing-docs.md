---
url: https://developers.cloudflare.com/changelog/post/2025-02-20-updated-pricing-docs/
title: Workers AI updated pricing \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:54.673045+00:00
---

# Workers AI updated pricing · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-02-20-updated-pricing-docs/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 20, 2025

## Workers AI updated pricing

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We've updated the Workers AI [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/) to include the latest models and how model usage maps to Neurons.

  * Each model's core input format(s) (tokens, audio seconds, images, etc) now include mappings to Neurons, making it easier to understand how your included Neuron volume is consumed and how you are charged at scale
  * Per-model pricing, instead of the previous bucket approach, allows us to be more flexible on how models are charged based on their size, performance and capabilities. As we optimize each model, we can then pass on savings for that model.
  * You will still only pay for what you consume: Workers AI inference is serverless, and not billed by the hour.



Going forward, models will be launched with their associated Neuron costs, and we'll be updating the Workers AI dashboard and API to reflect consumption in both raw units and Neurons. Visit the [Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/) page to learn more about Workers AI pricing.
