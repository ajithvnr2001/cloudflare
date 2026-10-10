---
url: https://developers.cloudflare.com/changelog/post/2026-10-01-dynamic-comparison-values/
title: Compare dynamic values in Rules expressions \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:29.748902+00:00
---

# Compare dynamic values in Rules expressions · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-01-dynamic-comparison-values/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 1, 2026

## Compare dynamic values in Rules expressions

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Rules expressions now support dynamic values on both sides of equality and ordering comparisons. You can compare request fields or function results with one another.

For example, compare the current request path with its original value:
    
    
    http.request.uri.path ne raw.http.request.uri.path

For supported operators and examples, refer to [Compare dynamic values](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#compare-dynamic-values).
