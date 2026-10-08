---
url: https://developers.cloudflare.com/changelog/post/2026-04-17-redirects-for-ai-training/
title: Introducing Redirects for AI Training \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:47.761621+00:00
---

# Introducing Redirects for AI Training · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-17-redirects-for-ai-training/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 17, 2026

## Introducing Redirects for AI Training

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-17-redirects-for-ai-training/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare's network now supports redirecting verified AI training crawlers to canonical URLs when they request deprecated or duplicate pages. When enabled via **AI Crawl Control** > **Quick Actions** , AI training crawlers that request a page with a canonical tag pointing elsewhere receive a 301 redirect to the canonical version. Humans, search engine crawlers, and AI Search agents continue to see the original page normally.

This feature leverages your existing `<link rel="canonical">` tags. No additional configuration required beyond enabling the toggle. Available on Pro, Business, and Enterprise plans at no additional cost.

Refer to the [Redirects for AI Training documentation](https://developers.cloudflare.com/ai-crawl-control/reference/redirects-for-ai-training/) for details.
