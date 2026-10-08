---
url: https://developers.cloudflare.com/changelog/post/2026-07-01-botbase-attribution-business-insights/
title: More visibility into bot traffic with BotBase and Business Insights \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:00.642878+00:00
---

# More visibility into bot traffic with BotBase and Business Insights · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-01-botbase-attribution-business-insights/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 1, 2026

## More visibility into bot traffic with BotBase and Business Insights

[Bots](https://developers.cloudflare.com/bots/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-01-botbase-attribution-business-insights/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

With Content Independence Day 2026, [Enterprise Bot Management](https://developers.cloudflare.com/bots/get-started/bot-management/) customers get two new tools that make bot traffic far easier to see and reason about: [BotBase](https://developers.cloudflare.com/bots/botbase/), a searchable directory of every bot Cloudflare tracks, and [Business Insights](https://developers.cloudflare.com/bots/business-insights/), a dashboard that shows how much value each crawler sends back to your business.

BotBase is Cloudflare's directory of all known bots and agents, available directly in the dashboard. It shows how Cloudflare classifies each bot by behavior — Search, Agent, Training, and other categories such as Transact, Data Collection, SEO, and Ads Verification — so you can understand why a given crawler is visiting you. You can search and filter the full catalogue, filter your own traffic down to a single bot to investigate its activity on your zone, and copy any bot's detection ID to target it precisely in [Security rules](https://developers.cloudflare.com/security/rules/). Every tracked bot in BotBase is also published in [Cloudflare Radar's bots and agents directory ↗︎](https://radar.cloudflare.com/bots/directory).

Business Insights is built for content owners and business decision-makers who want to know which bots help or harm their business, without reading rule syntax. The dashboard reports crawl-to-referral ratios both site-wide and per bot operator — comparing how often a company crawls your content against how many visitors it actually refers back — over the last 24 hours, 7 days, or 30 days. Each operator is labeled with Cloudflare's [updated classification](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/) and an action status of Allowed, Blocked, or Partially blocked, giving stakeholders a shared, at-a-glance view of the AI traffic reaching your site.

![The Business Insights dashboard, showing bot traffic, content page requests, crawl-to-referral ratio, and a per-operator bot activity table](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=8192,height=5064,format=webp/_astro/attribution-business-insights.Cu-ZtxkX.png)
