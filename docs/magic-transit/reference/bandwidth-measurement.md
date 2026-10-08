---
url: https://developers.cloudflare.com/magic-transit/reference/bandwidth-measurement/
title: Bandwidth measurement \u00b7 Cloudflare Magic Transit docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:19.499160+00:00
---

# Bandwidth measurement · Cloudflare Magic Transit docs

> Source: https://developers.cloudflare.com/magic-transit/reference/bandwidth-measurement/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Magic Transit](https://developers.cloudflare.com/magic-transit/)
  3. /Reference
  4. /Bandwidth measurement



# Bandwidth measurement

Last updated Sep 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/magic-transit/reference/bandwidth-measurement/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBandwidth limits and overagesCloudflare-originated traffic

Cloudflare measures Magic Transit usage based on the 95th percentile of clean bandwidth for your network. "Clean bandwidth" refers to the egress traffic Cloudflare routes to your network after applying all Distributed Denial of Service ([DDoS](https://developers.cloudflare.com/ddos-protection/)) mitigation and firewall functions. The usage measurement explicitly excludes attack traffic we block at our global network.

To measure 95th percentile bandwidth, Cloudflare records clean bandwidth leaving our global network at five-minute intervals, sorts these measurements in descending order, and discards the top 5% of measurements it recorded. The highest remaining value constitutes the 95th percentile bandwidth measurement for that time period.

## Bandwidth limits and overages

Magic Transit contracts may include a subscribed bandwidth amount, but this is a billing metric, not a technical limitation. Cloudflare does not restrict, throttle, or drop traffic when your usage exceeds your contracted bandwidth. Instead, overage charges apply according to your contract terms.

If you want to discuss adjusting your subscribed bandwidth or contract terms, contact your Cloudflare account team.

## Cloudflare-originated traffic

Clean bandwidth includes all egress traffic Cloudflare routes to your network through Magic Transit tunnels and interconnects. This includes traffic that originated from the public Internet, as well as response traffic from services within the Cloudflare network (such as Cloudflare CDN) destined to your servers.

For example, if you have onboarded `10.0.0.0/20` to Magic Transit and are advertising it from the Cloudflare edge, but have also advertised a more specific `10.0.1.0/24` via your ISP, the following applies:

  * **Internet traffic** to `10.0.1.0/24` reaches you via your ISP because the global Internet routing table uses Longest Prefix Match.
  * **Cloudflare-originated traffic** to `10.0.1.0/24` is routed through your Magic Transit tunnels and interconnects because Cloudflare keeps that traffic inside its own network when the covering /20 prefix is advertised from Cloudflare. This traffic counts toward your bandwidth usage.



**To avoid this:** If you do not want Cloudflare-originated traffic flowing through your Magic Transit tunnel, withdraw the covering prefix from Cloudflare. The traffic will then egress to the Internet and follow standard Internet routing (including your more specific ISP routes).

[PreviousAnti-replay protection](https://developers.cloudflare.com/magic-transit/reference/anti-replay-protection/)[NextEgress traffic](https://developers.cloudflare.com/magic-transit/reference/egress/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/magic-transit/reference/bandwidth-measurement.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
