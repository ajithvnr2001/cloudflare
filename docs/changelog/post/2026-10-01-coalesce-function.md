---
url: https://developers.cloudflare.com/changelog/post/2026-10-01-coalesce-function/
title: Handle missing values with coalesce() \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:18.257808+00:00
---

# Handle missing values with coalesce() · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-01-coalesce-function/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 1, 2026

## Handle missing values with coalesce()

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-01-coalesce-function/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The `coalesce()` function returns the first argument that is not nil. Use it to provide a fallback in rule expressions:
    
    
    http.request.uri.path eq coalesce(http.request.uri.args["expected_path"][0], "/")

For details, refer to the [`coalesce()` function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#coalesce).
