---
url: https://developers.cloudflare.com/changelog/post/2026-09-15-waf-release/
title: WAF Release - 2026-09-15 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:14.217108+00:00
---

# WAF Release - 2026-09-15 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-15-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 15, 2026

## WAF Release - 2026-09-15

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-15-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces new threat detections to enhance protection against command injection attempts, Server-Side Request Forgery (SSRF) targeting cloud metadata, and information disclosure within version control history.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...ca453d31| N/A| SSRF - Cloud - 3| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...e540f17f| N/A| Version Control - Information Disclosure - Beta| Log| Block| This rule is merged into the original rule "Version Control - Information Disclosure" (ID: ...0550c529).  
Cloudflare Managed Ruleset| ...ba458b4b| N/A| Command Injection - Generic 10| Log| Block| This is a new detection.
