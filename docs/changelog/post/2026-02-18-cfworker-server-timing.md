---
url: https://developers.cloudflare.com/changelog/post/2026-02-18-cfworker-server-timing/
title: New cfWorker metric in Server-Timing header \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:37.705005+00:00
---

# New cfWorker metric in Server-Timing header · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-18-cfworker-server-timing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 18, 2026

## New cfWorker metric in Server-Timing header

[Analytics](https://developers.cloudflare.com/analytics/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-18-cfworker-server-timing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Server-Timing header now includes a new `cfWorker` metric that measures time spent executing Cloudflare Workers, including any subrequests performed by the Worker. This helps developers accurately identify whether high Time to First Byte (TTFB) is caused by Worker processing or slow upstream dependencies.

Previously, Worker execution time was included in the `edge` metric, making it harder to identify true edge performance. The new `cfWorker` metric provides this visibility:

Metric | Description  
---|---  
`edge` | Total time spent on the Cloudflare edge, including Worker execution  
`origin` | Time spent fetching from the origin server  
`cfWorker` | Time spent in Worker execution, including subrequests but excluding origin fetch time  
  
#### Example response
    
    
    Server-Timing: cdn-cache; desc=DYNAMIC, edge; dur=20, origin; dur=100, cfWorker; dur=7

In this example, the edge took 20ms, the origin took 100ms, and the Worker added just 7ms of processing time.

#### Availability

The `cfWorker` metric is enabled by default if you have [Real User Monitoring (RUM)](https://developers.cloudflare.com/web-analytics/) enabled. Otherwise, you can enable it using [Rules](https://developers.cloudflare.com/rules/).

This metric is particularly useful for:

  * **Performance debugging** : Quickly determine if latency is caused by Worker code, external API calls within Workers, or slow origins.
  * **Optimization targeting** : Identify which component of your request path needs optimization.
  * **Real User Monitoring (RUM)** : Access detailed timing breakdowns directly from response headers for client-side analytics.



For more information about Server-Timing headers, refer to the [W3C Server Timing specification ↗︎](https://www.w3.org/TR/server-timing/).
