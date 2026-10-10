---
url: https://developers.cloudflare.com/changelog/post/2026-08-26-emergency-waf-release/
title: WAF Release - 2026-08-26 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.184151+00:00
---

# WAF Release - 2026-08-26 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-26-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 26, 2026

## WAF Release - 2026-08-26 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This emergency release updates an existing Next.js remote code execution rule to identify CVE-2026-75604 and adds a new rule for remote code execution in the Next.js Image Optimizer via crafted AVIF images.

**Key Findings**

  * CVE-2026-75604 affects Windows-hosted Next.js applications using both the Pages Router and App Router without Cache Components and can lead to unauthenticated remote code execution.

  * GHSA-2xp9-vwfh-vxw4 affects the Next.js Image Optimizer and can lead to unauthenticated remote code execution when it optimizes an attacker-controlled AVIF image.




**Impact**

Next.js recommends updating to version 16.3.3 or 15.5.24 to address these vulnerabilities.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...2ca6cce3| N/A| Next.js - Remote Code Execution - CVE:CVE-2026-75604| Block| N/A| Rule metadata description refined. Detection unchanged.  
Cloudflare Managed Ruleset| ...80256efe| N/A| Next.js - Image Optimizer Remote Code Execution via Crafted AVIF| N/A| Block| This is a new detection.
