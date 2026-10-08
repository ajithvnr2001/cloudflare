---
url: https://developers.cloudflare.com/analytics/network-analytics/understand/concepts/
title: Network Analytics concepts \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:16.305034+00:00
---

# Network Analytics concepts · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/network-analytics/understand/concepts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[Network analytics](https://developers.cloudflare.com/analytics/network-analytics/)

  4. /About
  5. /Concepts



# Concepts

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/network-analytics/understand/concepts/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdaptive Bit Rate samplingEdge Sample Enrichment

## Adaptive Bit Rate sampling

With Adaptive Bit Rate (ABR) sampling, every analytics query that supports ABR will be calculated at a resolution matching the query. Depending on the size of your query, the ABR mechanism will choose the best sampling rate and fetch a response from one of the sample tables encapsulated behind each [Network Analytics node](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/). The cardinality and accuracy are preserved even for historical data.

For more background information on Adaptive Bit Rate sampling, refer to the [Explaining Cloudflare's ABR Analytics ↗︎](https://blog.cloudflare.com/explaining-cloudflares-abr-analytics/) blog post.

## Edge Sample Enrichment

Network Analytics can provide accurate data due to the sample rate and to Edge Sample Enrichment.

Sample rates vary depending on the mitigation service. For example:

  * The sample rate for `dosd` changes dynamically from 1/100 to 1/10,000 packets based on the volume of packets.
  * The sample rate for Network Firewall events changes dynamically from 1/100 to 1/1,000,000 packets based on the number of packets.
  * The sample rate for `flowtrackd` is 1/10,000 packets.



NA uses a data logging pipeline that relies on Edge Sample Enrichment. By delegating the packet sample enrichment and cross-referencing to the global data centers, the data pipeline’s resilience and tolerance against congestion are improved. Using this method, enriched packet samples are immediately stored in Cloudflare's core data centers as soon as they arrive.

[PreviousGet started](https://developers.cloudflare.com/analytics/network-analytics/get-started/)[NextMain dashboard](https://developers.cloudflare.com/analytics/network-analytics/understand/main-dashboard/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/network-analytics/understand/concepts.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
