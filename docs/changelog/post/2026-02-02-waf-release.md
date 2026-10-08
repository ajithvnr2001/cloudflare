---
url: https://developers.cloudflare.com/changelog/post/2026-02-02-waf-release/
title: WAF Release - 2026-02-02 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:35.383465+00:00
---

# WAF Release - 2026-02-02 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-02-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 2, 2026

## WAF Release - 2026-02-02

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-02-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release introduces new detections for CVE-2025-64459 and CVE-2025-24893.

**Key Findings**

  * CVE-2025-64459: Django versions prior to 5.1.14, 5.2.8, and 4.2.26 are vulnerable to SQL injection via crafted dictionaries passed to QuerySet methods and the `Q()` class.
  * CVE-2025-24893: XWiki allows unauthenticated remote code execution through crafted requests to the SolrSearch endpoint, affecting the entire installation.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...30698ff3| N/A| XWiki - Remote Code Execution - CVE:CVE-2025-24893 2| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...da8ba7e6| N/A| Django SQLI - CVE:CVE-2025-64459| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...8d667511| N/A| NoSQL, MongoDB - SQLi - Comparison - 2| Block| Block| Rule metadata description refined. Detection unchanged.
