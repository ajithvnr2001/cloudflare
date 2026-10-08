---
url: https://developers.cloudflare.com/changelog/post/2026-07-17-emergency-waf-release/
title: WAF Release - 2026-07-17 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:04.075542+00:00
---

# WAF Release - 2026-07-17 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-17-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 17, 2026

## WAF Release - 2026-07-17 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-17-emergency-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This emergency release adds a new managed rule to block active exploitation of a critical remote code execution (RCE) and SQL injection (SQLi) vulnerability found in popular web frameworks.

**Key Findings**

  * Generic Frameworks - Unauthenticated RCE: Attackers can execute arbitrary system commands with web server privileges by sending malicious input containing invalid path sequences during request processing.

  * Generic Frameworks - SQLi: Attackers can execute unauthorized database queries due to a failure to sanitize input values within request parameters.


Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...550664b6| N/A| Generic Rules - Unauthenticated RCE| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...ed933fcc| N/A| Generic Rules - SQLi | N/A| Block| This is a new detection.  
Cloudflare Free Ruleset| ...b5ec246a| N/A| Generic Rules - Unauthenticated RCE | N/A| Block| This is a new detection.  
Cloudflare Free Ruleset| ...33697a1a| N/A| Generic Rules - SQLi | N/A| Block| This is a new detection.
