---
url: https://developers.cloudflare.com/changelog/post/2026-04-17-radar-ai-insights-updates/
title: AI Insights updates on Cloudflare Radar \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:40.041478+00:00
---

# AI Insights updates on Cloudflare Radar · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-17-radar-ai-insights-updates/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 17, 2026

## AI Insights updates on Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) adds three new features to the [AI Insights ↗︎](https://radar.cloudflare.com/ai-insights) page, expanding visibility into how AI bots, crawlers, and agents interact with the web.

#### Adoption of AI agent standards

The AI Insights page now includes an [adoption of AI agent standards ↗︎](https://radar.cloudflare.com/ai-insights#adoption-of-ai-agent-standards) widget that tracks how websites adopt agent-facing standards. The data is filterable by domain category and updated weekly on Mondays. This data is also available through the [Agent Readiness API reference](https://developers.cloudflare.com/api/resources/radar/subresources/agent_readiness/methods/summary/).

![Screenshot of the adoption of AI agent standards chart](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1332,format=webp/_astro/agent-readiness-adoption-chart.B3ATN59P.png)

[URL Scanner ↗︎](https://radar.cloudflare.com/scan) reports now include an **Agent readiness** tab that evaluates a scanned URL against the criteria used by the [Agent Readiness score tool ↗︎](https://isitagentready.com/).

![Screenshot of the URL Scanner agent readiness tab](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1999,height=1145,format=webp/_astro/agent-readiness-url-scanner.DRVuuaUi.png)

For more details, refer to the [Agent Readiness blog post ↗︎](https://blog.cloudflare.com/agent-readiness/).

#### Markdown for Agents savings

A new [savings gauge ↗︎](https://radar.cloudflare.com/ai-insights#markdown-for-agents-savings) shows the median response-size reduction when serving Markdown instead of HTML to AI bots and crawlers. This highlights the bandwidth and token savings that [Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) provides.

![Screenshot of the Markdown for Agents savings gauge](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=614,height=652,format=webp/_astro/markdown-for-agents-savings.Di1GjNON.png)

For more details, refer to the [Markdown for Agents API reference](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/markdown_for_agents/methods/summary).

#### Response status

The new [response status widget ↗︎](https://radar.cloudflare.com/ai-insights#response-status) displays the distribution of HTTP response status codes returned to AI bots and crawlers. Results are groupable by individual status code (200, 403, 404) or by category (2xx, 3xx, 4xx, 5xx).

The same widget is available on each verified bot's detail page (only available for AI bots), for example [Google ↗︎](https://radar.cloudflare.com/bots/directory/google#response-status).

![Screenshot of the response status distribution widget](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=878,format=webp/_astro/ai-response-status.BwSMF23Z.png)

Explore all three features on the [Cloudflare Radar AI Insights ↗︎](https://radar.cloudflare.com/ai-insights) page.
