---
url: https://developers.cloudflare.com/changelog/post/2025-05-19-waf-release/
title: WAF Release - 2025-05-19 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:12.652938+00:00
---

# WAF Release - 2025-05-19 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-19-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 19, 2025

## WAF Release - 2025-05-19

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-19-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's analysis covers four vulnerabilities, with three rated critical due to their Remote Code Execution (RCE) potential. One targets a high-traffic frontend platform, while another targets a popular content management system. These detections are now part of the Cloudflare Managed Ruleset in _Block_ mode.

**Key Findings**

  * Commvault Command Center (CVE-2025-34028) exposes an unauthenticated RCE via insecure command injection paths in the web UI. This is critical due to its use in enterprise backup environments.
  * BentoML (CVE-2025-27520) reveals an exploitable vector where serialized payloads in model deployment APIs can lead to arbitrary command execution. This targets modern AI/ML infrastructure.
  * Craft CMS (CVE-2024-56145) allows RCE through template injection in unauthenticated endpoints. It poses a significant risk for content-heavy websites with plugin extensions.
  * Apache HTTP Server (CVE-2024-38475) discloses sensitive server config data due to misconfigured `mod_proxy` behavior. While not RCE, this is useful for pre-attack recon.



**Impact**

These newly detected vulnerabilities introduce critical risk across modern web stacks, AI infrastructure, and content platforms: unauthenticated RCEs in Commvault, BentoML, and Craft CMS enable full system compromise with minimal attacker effort.

Apache HTTPD information leak can support targeted reconnaissance, increasing the success rate of follow-up exploits. Organizations using these platforms should prioritize patching and monitor for indicators of exploitation using updated WAF detection rules.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...75129820| 100745| Apache HTTP Server - Information Disclosure - CVE:CVE-2024-38475| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...26a517f1| 100747| Commvault Command Center - Remote Code Execution - CVE:CVE-2025-34028| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...d7619ccb| 100749| BentoML - Remote Code Execution - CVE:CVE-2025-27520| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...f15bfda4| 100753| Craft CMS - Remote Code Execution - CVE:CVE-2024-56145| Log| Block| This is a New Detection
