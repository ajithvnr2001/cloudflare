---
url: https://developers.cloudflare.com/changelog/post/2026-09-02-origin-range-requests-rulesets-api/
title: Configure Origin Range Requests with the Rulesets API \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:12.411347+00:00
---

# Configure Origin Range Requests with the Rulesets API · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-02-origin-range-requests-rulesets-api/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 2, 2026

## Configure Origin Range Requests with the Rulesets API

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-02-origin-range-requests-rulesets-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Rulesets API now supports Origin Range Requests in Cache Rules. This setting lets Cloudflare fetch large files from your origin in cache-aligned byte ranges. Cloudflare may expand a client range and issue several single-range origin requests.

Set `origin_range_requests.mode` to `on`, `off`, or `default` for any traffic matched by a Cache Rule.

To override Cloudflare's default Origin Range Requests behavior, set the mode to `off`. The following rule turns off generated origin range requests for all traffic without changing cache eligibility:
    
    
    {
      "expression": "true",
      "action": "set_cache_settings",
      "action_parameters": {
        "origin_range_requests": {
          "mode": "off"
        }
      }
    }

Origin Range Requests do not make otherwise ineligible content cacheable. If your origin ignores `Range` and returns a complete `200 OK`, Cloudflare can use the response but must download the complete file. Origins should honor `Accept-Encoding: identity` and return consistent, unencoded partial responses.

For configuration details and mode behavior, refer to [Origin Range Requests in Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/settings/#origin-range-requests). For client responses and the complete origin contract, refer to [Range request behavior](https://developers.cloudflare.com/cache/reference/range-requests/).
