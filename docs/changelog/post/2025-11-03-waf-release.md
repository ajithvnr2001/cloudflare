---
url: https://developers.cloudflare.com/changelog/post/2025-11-03-waf-release/
title: WAF Release - 2025-11-03 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:47.199292+00:00
---

# WAF Release - 2025-11-03 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-03-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 3, 2025

## WAF Release - 2025-11-03

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week highlights enhancements to detection signatures improving coverage for vulnerabilities in Adobe Commerce and Magento Open Source, linked to CVE-2025-54236.

**Key Findings**

This vulnerability allows unauthenticated attackers to take over customer accounts through the Commerce REST API and, in certain configurations, may lead to remote code execution. The latest update provides enhanced detection logic for resilient protection against exploitation attempts.

**Impact**

  * Adobe Commerce (CVE-2025-54236): Exploitation may allow attackers to hijack sessions, execute arbitrary commands, steal data, and disrupt storefronts, resulting in confidentiality and integrity risks for merchants. Administrators are strongly encouraged to apply vendor patches without delay.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...cb6d5fe5| 100774C| Adobe Commerce - Remote Code Execution - CVE:CVE-2025-54236| Log| Block| This is an improved detection.
