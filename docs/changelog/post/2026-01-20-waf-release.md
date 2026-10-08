---
url: https://developers.cloudflare.com/changelog/post/2026-01-20-waf-release/
title: WAF Release - 2026-01-20 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:34.282802+00:00
---

# WAF Release - 2026-01-20 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-20-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 20, 2026

## WAF Release - 2026-01-20

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-20-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release focuses on improvements to existing detections to enhance coverage.

**Key Findings**

  * Existing rule enhancements have been deployed to improve detection resilience against SQL injection.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...68d90c8f| N/A| SQLi - Comment - Beta| Log| Block| This rule is merged into the original rule "SQLi - Comment" (ID: ...6d8d8fe4)  
Cloudflare Managed Ruleset| ...faa045cf| N/A | SQLi - Comparison - Beta | Log | Block  
| This rule is merged into the original rule "SQLi - Comparison" (ID: ...e7907480)
