---
url: https://developers.cloudflare.com/analytics/analytics-engine/limits/
title: Workers Analytics Engine \u2014\u00a0Limits \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:09.476035+00:00
---

# Workers Analytics Engine — Limits · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/analytics-engine/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)
  4. /Limits



# Limits

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/analytics-engine/limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewData retention

The following limits apply to Workers Analytics Engine:

  * Analytics Engine will accept up to twenty blobs, twenty doubles, and one index per call to `writeDataPoint`.
  * The total size of all blobs in a request must not exceed **16 KB**. The 16 KB size limit for the blobs field applies to **each individual data point** , regardless of how many are included in a single request using writeDataPoints().
  * Each index must not be more than 96 bytes.
  * You can write a maximum of 250 data points per Worker invocation (client HTTP request). Each call to `writeDataPoint` counts towards this limit.



## Data retention

Data written to Workers Analytics Engine is stored for three months.

Interested in longer retention periods? Join the `#analytics-engine` channel in the [Cloudflare Developers Discord ↗︎](https://discord.cloudflare.com/) and tell us more about what you are building.

[PreviousPricing](https://developers.cloudflare.com/analytics/analytics-engine/pricing/)[NextOverview](https://developers.cloudflare.com/analytics/sql-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/analytics-engine/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
