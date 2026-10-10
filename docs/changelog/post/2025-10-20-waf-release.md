---
url: https://developers.cloudflare.com/changelog/post/2025-10-20-waf-release/
title: WAF Release - 2025-10-20 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:47.554367+00:00
---

# WAF Release - 2025-10-20 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-20-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 20, 2025

## WAF Release - 2025-10-20

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s update introduces an enhanced rule that expands detection coverage for a critical vulnerability in Oracle E-Business Suite. It also improves an existing rule to provide more reliable coverage in request processing.

**Key Findings**

New WAF rule deployed for Oracle E-Business Suite (CVE-2025-61882) to block unauthenticated attacker's network access via HTTP to compromise Oracle Concurrent Processing. If successfully exploited, this vulnerability may result in remote code execution.

**Impact**

  * Successful exploitation of CVE-2025-61882 allows unauthenticated attackers to execute arbitrary code remotely by chaining multiple weaknesses, enabling lateral movement into internal services, data exfiltration, and large-scale extortionware deployment within Oracle E-Business Suite environments.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...2b4101ab| 100598A| Remote Code Execution - Common Bash Bypass - Beta| Log| Block| This rule is merged into the original rule "Remote Code Execution - Common Bash Bypass" (ID: ...50cec478)  
Cloudflare Managed Ruleset| ...a1118614| 100916A| Oracle E-Business Suite - Remote Code Execution - CVE:CVE-2025-61882 - 2| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...c22b51d3| N/A| HTTP Truncated| N/A| Disabled| This is a New Detection
