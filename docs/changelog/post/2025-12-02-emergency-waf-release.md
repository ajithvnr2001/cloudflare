---
url: https://developers.cloudflare.com/changelog/post/2025-12-02-emergency-waf-release/
title: WAF Release - 2025-12-02 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:30.493164+00:00
---

# WAF Release - 2025-12-02 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-02-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 2, 2025

## WAF Release - 2025-12-02 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-02-emergency-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's emergency release introduces a new rule to block a critical RCE vulnerability in widely-used web frameworks through unsafe deserialization patterns.

**Key Findings**

New WAF rule deployed for RCE Generic Framework to block malicious POST requests containing unsafe deserialization patterns. If successfully exploited, this vulnerability allows attackers with network access via HTTP to execute arbitrary code remotely.

**Impact**

  * Successful exploitation allows unauthenticated attackers to execute arbitrary code remotely through crafted serialization payloads, enabling complete system compromise, data exfiltration, and potential lateral movement within affected environments.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...5fb92fba| N/A| RCE Generic - Framework| N/A| Block| This is a new detection.  
Cloudflare Free Ruleset| ...99702280| N/A| RCE Generic - Framework| N/A| Block| This is a new detection.
