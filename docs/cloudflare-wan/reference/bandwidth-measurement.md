---
url: https://developers.cloudflare.com/cloudflare-wan/reference/bandwidth-measurement/
title: Bandwidth measurement \u00b7 Cloudflare WAN docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:30.867360+00:00
---

# Bandwidth measurement · Cloudflare WAN docs

> Source: https://developers.cloudflare.com/cloudflare-wan/reference/bandwidth-measurement/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)
  3. /Reference
  4. /Bandwidth measurement



# Bandwidth measurement

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-wan/reference/bandwidth-measurement/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow bandwidth is measured95th percentile calculation

Cloudflare measures Cloudflare WAN (formerly Magic WAN) usage based on the 95th percentile of bandwidth utilized by your configured network. This measurement reflects your overall network capacity consumption.

## How bandwidth is measured

Cloudflare WAN bandwidth includes the sum of traffic routed to and from the Cloudflare WAN network namespace across all your connections. This measurement includes traffic from the following tunnel types:

  * [GRE (Generic Routing Encapsulation) ↗︎](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)
  * [IPsec (Internet Protocol Security) ↗︎](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)
  * [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-wan/zero-trust/cloudflare-tunnel/)
  * [Cloudflare Network Interconnect](https://developers.cloudflare.com/network-interconnect/)



For each tunnel, Cloudflare uses the highest 95th percentile value (ingress or egress traffic). The usage measurement excludes [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) traffic.

## 95th percentile calculation

The 95th percentile method is an industry-standard approach to bandwidth measurement that accounts for short traffic spikes. By discarding the highest 5% of samples, the measurement reflects your sustained bandwidth usage rather than momentary peaks.

To calculate the 95th percentile, Cloudflare records bandwidth to and from the global network at five-minute intervals, sorts these measurements in descending order, and discards the top 5% of recorded measurements. The highest remaining value is the 95th percentile bandwidth measurement for that time period.

[PreviousAnti-replay protection](https://developers.cloudflare.com/cloudflare-wan/reference/anti-replay-protection/)[NextDevice compatibility](https://developers.cloudflare.com/cloudflare-wan/reference/device-compatibility/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-wan/reference/bandwidth-measurement.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
