---
url: https://developers.cloudflare.com/changelog/post/2026-05-04-waf-release/
title: WAF Release - 2026-05-04 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:38.915430+00:00
---

# WAF Release - 2026-05-04 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-04-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 4, 2026

## WAF Release - 2026-05-04

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release focuses on new detections to expand coverage across command injection, SQL injection, PHP object injection, remote code execution, and XSS attack vectors.

**Key Findings**

  * Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.



**Continuous Rule Improvements**

We are continuously refining our managed rules to provide more resilient protection and deeper insights into attack patterns. To ensure an optimal security posture, we recommend consistently monitoring the Security Events dashboard and adjusting rule actions as these enhancements are deployed.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...f0884a68| N/A| XSS, HTML Injection - Object Tag - Body (beta)| Log| Block| This is a new detection. This rule is merged into the original rule "XSS, HTML Injection - Object Tag" (ID: ...0c14e284).  
Cloudflare Managed Ruleset| ...ff012303| N/A| XSS, HTML Injection - Object Tag - Headers| Log| Block| This is a new detection. The rule previously known as "XSS, HTML Injection - Object Tag - Headers (beta)" is now renamed to "XSS, HTML Injection - Object Tag - Headers".  
Cloudflare Managed Ruleset| ...16f921d9| N/A| XSS, HTML Injection - Object Tag - URI| Log| Block| This is a new detection. The rule previously known as "XSS, HTML Injection - Object Tag - URI (beta)" is now renamed to "XSS, HTML Injection - Object Tag - URI".  
Cloudflare Managed Ruleset| ...dc90d21a| N/A| Command Injection - Generic 9 - Body Vector - Beta| N/A| Disabled| This is a new detection. This rule is merged into the original rule "Command Injection - Generic 9 - Body Vector" (ID: ...0677175f)  
Cloudflare Managed Ruleset| ...f8960375| N/A| Command Injection - Generic 9 - Header Vector - Beta| N/A| Disabled| This is a new detection. This rule is merged into the original rule "Command Injection - Generic 9 - Header Vector" (ID: ...1eb7a999)  
Cloudflare Managed Ruleset| ...ef47a800| N/A| Command Injection - Generic 9 - URI Vector - Beta| N/A| Disabled| This is a new detection. This rule is merged into the original rule "Command Injection - Generic 9 - URI Vector" (ID: ...97321c6c)  
Cloudflare Managed Ruleset| ...beebf804| N/A| Command Injection - Sleep - Body| N/A| Disabled| This is a new detection. The rule previously known as "Command Injection

  * Sleep" is now renamed to "Command Injection - Sleep - Body".

  
Cloudflare Managed Ruleset| ...0d257566| N/A| Command Injection - Sleep - Headers| N/A| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...1856fe86| N/A| Command Injection - Sleep - URI| N/A| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...e6e43c37| N/A| Fortinet FortiSandbox - Command Injection - CVE:CVE-2026-39808| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...88118795| N/A| Remote Code Execution - Common Bash Bypass - Headers| N/A| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...9299d53b| N/A| Remote Code Execution - Common Bash Bypass - URI| N/A| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...b0bf33f9| N/A| Remote Code Execution - Common Bash Bypass - Body - Beta| N/A| Disabled| This is a new detection. This rule is merged into the original rule "Remote Code Execution - Common Bash Bypass Body" (ID: ...efb7e5b9). The rule previously known as "Remote Code Execution - Common Bash Bypass Beta" is now renamed to "Remote Code Execution - Common Bash Bypass Body".  
Cloudflare Managed Ruleset| ...33bfe8b9| N/A| PHP Object Injection - 2 - Body - Beta| N/A| Disabled| This is a new detection. This rule is merged into the original rule "PHP Object Injection - 2" (ID: ...161aafdc)  
Cloudflare Managed Ruleset| ...29552387| N/A| PHP Object Injection - 2 - Headers| N/A| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...8104f4c5| N/A| PHP Object Injection - 2 - URI| N/A| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...6a46201e| N/A| SQLi - DROP - 2 - Beta| N/A| Disabled| This is a new detection. This rule is merged into the original rule "SQLi - DROP - 2" (ID: ...48ac2221)  
Cloudflare Managed Ruleset| ...8b7f85ee| N/A| SQLi - DROP - 2 - Headers| N/A| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...1546b5f0| N/A| SQLi - DROP - 2 - URI| N/A| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...1e053dce| N/A| SmarterMail - Remote Code Execution - CVE:CVE-2026-24423| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...d0023a36| N/A| SQLi - SELECT Expression - Body| Block| Disabled| Action changed  
Cloudflare Managed Ruleset| ...26cc211f| N/A| SQLi - String Concatenation - URI| Block| Disabled| Action changed
