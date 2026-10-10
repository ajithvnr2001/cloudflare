---
url: https://developers.cloudflare.com/changelog/post/2026-09-30-waf-release/
title: WAF Release - 2026-09-30 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:30.038687+00:00
---

# WAF Release - 2026-09-30 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-30-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 30, 2026

## WAF Release - 2026-09-30

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces new detections to enhance protection against a specific GitLab path traversal vulnerability, alongside advanced generic rules targeting HTTP request smuggling, directory traversal, and command injection attempts.

**Key Findings**

  * CVE-2026-85706: A path traversal vulnerability affecting GitLab.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...cb14ded8| N/A| Broken Access Control - Directory Traversal| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...0364bd7e| N/A| HTTP Request Smuggling - Request Body Anomaly - Beta| Log| Block| This rule is merged into the original rule "HTTP/2 Request Smuggling - Request Body Anomaly" (ID: ...1489d892).  
Cloudflare Managed Ruleset| ...d498a69a| N/A| Command Injection - Generic 8 - body - Beta| Disabled| Disabled| This rule is merged into the original rule "Command Injection - Generic 8 - body" (ID: ...413592e2).  
Cloudflare Managed Ruleset| ...87ae8cfc| N/A| GitLab - Path Traversal- CVE:CVE-2026-85706| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...549f7356| N/A| Generic - Request routing cache inconsistency| N/A| Block| This is a new detection.
