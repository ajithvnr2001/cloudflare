---
url: https://developers.cloudflare.com/changelog/post/2026-04-27-waf-release/
title: WAF Release - 2026-04-27 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:51.226741+00:00
---

# WAF Release - 2026-04-27 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-27-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 27, 2026

## WAF Release - 2026-04-27

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-27-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release focuses on new improvements to enhance coverage.

**Key Findings**

  * Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.



**Continuous Rule Improvements**

We are continuously refining our managed rules to provide more resilient protection and deeper insights into attack patterns. To ensure an optimal security posture, we recommend consistently monitoring the Security Events dashboard and adjusting rule actions as these enhancements are deployed.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...80cec1dd| N/A| PostgreSQL - SQLi - COPY - Beta| Log| Block| This is a new detection. This rule is merged into the original rule "PostgreSQL - SQLi - COPY - Body (ID: ...e7265a4e). The rule previously known as "PostgreSQL - SQLi - COPY" is now renamed to "PostgreSQL - SQLi - COPY - Body".  
Cloudflare Managed Ruleset| ...2903de89| N/A| PostgreSQL - SQLi - COPY - Headers| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...1036cfa6| N/A| PostgreSQL - SQLi - COPY - URI| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...55ff389e| N/A| SQLi - AND/OR MAKE_SET/ELT - Beta| Log| Block| This is a new detection. This rule is merged into the original rule "SQLi - AND/OR MAKE_SET/ELT - Body" (ID: ...252d3934). The rule previously known as "SQLi - AND/OR MAKE_SET/ELT" is now renamed to "SQLi - AND/OR MAKE_SET/ELT - Body".  
Cloudflare Managed Ruleset| ...346487f9| N/A| SQLi - AND/OR MAKE_SET/ELT - Headers| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...1ac6ceca| N/A| SQLi - AND/OR MAKE_SET/ELT - URI| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...dd471337| N/A| SQLi - Common Patterns - Beta| Log| Block| This is a new detection. This rule is merged into the original rule "SQLi - Common Patterns - Body" (ID: ...cb5d0b9b). The rule previously known as "SQLi - Common Patterns" is now renamed to "SQLi - Common Patterns - Body".  
Cloudflare Managed Ruleset| ...975c07b7| N/A| SQLi - Common Patterns - Headers| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...05b1b06b| N/A| SQLi - Common Patterns - URI| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...dd0ba3c7| N/A| SQLi - Equation - Beta| Log| Block| This is a new detection. This rule is merged into the original rule "SQLi - Equation - Body" (ID: ...c2eb3e7f). The rule previously known as "SQLi - Equation" is now renamed to "SQLi - Equation - Body".  
Cloudflare Managed Ruleset| ...3d1c2384| N/A| SQLi - Equation - Headers| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...e1149ea6| N/A| SQLi - Equation - URI| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...205adbb0| N/A| SQLi - AND/OR Digit Operator Digit - Beta| Log| Block| This is a new detection. This rule is merged into the original rule "SQLi - AND/OR Digit Operator Digit - Body" (ID: ...3893c564). The rule previously known as "SQLi - AND/OR Digit Operator Digit" is now renamed to "SQLi - AND/OR Digit Operator Digit - Body".  
Cloudflare Managed Ruleset| ...ad2abbaa| N/A| SQLi - AND/OR Digit Operator Digit - Headers| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...53acbc0d| N/A| SQLi - AND/OR Digit Operator Digit - URI| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...2b45a97d| N/A| SQLi - Benchmark Function - Beta| Log| Block| This is a new detection. This rule is merged into the original rule "SQLi - Benchmark Function - Body" (ID: ...2ebc44ad). The rule previously known as "SQLi - Benchmark Function" is now renamed to "SQLi - Benchmark Function - Body".  
Cloudflare Managed Ruleset| ...9889aadc| N/A| SQLi - Benchmark Function - Headers| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...491b28e9| N/A| SQLi - Benchmark Function - URI| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...2aa649de| N/A| SQLi - Comparison - Beta| Log| Block| This is a new detection. This rule is merged into the original rule "SQLi - Comparison - Body" (ID: ...e7907480). The rule previously known as "SQLi - Comparison" is now renamed to "SQLi - Comparison - Body".  
Cloudflare Managed Ruleset| ...39e3e013| N/A| SQLi - Comparison - Headers| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...f4bdb492| N/A| SQLi - Comparison - URI| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...a1ff3b34| N/A| SQLi - String Concatenation - Body - Beta| Log| Block| This is a new detection. This rule is merged into the original rule "SQLi - String Concatenation - Headers" (ID: ...2116d2fe).The rule previously known as "SQLi - String Concatenation - Headers" is now renamed to "SQLi - String Concatenation - Body".   
Cloudflare Managed Ruleset| ...0d0e6c3b| N/A| SQLi - String Concatenation - Headers| Log| Block| This is a new detection.(Former Id was ...846d1940)  
Cloudflare Managed Ruleset| ...26cc211f| N/A| SQLi - String Concatenation - URI| Log| Block| This is a new detection. (Former Id was ...8fae8c84)  
Cloudflare Managed Ruleset| ...eacc78ab| N/A| SQLi - SELECT Expression - Beta| Log| Block| This is a new detection. This rule is merged into the original rule "SQLi - SELECT Expression - Body" (ID: ...d0023a36). The rule previously known as "SQLi - SELECT Expression" is now renamed to "SQLi - SELECT Expression - Body".  
Cloudflare Managed Ruleset| ...630bb223| N/A| SQLi - SELECT Expression - Headers| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...dcd6efb5| N/A| SQLi - SELECT Expression - URI| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...18c47cea| N/A| SQLi - ORD and ASCII - Beta| Log| Block| This is a new detection. This rule is merged into the original rule "SQLi - ORD and ASCII- Body" (ID: ...d0d207f9). The rule previously known as "SQLi - ORD and ASCII" is now renamed to "SQLi - ORD and ASCII- Body".  
Cloudflare Managed Ruleset| ...bdb1618f| N/A| SQLi - ORD and ASCII - URI| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...1d0906b6| N/A| SQLi - ORD and ASCII - Headers| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...9fe4eff5| N/A| SQLi - Destructive Operations| Log| Block| This is a new detection.
