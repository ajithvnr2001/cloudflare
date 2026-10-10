---
url: https://developers.cloudflare.com/changelog/post/2025-12-11-emergency-waf-release/
title: WAF Release - 2025-12-11 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:45.897760+00:00
---

# WAF Release - 2025-12-11 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-11-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 11, 2025

## WAF Release - 2025-12-11 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This emergency release introduces rules for CVE-2025-55183 and CVE-2025-55184, targeting server-side function exposure and resource-exhaustion patterns, respectively.

**Key Findings**

Added coverage for Leaking Server Functions (CVE-2025-55183) and React Function DoS detection (CVE-2025-55184).

**Impact**

These updates strengthen protection for server-function abuse techniques (CVE-2025-55183, CVE-2025-55184) that may expose internal logic or disrupt application availability.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...fefb4e9b| N/A| React - Leaking Server Functions - CVE:CVE-2025-55183| N/A| Block| This was labeled as Generic - Server Function Source Code Exposure.  
Cloudflare Free Ruleset| ...251e86aa| N/A| React - Leaking Server Functions - CVE:CVE-2025-55183| N/A| Block| This was labeled as Generic - Server Function Source Code Exposure.  
Cloudflare Managed Ruleset| ...102ec699| N/A| React - DoS - CVE:CVE-2025-55184| N/A| Disabled| This was labeled as Generic – Server Function Resource Exhaustion.
