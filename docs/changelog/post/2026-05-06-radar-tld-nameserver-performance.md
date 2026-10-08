---
url: https://developers.cloudflare.com/changelog/post/2026-05-06-radar-tld-nameserver-performance/
title: TLD Nameserver Performance in Cloudflare Radar \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:51.662819+00:00
---

# TLD Nameserver Performance in Cloudflare Radar · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-06-radar-tld-nameserver-performance/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 6, 2026

## TLD Nameserver Performance in Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-06-radar-tld-nameserver-performance/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) now provides TLD authoritative nameserver performance insights, measuring response time (latency) as observed from Cloudflare's [1.1.1.1](https://developers.cloudflare.com/1.1.1.1/) resolver infrastructure when forwarding queries upstream to TLD nameservers.

New widgets on [TLD detail pages ↗︎](https://radar.cloudflare.com/tlds/com):

  * [**Aggregate nameserver latency** ↗︎](https://radar.cloudflare.com/tlds/com#tld-ns-latency): Response time percentiles (p25/p50/p75) for all authoritative nameservers of the selected TLD.
  * [**Latency per nameserver** ↗︎](https://radar.cloudflare.com/tlds/com#tld-ns-latency-by-ns): Median response time (p50) broken down by each authoritative nameserver over time.

![Latency per nameserver chart](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1268,format=webp/_astro/tld-nameserver-latency-by-ns.CZGT23Vk.png)

  * [**Median latency geographic distribution** ↗︎](https://radar.cloudflare.com/tlds/com#geographical-distribution): p50 response time by Cloudflare data center country, displayed on a choropleth map.
  * [**TLD ranking over time** ↗︎](https://radar.cloudflare.com/tlds/com#tld-ranking): Daily DNS magnitude rank and magnitude value with a Rank/Magnitude toggle.
  * [**Rank change deltas** ↗︎](https://radar.cloudflare.com/tlds): 1 week, 4 weeks, and 3 months rank changes added to the TLD magnitude table and the TLD detail info panel.

![TLD Rankings by DNS Magnitude table with rank change deltas](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2642,height=1446,format=webp/_astro/tld-magnitude-rank-deltas.BaT-jII_.webp)

The new [`TLD Performance`](https://developers.cloudflare.com/api/resources/radar/subresources/tlds/subresources/performance/) API provides the following endpoints:

  * [`/tlds/performance/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/tlds/subresources/performance/methods/summary/) — TLD nameserver performance summarized by dimension.
  * [`/tlds/performance/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/tlds/subresources/performance/methods/timeseries_groups/) — TLD nameserver performance over time grouped by dimension.



Available dimensions: `LATENCY` (aggregate p25/p50/p75), `NAMESERVER_LATENCY` (per-nameserver p50), `LOCATION_LATENCY` (per-data-center-country p50).

TLD Performance is also available as a dataset in the [Data Explorer ↗︎](https://radar.cloudflare.com/explorer?dataSet=tlds.performance).

Check out the updated [TLD detail page ↗︎](https://radar.cloudflare.com/tlds/com).
