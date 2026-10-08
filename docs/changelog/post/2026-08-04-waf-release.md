---
url: https://developers.cloudflare.com/changelog/post/2026-08-04-waf-release/
title: WAF Release - 2026-08-04 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:06.744611+00:00
---

# WAF Release - 2026-08-04 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-04-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 4, 2026

## WAF Release - 2026-08-04

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-04-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces new rules and updates Microsoft SharePoint RCE alongside enhanced SSRF cloud protection rule actions.

**Key Findings**

  * CVE-2026-50522: An insecure deserialization vulnerability in Microsoft SharePoint Server. This may allow an unauthenticated attacker to execute arbitrary code using crafted requests.
  * CVE-2026-66066: An improper input processing vulnerability in Ruby on Rails Active Storage image variant transformations. This may allow an unauthenticated attacker to perform arbitrary file reads and achieve Remote Code Execution (RCE) using maliciously crafted payload requests.
  * Generic Cloud Protections: Added improved detection logic targeting Server-Side Request Forgery (SSRF) in cloud-hosted applications.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...052b07cf| N/A| Microsoft SharePoint - Remote Code Execution - CVE:CVE-2026-50522| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...3a5b40d6| N/A| Rails - Arbitrary File Read & RCE - CVE:CVE-2026-66066| Block| Block| This was labeled as File Upload - RCE.  
Cloudflare Managed Ruleset| ...743a63ec| N/A| SSRF - Local - 2 - Beta| Disabled|  \- | This detection has been removed.  
Cloudflare Managed Ruleset| ...c2e84e2d| N/A| SSRF - Cloud - Beta| Disabled|  \- | This detection has been removed.  
Cloudflare Managed Ruleset| ...ab8af26f| N/A| SSRF - Cloud - 2 - Beta| Disabled|  \- | This detection has been removed.  
Cloudflare Managed Ruleset| ...25ba9d7c| N/A| SSRF - Cloud| Disabled| Block| We are changing the action for this rule from Disabled to BLOCK  
Cloudflare Managed Ruleset| ...01a076eb| N/A| SSRF - Local - Beta| Disabled|  \- | This detection has been removed.
