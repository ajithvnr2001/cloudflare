---
url: https://developers.cloudflare.com/changelog/post/2025-04-18-custom-fields-raw-transformed-values/
title: Custom fields raw and transformed values support \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:10.062506+00:00
---

# Custom fields raw and transformed values support · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-18-custom-fields-raw-transformed-values/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 18, 2025

## Custom fields raw and transformed values support

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-18-custom-fields-raw-transformed-values/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Custom Fields now support logging both **raw and transformed values** for request and response headers in the HTTP requests dataset.

These fields are configured per zone and apply to all Logpush jobs in that zone that include request headers, response headers. Each header can be logged in only one format—either raw or transformed—not both.

By default:

  * Request headers are logged as raw values
  * Response headers are logged as transformed values



These defaults can be overridden to suit your logging needs.

Note

Transformed and raw values for request and response headers are available **only via the API** and cannot be set through the UI.

For more information refer to [Custom fields](https://developers.cloudflare.com/logs/logpush/logpush-job/custom-fields/) documentation
