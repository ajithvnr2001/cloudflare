---
url: https://developers.cloudflare.com/changelog/post/2026-10-09-http3-499-reporting-improvement/
title: Improved HTTP/3 client cancellation reporting \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T07:57:29.056847+00:00
---

# Improved HTTP/3 client cancellation reporting · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-09-http3-499-reporting-improvement/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 9, 2026

## Improved HTTP/3 client cancellation reporting

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has improved how it handles and reports client-cancelled HTTP/3 requests across Free, Pro, Business, and Enterprise plans. Customers now get a clearer view of client behavior in Cloudflare analytics and, where available, logs.

Previously, Cloudflare did not always stop an HTTP/3 request when the client cancelled its request stream. Some cancellations were already recorded as `499`, while others continued to the origin and showed the eventual upstream status.

Cloudflare now stops affected requests sooner, reducing unnecessary origin work, and records them as `499`. Customers may notice more `499` status codes for HTTP/3 traffic. This reflects more consistent reporting of existing cancellations, not an increase in failed requests.

Customers who use `499` status codes in availability calculations should consider excluding them from server-side error rates because they represent requests cancelled by clients.

For more information, refer to [Error 499](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-499/).
