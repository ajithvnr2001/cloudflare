---
url: https://developers.cloudflare.com/hyperdrive/platform/pricing/
title: Pricing \u00b7 Cloudflare Hyperdrive docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:33.304475+00:00
---

# Pricing · Cloudflare Hyperdrive docs

> Source: https://developers.cloudflare.com/hyperdrive/platform/pricing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)
  3. /Platform
  4. /Pricing



# Pricing

Last updated Jun 18, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/hyperdrive/platform/pricing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPlanetScale Postgres & MySQLPricing FAQ Does connection pooling or query caching incur additional charges? Are cached queries counted the same as uncached queries? Does Hyperdrive charge for data transfer / egress?

Hyperdrive is included in both the Free and Paid [Workers plans](https://developers.cloudflare.com/workers/platform/pricing/).

| Free plan1 | Paid plan  
---|---|---  
Database queries2 | 100,000 / day | Unlimited  
  
Footnotes

1: The Workers Free plan includes limited Hyperdrive usage. All limits reset daily at 00:00 UTC. If you exceed any one of these limits, further operations of that type will fail with an error.

2: Database queries refers to any database statement made via Hyperdrive, whether a query (`SELECT`), a modification (`INSERT`,`UPDATE`, or `DELETE`) or a schema change (`CREATE`, `ALTER`, `DROP`).

## Footnotes

  1. The Workers Free plan includes limited Hyperdrive usage. All limits reset daily at 00:00 UTC. If you exceed any one of these limits, further operations of that type will fail with an error. ↩

  2. Database queries refers to any database statement made via Hyperdrive, whether a query (`SELECT`), a modification (`INSERT`,`UPDATE`, or `DELETE`) or a schema change (`CREATE`, `ALTER`, `DROP`). ↩




Hyperdrive limits are automatically adjusted when subscribed to a Workers Paid plan. Hyperdrive's [connection pooling and query caching](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/) are included in Workers Paid plan, so do not incur any additional charges.

## PlanetScale Postgres & MySQL

You can create PlanetScale Postgres and MySQL databases from Cloudflare and bill PlanetScale database usage through your Cloudflare account as a pay-as-you-go customer.

PlanetScale database usage is separate from Hyperdrive usage. When you create a PlanetScale database from the Cloudflare dashboard, PlanetScale usage appears on your Cloudflare invoice each billing period as a dollar total at PlanetScale's standard [pricing ↗︎](https://planetscale.com/pricing).

You can view per-database billing usage in the [PlanetScale dashboard ↗︎](https://planetscale.com/docs/billing#organization-usage-and-billing-page). To learn how PlanetScale databases work with Workers and Hyperdrive, refer to [PlanetScale Postgres and MySQL with Hyperdrive](https://developers.cloudflare.com/hyperdrive/planetscale/).

## Pricing FAQ

### Does connection pooling or query caching incur additional charges?

No. Hyperdrive's built-in cache and connection pooling are included within the stated plans above. There are no hidden limits other than those [published](https://developers.cloudflare.com/hyperdrive/platform/limits/).

### Are cached queries counted the same as uncached queries?

Yes, any query made through Hyperdrive, whether cached or uncached, whether query or mutation, is counted according to the limits above.

### Does Hyperdrive charge for data transfer / egress?

No.

Note

For questions about pricing, refer to the [pricing FAQs](https://developers.cloudflare.com/hyperdrive/reference/faq/#pricing).

[PreviousDemos and architectures](https://developers.cloudflare.com/hyperdrive/demos/)[NextLimits](https://developers.cloudflare.com/hyperdrive/platform/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/hyperdrive/platform/pricing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
