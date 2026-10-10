---
url: https://developers.cloudflare.com/changelog/post/2025-07-21-waf-release/
title: WAF Release - 2025-07-21 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:50.714017+00:00
---

# WAF Release - 2025-07-21 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-21-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 21, 2025

## WAF Release - 2025-07-21

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's update spotlights several critical vulnerabilities across Citrix NetScaler Memory Disclosure, FTP servers and network application. Several flaws enable unauthenticated remote code execution or sensitive data exposure, posing a significant risk to enterprise security.

**Key Findings**

  * Wing FTP Server (CVE-2025-47812): A critical Remote Code Execution (RCE) vulnerability that enables unauthenticated attackers to execute arbitrary code with root/SYSTEM-level privileges by exploiting a Lua injection flaw.
  * Infoblox NetMRI (CVE-2025-32813): A remote unauthenticated command injection flaw that allows an attacker to execute arbitrary commands, potentially leading to unauthorized access.
  * Citrix Netscaler ADC (CVE-2025-5777, CVE-2023-4966): A sensitive information disclosure vulnerability, also known as "Citrix Bleed2", that allows the disclosure of memory and subsequent remote access session hijacking.
  * Akamai CloudTest (CVE-2025-49493): An XML External Entity (XXE) injection that could lead to read local files on the system by manipulating XML input.



**Impact**

These vulnerabilities affect critical enterprise infrastructure, from file transfer services and network management appliances to application delivery controllers. The Wing FTP RCE and Infoblox command injection flaws offer direct paths to deep system compromise, while the Citrix "Bleed2" and Akamai XXE vulnerabilities undermine system integrity by enabling session hijacking and sensitive data theft.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...3461ec9e| 100804| BerriAI - SSRF - CVE:CVE-2024-6587| Log| Log| This is a New Detection  
Cloudflare Managed Ruleset| ...5199b58a| 100805| Wing FTP Server - Remote Code Execution - CVE:CVE-2025-47812| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...919a91a4| 100807| Infoblox NetMRI - Command Injection - CVE:CVE-2025-32813| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...7899130f| 100808| Citrix Netscaler ADC - Buffer Error - CVE:CVE-2025-5777| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...d1cf8e08| 100809| Citrix Netscaler ADC - Information Disclosure - CVE:CVE-2023-4966| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...6e70469f| 100810| Akamai CloudTest - XXE - CVE:CVE-2025-49493| Log| Block| This is a New Detection
