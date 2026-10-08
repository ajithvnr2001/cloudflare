---
url: https://developers.cloudflare.com/changelog/post/2026-02-16-waf-release/
title: WAF Release - 2026-02-16 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:37.930218+00:00
---

# WAF Release - 2026-02-16 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-16-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 16, 2026

## WAF Release - 2026-02-16

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-16-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release introduces new detections for CVE-2025-68645 and CVE-2025-31125.

**Key Findings**

  * CVE-2025-68645: A Local File Inclusion (LFI) vulnerability in the Webmail Classic UI of Zimbra Collaboration Suite (ZCS) 10.0 and 10.1 allows unauthenticated remote attackers to craft requests to the `/h/rest` endpoint, improperly influence internal dispatching, and include arbitrary files from the WebRoot directory.
  * CVE-2025-31125: Vite, the JavaScript frontend tooling framework, exposes content of non-allowed files via `?inline&import` when its development server is network-exposed, enabling unauthorized attackers to read arbitrary files and potentially leak sensitive information.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...833761f7| N/A| Zimbra - Local File Inclusion - CVE:CVE-2025-68645| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...950ed8c8| N/A| Vite - WASM Import Path Traversal - CVE:CVE-2025-31125| Log| Block| This is a new detection.
