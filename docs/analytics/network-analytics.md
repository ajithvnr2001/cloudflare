---
url: https://developers.cloudflare.com/analytics/network-analytics/
title: Cloudflare Network Analytics \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:15.522432+00:00
---

# Cloudflare Network Analytics · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/network-analytics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /Network analytics



# Network analytics

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/network-analytics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRemarksRelated resources

Cloudflare Network Analytics (version 2) provides near real-time visibility into network and transport-layer traffic patterns and DDoS attacks. Network Analytics visualizes packet and bit-level data, the same data available via the Network Analytics dataset of the GraphQL Analytics API.

Requirements

Network Analytics requires the following:

  * A Cloudflare Enterprise plan.
  * Cloudflare Magic Transit or Spectrum.
  * Cloudflare WAN.



For a technical deep-dive into Network Analytics, refer to our [blog post ↗︎](https://blog.cloudflare.com/building-network-analytics-v2/).

## Remarks

  * The Network Analytics logs refer to IP traffic of Magic Transit customer prefixes/leased IP addresses or Spectrum applications. These logs are not directly associated with the [zones](https://developers.cloudflare.com/fundamentals/concepts/accounts-and-zones/#zones) in your Cloudflare account.

  * The data retention for Network Analytics is 16 weeks. Additionally, data older than eight weeks might have lower resolution when using narrow time frames.




## Related resources

  * [Cloudflare GraphQL API](https://developers.cloudflare.com/analytics/graphql-api/)
  * [Cloudflare Logpush](https://developers.cloudflare.com/logs/logpush/)
  * [Migrating from Network Analytics v1 to Network Analytics v2](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/)



[PreviousCustom dashboards](https://developers.cloudflare.com/analytics/custom-dashboards/)[NextGet started](https://developers.cloudflare.com/analytics/network-analytics/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/network-analytics/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
