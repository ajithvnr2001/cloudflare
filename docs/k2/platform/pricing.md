---
url: https://developers.cloudflare.com/k2/platform/pricing/
title: K2 - Pricing \u00b7 Cloudflare K2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:39.097781+00:00
---

# K2 - Pricing · Cloudflare K2 docs

> Source: https://developers.cloudflare.com/k2/platform/pricing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[K2](https://developers.cloudflare.com/k2/)
  3. /Platform
  4. /Pricing



# Pricing

Last updated Oct 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/k2/platform/pricing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewK2 pricing Data produced Data consumed Data retainedBilling examples Example: one consumer Example: fan-out to three consumersCloudflare billing policy

Pricing availability

K2 is in public beta and billing is not enabled at this time. We will provide at least 30 days notice before billing begins. Pricing may change and is shared in advance so that you can estimate what your costs will be once Cloudflare starts billing for usage.

K2 is available on the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/). K2 charges based on three dimensions:

  * **Data produced** : The volume of data written to streams.
  * **Data consumed** : The volume of data read from streams by consumers.
  * **Data retained** : The volume of data stored in streams.



All three dimensions are measured in uncompressed bytes: the size of your records before any compression, such as gzip compression of an HTTP request body.

## K2 pricing

| Workers Paid 1  
---|---  
**Data produced** | $0.04 / GB  
**Data consumed** | $0.04 / GB  
**Data retained** | $0.02 / GB / month  
  
### Data produced

Data produced is the volume of records written to a stream, through the [HTTP API or a Workers binding](https://developers.cloudflare.com/k2/features/produce/).

### Data consumed

Data consumed is the volume of records read from a stream through [subscriptions](https://developers.cloudflare.com/k2/features/consume/). Each subscription reads every record independently, so a stream with more subscriptions consumes more data.

### Data retained

Data retained is the volume of records stored in a stream, billed per GB per month. How much data a stream stores depends on how much you produce and on the stream's [retention period](https://developers.cloudflare.com/k2/configuration/#retention).

## Billing examples

### Example: one consumer

An application produces 100 GB of events per month to a stream. One subscription consumes every record, and the stream stores an average of 25 GB over the month.

Dimension | Usage | Rate | Cost  
---|---|---|---  
Data produced | 100 GB | $0.04 / GB | $4.00  
Data consumed | 100 GB | $0.04 / GB | $4.00  
Data retained | 25 GB | $0.02 / GB / month | $0.50  
**Total** |  |  | **$8.50**  
  
### Example: fan-out to three consumers

The same stream is read by three subscriptions, for example an alerting system, an archiver, and an analytics pipeline. Each subscription consumes every record.

Dimension | Usage | Rate | Cost  
---|---|---|---  
Data produced | 100 GB | $0.04 / GB | $4.00  
Data consumed | 300 GB (3 × 100 GB) | $0.04 / GB | $12.00  
Data retained | 25 GB | $0.02 / GB / month | $0.50  
**Total** |  |  | **$16.50**  
  
## Cloudflare billing policy

To learn more about how usage is billed, refer to [Cloudflare Billing Policy](https://developers.cloudflare.com/billing/understand/billing-policy/).

## Footnotes

  1. K2 both bills and measures usage based on a gigabyte   
(1 GB = 1,000,000,000 bytes) and not a gibibyte (GiB).   
↩




[PreviousConfiguration](https://developers.cloudflare.com/k2/configuration/)[NextLimits](https://developers.cloudflare.com/k2/platform/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/k2/platform/pricing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
