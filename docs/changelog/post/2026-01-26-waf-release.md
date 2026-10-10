---
url: https://developers.cloudflare.com/changelog/post/2026-01-26-waf-release/
title: WAF Release - 2026-01-26 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:44.631142+00:00
---

# WAF Release - 2026-01-26 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-26-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 26, 2026

## WAF Release - 2026-01-26

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release introduces new detections for denial-of-service attempts targeting React CVE-2026-23864 (<https://www.cve.org/CVERecord?id=CVE-2026-23864>[ ↗︎](https://www.cve.org/CVERecord?id=CVE-2026-23864)).

**Key Findings**

  * CVE-2026-23864 (<https://www.cve.org/CVERecord?id=CVE-2026-23864>[ ↗︎](https://www.cve.org/CVERecord?id=CVE-2026-23864)) affects `react-server-dom-parcel`, `react-server-dom-turbopack`, and `react-server-dom-webpack` packages.
  * Attackers can send crafted HTTP requests to Server Function endpoints, causing server crashes, out-of-memory exceptions, or excessive CPU usage.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...61680354| N/A| React Server - DOS - CVE:CVE-2026-23864 - 1| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...dcdffcf8| N/A| React Server - DOS - CVE:CVE-2026-23864 - 2| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...349edbc6| N/A| React Server - DOS - CVE:CVE-2026-23864 - 3| N/A| Block| This is a new detection.
