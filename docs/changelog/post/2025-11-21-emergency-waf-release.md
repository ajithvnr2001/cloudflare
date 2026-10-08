---
url: https://developers.cloudflare.com/changelog/post/2025-11-21-emergency-waf-release/
title: WAF Release - 2025-11-21 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:29.922287+00:00
---

# WAF Release - 2025-11-21 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-21-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 21, 2025

## WAF Release - 2025-11-21

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-21-emergency-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release introduces a critical detection for CVE-2025-61757, a vulnerability in the Oracle Identity Manager REST WebServices component.

**Key Findings**

This flaw allows unauthenticated attackers with network access over HTTP to fully compromise the Identity Manager, potentially leading to a complete takeover.

**Impact**

Oracle Identity Manager (CVE-2025-61757): Exploitation could allow an unauthenticated remote attacker to bypass security checks by sending specially crafted requests to the application's message processor. This enables the creation of arbitrary employee accounts, which can be leveraged to modify system configurations and achieve full system compromise.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...39fdbe7e| N/A| Oracle Identity Manager - Pre-Auth RCE - CVE:CVE-2025-61757| N/A| Block| This is a new detection.
