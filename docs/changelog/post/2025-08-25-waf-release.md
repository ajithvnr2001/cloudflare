---
url: https://developers.cloudflare.com/changelog/post/2025-08-25-waf-release/
title: WAF Release - 2025-08-25 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:49.611758+00:00
---

# WAF Release - 2025-08-25 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-25-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 25, 2025

## WAF Release - 2025-08-25

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**This week's update**

This week, critical vulnerabilities were disclosed that impact widely used open-source infrastructure, creating high-risk scenarios for code execution and operational disruption.

**Key Findings**

  * Apache HTTP Server – Code Execution (CVE-2024-38474): A flaw in Apache HTTP Server allows attackers to achieve remote code execution, enabling full compromise of affected servers. This vulnerability threatens the confidentiality, integrity, and availability of critical web services.

  * Laravel (CVE-2024-55661): A security flaw in Laravel introduces the potential for remote code execution under specific conditions. Exploitation could provide attackers with unauthorized access to application logic and sensitive backend data.




**Impact**

These vulnerabilities pose severe risks to enterprise environments and open-source ecosystems. Remote code execution enables attackers to gain deep system access, steal data, disrupt services, and establish persistent footholds for broader intrusions. Given the widespread deployment of Apache HTTP Server and Laravel in production systems, timely patching and mitigation are critical.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...28050359| 100822_BETA| WordPress:Plugin:WPBookit - Remote Code Execution - CVE:CVE-2025-6058| N/A| Disabled| This was merged in to the original rule "WordPress:Plugin:WPBookit - Remote Code Execution - CVE:CVE-2025-6058" (ID: ...194f7b2d)  
Cloudflare Managed Ruleset| ...3bdcdbad| 100831| Apache HTTP Server - Code Execution - CVE:CVE-2024-38474| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...02eaac5b| 100846| Laravel - Remote Code Execution - CVE:CVE-2024-55661| Log| Disabled| This is a New Detection
