---
url: https://developers.cloudflare.com/changelog/post/2025-09-29-waf-release/
title: WAF Release - 2025-09-29 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:48.194466+00:00
---

# WAF Release - 2025-09-29 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-29-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 29, 2025

## WAF Release - 2025-09-29

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week highlights four important vendor- and component-specific issues: an authentication bypass in SimpleHelp (CVE-2024-57727), an information-disclosure flaw in Flowise Cloud (CVE-2025-58434), an SSRF in the WordPress plugin Ditty (CVE-2025-8085), and a directory-traversal bug in Vite (CVE-2025-30208). These are paired with improvements to our generic detection coverage (SQLi, SSRF) to raise the baseline and reduce noisy gaps.

**Key Findings**

  * SimpleHelp (CVE-2024-57727): Authentication bypass in SimpleHelp that can allow unauthorized access to management interfaces or sessions.

  * Flowise Cloud (CVE-2025-58434): Information-disclosure vulnerability in Flowise Cloud that may expose sensitive configuration or user data to unauthenticated or low-privileged actors.

  * WordPress:Plugin: Ditty (CVE-2025-8085): SSRF in the Ditty WordPress plugin enabling server-side requests that could reach internal services or cloud metadata endpoints.

  * Vite (CVE-2025-30208): Directory-traversal vulnerability in Vite allowing access to filesystem paths outside the intended web root.




**Impact**

These vulnerabilities allow attackers to gain access, escalate privileges, or execute actions that were previously unavailable:

  * SimpleHelp (CVE-2024-57727): An authentication bypass that can let unauthenticated attackers access management interfaces or hijack sessions — enabling lateral movement, credential theft, or privilege escalation within affected environments.

  * Flowise Cloud (CVE-2025-58434): Information-disclosure flaw that can expose sensitive configuration, tokens, or user data; leaked secrets may be chained into account takeover or privileged access to backend services.

  * WordPress:Plugin: Ditty (CVE-2025-8085): SSRF that enables server-side requests to internal services or cloud metadata endpoints, potentially allowing attackers to retrieve credentials or reach otherwise inaccessible infrastructure, leading to privilege escalation or cloud resource compromise.

  * Vite (CVE-2025-30208): Directory-traversal vulnerability that can expose filesystem contents outside the web root (configuration files, keys, source code), which attackers can use to escalate privileges or further compromise systems.


Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...8c2e30fb| 100717| SimpleHelp - Auth Bypass - CVE:CVE-2024-57727| Log| Block| This rule is merged to 100717 in legacy WAF and ...958094d3 in new WAF  
Cloudflare Managed Ruleset| ...d58b886b| 100775| Flowise Cloud - Information Disclosure - CVE:CVE-2025-58434| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...9bce1ff4| 100881| WordPress:Plugin:Ditty - SSRF - CVE:CVE-2025-8085| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...ddc329dd| 100887| Vite - Directory Traversal - CVE:CVE-2025-30208| Log| Block| This is a New Detection
