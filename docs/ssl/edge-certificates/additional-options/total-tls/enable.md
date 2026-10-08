---
url: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/enable/
title: Enable Total TLS \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:38.940311+00:00
---

# Enable Total TLS · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/enable/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)Additional options

  4. /[Total TLS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/)
  5. /Enable



# Enable

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/enable/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAspects to consider

To enable [Total TLS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/) \- which issues individual certificates for your proxied hostnames - follow these instructions:

To enable Total TLS in the dashboard:

  1. In the Cloudflare dashboard, go to the **Edge Certificates** page.

[ Go to **Edge Certificates** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates)
  2. For **Total TLS** , switch the toggle to **On** and - if desired - choose an issuing **Certificate Authority**.




To enable Total TLS with the API, send a [`PATCH`](https://developers.cloudflare.com/api/resources/acm/subresources/total_tls/methods/create/) request with the `enabled` parameter set to your desired setting (`true` or `false`).

You can also specify a desired certificate authority by adding a value to the `certificate_authority` parameter.

## Aspects to consider

  * Total TLS certificates follow the Common Name (CN) restriction of 64 characters ([RFC 5280 ↗︎](https://www.rfc-editor.org/rfc/rfc5280.html)). If you have a hostname that exceeds this length, you can create an [Advanced Certificate](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/#create-a-certificate) via API to cover it.




[PreviousOverview](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/)[NextError messages](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/error-messages/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/additional-options/total-tls/enable.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
