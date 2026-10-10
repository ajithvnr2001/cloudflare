---
url: https://developers.cloudflare.com/changelog/post/2025-10-24-emergency-waf-release/
title: WAF Release - 2025-10-24 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:47.532901+00:00
---

# WAF Release - 2025-10-24 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-24-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 24, 2025

## WAF Release - 2025-10-24 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release introduces a new detection signature that enhances coverage for a critical vulnerability in Windows Server Update Services (WSUS), tracked as CVE-2025-59287.

**Key Findings**

The vulnerability allows unauthenticated attackers to potentially achieve remote code execution. The updated detection logic strengthens defenses by improving resilience against exploitation attempts targeting this flaw.

**Impact**

Successful exploitation of CVE-2025-59287 could enable attackers to hijack sessions, execute arbitrary commands, exfiltrate sensitive data, and disrupt storefront operations. These actions pose significant confidentiality and integrity risks to affected environments. Administrators should apply vendor patches immediately to mitigate exposure.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...bd72ba08| N/A| Windows Server - Deserialization - CVE:CVE-2025-59287| N/A| Block| This is a New Detection
