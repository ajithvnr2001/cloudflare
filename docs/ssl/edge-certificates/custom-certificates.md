---
url: https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/
title: Custom certificates \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:40.062654+00:00
---

# Custom certificates · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)
  4. /Custom certificates



# Custom certificates

Last updated Sep 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCertificate packsAvailabilityRelated features Certificate Signing Requests (CSRs) Geo Key Manager (private key restriction) Keyless SSL Certificate pinning

Custom certificates are meant for Business and Enterprise customers who want to use their own SSL certificates.

  


Use custom certificates when you need control over the certificate authority (CA) or require Organization Validated (OV) or Extended Validation (EV) certificates that Cloudflare-managed options do not support.

Unlike [Universal SSL](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/) or [advanced certificates](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/), Cloudflare does not manage issuance and renewal for custom certificates. You are responsible for the following:

  * [Upload the certificate](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/uploading/#upload-a-custom-certificate).
  * [Update the certificate](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/uploading/#update-or-renew-an-existing-custom-certificate) before it expires.
  * [Monitor the certificate expiration date](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/renewing/) to avoid downtime.



Note

If your custom certificate does not cover all of your first-level hostnames, you can enable [Universal SSL certificate](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/) to cover them.

If your custom certificate is from a [certificate authority that Cloudflare partners with](https://developers.cloudflare.com/ssl/reference/certificate-authorities/), consider switching to a Cloudflare-managed certificate to benefit from automatic issuance and renewal.

## Certificate packs

Before deploying custom certificates to Cloudflare's global network, Cloudflare automatically groups the certificates into certificate packs.

A certificate pack is a group of certificates that share the same set of hostnames — for example, `example.com` and `*.example.com` — but use different signature algorithms.

Each pack can include up to three certificates, one from each of the following signature algorithms:

  * `SHA-2/RSA`
  * `SHA-2/ECDSA`
  * `SHA-1/RSA`



Each pack only counts as one SSL certificate against your custom certificate quota.

Note

You cannot delete the primary certificate if secondary certificates are present in the pack.

## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | No | No | Yes | Yes  
Certificate packs included | 0 | 0 | 5 Modern and 1 Legacy | 5 Modern (can purchase more) and 1 Legacy (can purchase more)  
  
## Related features

### Certificate Signing Requests (CSRs)

You can use Cloudflare to generate a [Certificate Signing Request (CSR)](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/certificate-signing-requests/) for your custom certificate. When you do, Cloudflare generates and securely stores the private key associated with the CSR.

### Geo Key Manager (private key restriction)

By default, Cloudflare encrypts and securely distributes private keys to all Cloudflare data centers, where they can be used for local SSL/TLS termination. If you want to restrict where your private keys may be used, use [Geo Key Manager](https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/).

### Keyless SSL

If you want to upload a custom certificate but retain your private key on your own infrastructure, consider using [Keyless SSL](https://developers.cloudflare.com/ssl/keyless-ssl/).

### Certificate pinning

Custom certificates are the only certificate type where certificate pinning can work on Cloudflare. For guidance on pinning and its risks, refer to [Certificate pinning](https://developers.cloudflare.com/ssl/reference/certificate-pinning/).

[PreviousAPI commands](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/api-commands/)[NextManage custom certificates](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/uploading/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/custom-certificates/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
