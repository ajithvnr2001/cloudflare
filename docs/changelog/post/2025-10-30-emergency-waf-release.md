---
url: https://developers.cloudflare.com/changelog/post/2025-10-30-emergency-waf-release/
title: WAF Release - 2025-10-30 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:47.269837+00:00
---

# WAF Release - 2025-10-30 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-30-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 30, 2025

## WAF Release - 2025-10-30 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release introduces a new detection signature that enhances coverage for a critical vulnerability in Oracle E-Business Suite, tracked as CVE-2025-61884.

**Key Findings**

The flaw is easily exploitable and allows an unauthenticated attacker with network access to compromise Oracle Configurator, which can grant access to sensitive resources and configuration data. The affected versions include 12.2.3 through 12.2.14.

**Impact**

Successful exploitation of CVE-2025-61884 may result in unauthorized access to critical business data or full exposure of information accessible through Oracle Configurator. Administrators are strongly advised to apply vendor's patches and recommended mitigations to reduce this exposure.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...8827402f| N/A| Oracle E-Business Suite - SSRF - CVE:CVE-2025-61884| N/A| Block| This is a New Detection
