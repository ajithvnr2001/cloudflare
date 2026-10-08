---
url: https://developers.cloudflare.com/changelog/post/2025-11-07-cache-keys-for-cloudflare-trace/
title: Inspect Cache Keys with Cloudflare Trace \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:28.616388+00:00
---

# Inspect Cache Keys with Cloudflare Trace · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-07-cache-keys-for-cloudflare-trace/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 7, 2025

## Inspect Cache Keys with Cloudflare Trace

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-07-cache-keys-for-cloudflare-trace/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now see the exact cache key generated for any request directly in Cloudflare Trace. This visibility helps you troubleshoot cache hits and misses, and verify that your Custom Cache Keys — configured via Cache Rules or Page Rules — are working as intended.

Previously, diagnosing caching behavior required inferring the key from configuration settings. Now, you can confirm that your custom logic for headers, query strings, and device types is correctly applied.

Access Trace via the [dashboard](https://developers.cloudflare.com/rules/trace-request/how-to/#use-trace-in-the-dashboard) or [API](https://developers.cloudflare.com/api/resources/request_tracer/methods/trace/), either manually for ad-hoc debugging or automated as part of your quality-of-service monitoring.

#### Example scenario

If you have a Cache Rule that segments content based on a specific cookie (for example, `user_region`), run a Trace with that cookie present to confirm the `user_region` value appears in the resulting cache key.

The Trace response includes the cache key in the `cache` object:
    
    
    {
      "step_name": "request",
      "type": "cache",
      "matched": true,
      "public_name": "Cache Parameters",
      "cache": {
        "key": {
          "zone_id": "023e105f4ecef8ad9ca31a8372d0c353",
          "scheme": "https",
          "host": "example.com",
          "uri": "/images/hero.jpg"
        },
        "key_string": "023e105f4ecef8ad9ca31a8372d0c353::::https://example.com/images/hero.jpg:::::"
      }
    }

#### Get started

To learn more, refer to the [Trace documentation](https://developers.cloudflare.com/rules/trace-request/) and our guide on [Custom Cache Keys](https://developers.cloudflare.com/cache/how-to/cache-keys/).
