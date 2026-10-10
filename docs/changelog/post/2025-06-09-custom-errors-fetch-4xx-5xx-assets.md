---
url: https://developers.cloudflare.com/changelog/post/2025-06-09-custom-errors-fetch-4xx-5xx-assets/
title: More flexible fallback handling \u2014 Custom Errors now support fetching assets returned with 4xx or 5xx status codes \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:51.969214+00:00
---

# More flexible fallback handling — Custom Errors now support fetching assets returned with 4xx or 5xx status codes · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-09-custom-errors-fetch-4xx-5xx-assets/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 9, 2025

## More flexible fallback handling — Custom Errors now support fetching assets returned with 4xx or 5xx status codes

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Custom Errors](https://developers.cloudflare.com/rules/custom-errors/) can now fetch and store [assets](https://developers.cloudflare.com/rules/custom-errors/create-rules/#create-a-custom-error-asset-dashboard) and [error pages](https://developers.cloudflare.com/rules/custom-errors/#error-pages) from your origin even if they are served with a 4xx or 5xx HTTP status code — previously, only 200 OK responses were allowed.

**What’s new:**

  * You can now upload error pages and error assets that return error status codes (for example, 403, 500, 502, 503, 504) when fetched.
  * These assets are stored and minified at the edge, so they can be reused across multiple Custom Error rules without triggering requests to the origin.



This is especially useful for retrieving error content or downtime banners from your backend when you can’t override the origin status code.

Learn more in the [Custom Errors](https://developers.cloudflare.com/rules/custom-errors/) documentation.
