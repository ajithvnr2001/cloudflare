---
url: https://developers.cloudflare.com/basin-pipelines/platform/pricing/
title: Basin Pipelines - Pricing \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:25.263893+00:00
---

# Basin Pipelines - Pricing · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/platform/pricing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /Platform
  4. /Pricing



# Pricing

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/platform/pricing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBasin Pipelines pricing Streams SQL transforms SinksBilling examples Example: filtered ingest to Iceberg with SQLCloudflare billing policy

Basin Pipelines charges based on two dimensions:

  1. **SQL transforms** : The volume of data processed by stateless SQL.
  2. **Sinks** : The volume of data delivered to each sink destination.



Ingress into a Pipeline stream is free. Standard [R2 storage and operations](https://developers.cloudflare.com/r2/pricing/) charges apply for data written to R2 buckets. [Basin Catalog](https://developers.cloudflare.com/basin-catalog/platform/pricing/) charges apply when writing to Iceberg tables.

All included usage is on a monthly basis.

## Basin Pipelines pricing

| Workers Paid  
---|---  
**Streams (ingress)** |   
Included | Unlimited  
**SQL transforms** |   
Included | 50 GB / month  
Additional | $0.04 / GB  
**Sinks (egress)** 1 |   
Included | 50 GB / month  
R2 — JSON format | $0.03 / GB  
R2 — Parquet / Iceberg | $0.06 / GB  
  
### Streams

Streams provide durable, distributed log storage that buffers incoming messages. Ingress into a stream is free regardless of volume. A single stream can be read by multiple pipelines.

### SQL transforms

SQL transforms let you filter, reshape, and compute over data before it reaches a sink. Any query currently counts as a transform.

Pricing covers stateless transforms (for example, filter, reshape, unnest, cast, and compute). Future stateful operations such as aggregations, joins, and windows may be priced separately.

### Sinks

Sink pricing is based on the volume of uncompressed data delivered to the destination. The rate varies by output format:

  * **JSON** : $0.03 / GB — lowest compute cost, suitable for simple log forwarding.
  * **Parquet / Iceberg** : $0.06 / GB — higher compute cost for columnar encoding and Iceberg table management. Best for analytics workloads.



## Billing examples

### Example: filtered ingest to Iceberg with SQL

A pipeline ingests 500 GB of event data per month. A SQL transform filters and reshapes the data, reducing output to 300 GB written to a Basin Catalog Iceberg table.

Dimension | Usage | Included | Billable | Cost  
---|---|---|---|---  
Streams | 500 GB | Unlimited | 0 GB | $0.00  
SQL transforms | 500 GB | 50 GB | 450 GB | $18.00  
Sinks (Iceberg) | 300 GB | 50 GB | 250 GB | $15.00  
**Total** |  |  |  | **$33.00**  
  
## Cloudflare billing policy

To learn more about how usage is billed, refer to [Cloudflare Billing Policy](https://developers.cloudflare.com/billing/understand/billing-policy/).

## Footnotes

  1. Sink egress is measured on uncompressed data. ↩




[PreviousMetrics and analytics](https://developers.cloudflare.com/basin-pipelines/observability/metrics/)[NextLimits](https://developers.cloudflare.com/basin-pipelines/platform/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/platform/pricing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
