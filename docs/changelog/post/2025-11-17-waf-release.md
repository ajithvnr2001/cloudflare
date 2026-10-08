---
url: https://developers.cloudflare.com/changelog/post/2025-11-17-waf-release/
title: WAF Release - 2025-11-17 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:29.548371+00:00
---

# WAF Release - 2025-11-17 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-17-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 17, 2025

## WAF Release - 2025-11-17

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-17-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week highlights enhancements to detection signatures improving coverage for vulnerabilities in DELMIA Apriso, linked to CVE-2025-6205.

**Key Findings**

This vulnerability allows unauthenticated attackers to gain privileged access to the application. The latest update provides enhanced detection logic for resilient protection against exploitation attempts.

**Impact**

  * DELMIA Apriso (CVE-2025-6205): Exploitation could allow an unauthenticated remote attacker to bypass security checks by sending specially crafted requests to the application's message processor. This enables the creation of arbitrary employee accounts, which can be leveraged to modify system configurations and achieve full system compromise.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...d256f4bc| N/A| DELMIA Apriso - Auth Bypass - CVE:CVE-2025-6205| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...1a3e521e| N/A| PHP Wrapper Injection - Body| N/A| Disabled| Rule metadata description refined. Detection unchanged.  
Cloudflare Managed Ruleset| ...8f76bd74| N/A| PHP Wrapper Injection - URI| N/A| Disabled| Rule metadata description refined. Detection unchanged.
