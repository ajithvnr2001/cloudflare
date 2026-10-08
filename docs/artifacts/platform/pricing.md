---
url: https://developers.cloudflare.com/artifacts/platform/pricing/
title: Pricing \u00b7 Cloudflare Artifacts docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:21.996646+00:00
---

# Pricing · Cloudflare Artifacts docs

> Source: https://developers.cloudflare.com/artifacts/platform/pricing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Artifacts](https://developers.cloudflare.com/artifacts/)
  3. /Platform
  4. /Pricing



# Pricing

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/artifacts/platform/pricing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewArtifacts pricingStorage usage

Artifacts is currently only available on the Workers Paid plan.

Note

Cloudflare will begin billing for Artifacts operations and storage on October 14, 2026.

Artifacts pricing is billed on two dimensions:

  * **Operations** : the number of repo operations, such as `create`, `push`, `pull`, and `clone`.
  * **Storage** : the total amount of stored data, measured in gigabyte-months (`GB-mo`).



## Artifacts pricing

Unit | Workers Free | Workers Paid  
---|---|---  
Operations (1,000 operations) | Unavailable | First 10,000 per month + $0.15 per additional 1,000 operations  
Storage (GB-mo) | Unavailable | First 1 GB per month + $0.50 per additional GB-mo  
  
## Storage usage

Storage is billed using gigabyte-month (`GB-mo`) as the billing metric, identical to [Durable Objects SQL storage](https://developers.cloudflare.com/durable-objects/platform/pricing/#sqlite-storage-backend). A `GB-mo` is calculated by averaging peak storage per day over a 30-day billing period.

  * Storage is calculated across all repositories.
  * Replicas do not add storage charges. Storage is replicated by default, and you do not need to manage repository availability or uptime.
  * Repos remain stored until you explicitly delete them.



[PreviousSandbox SDK + Artifacts](https://developers.cloudflare.com/artifacts/examples/sandbox-sdk-artifacts/)[NextLimits](https://developers.cloudflare.com/artifacts/platform/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/artifacts/platform/pricing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
