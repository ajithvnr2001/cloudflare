---
url: https://developers.cloudflare.com/changelog/post/2025-10-03-waf-release/
title: WAF Release - 2025-10-03 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:48.071839+00:00
---

# WAF Release - 2025-10-03 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-03-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 3, 2025

## WAF Release - 2025-10-03

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**Managed Ruleset Updated**

This update introduces 21 new detections in the Cloudflare Managed Ruleset (all currently set to Disabled mode to preserve remediation logic and allow quick activation if needed). The rules cover a broad spectrum of threats - SQL injection techniques, command and code injection, information disclosure of common files, URL anomalies, and cross-site scripting.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...d61fac74| 100902| Generic Rules - Command Execution - 2| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...514aeeb8| 100908| Generic Rules - Command Execution - 3| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...8d46a6f4| 100910| Generic Rules - Command Execution - 4| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...1bd0a329| 100915| Generic Rules - Command Execution - 5| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...5e51450a| 100899| Generic Rules - Content-Type Abuse| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...7996012f| 100914| Generic Rules - Content-Type Injection| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...93209312| 100911| Generic Rules - Cookie Header Injection| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...0f373b3f| 100905| Generic Rules - NoSQL Injection| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...78a0ed04| 100913| Generic Rules - NoSQL Injection - 2| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...5d649624| 100907| Generic Rules - Parameter Pollution| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...fd1c674e| 100906| Generic Rules - PHP Object Injection| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...34c88168| 100904| Generic Rules - Prototype Pollution| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...3ab43f7e| 100897| Generic Rules - Prototype Pollution 2| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...0d94ee22| 100903| Generic Rules - Reverse Shell| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...d5add8e3| 100909| Generic Rules - Reverse Shell - 2| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...565c78b0| 100898| Generic Rules - SSJI NoSQL| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...12b837a0| 100896| Generic Rules - SSRF| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...11c4fb00| 100895| Generic Rules - Template Injection| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...d3ed0123| 100895A| Generic Rules - Template Injection - 2| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...7501a1d9| 100912| Generic Rules - XXE| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...dc55cdb6| 100900| Relative Paths - Anomaly Headers| N/A| Disabled| This is a New Detection
