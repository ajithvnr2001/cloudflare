---
url: https://developers.cloudflare.com/changelog/post/2026-08-03-pipelines-billing-enabled/
title: Billing is now enabled for Pipelines \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:06.313602+00:00
---

# Billing is now enabled for Pipelines · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-03-pipelines-billing-enabled/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 3, 2026

## Billing is now enabled for Pipelines

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-03-pipelines-billing-enabled/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Billing is now enabled for [Cloudflare Pipelines](https://developers.cloudflare.com/basin-pipelines/) on non-enterprise accounts. Pipelines usage beyond the included free tier will appear on your next invoice.

Pipelines charges based on two usage dimensions. Ingress into a Pipeline stream remains free regardless of volume:

  * **SQL transforms** : $0.04 / GB for stateless transforms (filter, reshape, unnest, cast, compute).
  * **Sinks (egress)** : $0.03 / GB for JSON output, $0.06 / GB for Parquet or Iceberg output.



Workers Paid plans include 50 GB / month for both SQL transforms and sinks. Standard [R2 storage and operations](https://developers.cloudflare.com/r2/pricing/) charges apply for data written to R2 buckets, and [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/platform/pricing/) charges apply when writing to Iceberg tables.

For example, a pipeline that ingests 500 GB of event data per month, uses a SQL transform to filter and reshape it, and writes 300 GB to an R2 Data Catalog Iceberg table would be billed as follows:

Dimension | Usage | Included | Billable | Cost  
---|---|---|---|---  
Streams | 500 GB | Unlimited | 0 GB | $0.00  
SQL transforms | 500 GB | 50 GB | 450 GB | $18.00  
Sinks (Iceberg) | 300 GB | 50 GB | 250 GB | $15.00  
**Total** |  |  |  | **$33.00**  
  
For full pricing details and billing examples, refer to [Pipelines pricing](https://developers.cloudflare.com/basin-pipelines/platform/pricing/).
