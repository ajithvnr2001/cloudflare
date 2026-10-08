---
url: https://developers.cloudflare.com/changelog/post/2025-09-22-waf-release/
title: WAF Release - 2025-09-22 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:23.504244+00:00
---

# WAF Release - 2025-09-22 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-22-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 22, 2025

## WAF Release - 2025-09-22

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-22-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week emphasizes two critical vendor-specific vulnerabilities: a full elevation-of-privilege in Microsoft Azure Networking (CVE-2025-54914) and a server-side template injection (SSTI) leading to remote code execution (RCE) in Skyvern (CVE-2025-49619). These are complemented by enhancements in generic detections (SQLi, SSRF) to improve baseline coverage.

**Key Findings**

  * Azure (CVE-2025-54914): Vulnerability in Azure Networking allowing elevation of privileges.

  * Skyvern (CVE-2025-49619): Skyvern ≤ 0.1.85 has a server-side template injection (SSTI) vulnerability in its Prompt field (workflow blocks) via Jinja2. Authenticated users with low privileges can get remote code execution (blind).

  * Generic SQLi / SSRF improvements: Expanded rule coverage to detect obfuscated SQL injection patterns and SSRF across host, local, and cloud contexts.




**Impact**

These vulnerabilities allow attackers to escalate privileges or execute code under conditions where previously they could not:

  * Azure CVE-2025-54914 enables an attacker from the network with no credentials to gain high-level access within Azure Networking; could lead to full compromise of networking components.

  * Skyvern CVE-2025-49619 allows authenticated users with minimal privilege to exploit SSTI for remote code execution, undermining isolation of workflow components.

  * The improvements for SQLi and SSRF reduce risk from common injection and request-based attacks.


Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...6a135cbf| 100146| SSRF - Host - 2| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...57035abf| 100146B| SSRF - Local - 2| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...bbe18d50| 100146C| SSRF - Cloud - 2| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...956c1961| 100714| Azure - Auth Bypass - CVE:CVE-2025-54914| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...c5ced231| 100758| Skyvern - Remote Code Execution - CVE:CVE-2025-49619| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...84a619a1| 100773| Next.js - SSRF| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...983ff2dd| 100774| Adobe Commerce - Remote Code Execution - CVE:CVE-2025-54236| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...0380a1a6| 100800_BETA| SQLi - Obfuscated Boolean - Beta| Log| Block| This rule has been merged into the original rule (ID: ...5563445f)
