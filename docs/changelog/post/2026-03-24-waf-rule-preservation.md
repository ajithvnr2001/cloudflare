---
url: https://developers.cloudflare.com/changelog/post/2026-03-24-waf-rule-preservation/
title: Advanced WAF customization for AI Crawl Control blocks \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:41.591926+00:00
---

# Advanced WAF customization for AI Crawl Control blocks · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-24-waf-rule-preservation/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 24, 2026

## Advanced WAF customization for AI Crawl Control blocks

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Crawl Control now supports extending the underlying WAF rule with custom modifications. Any changes you make directly in the WAF custom rules editor — such as adding path-based exceptions, extra user agents, or additional expression clauses — are preserved when you update crawler actions in AI Crawl Control.

If the WAF rule expression has been modified in a way AI Crawl Control cannot parse, a warning banner appears on the **Crawlers** page with a link to view the rule directly in WAF.

For more information, refer to [WAF rule management](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/#waf-rule-management).
