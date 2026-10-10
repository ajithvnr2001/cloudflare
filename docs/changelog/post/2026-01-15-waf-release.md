---
url: https://developers.cloudflare.com/changelog/post/2026-01-15-waf-release/
title: WAF Release - 2026-01-15 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:45.147532+00:00
---

# WAF Release - 2026-01-15 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-15-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 15, 2026

## WAF Release - 2026-01-15

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release focuses on improvements to existing detections to enhance coverage.

**Key Findings**

  * Existing rule enhancements have been deployed to improve detection resilience against SQL Injection.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...ad7dad3e| N/A| SQLi - String Function - Beta| Log| Block| This rule is merged into the original rule "SQLi - String Function" (ID: ...d32b798c)  
Cloudflare Managed Ruleset| ...9e553ad3| N/A | SQLi - Sub Query - Beta | Log | Block  
| This rule is merged into the original rule "SQLi - Sub Query" (ID: ...743e66b1)
