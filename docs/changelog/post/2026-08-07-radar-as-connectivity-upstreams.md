---
url: https://developers.cloudflare.com/changelog/post/2026-08-07-radar-as-connectivity-upstreams/
title: AS-level connectivity and upstream providers on Cloudflare Radar \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:07.209414+00:00
---

# AS-level connectivity and upstream providers on Cloudflare Radar · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-07-radar-as-connectivity-upstreams/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 7, 2026

## AS-level connectivity and upstream providers on Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-07-radar-as-connectivity-upstreams/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) expands its [Routing section ↗︎](https://radar.cloudflare.com/routing) with two widgets on AS pages, such as [AS13335 ↗︎](https://radar.cloudflare.com/routing/as13335), that describe how a network reaches the rest of the Internet: the paths it takes toward the [Tier-1 ↗︎](https://en.wikipedia.org/wiki/Tier_1_network) networks, and the mix of direct upstreams carrying its routes. Both are derived from [RouteViews ↗︎](https://www.routeviews.org/) RIB snapshots, unioned across selected collectors.

#### AS-level connectivity

The **AS-level connectivity** graph aggregates the BGP paths an AS uses to reach the Tier-1 networks, unioned across all the prefixes it announces, as observed by selected RouteViews collectors. It reads from left to right, starting at the queried AS and ending at the Tier-1 networks, and each node is labeled with its AS number, country, and organization name. Tier-1 nodes are marked so they stand apart from the intermediate networks that lead to them.

By default, the graph shows the network's direct connections to Tier-1 networks plus the indirect paths, which keeps the view readable. A **Show full paths** toggle expands it to every observed path, including transit through Tier-1 networks the AS already connects to. An IP version selector switches between IPv4 and IPv6, because the paths reaching Tier-1 networks may differ between the two address families.

![AS-level connectivity graph for AS13335, showing Tier-1 networks it reaches directly alongside paths that reach others through intermediate networks](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1526,format=webp/_astro/as-level-connectivity-graph.DGv8lrUx.png)

This is the AS-level counterpart to the **Real-time connectivity** graph on prefix pages, such as the one for [1.1.1.0/24 ↗︎](https://radar.cloudflare.com/routing/prefix/1.1.1.0/24). Instead of covering a single prefix, it covers the union of paths for all prefixes an AS announces, which makes it a fast way to read a network's transit hierarchy: which providers it depends on, how many hops separate it from the core, and whether its paths to the core are diverse or concentrated. For more information on the prefix-level graph, refer to [BGP real-time routes](https://developers.cloudflare.com/radar/glossary/#bgp-real-time-routes).

#### Upstream providers

The **Upstream providers** widget tracks the share of an AS's observed paths carried by each of its direct upstream networks over time, drawn as a stacked area chart. Up to 10 upstreams appear as their own series and the remaining ones are grouped into **Other**. Transit changes such as adding a provider, dropping one, or moving traffic between them appear as movement between bands rather than as a single aggregate number. As with the connectivity graph, an IP version selector switches between IPv4 and IPv6.

![Stacked area chart of the share of AS13335's observed paths carried by each of its top 10 direct upstreams, with the remainder grouped into Other](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=976,format=webp/_astro/as-upstream-providers-timeseries.BUc6CJaT.png)

#### API endpoints

The data behind both widgets is also available through two new endpoints on the [`BGP`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/) API:

  * [`/bgp/routes/paths/{asn}`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/subresources/paths/methods/list/) — Returns the ordered AS path segments an AS uses to reach the Tier-1 networks, each with its observed path count, peer count, and contributing collectors, alongside the name and country of every ASN in the response. Pass `collector` to scope the result to a single RouteViews collector.
  * [`/bgp/routes/upstreams/{asn}/timeseries`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/subresources/upstreams/methods/timeseries/) — Returns the share of an AS's observed paths carried by each direct upstream over time. Use `limit` to control how many upstreams come back as separate series before the rest are grouped into an `OTHER` series, and `ipVersion` to select the address family.



Visit the [AS13335 routing page ↗︎](https://radar.cloudflare.com/routing/as13335) to explore both widgets, or swap in any other AS number.
