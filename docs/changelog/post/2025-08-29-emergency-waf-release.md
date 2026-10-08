---
url: https://developers.cloudflare.com/changelog/post/2025-08-29-emergency-waf-release/
title: WAF Release - 2025-08-29 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:21.036067+00:00
---

# WAF Release - 2025-08-29 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-29-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 29, 2025

## WAF Release - 2025-08-29 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-29-emergency-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**This week's update**

This week, new critical vulnerabilities were disclosed in Next.js’s image optimization functionality, exposing a broad range of production environments to risks of data exposure and cache manipulation.

**Key Findings**

  * CVE-2025-55173: Arbitrary file download from the server via image optimization.

  * CVE-2025-57752: Cache poisoning leading to unauthorized data disclosure.




**Impact**

Exploitation could expose sensitive files, leak user or backend data, and undermine application trust. Given Next.js’s wide use, immediate patching and cache hardening are strongly advised.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...9ff4bfe3| 100613| Next.js - Dangerous File Download - CVE:CVE-2025-55173| N/A| Block| This is a new detection  
Cloudflare Managed Ruleset| ...69b9ea7d| 100616| Next.js - Information Disclosure - CVE:CVE-2025-57752| N/A| Block| This is a new detection
