---
url: https://developers.cloudflare.com/changelog/post/2025-06-02-waf-release/
title: WAF Release - 2025-06-02 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:13.234715+00:00
---

# WAF Release - 2025-06-02 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-02-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 2, 2025

## WAF Release - 2025-06-02

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-02-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s roundup highlights five high-risk vulnerabilities affecting SD-WAN, load balancers, and AI platforms. Several flaws enable unauthenticated remote code execution or authentication bypass.

**Key Findings**

  * Versa Concerto SD-WAN (CVE-2025-34026, CVE-2025-34027): Authentication bypass vulnerabilities allow attackers to gain unauthorized access to SD-WAN management interfaces, compromising network segmentation and control.
  * Kemp LoadMaster (CVE-2024-7591): Remote Code Execution vulnerability enables attackers to execute arbitrary commands, potentially leading to full device compromise within enterprise load balancing environments.
  * AnythingLLM (CVE-2024-0759): Server-Side Request Forgery (SSRF) flaw allows external attackers to force the LLM backend to make unauthorized internal network requests, potentially exposing sensitive internal resources.
  * Anyscale Ray (CVE-2023-48022): Remote Code Execution vulnerability affecting distributed AI workloads, allowing attackers to execute arbitrary code on Ray cluster nodes.
  * Server-Side Request Forgery (SSRF) - Generic & Obfuscated Payloads: Ongoing advancements in SSRF payload techniques observed, including obfuscation and expanded targeting of cloud metadata services and internal IP ranges.



**Impact**

These vulnerabilities expose critical infrastructure across networking, AI platforms, and SaaS integrations. Unauthenticated RCE and auth bypass flaws in Versa Concerto, Kemp LoadMaster, and Anyscale Ray allow full system compromise. AnythingLLM and SSRF payload variants expand attack surfaces into internal cloud resources, sensitive APIs, and metadata services, increasing risk of privilege escalation, data theft, and persistent access.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...39b52f02| 100764| Versa Concerto SD-WAN - Auth Bypass - CVE:CVE-2025-34027| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...a34edb97| 100765| Versa Concerto SD-WAN - Auth Bypass - CVE:CVE-2025-34026| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...0d99b2db| 100766| Kemp LoadMaster - Remote Code Execution - CVE:CVE-2024-7591| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...95aa3a4f| 100767| AnythingLLM - SSRF - CVE:CVE-2024-0759| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...840a0966| 100768| Anyscale Ray - Remote Code Execution - CVE:CVE-2023-48022| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...9d16ee18| 100781| SSRF - Generic Payloads| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...5c963d9d| 100782| SSRF - Obfuscated Payloads| N/A| Disabled| This is a New Detection
