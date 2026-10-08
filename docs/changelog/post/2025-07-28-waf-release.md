---
url: https://developers.cloudflare.com/changelog/post/2025-07-28-waf-release/
title: WAF Release - 2025-07-28 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:17.643029+00:00
---

# WAF Release - 2025-07-28 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-28-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 28, 2025

## WAF Release - 2025-07-28

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-28-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s update spotlights several vulnerabilities across Apache Tomcat, MongoDB, and Fortinet FortiWeb. Several flaws related with a memory leak in Apache Tomcat can lead to a denial-of-service attack. Additionally, a code injection flaw in MongoDB's Mongoose library allows attackers to bypass security controls to access restricted data.

**Key Findings**

  * Fortinet FortiWeb (CVE-2025-25257): An improper neutralization of special elements used in a SQL command vulnerability in Fortinet FortiWeb versions allows an unauthenticated attacker to execute unauthorized SQL code or commands.

  * Apache Tomcat (CVE-2025-31650): A improper Input Validation vulnerability in Apache Tomcat that could create memory leak when incorrect error handling for some invalid HTTP priority headers resulted in incomplete clean-up of the failed request.

  * MongoDB (CVE-2024-53900, CVE:CVE-2025-23061): Improper use of `$where` in match and a nested `$where` filter with a `populate()` match in Mongoose can lead to search injection.




**Impact**

These vulnerabilities target user-facing components, web application servers, and back-end databases. A SQL injection flaw in Fortinet FortiWeb can lead to data theft or system compromise. A separate issue in Apache Tomcat involves a memory leak from improper input validation, which could be exploited for a denial-of-service (DoS) attack. Finally, a vulnerability in MongoDB's Mongoose library allows attackers to bypass security filters and access unauthorized data through malicious search queries.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...3461ec9e| 100804| BerriAI - SSRF - CVE:CVE-2024-6587| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...0cb13e1d| 100812| Fortinet FortiWeb - Remote Code Execution - CVE:CVE-2025-25257| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...67fae7f7| 100813| Apache Tomcat - DoS - CVE:CVE-2025-31650| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...4b6a5bb1| 100815| MongoDB - Remote Code Execution - CVE:CVE-2024-53900, CVE:CVE-2025-23061| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...688f8e79| 100816| MongoDB - Remote Code Execution - CVE:CVE-2024-53900, CVE:CVE-2025-23061| Log| Block| This is a New Detection
