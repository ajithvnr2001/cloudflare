---
url: https://developers.cloudflare.com/changelog/post/2026-01-12-waf-release/
title: WAF Release - 2026-01-12 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:45.305255+00:00
---

# WAF Release - 2026-01-12 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-12-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 12, 2026

## WAF Release - 2026-01-12

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release focuses on improvements to existing detections to enhance coverage.

**Key Findings**

  * Existing rule enhancements have been deployed to improve detection resilience against SQL Injection.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...48a1841a| N/A| SQLi - AND/OR MAKE_SET/ELT - Beta| Log| Block| This rule is merged into the original rule "SQLi - AND/OR MAKE_SET/ELT" (ID: ...252d3934)  
Cloudflare Managed Ruleset| ...9e553ad3| N/A | SQLi - Benchmark Function - Beta | Log | Block  
| This rule is merged into the original rule "SQLi - Benchmark Function" (ID: ...2ebc44ad)
