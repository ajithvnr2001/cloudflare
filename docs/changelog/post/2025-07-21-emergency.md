---
url: https://developers.cloudflare.com/changelog/post/2025-07-21-emergency/
title: WAF Release - 2025-07-21 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:50.881240+00:00
---

# WAF Release - 2025-07-21 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-21-emergency/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 21, 2025

## WAF Release - 2025-07-21 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's update highlights several high-impact vulnerabilities affecting Microsoft SharePoint Server. These flaws, involving unsafe deserialization, allow unauthenticated remote code execution over the network, posing a critical threat to enterprise environments relying on SharePoint for collaboration and document management.

**Key Findings**

  * Microsoft SharePoint Server (CVE-2025-53770): A critical vulnerability involving unsafe deserialization of untrusted data, enabling unauthenticated remote code execution over the network. This flaw allows attackers to execute arbitrary code on vulnerable SharePoint servers without user interaction.
  * Microsoft SharePoint Server (CVE-2025-53771): A closely related deserialization issue that can be exploited by unauthenticated attackers, potentially leading to full system compromise. The vulnerability highlights continued risks around insecure serialization logic in enterprise collaboration platforms.



**Impact**

Together, these vulnerabilities significantly weaken the security posture of on-premise Microsoft SharePoint Server deployments. By enabling remote code execution without authentication, they open the door for attackers to gain persistent access, deploy malware, and move laterally across enterprise environments.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...2168f6f0| 100817| Microsoft SharePoint - Deserialization - CVE:CVE-2025-53770| N/A| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...8de656c4| 100818| Microsoft SharePoint - Deserialization - CVE:CVE-2025-53771| N/A| Block| This is a New Detection  
  
For more details, also refer to [our blog ↗︎](https://blog.cloudflare.com/cloudflare-protects-against-critical-sharepoint-vulnerability-cve-2025-53770/).
