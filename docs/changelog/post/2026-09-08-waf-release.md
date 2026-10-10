---
url: https://developers.cloudflare.com/changelog/post/2026-09-08-waf-release/
title: WAF Release - 2026-09-08 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.550611+00:00
---

# WAF Release - 2026-09-08 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-08-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 8, 2026

## WAF Release - 2026-09-08

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release enhances detection logic for existing rules targeting Next.js remote code execution (RCE) vulnerabilities by consolidating active beta rules into baseline signatures.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...c76ba662| N/A| Next.js - Image Optimizer Remote Code Execution via Crafted AVIF - Beta| Log| Block| This rule is merged into the original rule "Next.js - Image Optimizer Remote Code Execution via Crafted AVIF" (ID: ...80256efe).  
Cloudflare Managed Ruleset| ...208457cf| N/A| Next.js - Remote Code Execution - CVE:CVE-2026-75604 - Beta| Log| Block| This rule is merged into the original rule "Next.js - Remote Code Execution - CVE:CVE-2026-75604" (ID: ...2ca6cce3).
