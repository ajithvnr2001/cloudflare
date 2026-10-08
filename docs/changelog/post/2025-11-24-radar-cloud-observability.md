---
url: https://developers.cloudflare.com/changelog/post/2025-11-24-radar-cloud-observability/
title: Cloud Services Observability in Cloudflare Radar \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:30.202292+00:00
---

# Cloud Services Observability in Cloudflare Radar · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-24-radar-cloud-observability/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 24, 2025

## Cloud Services Observability in Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-24-radar-cloud-observability/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) introduces HTTP Origins insights, providing visibility into the status of traffic between Cloudflare's global network and cloud-based origin infrastructure.

The new [`Origins`](https://developers.cloudflare.com/api/resources/radar/subresources/origins/) API provides provides the following endpoints:

  * [`/origins`](https://developers.cloudflare.com/api/resources/radar/subresources/origins/methods/list/) \- Lists all origins (cloud providers and associated regions).
  * [`/origins/{origin}`](https://developers.cloudflare.com/api/resources/radar/subresources/origins/methods/get/) \- Retrieves information about a specific origin (cloud provider).
  * [`/origins/timeseries`](https://developers.cloudflare.com/api/resources/radar/subresources/origins/methods/timeseries/) \- Retrieves normalized time series data for a specific origin, including the following metrics: 
    * `REQUESTS`: Number of requests
    * `CONNECTION_FAILURES`: Number of connection failures
    * `RESPONSE_HEADER_RECEIVE_DURATION`: Duration of the response header receive
    * `TCP_HANDSHAKE_DURATION`: Duration of the TCP handshake
    * `TCP_RTT`: TCP round trip time
    * `TLS_HANDSHAKE_DURATION`: Duration of the TLS handshake
  * [`/origins/summary`](https://developers.cloudflare.com/api/resources/radar/subresources/origins/methods/summary/) \- Retrieves HTTP requests to origins summarized by a dimension.
  * [`/origins/timeseries_groups`](https://developers.cloudflare.com/api/resources/radar/subresources/origins/methods/timeseries_groups/) \- Retrieves timeseries data for HTTP requests to origins grouped by a dimension.



The following dimensions are available for the `summary` and `timeseries_groups` endpoints:

  * `region`: Origin region
  * `success_rate`: Success rate of requests (2XX versus 5XX response codes)
  * `percentile`: Percentiles of metrics listed above



Additionally, the [`Annotations`](https://developers.cloudflare.com/api/resources/radar/subresources/annotations/) and [`Traffic Anomalies`](https://developers.cloudflare.com/api/resources/radar/subresources/traffic_anomalies/) APIs have been extended to support origin outages and anomalies, enabling automated detection and alerting for origin infrastructure issues.

![Screenshot of the cloud service status heatmap](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=970,format=webp/_astro/cloud-service-status.DoGHSNmz.png)

Check out the [new Radar page ↗︎](https://radar.cloudflare.com/cloud-observatory).
