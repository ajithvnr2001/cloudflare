---
url: https://developers.cloudflare.com/data-localization/how-to/load-balancing/
title: Load Balancing \u00b7 Cloudflare Data Localization Suite docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:42.147102+00:00
---

# Load Balancing · Cloudflare Data Localization Suite docs

> Source: https://developers.cloudflare.com/data-localization/how-to/load-balancing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Data Localization Suite](https://developers.cloudflare.com/data-localization/)
  3. /[Configuration guides](https://developers.cloudflare.com/data-localization/how-to/)
  4. /Load Balancing



# Load Balancing

Last updated Jul 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/data-localization/how-to/load-balancing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRegional ServicesCustomer Metadata Boundary

The following sections describe how to configure Load Balancing with Regional Services and Customer Metadata Boundary to control where load balancing decisions and traffic processing occur.

## Regional Services

You can load balance traffic at different levels of the networking stack depending on the [proxy mode](https://developers.cloudflare.com/load-balancing/understand-basics/proxy-modes/): Layer 7 (`HTTP/S`) and Layer 4 (`TCP`) are supported; however, `DNS-only` is not supported, as it is not [proxied](https://developers.cloudflare.com/dns/proxy-status/).

To configure Regional Services for hostnames [proxied](https://developers.cloudflare.com/dns/proxy-status/) (meaning traffic routes through Cloudflare) through Cloudflare and ensure that the Load Balancer is available only in-region, follow these steps for the dashboard or API configuration:

  1. In the Cloudflare dashboard, go to the **Load balancing** page.

[ Go to **Load Balancing** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/traffic/load-balancing)
  2. Follow the steps to [create a load balancer](https://developers.cloudflare.com/load-balancing/load-balancers/create-load-balancer/#create-a-load-balancer).

  3. From the **Data Localization** dropdown, select the region you would like to use on your domain.

  4. Select **Next** and continue with the regular setup.

  5. Select **Save**.




  1. Follow the instructions outlined to [create a load balancer](https://developers.cloudflare.com/load-balancing/load-balancers/create-load-balancer/#create-a-load-balancer) via API.
  2. Run the [API POST](https://developers.cloudflare.com/data-localization/regional-services/regional-hostnames/#configure-regional-services-via-api) command on the Load Balancer hostname to create a `regional_hostnames` with a specific region.



## Customer Metadata Boundary

[Load Balancing Analytics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/) are not available outside the US region when using Customer Metadata Boundary.

With Customer Metadata Boundary set to `EU`, **Traffic** > **Load Balancing Analytics** > **Overview and Latency** tab in the zone dashboard will not be populated.

Refer to the [Load Balancing documentation](https://developers.cloudflare.com/load-balancing/) for more information.

[PreviousCache](https://developers.cloudflare.com/data-localization/how-to/cache/)[NextCloudflare for SaaS](https://developers.cloudflare.com/data-localization/how-to/cloudflare-for-saas/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/data-localization/how-to/load-balancing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
