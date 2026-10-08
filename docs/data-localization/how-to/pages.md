---
url: https://developers.cloudflare.com/data-localization/how-to/pages/
title: Pages \u00b7 Cloudflare Data Localization Suite docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:42.171910+00:00
---

# Pages · Cloudflare Data Localization Suite docs

> Source: https://developers.cloudflare.com/data-localization/how-to/pages/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Data Localization Suite](https://developers.cloudflare.com/data-localization/)
  3. /[Configuration guides](https://developers.cloudflare.com/data-localization/how-to/)
  4. /Pages



# Pages

Last updated Jul 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/data-localization/how-to/pages/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRegional ServicesCustomer Metadata Boundary

The following sections describe how to configure Cloudflare Pages with Regional Services and Customer Metadata Boundary to control where your Pages project is processed and where logs are stored.

## Regional Services

To configure Regional Services for hostnames [proxied](https://developers.cloudflare.com/dns/proxy-status/) (meaning traffic routes through Cloudflare) through Cloudflare and ensure that processing of a Pages project occurs only in-region, follow these steps for the dashboard or API configuration:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select your Pages project.

  3. Follow these steps to [create a Custom Domain](https://developers.cloudflare.com/pages/configuration/custom-domains/).

  4. Go to the **DNS** of the zone you configured the Custom Domain for.

  5. From the **Region** dropdown, select the region you would like to use on your domain.

  6. Select **Save**.




  1. Use the [API POST](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/create/) command to add a Custom Domain to a Pages project.
  2. Run the [API POST](https://developers.cloudflare.com/data-localization/regional-services/regional-hostnames/#configure-regional-services-via-api) command on the Pages Custom Domain to create a `regional_hostnames` with a specific Region.



Note

Regional Services only applies to the Custom Domain configured for a Pages project.

## Customer Metadata Boundary

Customer Metadata Boundary applies to the Custom Domain configured, as well as the [*.pages.dev](https://developers.cloudflare.com/pages/configuration/preview-deployments/) subdomain. You also have the option to disable access to the [`.dev` domain](https://developers.cloudflare.com/pages/configuration/custom-domains/#disable-access-to-pagesdev-subdomain).

For information on available Analytics and Metrics, review the [Cloudflare product compatibility](https://developers.cloudflare.com/data-localization/compatibility/) page.

It is recommended not to store any Personally Identifiable Information (PII) in the Pages project's static assets.

Note

Page [Functions](https://developers.cloudflare.com/pages/functions/) are implemented as Cloudflare Workers. Refer to the Workers section for more information.

Refer to the [Pages documentation](https://developers.cloudflare.com/pages) for more information.

[PreviousZero Trust](https://developers.cloudflare.com/data-localization/how-to/zero-trust/)[NextCache](https://developers.cloudflare.com/data-localization/how-to/cache/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/data-localization/how-to/pages.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
