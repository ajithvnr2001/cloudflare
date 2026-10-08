---
url: https://developers.cloudflare.com/data-localization/how-to/cache/
title: Cache \u00b7 Cloudflare Data Localization Suite docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:41.909027+00:00
---

# Cache · Cloudflare Data Localization Suite docs

> Source: https://developers.cloudflare.com/data-localization/how-to/cache/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Data Localization Suite](https://developers.cloudflare.com/data-localization/)
  3. /[Configuration guides](https://developers.cloudflare.com/data-localization/how-to/)
  4. /Cache



# Cache

Last updated Jul 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/data-localization/how-to/cache/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRegional Services Egress to originCustomer Metadata Boundary

The following sections describe how to configure Cache with Regional Services and Customer Metadata Boundary to control where cached content is stored and served from.

## Regional Services

To configure Regional Services for hostnames [proxied](https://developers.cloudflare.com/dns/proxy-status/) (meaning traffic routes through Cloudflare) through Cloudflare and ensure that [eligible assets](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/) are cached only in-region, follow these steps for the dashboard or API configuration:

  1. In the Cloudflare dashboard, go to the **Records** page.

[ Go to **Records** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/dns/records)
  2. Follow these steps to [create a DNS record](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/).

  3. From the **Region** dropdown, select the region you would like to use on your domain.

  4. Select **Save**.




  1. To create records with the API, use the [API POST](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/create/) command.
  2. Run the [API POST](https://developers.cloudflare.com/data-localization/regional-services/regional-hostnames/#configure-regional-services-via-api) command on the hostname to create a `regional_hostnames` with a specific region.



Note

Take into consideration that only [Generic Global Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/#generic-global-tiered-cache) and [Custom Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/#custom-tiered-cache) respect Regional Services. [Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/#smart-tiered-cache) is incompatible with Regional Services.

### Egress to origin

Regional Services controls where user traffic is decrypted and processed within Cloudflare's network. It does not by itself guarantee the geolocation of the egress IPs used by the Cloudflare CDN when connecting to your origin server. Egress IPs to your origin are site-local IPs from the in-region data center where the request was processed.

If you need guaranteed egress IP geolocation — for example, to allowlist Cloudflare IPs on your origin from a specific country — use [Dedicated CDN Egress IPs](https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/) in combination with Regional Services.

## Customer Metadata Boundary

[Cache Analytics](https://developers.cloudflare.com/cache/performance-review/cache-analytics/), Generic Global Tiered Cache and Custom Tiered Cache are compatible with Customer Metadata Boundary. With Customer Metadata Boundary set to EU, the **Caching** > **Tiered Cache** tab in the zone dashboard will not be populated.

For more information on CDN and caching, refer to the [Cache documentation](https://developers.cloudflare.com/cache/).

[PreviousPages](https://developers.cloudflare.com/data-localization/how-to/pages/)[NextLoad Balancing](https://developers.cloudflare.com/data-localization/how-to/load-balancing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/data-localization/how-to/cache.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
