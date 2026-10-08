---
url: https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/
title: Methods \u2014 Domain Control Validation \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:39.386843+00:00
---

# Methods — Domain Control Validation · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)

  4. /[Domain control validation (DCV)](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/)
  5. /Methods



# Methods

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPerform DCVVerify DCV statusUpdate DCV methods

Before a certificate authority (CA) will issue a certificate for a domain, the requester must prove they have control over that domain. This process is known as domain control validation (DCV).

## Perform DCV

For details on each method available for DCV, refer to the following resources:

  * [Delegated](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/)
  * [TXT](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/txt/)
  * [HTTP](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/http/)



Note

For guidance on when you need to perform DCV, refer to [Domain Control Validation](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/).

* * *

## Verify DCV status

To verify the [DCV status](https://developers.cloudflare.com/ssl/reference/certificate-statuses/) of a certificate, either monitor the certificate's status on the [**Edge Certificates** ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates) page or use the [Verification Status endpoint](https://developers.cloudflare.com/api/resources/ssl/subresources/verification/methods/get/).

A status of `active` means that the certificate has been deployed to Cloudflare’s global network and will be served as soon as HTTP traffic is proxied to Cloudflare.

## Update DCV methods

You cannot update the DCV method for an active certificate. To update the DCV method for a subdomain, wait until the DCV expires and then change the DCV method.

[PreviousOverview](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/)[NextDelegated](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/changing-dcv-method/methods/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
