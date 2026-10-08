---
url: https://developers.cloudflare.com/changelog/post/2025-09-03-log-headers-and-cookies/
title: Logging headers and cookies using custom fields \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:21.570055+00:00
---

# Logging headers and cookies using custom fields · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-03-log-headers-and-cookies/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 3, 2025

## Logging headers and cookies using custom fields

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-03-log-headers-and-cookies/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/) now supports logging and filtering on header or cookie fields in the [`http_requests` dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/).

Create a custom field to log desired header or cookie values into the `http_requests` dataset and Log Explorer will import these as searchable fields. Once configured, use the custom SQL editor in Log Explorer to view or filter on these requests.

![Edit Custom fields](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1790,height=404,format=webp/_astro/edit-custom-fields.Cy4qXSpL.png)

For more details, refer to [Headers and cookies](https://developers.cloudflare.com/log-explorer/log-search/#headers-and-cookies).
