---
url: https://developers.cloudflare.com/changelog/post/2026-02-25-radar-aspa-insights/
title: RPKI ASPA Deployment Insights on Cloudflare Radar \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.236463+00:00
---

# RPKI ASPA Deployment Insights on Cloudflare Radar · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-25-radar-aspa-insights/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 25, 2026

## RPKI ASPA Deployment Insights on Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) now includes [Autonomous System Provider Authorization (ASPA) ↗︎](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/) deployment insights, providing visibility into the adoption and verification of ASPA objects across the global routing ecosystem.

#### New API endpoints

The new [`ASPA`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/) API provides the following endpoints:

  * [`/bgp/rpki/aspa/snapshot`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/snapshot/) \- Retrieves current or historical ASPA objects.
  * [`/bgp/rpki/aspa/changes`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/changes/) \- Retrieves changes to ASPA objects over time.
  * [`/bgp/rpki/aspa/timeseries`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/timeseries/) \- Retrieves ASPA object counts over time as a timeseries.



#### New Radar widgets

The [global routing page ↗︎](https://radar.cloudflare.com/routing) now shows the ASPA deployment trend over time by counting daily ASPA objects.

![Screenshot of the ASPA deployment trend chart](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=876,format=webp/_astro/aspa-global-trend.CXGWGFL4.png)

The global routing page also displays the most recent ASPA objects, searchable by ASN or AS name.

![Screenshot of the ASPA objects table](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1852,format=webp/_astro/aspa-global-table.vHUyNoTh.png)

On country and region routing pages, a new widget shows the ASPA deployment rate for ASNs registered in the selected country or region.

![Screenshot of the ASPA deployment trent chart for Germany](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=876,format=webp/_astro/aspa-germany-trend.DIH6CESC.png)

On AS routing pages, the connectivity table now includes checkmarks for ASPA-verified upstreams. All ASPA upstreams are listed in a dedicated table, and a timeline shows ASPA changes at daily granularity.

![Screenshot of the ASPA changes timeline on an AS routing page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2198,height=1212,format=webp/_astro/aspa-asn-timeline.Bnl6upJs.png)

Check out the [Radar routing page ↗︎](https://radar.cloudflare.com/routing) to explore the data.
