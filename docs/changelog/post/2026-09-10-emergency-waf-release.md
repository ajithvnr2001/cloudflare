---
url: https://developers.cloudflare.com/changelog/post/2026-09-10-emergency-waf-release/
title: WAF Release - 2026-09-10 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.380464+00:00
---

# WAF Release - 2026-09-10 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-10-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 10, 2026

## WAF Release - 2026-09-10 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This update provides immediate defense against a high-severity, actively exploited zero-day vulnerability targeting Adobe Commerce and Magento Open Source storefronts.

**Key Findings**

  * Adobe Commerce and Magento RCE (CVE-2026-75650 / "StyleSmuggler"): Unauthenticated Remote Code Execution (RCE) vulnerability caused by improper neutralization of special elements in the platform's template engine. Unauthenticated attackers can inject arbitrary PHP payloads through style properties to execute system commands and deploy persistent malware.



**Impact**

This emergency rule provides immediate edge-level mitigation and virtual patching, origin applications must be urgently updated. We strongly recommend to apply the hotfix outlined in Adobe Security Bulletin [APSB26-146](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/announcements/commerce-apsb26-146) and immediately rotate all potentially exposed encryption keys, integration tokens, and system credentials, as patching alone does not remediate an existing compromise.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...440f5c55| N/A| Adobe Commerce - Remote Code Execution - CVE:CVE-2026-75650| N/A| Block| This is a new detection.
