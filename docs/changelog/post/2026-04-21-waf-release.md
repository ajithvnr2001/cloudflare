---
url: https://developers.cloudflare.com/changelog/post/2026-04-21-waf-release/
title: WAF Release - 2026-04-21 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:39.884927+00:00
---

# WAF Release - 2026-04-21 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-21-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 21, 2026

## WAF Release - 2026-04-21

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release introduces a new detection for a Remote Code Execution (RCE) vulnerability in Apache ActiveMQ (CVE-2026-34197) and an updated signature for Magento 2 - Unrestricted File Upload. Alongside these detections, we are continuing our work on rule refinements to provide deeper security insights for our customers.

**Key Findings**

  * Apache ActiveMQ (CVE-2026-34197): A vulnerability in Apache ActiveMQ allows an unauthenticated, remote attacker to execute arbitrary code. This flaw occurs during the processing of specially crafted network packets, leading to potential full system compromise.

  * Magento 2 - Unrestricted File Upload - 2: This is a follow-up enhancement to our existing protections for Magento and Adobe Commerce.




**Impact**

Successful exploitation of these vulnerabilities could allow unauthenticated attackers to execute arbitrary code or gain full administrative control over affected servers. We strongly recommend applying official vendor patches for Apache ActiveMQ and Magento to address the underlying vulnerabilities.

**Continuous Rule Improvements**

We are continuously refining our managed rules to provide more resilient protection and deeper insights into attack patterns. To ensure an optimal security posture, we recommend consistently monitoring the Security Events dashboard and adjusting rule actions as these enhancements are deployed.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...ee159e2e| N/A| Command Injection - Generic 8 - uri| Log| Block| This is a new detection. Previous description was "Command Injection - Generic 8 - uri - Beta"  
Cloudflare Managed Ruleset| ...a15308cf| N/A| Command Injection - Generic 8 - body - Beta| Disabled| Disabled| This is a new detection. This rule is merged into the original rule "Command Injection - Generic 8 - body" (ID: ...413592e2). The rule previously known as "Command Injection - Generic 8" is now renamed to "Command Injection - Generic 8 - body".  
Cloudflare Managed Ruleset| ...958047ed| N/A| MySQL - SQLi - Executable Comment - Beta| Log| Block| This is a new detection. This rule is merged into the original rule "MySQL - SQLi - Executable Comment - Body" (ID: ...7bd2d8fa) The rule previously known as "MySQL - SQLi - Executable Comment" is now renamed to "MySQL - SQLi - Executable Comment - Body".  
Cloudflare Managed Ruleset| ...582cc559| N/A| MySQL - SQLi - Executable Comment - Headers| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...a16639d3| N/A| MySQL - SQLi - Executable Comment - URI| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...44f24211| N/A| Magento 2 - Unrestricted file upload - 2| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...bf170a17| N/A| Apache ActiveMQ - Remote Code Execution - CVE:CVE-2026-34197| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...8c2ac1a7| N/A| SQLi - Sleep Function - Beta| Log| Block| This is a new detection. This rule is merged into the original rule "SQLi - Sleep Function" (ID: ...f77e8d54)  
Cloudflare Managed Ruleset| ...4dacaeb8| N/A| SQLi - Sleep Function - Headers| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...ed4c9ece| N/A| SQLi - Sleep Function - URI| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...1dfa64df| N/A| SQLi - Probing - uri| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...4c62e2e7| N/A| SQLi - Probing - header| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...aab28ea1| N/A| SQLi - Probing - body| Disabled| Disabled| This is a new detection. This rule is merged into the original rule "SQLi - Probing" (ID: ...b4026c88)  
Cloudflare Managed Ruleset| ...20999be0| N/A| SQLi - Probing 2 | Disabled| Disabled| This rule had duplicate detection logic and has been deprecated.  
Cloudflare Managed Ruleset| ...d7aa0008| N/A| SQLi - UNION in MSSQL - Body| Disabled| Disabled| This rule has been renamed to differentiate from "SQLi - UNION in MSSQL" (ID: ...ee5e35fd) and contains updated rule logic.  
Cloudflare Managed Ruleset| ...a67d8561| N/A| SQLi - UNION - 3| Disabled| Disabled| This rule had duplicate detection logic and has been deprecated.  
Cloudflare Managed Ruleset| ...0af34bba| N/A| XSS, HTML Injection - Embed Tag - URI| Disabled| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...70282f38| N/A| XSS, HTML Injection - Embed Tag - Headers| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...23f4d718| N/A| XSS, HTML Injection - IFrame Tag - Src and Srcdoc Attributes - Headers| Log| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...6978def1| N/A| XSS, HTML Injection - Link Tag - Headers| Log| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...ebd81645| N/A| XSS, HTML Injection - Link Tag - URI| Disabled| Disabled| This is a new detection.
