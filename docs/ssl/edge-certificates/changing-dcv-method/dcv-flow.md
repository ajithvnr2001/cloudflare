---
url: https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/dcv-flow/
title: Domain control validation flow \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:39.353913+00:00
---

# Domain control validation flow · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/dcv-flow/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)

  4. /[Domain control validation (DCV)](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/)
  5. /Domain control validation flow



# Domain control validation flow

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/dcv-flow/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhere Cloudflare sits in the DCV processSteps in the processAspects to consider DCV tokens

To obtain [Universal](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/), [Advanced](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/), and [Custom hostname](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/) certificates, Cloudflare partners with different publicly trusted [certificate authorities (CAs)](https://developers.cloudflare.com/ssl/reference/certificate-authorities/).

However, every time a CA is requested to issue or renew a certificate, the requester must prove that they have control over the domain. That is when the DCV process takes place, with the proof usually consisting of placing an HTTP token at a standard URL path (`/.well-known/pki-validation`), or placing a TXT record at the authoritative DNS provider.

## Where Cloudflare sits in the DCV process

For the use cases mentioned above, there are three different parties involved in the process:

  * The website or application for which the certificate is issued.
  * The requester (Cloudflare).
  * The CA that processes the request.



## Steps in the process

In summary, five steps have to succeed after Cloudflare requests a CA to issue or renew a certificate:

  1. Cloudflare receives the DCV tokens from the CA.
  2. Cloudflare either places the tokens on your behalf ([Full DNS setup](https://developers.cloudflare.com/dns/zone-setups/full-setup/), [Delegated DCV](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/)), or makes the tokens available for you to place them.
  3. Cloudflare polls the validation URLs to check for the tokens.
  4. After Cloudflare can confirm that the tokens are placed via multiple DNS resolvers, the CA is asked to check as well.
  5. If the CA can confirm the tokens are placed, the certificate gets issued. If the CA cannot confirm the tokens are placed, the certificate is not issued and the tokens are no longer valid.



## Aspects to consider

  * Settings that interfere with the validation URLs - firewall blocks or misconfigured DNSSEC, for example - can cause issues with your certificate issuance or renewal. Refer to the [troubleshooting guide](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/troubleshooting/).
  * When your certificate is in `pending_validation` and valid tokens are in place, some security features targeting your zone's path for `/.well-known/*` can be automatically bypassed.

  * Certificate authority authorization (CAA) records may block certificate issuance. Refer to [CAA records](https://developers.cloudflare.com/ssl/edge-certificates/caa-records/).



### DCV tokens

DCV tokens are generated and controlled by the CA and not by Cloudflare. You can find further technical specification of how they work in [RFC 8555 ↗︎](https://www.rfc-editor.org/rfc/rfc8555#section-7.1.5).

  * As mentioned in Step 5, DCV tokens will change upon verification failures. For example, if a DCV check fails because of a DNSSEC issue, the certificate order is no longer valid and Cloudflare must start a new certificate request. Since tokens cannot be reused, a new token is required.

  * DCV tokens also have [validity periods](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/validation-backoff-schedule/). If you are handling the DCV process manually, it is recommended that you place the tokens as soon as the certificate is up for renewal. Otherwise, the tokens may expire and new tokens will be required.




[PreviousValidation backoff schedule](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/validation-backoff-schedule/)[NextTroubleshooting](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/changing-dcv-method/dcv-flow.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
