---
url: https://developers.cloudflare.com/changelog/post/2025-10-06-waf-release/
title: WAF Release - 2025-10-06 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:25.547082+00:00
---

# WAF Release - 2025-10-06 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-06-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 6, 2025

## WAF Release - 2025-10-06

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-06-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s highlights prioritise an emergency Oracle E-Business Suite RCE rule deployed to block active, high-impact exploitation. Also addressed are high-severity Chaos Mesh controller command-injection flaws that enable unauthenticated in-cluster RCE and potential cluster compromise, plus a form-data multipart boundary issue that permits HTTP Parameter Pollution (HPP). Two new generic SQLi detections were added to catch inline-comment obfuscation and information disclosure techniques.

**Key Findings**

  * New emergency rule released for Oracle E-Business Suite (CVE-2025-61882) addressing an actively exploited remote code execution vulnerability in core business application modules. Immediate mitigation deployed to protect enterprise workloads.

  * Chaos Mesh (CVE-2025-59358,CVE-2025-59359,CVE-2025-59360,CVE-2025-59361): A GraphQL debug endpoint on the Chaos Controller Manager is exposed without authentication; several controller mutations (`cleanTcs`, `killProcesses`, `cleanIptables`) are vulnerable to OS command injection.

  * Form-Data (CVE-2025-7783): Attackers who can observe `Math.random()` outputs and control request fields in form-data may exploit this flaw to perform HTTP parameter pollution, leading to request tampering or data manipulation.

  * Two new generic SQLi detections added to enhance baseline coverage against inline-comment obfuscation and information disclosure attempts.




**Impact**

  * CVE-2025-61882 — Oracle E-Business Suite remote code execution (emergency detection): attacker-controlled input can yield full system compromise, data exfiltration, and operational outage; immediate blocking enforced.

  * CVE-2025-59358 / CVE-2025-59359 / CVE-2025-59360 / CVE-2025-59361 — Unauthenticated command-injection in Chaos Mesh controllers allowing remote code execution, cluster compromise, and service disruption (high availability risk).

  * CVE-2025-7783 — Predictable multipart boundaries in form-data enabling HTTP Parameter Pollution; results include request tampering, parameter overwrite, and downstream data integrity loss.


Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...8650f52f| 100882| Chaos Mesh - Missing Authentication - CVE:CVE-2025-59358| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...2b8c3680| 100883| Chaos Mesh - Command Injection - CVE:CVE-2025-59359| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...ef859a04| 100884| Chaos Mesh - Command Injection - CVE:CVE-2025-59361| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...961f26a7| 100886| Form-Data - Parameter Pollution - CVE:CVE-2025-7783| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...26a4074c| 100888| Chaos Mesh - Command Injection - CVE:CVE-2025-59360| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...31101b2f| 100916| Oracle E-Business Suite - Remote Code Execution - CVE:CVE-2025-61882| N/A| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...29aa43c3| 100917| Generic Rules - SQLi - Inline Comment Injection| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...73c10b6f| 100918| Generic Rules - SQLi - Information Disclosure| N/A| Disabled| This is a New Detection
