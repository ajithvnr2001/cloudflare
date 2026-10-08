---
url: https://developers.cloudflare.com/changelog/post/2026-09-16-jsd-api-results/
title: Control JavaScript Detections API results \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:14.317071+00:00
---

# Control JavaScript Detections API results · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-16-jsd-api-results/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 16, 2026

## Control JavaScript Detections API results

[Bots](https://developers.cloudflare.com/bots/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-16-jsd-api-results/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Enterprise Bot Management customers can control whether Cloudflare uses results created through the JavaScript Detections API for bot scoring and detections.

Turn **JavaScript Detections for API traffic** on or off in **Security** > **Settings**. You can also configure the zone through the Bot Management API by setting `jsd_api_results_enabled`:
    
    
    {
    	"jsd_api_results_enabled": true
    }

This setting is separate from zone-wide script injection. When it is off, the API script can still execute and return `success` to the callback, but Cloudflare does not consume the result.

For more information, refer to [JavaScript Detections](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/#api).
