---
url: https://developers.cloudflare.com/changelog/post/2025-07-14-waf-release/
title: WAF Release - 2025-07-14 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:16.837892+00:00
---

# WAF Release - 2025-07-14 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-14-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 14, 2025

## WAF Release - 2025-07-14

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-14-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s vulnerability analysis highlights emerging web application threats that exploit modern JavaScript behavior and SQL parsing ambiguities. Attackers continue to refine techniques such as attribute overloading and obfuscated logic manipulation to evade detection and compromise front-end and back-end systems.

**Key Findings**

  * XSS – Attribute Overloading: A novel cross-site scripting technique where attackers abuse custom or non-standard HTML attributes to smuggle payloads into the DOM. These payloads evade traditional sanitization logic, especially in frameworks that loosely validate attributes or trust unknown tokens.
  * XSS – onToggle Event Abuse: Exploits the lesser-used onToggle event (triggered by elements like `<details>`) to execute arbitrary JavaScript when users interact with UI elements. This vector is often overlooked by static analyzers and can be embedded in seemingly benign components.



**Impact**

These vulnerabilities target both user-facing components and back-end databases, introducing potential vectors for credential theft, session hijacking, or full data exfiltration. The XSS variants bypass conventional filters through overlooked HTML behaviors, while the obfuscated SQLi enables attackers to stealthily probe back-end logic, making them especially difficult to detect and block.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...2aa3d845| 100798| XSS - Attribute Overloading| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...37548d06| 100799| XSS - OnToggle| Log| Block| This is a New Detection
