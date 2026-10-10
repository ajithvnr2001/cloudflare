---
url: https://developers.cloudflare.com/changelog/post/2025-02-04-radar-ai-insights/
title: Expanded AI insights in Cloudflare Radar \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:54.982800+00:00
---

# Expanded AI insights in Cloudflare Radar · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-02-04-radar-ai-insights/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 4, 2025

## Expanded AI insights in Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) has expanded its AI insights with new API endpoints for Internet services rankings, robots.txt analysis, and AI inference data.

#### Internet services ranking

Radar now provides [rankings for Internet services](https://developers.cloudflare.com/radar/glossary/#internet-services-ranking), including Generative AI platforms, based on anonymized 1.1.1.1 resolver data. Previously limited to the annual Year in Review, these insights are now available daily via the [API](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/subresources/internet_services/), through the following endpoints:

  * [`/ranking/internet_services/top`](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/subresources/internet_services/methods/top/) show service popularity at a specific date.
  * [`/ranking/internet_services/timeseries_groups`](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/subresources/internet_services/methods/timeseries_groups/) track ranking trends over time.



#### Robots.txt

Radar now analyzes [robots.txt](https://developers.cloudflare.com/radar/glossary/#robotstxt) files from the top 10,000 domains, identifying AI bot access rules. AI-focused user agents from [ai.robots.txt ↗︎](https://github.com/ai-robots-txt/ai.robots.txt) are categorized as:

  * **Fully allowed/disallowed** if directives apply to all paths (`*`).
  * **Partially allowed/disallowed** if restrictions apply to specific paths.



These insights are now available weekly via the [API](https://developers.cloudflare.com/api/resources/radar/subresources/robots_txt/), through the following endpoints:

  * [`/robots_txt/top/user_agents/directive`](https://developers.cloudflare.com/api/resources/radar/subresources/robots_txt/subresources/top/subresources/user_agents/methods/directive/) to get the top AI user agents by directive.
  * [`/robots_txt/top/domain_categories`](https://developers.cloudflare.com/api/resources/radar/subresources/robots_txt/subresources/top/methods/domain_categories/) to get the top domain categories by robots.txt files.



#### Workers AI

Radar now provides insights into public AI inference models from [Workers AI](https://developers.cloudflare.com/workers-ai/), tracking usage trends across **models** and **tasks**. These insights are now available via the [API](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/), through the following endpoints:

  * [`/ai/inference/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/subresources/summary/) to view aggregated `model` and `task` popularity.
  * [`/ai/inference/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/subresources/timeseries_groups/) to track changes over time for `model` or `task`.



Learn more about the new Radar AI insights in our [blog post ↗︎](https://blog.cloudflare.com/expanded-ai-insights-on-cloudflare-radar/).
