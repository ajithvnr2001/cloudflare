---
url: https://developers.cloudflare.com/changelog/post/2026-06-09-waf-release/
title: WAF Release - 2026-06-09 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:57.237770+00:00
---

# WAF Release - 2026-06-09 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-09-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 9, 2026

## WAF Release - 2026-06-09

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-09-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces new detections for a critical SQL injection vulnerability in Drupal installations utilizing PostgreSQL (CVE-2026-9082), alongside targeted protection for an unsafe deserialization flaw in the Mirasvit Cache Warmer extension (CVE-2026-45247). Additionally, this release includes coverage for a prototype pollution vector in Axios (CVE-2026-40175) and a new generic rule designed to identify and block sophisticated SQL Injection (SQLi) bypass attempts leveraging obfuscated boolean logic.

**Key Findings**

  * CVE-2026-9082: A database abstraction vulnerability affects Drupal sites configured with a PostgreSQL backend. Remote, unauthenticated attackers can exploit this flaw via crafted inputs to inject malicious SQL commands and access or manipulate backend data.

  * CVE-2026-45247: A PHP Object Injection vulnerability exists in the Mirasvit Cache Warmer extension for Magento and Adobe Commerce. This flaw stems from unsafe deserialization of untrusted user input, enabling unauthenticated attackers to execute arbitrary code on the hosting server.

  * CVE-2026-40175: A prototype pollution vulnerability affects the Axios HTTP client library. Attackers can exploit this to inject malicious properties into the global JavaScript object prototype, potentially causing application crashes (Denial of Service) or executing unauthorized code depending on the application structure.




**Impact**

Successful exploitation of these vulnerabilities could allow unauthenticated attackers to execute arbitrary code, manipulate database contents, or induce application crashes, leading to severe operational disruption or complete server compromise. These newly deployed signatures intercept these advanced malicious payloads at the edge before they can interact with vulnerable software configurations.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...387cf935| N/A| Axios - Prototype Pollution - CVE:CVE-2026-40175| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...417eb9e0| N/A| Drupal - PostgreSQL SQLi - CVE:CVE-2026-9082 - Body| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...fd3857fd| N/A| Drupal - PostgreSQL SQLi - CVE:CVE-2026-9082 - URI| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...aee241d2| N/A| SQLi - Obfuscated Boolean - Body| N/A| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...d8620070| N/A| SQLi - Obfuscated Boolean - Headers| N/A| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...e0be4d47| N/A| Mirasvit Cache Warmer - PHP Object Injection - CVE:CVE-2026-45247| N/A| Block| This is a new detection.
