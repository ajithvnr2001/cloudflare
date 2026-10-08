---
url: https://developers.cloudflare.com/changelog/post/2026-09-01-waf-release/
title: WAF Release - 2026-09-01 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:12.010717+00:00
---

# WAF Release - 2026-09-01 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-01-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 1, 2026

## WAF Release - 2026-09-01

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-01-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces a new threat detection to enhance protection against SQL injection (SQLi) attempts exploiting complex query syntax.

**Key Findings**

  * SQLi Protection: Improved coverage for SQL injection patterns involving WHERE comparisons combined with WITH clauses.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...bcfa0966| N/A| SQLi - WHERE Comparison With WITH Clause| Log| Block| This is a new detection.
