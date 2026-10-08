---
url: https://developers.cloudflare.com/data-localization/metadata-boundary/out-of-region-access/
title: Out of region access \u00b7 Cloudflare Data Localization Suite docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:43.642607+00:00
---

# Out of region access · Cloudflare Data Localization Suite docs

> Source: https://developers.cloudflare.com/data-localization/metadata-boundary/out-of-region-access/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Data Localization Suite](https://developers.cloudflare.com/data-localization/)
  3. /[Customer Metadata Boundary](https://developers.cloudflare.com/data-localization/metadata-boundary/)
  4. /Out of region access



# Out of region access

Last updated May 7, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/data-localization/metadata-boundary/out-of-region-access/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

With the default configuration for Customer Metadata Boundary, users who are physically located outside the configured storage region will not have access to view analytics on the dashboard or retrieve data through the standard API endpoint. When **Allow out-of-region access** is enabled, Customer Logs will still be stored exclusively within the configured region but will be made available to authorized users on your account regardless of their physical location.

This is useful when your operations, security, or engineering teams are distributed across multiple regions and need visibility into traffic analytics without relocating the underlying data.

For example, when **Allow out-of-region access** is **disabled** on an account configured for Customer Metadata Boundary in the US, users in Europe will not be able to see any analytics or Customer Logs on the dashboard.

When **Allow out-of-region access** is enabled on an account configured for Customer Metadata Boundary in the US, users in both Europe and the US will be able to see analytics on the dashboard even though the Customer Logs are stored exclusively in the US.

[PreviousLogpush datasets](https://developers.cloudflare.com/data-localization/metadata-boundary/logpush-datasets/)[NextFAQs](https://developers.cloudflare.com/data-localization/metadata-boundary/faq/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/data-localization/metadata-boundary/out-of-region-access.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
