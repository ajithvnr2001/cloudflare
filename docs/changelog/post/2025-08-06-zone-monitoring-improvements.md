---
url: https://developers.cloudflare.com/changelog/post/2025-08-06-zone-monitoring-improvements/
title: Improvements to Monitoring Using Zone Settings \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:18.928835+00:00
---

# Improvements to Monitoring Using Zone Settings · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-06-zone-monitoring-improvements/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 6, 2025

## Improvements to Monitoring Using Zone Settings

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-06-zone-monitoring-improvements/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Load Balancing Monitors support loading and applying settings for a specific zone to monitoring requests to origin endpoints. This feature has been migrated to new infrastructure to improve reliability, performance, and accuracy.

All zone monitors have been tested against the new infrastructure. There should be no change to health monitoring results of currently healthy and active pools. Newly created or re-enabled pools may need validation of their monitor zone settings before being introduced to service, especially regarding correct application of mTLS.

#### What you can expect:

  * More reliable application of zone settings to monitoring requests, including 
    * Authenticated Origin Pulls
    * Aegis Egress IP Pools
    * Argo Smart Routing
    * HTTP/2 to Origin
  * Improved support and bug fixes for retries, redirects, and proxied origin resolution
  * Improved performance and reliability of monitoring requests within the Cloudflare network
  * Unrelated CDN or WAF configuration changes should have no risk of impact to pool health


