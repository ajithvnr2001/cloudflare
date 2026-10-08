---
url: https://developers.cloudflare.com/changelog/post/2026-08-05-user-insights/
title: Track AI spend and catch anomalous usage with User Insights \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:06.853288+00:00
---

# Track AI spend and catch anomalous usage with User Insights · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-05-user-insights/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 5, 2026

## Track AI spend and catch anomalous usage with User Insights

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-05-user-insights/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway now includes User Insights, a dashboard that gives you two things at once: clear visibility into how much your organization spends on AI, and a security signal that surfaces users whose usage suddenly looks abnormal. It works on the traffic already flowing through your gateway, so there is no additional setup.

On the spend side, User Insights shows organization-wide totals for cost, requests, tokens, and adoption, and lets you drill into an individual user to see their spend, top models and providers, cache hit rate, and more. To attribute usage to individual users, add a user identifier with custom metadata or put your gateway behind Cloudflare Access.

On the security side, User Insights baselines each user's normal usage from their 95th percentile (p95) session cost over the last 30 days, then flags sessions that exceed both that baseline and an organization-level threshold. A sudden jump above a user's own pattern is often the first sign of a compromised credential or a misbehaving agent, so you can investigate before it shows up on your bill.

User Insights is available to all AI Gateway customers at no additional cost.
