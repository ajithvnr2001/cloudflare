---
url: https://developers.cloudflare.com/changelog/post/2025-06-16-waf-release/
title: WAF Release - 2025-06-16 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:51.641900+00:00
---

# WAF Release - 2025-06-16 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-16-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 16, 2025

## WAF Release - 2025-06-16

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s roundup highlights multiple critical vulnerabilities across popular web frameworks, plugins, and enterprise platforms. The focus lies on remote code execution (RCE), server-side request forgery (SSRF), and insecure file upload vectors that enable full system compromise or data exfiltration.

**Key Findings**

  * Cisco IOS XE (CVE-2025-20188): Critical RCE vulnerability enabling unauthenticated attackers to execute arbitrary commands on network infrastructure devices, risking total router compromise.
  * Axios (CVE-2024-39338): SSRF flaw impacting server-side request control, allowing attackers to manipulate internal service requests when misconfigured with unsanitized user input.
  * vBulletin (CVE-2025-48827, CVE-2025-48828): Two high-impact RCE flaws enabling attackers to remotely execute PHP code, compromising forum installations and underlying web servers.
  * Invision Community (CVE-2025-47916): A critical RCE vulnerability allowing authenticated attackers to run arbitrary code in community platforms, threatening data and lateral movement risk.
  * CrushFTP (CVE-2025-32102, CVE-2025-32103): SSRF vulnerabilities in upload endpoint processing permit attackers to pivot internal network scans and abuse internal services.
  * Roundcube (CVE-2025-49113): RCE via email processing enables attackers to execute code upon viewing a crafted email — particularly dangerous for webmail deployments.
  * WooCommerce WordPress Plugin (CVE-2025-47577): Dangerous file upload vulnerability permits unauthenticated users to upload executable payloads, leading to full WordPress site takeover.
  * Cross-Site Scripting (XSS) Detection Improvements: Enhanced detection patterns.



**Impact**

These vulnerabilities span core systems — from routers to e-commerce to email. RCE in Cisco IOS XE, Roundcube, and vBulletin poses full system compromise. SSRF in Axios and CrushFTP supports internal pivoting, while WooCommerce’s file upload bug opens doors to mass WordPress exploitation.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...35fefd53| 100783| Cisco IOS XE - Remote Code Execution - CVE:CVE-2025-20188| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...8332af5d| 100784| Axios - SSRF - CVE:CVE-2024-39338| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...2e1648d2| 100785| vBulletin - Remote Code Execution - CVE:CVE-2025-48827, CVE:CVE-2025-48828| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...0edcf1ef| 100786| Invision Community - Remote Code Execution - CVE:CVE-2025-47916| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...d6f5eb48| 100791| CrushFTP - SSRF - CVE:CVE-2025-32102, CVE:CVE-2025-32103| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...30baa18a| 100792| Roundcube - Remote Code Execution - CVE:CVE-2025-49113| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...229ba236| 100793| XSS - Ontoggle| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...fa338296| 100794| WordPress WooCommerce Plugin - Dangerous File Upload - CVE:CVE-2025-47577| Log| Block| This is a New Detection
