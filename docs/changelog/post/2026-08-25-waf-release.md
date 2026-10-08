---
url: https://developers.cloudflare.com/changelog/post/2026-08-25-waf-release/
title: WAF Release - 2026-08-25 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:10.815634+00:00
---

# WAF Release - 2026-08-25 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-25-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 25, 2026

## WAF Release - 2026-08-25

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-25-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release moves four new detections from Log to Block, merges the XSS, HTML Injection - Script Tag - Beta rule into the original rule, and adds a Generic Rules - Remote Code Execution rule in Block mode.

**Key Findings**

  * Four new detections move from Log to Block: HTTP/2 Request Smuggling - Request Body Anomaly and XSS - JavaScript Event Handler Coercion across Headers, Body, and URI.

  * The XSS, HTML Injection - Script Tag - Beta rule is merged into the original rule.

  * A Generic Rules - Remote Code Execution detection is added in Block mode.


Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...1489d892| N/A| HTTP/2 Request Smuggling - Request Body Anomaly| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...20646260| N/A| XSS - JavaScript Event Handler Coercion - Headers| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...d706d517| N/A| XSS - JavaScript Event Handler Coercion - Body| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...660886c8| N/A| XSS - JavaScript Event Handler Coercion - URI| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...c293b926| N/A| XSS, HTML Injection - Script Tag - Beta| Log| Block| This rule is merged into the original rule "XSS, HTML Injection - Script Tag" (ID: ...7b58420b).  
Cloudflare Managed Ruleset| ...2ca6cce3| N/A| Generic Rules - Remote Code Execution| N/A| Block| This is a new detection.
