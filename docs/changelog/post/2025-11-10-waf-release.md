---
url: https://developers.cloudflare.com/changelog/post/2025-11-10-waf-release/
title: WAF Release - 2025-11-10 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:47.017068+00:00
---

# WAF Release - 2025-11-10 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-10-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 10, 2025

## WAF Release - 2025-11-10

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release introduces new detections for Prototype Pollution across three common vectors: URI, Body, and Header/Form.

**Key Findings**

  * These attacks can affect both API and web applications by altering normal behavior or bypassing security controls.



**Impact**

Exploitation may allow attackers to change internal logic or cause unexpected behavior in applications using JavaScript or Node.js frameworks. Developers should sanitize input keys and avoid merging untrusted data structures.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...606285e6| N/A| Generic Rules - Prototype Pollution - URI| Log| Disabled| This is a new detection  
Cloudflare Managed Ruleset| ...4f59ff26| N/A| Generic Rules - Prototype Pollution - Body| Log| Disabled| This is a new detection  
Cloudflare Managed Ruleset| ...7efbeb39| N/A| Generic Rules - Prototype Pollution - Header - Form| Log| Disabled| This is a new detection
