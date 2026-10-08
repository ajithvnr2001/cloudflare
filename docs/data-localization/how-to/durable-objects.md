---
url: https://developers.cloudflare.com/data-localization/how-to/durable-objects/
title: Durable Objects \u00b7 Cloudflare Data Localization Suite docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:41.970651+00:00
---

# Durable Objects · Cloudflare Data Localization Suite docs

> Source: https://developers.cloudflare.com/data-localization/how-to/durable-objects/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Data Localization Suite](https://developers.cloudflare.com/data-localization/)
  3. /[Configuration guides](https://developers.cloudflare.com/data-localization/how-to/)
  4. /Durable Objects



# Durable Objects

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/data-localization/how-to/durable-objects/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRegional ServicesCustomer Metadata Boundary

The following sections describe how to configure Durable Objects with Regional Services and Customer Metadata Boundary to control where your Durable Objects run, persist data, and where logs are stored.

## Regional Services

To configure Regional Services for hostnames [proxied](https://developers.cloudflare.com/dns/proxy-status/) (meaning traffic routes through Cloudflare) through Cloudflare and ensure that processing of a Durable Object (DO) occurs only in-region, follow these steps:

  1. Follow the steps in the Durable Objects [Get Started](https://developers.cloudflare.com/durable-objects/get-started/) guide.
  2. [Restrict Durable Objects to a jurisdiction](https://developers.cloudflare.com/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction), in order to control where the DO itself runs and persists data, by creating a jurisidictional subnamespace in your Worker’s code.
  3. Follow the [Workers guide](https://developers.cloudflare.com/data-localization/how-to/workers/#regional-services) to configure a custom domain with Regional Services, in order to control the regions from which Cloudflare responds to requests.



## Customer Metadata Boundary

DO Logs and Analytics are not available outside the US region when using Customer Metadata Boundary. With Customer Metadata Boundary set to `EU`, **Workers & Pages** > **Workers** > **Metrics** tab related to DO in the zone dashboard will not be populated.

Refer to the [Durable Objects documentation](https://developers.cloudflare.com/durable-objects/) for more information.

[PreviousR2 Object Storage](https://developers.cloudflare.com/data-localization/how-to/r2/)[NextWorkers](https://developers.cloudflare.com/data-localization/how-to/workers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/data-localization/how-to/durable-objects.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
