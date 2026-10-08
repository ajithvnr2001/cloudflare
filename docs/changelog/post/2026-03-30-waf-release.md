---
url: https://developers.cloudflare.com/changelog/post/2026-03-30-waf-release/
title: WAF Release - 2026-03-30 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:43.847124+00:00
---

# WAF Release - 2026-03-30 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-30-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 30, 2026

## WAF Release - 2026-03-30

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-30-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release introduces new detections for a critical authentication bypass vulnerability in Fortinet products (CVE-2025-59718), alongside three new generic detection rules designed to identify and block HTTP Parameter Pollution attempts. Additionally, this release includes targeted protection for a high-impact unrestricted file upload vulnerability in Magento and Adobe Commerce.

**Key Findings**

  * CVE-2025-59718: An improper cryptographic signature verification vulnerability in Fortinet FortiOS, FortiProxy, and FortiSwitchManager. This may allow an unauthenticated attacker to bypass the FortiCloud SSO login authentication using a maliciously crafted SAML message, if that feature is enabled on the device.

  * Magento 2 - Unrestricted File Upload: A critical flaw in Magento and Adobe Commerce allows unauthenticated attackers to bypass security checks and upload malicious files to the server, potentially leading to Remote Code Execution (RCE).




**Impact**

Successful exploitation of the Fortinet and Magento vulnerabilities could allow unauthenticated attackers to gain administrative control or deploy webshells, leading to complete server compromise and data theft.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...2f7f95e9| N/A| Generic Rules - Parameter Pollution - Body| Log| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...319731a4| N/A | Generic Rules - Parameter Pollution - Header - Form | Log | Disabled  
| This is a new detection.  
Cloudflare Managed Ruleset| ...def262dd| N/A | Generic Rules - Parameter Pollution - URI | Log | Disabled  
| This is a new detection.  
Cloudflare Managed Ruleset| ...70a36147| N/A| Magento 2 - Unrestricted file upload| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...2ffcca9f| N/A| Fortinet FortiCloud SSO - Authentication Bypass - CVE:CVE-2025-59718| Log| Block| This is a new detection.
