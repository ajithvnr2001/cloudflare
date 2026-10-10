---
url: https://developers.cloudflare.com/changelog/post/2026-06-23-waf-release/
title: WAF Release - 2026-06-23 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:36.100490+00:00
---

# WAF Release - 2026-06-23 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-23-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 23, 2026

## WAF Release - 2026-06-23

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release introduces new managed protection to address a critical pre-authentication OS command injection vulnerability in Ivanti Sentry (CVE-2026-10520).

**Key Findings**

  * CVE-2026-10520: An OS command injection vulnerability in Ivanti Sentry allows remote, unauthenticated attackers to execute arbitrary system commands with root privileges. The flaw stems from improper sanitization of input strings parsed during internal configuration handling.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...242fdf83| N/A| Ivanti Sentry - Command Injection - CVE:CVE-2026-10520| Log| Block| This is a new detection.
