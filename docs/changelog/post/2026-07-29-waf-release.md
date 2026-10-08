---
url: https://developers.cloudflare.com/changelog/post/2026-07-29-waf-release/
title: WAF Release - 2026-07-29 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:05.300872+00:00
---

# WAF Release - 2026-07-29 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-29-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 29, 2026

## WAF Release - 2026-07-29

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-29-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces new rules and updates existing threat signatures to provide targeted protections for vulnerabilities in Nuxt Server Island components and Alibaba Fastjson deserialization routines, alongside enhanced protections for cloud metadata Server-Side Request Forgery (SSRF) and obfuscated command injection attempts.

**Key Findings**

  * Nuxt Server Island - RCE(GHSA-9473-5f9j-94wq): An unauthenticated vulnerability in Nuxt Server Islands where remote attackers can supply arbitrary component names or props to endpoints. Manipulating these parameters allows unauthenticated component Remote Code Execution (RCE) on the server.

  * Alibaba Fastjson JSONType Remote Code Execution: A unauthenticated remote code execution vulnerability in Alibaba Fastjson (≤ 1.2.83) during JSON deserialization. Under default configurations, attackers can execute arbitrary system commands, bypassing traditional classpath and gadget-based defenses.

  * Generic Protections (SSRF & Command Injection): Added improved detection logic targeting Server-Side Request Forgery (SSRF) in cloud-hosted applications, alongside new rules targeting obfuscated command injection patterns across request parameters.


Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...c2e84e2d| N/A| SSRF - Cloud - Beta| Log| Block| This is an improved detection.  
Cloudflare Managed Ruleset| ...761e7a4c| N/A| Command Injection - Obfuscation| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...7347c892| N/A| Alibaba Fastjson JSONType Remote Code Execution - Body| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...8ec012ea| N/A| Nuxt Server Island - RCE| N/A| Block| This is a new detection.This was labeled as Generic Rules - RCE.  
Cloudflare Managed Ruleset| ...3590a4ad| N/A| Generic Rules - RCE| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...9c6dff1c| N/A| Generic Rules - XSS| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...3a5b40d6| N/A| File Upload - RCE| N/A| Block| This is a new detection.  
Cloudflare Free Ruleset| ...cfe1a93c| N/A| Generic Rules - RCE| N/A| Block| This is a new detection.  
Cloudflare Free Ruleset| ...9ab5ed95| N/A| Generic Rules - XSS| N/A| Block| This is a new detection.  
Cloudflare Free Ruleset| ...1b7f9c67| N/A| File Upload - RCE| N/A| Block| This is a new detection.
