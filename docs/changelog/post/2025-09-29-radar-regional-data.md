---
url: https://developers.cloudflare.com/changelog/post/2025-09-29-radar-regional-data/
title: Regional Data in Cloudflare Radar \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:24.815109+00:00
---

# Regional Data in Cloudflare Radar · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-29-radar-regional-data/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 29, 2025

## Regional Data in Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-29-radar-regional-data/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) now introduces Regional Data, providing traffic insights that bring a more localized perspective to the traffic trends shown on Radar.

The following API endpoints are now available:

  * [`Get Geolocation`](https://developers.cloudflare.com/api/resources/radar/subresources/geolocations/methods/get/) \- Retrieves geolocation by `geoId`.
  * [`List Geolocations`](https://developers.cloudflare.com/api/resources/radar/subresources/geolocations/methods/list/) \- Lists geolocations.
  * [`NetFlows Summary By Dimension`](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/methods/summary_v2/) \- Retrieves NetFlows summary by dimension.



All `summary` and `timeseries_groups` endpoints in [`HTTP`](https://developers.cloudflare.com/api/resources/radar/subresources/http/) and [`NetFlows`](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/) now include an `adm1` dimension for grouping data by first level administrative division (for example, state, province, etc.)

A new filter `geoId` was also added to all endpoints in [`HTTP`](https://developers.cloudflare.com/api/resources/radar/subresources/http/) and [`NetFlows`](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/), allowing filtering by a specific administrative division.

Check out the new Regional traffic insights on a country specific traffic page [new Radar page ↗︎](https://radar.cloudflare.com/traffic/pt).
