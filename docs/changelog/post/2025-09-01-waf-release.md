---
url: https://developers.cloudflare.com/changelog/post/2025-09-01-waf-release/
title: WAF Release - 2025-09-01 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:21.379399+00:00
---

# WAF Release - 2025-09-01 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-01-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 1, 2025

## WAF Release - 2025-09-01

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-01-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**This week's update**

This week, a critical vulnerability was disclosed in Fortinet FortiWeb (versions 7.6.3 and below, versions 7.4.7 and below, versions 7.2.10 and below, and versions 7.0.10 and below), linked to improper parameter handling that could allow unauthorized access.

**Key Findings**

  * Fortinet FortiWeb (CVE-2025-52970): A vulnerability may allow an unauthenticated remote attacker with access to non-public information to log in as any existing user on the device via a specially crafted request.



**Impact**

Exploitation could allow an unauthenticated attacker to impersonate any existing user on the device, potentially enabling them to modify system settings or exfiltrate sensitive information, posing a serious security risk. Upgrading to the latest vendor-released version is strongly recommended.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...c49b7cf8| 100586| Fortinet FortiWeb - Auth Bypass - CVE:CVE-2025-52970| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...790c9dde| 100136C| XSS - JavaScript - Headers and Body| N/A| N/A| Rule metadata description refined. Detection unchanged.
