---
url: https://developers.cloudflare.com/changelog/post/2025-07-07-waf-release/
title: WAF Release - 2025-07-07 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:51.027240+00:00
---

# WAF Release - 2025-07-07 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-07-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 7, 2025

## WAF Release - 2025-07-07

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s roundup uncovers critical vulnerabilities affecting enterprise VoIP systems, webmail platforms, and a popular JavaScript framework. The risks range from authentication bypass to remote code execution (RCE) and buffer handling flaws, each offering attackers a path to elevate access or fully compromise systems.

**Key Findings**

  * Next.js - Auth Bypass: A newly detected authentication bypass flaw in the Next.js framework allows attackers to access protected routes or APIs without proper authorization, undermining application access controls.
  * Fortinet FortiVoice (CVE-2025-32756): A buffer error vulnerability in FortiVoice systems that could lead to memory corruption and potential code execution or service disruption in enterprise telephony environments.
  * Roundcube (CVE-2025-49113): A critical RCE flaw allowing unauthenticated attackers to execute arbitrary PHP code via crafted requests, leading to full compromise of mail servers and user inboxes.



**Impact**

These vulnerabilities affect core business infrastructure, from web interfaces to voice communications and email platforms. The Roundcube RCE and FortiVoice buffer flaw offer potential for deep system access, while the Next.js auth bypass undermines trust boundaries in modern web apps.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...7eb35ee6| 100795| Next.js - Auth Bypass| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...c329aeb0| 100796| Fortinet FortiVoice - Buffer Error - CVE:CVE-2025-32756| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...ab314023| 100797| Roundcube - Remote Code Execution - CVE:CVE-2025-49113| Log| Disabled| This is a New Detection
