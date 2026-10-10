---
url: https://developers.cloudflare.com/changelog/post/2025-12-03-emergency-waf-release/
title: WAF Release - 2025-12-03 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:46.189141+00:00
---

# WAF Release - 2025-12-03 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-03-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 3, 2025

## WAF Release - 2025-12-03 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The WAF rule deployed yesterday to block unsafe deserialization-based RCE has been updated. The rule description now reads “React – RCE – CVE-2025-55182”, explicitly mapping to the recently disclosed React Server Components vulnerability. Detection logic remains unchanged.

**Key Findings**

Rule description updated to reference React – RCE – CVE-2025-55182 while retaining existing unsafe-deserialization detection.

**Impact**

Improved classification and traceability with no change to coverage against remote code execution attempts.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...5fb92fba| N/A| React - RCE - CVE:CVE-2025-55182| N/A| Block| Rule metadata description changed. Detection unchanged.  
Cloudflare Free Ruleset| ...99702280| N/A| React - RCE - CVE:CVE-2025-55182| N/A| Block| Rule metadata description changed. Detection unchanged.
