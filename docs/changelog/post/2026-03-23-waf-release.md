---
url: https://developers.cloudflare.com/changelog/post/2026-03-23-waf-release/
title: WAF Release - 2026-03-23 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:42.519174+00:00
---

# WAF Release - 2026-03-23 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-23-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 23, 2026

## WAF Release - 2026-03-23

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-23-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release focuses on new improvements to enhance coverage.

**Key Findings**

  * Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...97321c6c| N/A| Command Injection - Generic 9 - URI Vector| Log| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...1eb7a999| N/A | Command Injection - Generic 9 - Header Vector | Log | Disabled  
| This is a new detection.  
Cloudflare Managed Ruleset| ...0677175f| N/A | Command Injection - Generic 9 - Body Vector | Log | Disabled  
| This is a new detection.  
Cloudflare Managed Ruleset| ...479da68f| N/A| PHP, vBulletin, jQuery File Upload - Code Injection, Dangerous File Upload - CVE:CVE-2018-9206, CVE:CVE-2019-17132 (beta)| Log| Block| This rule has been merged into the original rule "PHP, vBulletin, jQuery File Upload - Code Injection, Dangerous File Upload - CVE:CVE-2018-9206, CVE:CVE-2019-17132" (ID: ...824b817c)
