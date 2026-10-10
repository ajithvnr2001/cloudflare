---
url: https://developers.cloudflare.com/changelog/post/2026-05-20-waf-release/
title: WAF Release - 2026-05-20 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:37.939838+00:00
---

# WAF Release - 2026-05-20 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-20-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 20, 2026

## WAF Release - 2026-05-20

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**Key Findings**

  * Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.



**Continuous Rule Improvements**

We are continuously refining our managed rules to provide more resilient protection and deeper insights into attack patterns. To ensure an optimal security posture, we recommend consistently monitoring the Security Events dashboard and adjusting rule actions as these enhancements are deployed.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...9e9c068d| N/A| Sitecore - Cache Poisoning - CVE:CVE-2025-53693 Beta| N/A| Block| This rule is merged into the original rule "Sitecore - Cache Poisoning - CVE:CVE-2025-53693" (ID: ...7c5b669c).
