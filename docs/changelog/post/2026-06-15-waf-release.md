---
url: https://developers.cloudflare.com/changelog/post/2026-06-15-waf-release/
title: WAF Release - 2026-06-15 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:36.615825+00:00
---

# WAF Release - 2026-06-15 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-15-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 15, 2026

## WAF Release - 2026-06-15

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release introduces new managed protection to address a critical SQL injection vulnerability in Ghost CMS (CVE-2026-26980) and a new generic rule designed to identify and block sophisticated SQL Injection (SQLi) bypass attempts leveraging obfuscated boolean logic. These rules protect affected installations from unauthorized data exfiltration at the network edge.

**Key Findings**

  * CVE-2026-26980: A blind SQL injection vulnerability in the Ghost CMS Content API (versions 3.24.0 to 6.19.0) allows unauthenticated remote attackers to inject malicious SQL commands via query parameters due to improper input validation.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...b4c29bc6| N/A| Ghost CMS - SQLi - CVE:CVE-2026-26980| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...b56f403f| N/A| SQLi - Obfuscated Boolean - URI| Log| Disabled| This is a new detection.
