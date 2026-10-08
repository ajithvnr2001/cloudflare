---
url: https://developers.cloudflare.com/changelog/post/2026-09-29-user-insights-task-analysis/
title: Identify model overuse and potential savings with User Insights \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:17.048529+00:00
---

# Identify model overuse and potential savings with User Insights · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-29-user-insights-task-analysis/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 29, 2026

## Identify model overuse and potential savings with User Insights

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-29-user-insights-task-analysis/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway User Insights now gives you more context about the traffic flowing through your gateway. It shows what users and agents are doing with AI, and where a selected model may be more capable than a task requires.

On the analysis side, User Insights groups conversations by task, tracks conversation turns, and helps you compare model fit with cost and latency.

![User Insights task and model analysis grouped by task categories](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1434,height=606,format=webp/_astro/user-insights-task-analysis.CS2pm7wg.png)

The Potential Savings view highlights requests that may work with faster or less expensive models without compromising output quality. These are the same signals that Cloudflare's [Auto Router](https://developers.cloudflare.com/ai-gateway/features/auto-router/) uses to select a model based on task and cost.

![Potential Savings view comparing tasks and suggested models](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1506,height=669,format=webp/_astro/user-insights-potential-savings.C7j_Gjcn.png)

These new insights are available to all AI Gateway customers at no additional cost. For more information, refer to [User Insights](https://developers.cloudflare.com/ai-gateway/observability/user-insights/).
