---
url: https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/
title: Domain control validation (DCV) \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:39.240528+00:00
---

# Domain control validation (DCV) · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)
  4. /Domain control validation (DCV)



# Domain control validation (DCV)

Last updated May 7, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFull DNS setup - no action requiredPartial DNS setup - action sometimes required Non-wildcard certificates Wildcard certificates

Before a certificate authority (CA) will issue a certificate for a domain, the requester must prove they have control over that domain. This process is known as domain control validation (DCV).

If DCV is not completed, the CA cannot issue or renew the certificate, and visitors to your site will see SSL/TLS errors.

Note

Refer to [Domain control validation flow](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/dcv-flow/) to learn more about the steps and parties involved in the DCV process.

For [custom certificates](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/), you handle DCV directly with the CA when requesting or renewing the certificate.

For certificates issued through Cloudflare, whether DCV is automatic depends on your DNS setup.

* * *

## Full DNS setup - no action required

If your domain is on a [**full setup**](https://developers.cloudflare.com/dns/zone-setups/full-setup/) — meaning that Cloudflare runs your authoritative nameservers — Cloudflare handles DCV automatically on your behalf using a TXT record. For more details, refer to [Enable Universal SSL](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/#full-dns-setup).

* * *

## Partial DNS setup - action sometimes required

If your application is on a [partial DNS setup](https://developers.cloudflare.com/dns/zone-setups/partial-setup/) — meaning that Cloudflare does not run your authoritative nameservers — you may need to perform additional steps to complete DCV.

### Non-wildcard certificates

If every hostname on a non-wildcard certificate is [proxying traffic](https://developers.cloudflare.com/dns/proxy-status/) through Cloudflare and the DCV method is [HTTP](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/http/), Cloudflare can automatically complete DCV on your behalf.

This applies to customers using [Universal](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/) or [Advanced certificates](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/).

If one of the hostnames on the certificate is not proxying traffic through Cloudflare, certificate issuance and renewal will vary based on the type of certificate you are using:

  * **Universal** : Perform DCV using one of the available [methods](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/).
  * **Advanced** : In most cases, you can opt for [Delegated DCV](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/), which greatly simplifies certificate management.



Tip

If all hostnames are proxied and non-wildcard but you are using [TXT](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/txt/) as DCV method for advanced certificates, also consider [Delegated DCV](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/) to simplify the process.

### Wildcard certificates

For wildcard hostname certificates, certificate issuance and renewal varies based on the type of certificate you are using:

  * **Universal** : Perform DCV using [TXT validation method](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/txt/).
  * **Advanced** : In most cases, you can opt for [Delegated DCV](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/), which greatly simplifies certificate management.



If you cannot use Delegated DCV, you need to use [TXT based DCV](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/txt/) for certificate issuance and renewal. This means you will need to place one TXT DCV token for every hostname on the certificate. If one or more of the hostnames on the certificate fails to validate, the certificate will not be issued or renewed.

This means that a wildcard certificate covering `example.com` and `*.example.com` will require two DCV tokens to be placed at the authoritative DNS provider. Similarly, a certificate with five hostnames in the SAN (including a wildcard) will require five DCV tokens to be placed at the authoritative DNS provider.

[PreviousEnforce HTTPS connections](https://developers.cloudflare.com/ssl/edge-certificates/encrypt-visitor-traffic/)[NextOverview](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/changing-dcv-method/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
