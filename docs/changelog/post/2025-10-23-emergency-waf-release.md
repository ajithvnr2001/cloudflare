---
url: https://developers.cloudflare.com/changelog/post/2025-10-23-emergency-waf-release/
title: WAF Release - 2025-10-23 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:47.794811+00:00
---

# WAF Release - 2025-10-23 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-23-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 23, 2025

## WAF Release - 2025-10-23 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week highlights enhancements to detection signatures improving coverage for vulnerabilities in Adobe Commerce and Magento Open Source, linked to CVE-2025-54236.

**Key Findings**

This vulnerability allows unauthenticated attackers to take over customer accounts through the Commerce REST API and, in certain configurations, may lead to remote code execution. The latest update enhances detection logic to provide more resilient protection against exploitation attempts.

**Impact**

Adobe Commerce (CVE-2025-54236): Exploitation may allow attackers to hijack sessions, execute arbitrary commands, steal data, and disrupt storefronts, resulting in confidentiality and integrity risks for merchants. Administrators are strongly encouraged to apply vendor patches without delay.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...c6ef59a1| N/A| Adobe Commerce - Remote Code Execution - CVE:CVE-2025-54236| N/A| Block| This is a New Detection
