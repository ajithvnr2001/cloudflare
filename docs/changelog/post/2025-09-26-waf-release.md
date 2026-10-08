---
url: https://developers.cloudflare.com/changelog/post/2025-09-26-waf-release/
title: WAF Release - 2025-09-26 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:24.445273+00:00
---

# WAF Release - 2025-09-26 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-26-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 26, 2025

## WAF Release - 2025-09-26

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-26-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**Managed Ruleset Updated**

This update introduces 11 new detections in the Cloudflare Managed Ruleset (all currently set to Disabled mode to preserve remediation logic and allow quick activation if needed). The rules cover a broad spectrum of threats - SQL injection techniques, command and code injection, information disclosure of common files, URL anomalies, and cross-site scripting.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...a67d8561| 100859A| SQLi - UNION - 3| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...4de80468| 100889| Command Injection - Generic 9| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...f2be3ddf| 100890| Information Disclosure - Common Files - 2| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...80a252a8| 100891| Anomaly:URL - Relative Paths| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...7e7d3865| 100894| XSS - Inline Function| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...3792565c| 100895| XSS - DOM| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...42978e38| 100896| SQLi - MSSQL Length Enumeration| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...3ab43f7e| 100897| Generic Rules - Code Injection - 3| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...c1686741| 100898| SQLi - Evasion| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...20999be0| 100899| SQLi - Probing 2| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...b4026c88| 100900| SQLi - Probing| N/A| Disabled| This is a New Detection
