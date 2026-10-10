---
url: https://developers.cloudflare.com/changelog/post/2025-12-10-emergency-waf-release/
title: WAF Release - 2025-12-10 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:45.967109+00:00
---

# WAF Release - 2025-12-10 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-10-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 10, 2025

## WAF Release - 2025-12-10 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This additional week's emergency release introduces improvements to our existing rule for React – Remote Code Execution – CVE-2025-55182 - 2, along with two new generic detections covering server-side function exposure and resource-exhaustion patterns.

**Key Findings**

Enhanced detection logic for React – RCE – CVE-2025-55182, added Generic – Server Function Source Code Exposure, and added Generic – Server Function Resource Exhaustion.

**Impact**

These updates strengthen protection against React RCE exploitation attempts and broaden coverage for common server-function abuse techniques that may expose internal logic or disrupt application availability.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...15fce168| N/A| React - Remote Code Execution - CVE:CVE-2025-55182 - 2| N/A| Block| This is an improved detection.  
Cloudflare Free Ruleset| ...74746aff| N/A| React - Remote Code Execution - CVE:CVE-2025-55182 - 2| N/A| Block| This is an improved detection.  
Cloudflare Managed Ruleset| ...fefb4e9b| N/A| Generic - Server Function Source Code Exposure| N/A| Block| This is a new detection.  
Cloudflare Free Ruleset| ...251e86aa| N/A| Generic - Server Function Source Code Exposure| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...102ec699| N/A| Generic - Server Function Resource Exhaustion| N/A| Disabled| This is a new detection.
