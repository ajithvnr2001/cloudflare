---
url: https://developers.cloudflare.com/changelog/post/2025-09-24-emergency-waf-release/
title: WAF Release - 2025-09-24 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:48.569734+00:00
---

# WAF Release - 2025-09-24 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-24-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 24, 2025

## WAF Release - 2025-09-24 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week highlights a critical vendor-specific vulnerability: a deserialization flaw in the License Servlet of Fortra’s GoAnywhere MFT. By forging a license response signature, an attacker can trigger deserialization of arbitrary objects, potentially leading to command injection.

**Key Findings**

  * GoAnywhere MFT (CVE-2025-10035): Deserialization vulnerability in the License Servlet that allows attackers with a forged license response signature to deserialize arbitrary objects, potentially resulting in command injection.



**Impact**

GoAnywhere MFT (CVE-2025-10035): Exploitation enables attackers to escalate privileges or achieve remote code execution via command injection.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...e08b39f3| 100787| Fortra GoAnywhere - Auth Bypass - CVE:CVE-2025-10035| N/A| Block| This is a New Detection
