---
url: https://developers.cloudflare.com/changelog/post/2026-09-22-waf-release/
title: WAF Release - 2026-09-22 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:15.510420+00:00
---

# WAF Release - 2026-09-22 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-22-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 22, 2026

## WAF Release - 2026-09-22

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-22-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces new threat detections to enhance protection against Server-Side Request Forgery (SSRF) attempts using non-standard IP notations or jar loopback payloads, alongside new defenses against Server-Side Template Injection (SSTI) targeting Jinja environments.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...5f21b651| N/A| SSRF - Cloud,Link-Local non-standard IP notation| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...0f0313d6| N/A| SSRF - Block jar HTTP loopback payload| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...75cd912a| N/A| SSRF - Local non-standard IP notation| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...a1ba83f6| N/A| SSTI - Jinja Dangerous Globals Chain| Log| Block| This is a new detection.
