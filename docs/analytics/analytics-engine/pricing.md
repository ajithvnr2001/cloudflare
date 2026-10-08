---
url: https://developers.cloudflare.com/analytics/analytics-engine/pricing/
title: Workers Analytics Engine \u2014\u00a0Pricing \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:09.545650+00:00
---

# Workers Analytics Engine — Pricing · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/analytics-engine/pricing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)
  4. /Pricing



# Pricing

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/analytics-engine/pricing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Data points written Read queries

Workers Analytics Engine is priced based on two metrics — data points written, and read queries.

Plan | Data points written | Read queries  
---|---|---  
**Workers Paid** | 10 million included per month   
(+$0.25 per additional million) | 1 million included per month (+$1.00 per additional million)  
**Workers Free** | 100,000 included per day | 10,000 included per day  
  
Pricing availability

Currently, you will not be billed for your use of Workers Analytics Engine. Pricing information here is shared in advance, so that you can estimate what your costs will be once Cloudflare starts billing for usage in the coming months.

If you are an Enterprise customer, contact your account team for information about Workers Analytics Engine pricing and billing.

### Data points written

Every time you call [`writeDataPoint()`](https://developers.cloudflare.com/analytics/analytics-engine/get-started/#2-write-data-points-from-your-worker) in a Worker, this counts as one data point written.

Each data point written costs the same amount. There is no extra cost to add dimensions or cardinality, and no additional cost for writing more data in a single data point.

### Read queries

Every time you post to Workers Analytics Engine's [SQL API](https://developers.cloudflare.com/analytics/analytics-engine/sql-api/), this counts as one read query.

Each read query costs the same amount. There is no extra cost for more or less complex queries, and no extra cost for reading only a few rows of data versus many rows of data.

[PreviousSampling with WAE](https://developers.cloudflare.com/analytics/analytics-engine/sampling/)[NextLimits](https://developers.cloudflare.com/analytics/analytics-engine/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/analytics-engine/pricing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
