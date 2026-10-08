---
url: https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/bundling-methodologies/
title: Bundle methodologies \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:40.365520+00:00
---

# Bundle methodologies · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/bundling-methodologies/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)

  4. /[Custom certificates](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/)
  5. /Bundle methodologies



# Bundle methodologies

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/bundling-methodologies/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIntermediate and root certificatesMethodologies Compatible Modern User-defined

When an SSL certificate is deployed to Cloudflare's global network, it may be augmented with intermediate and root certificates to assist the user agent in finding a chain to a publicly trusted root.

You can control the mechanics of how certificates are bundled by specifying a bundling methodology.

## Intermediate and root certificates

Cloudflare maintains intermediate and root certificates used for bundling on a [GitHub repository ↗︎](https://github.com/cloudflare/cfssl_trust). As the certificates expire or are removed by certificate authorities, Cloudflare removes and adds them accordingly.

Expiration values for these certificates may appear in the `expires_on` field when you use the [Analyze Certificate endpoint](https://developers.cloudflare.com/api/resources/ssl/subresources/analyze/methods/create/) \- often when the methodology you specify is Compatible. However, these expiration values reflect intermediate and root certificates - which are handled by Cloudflare -, not the leaf certificate you would have previously uploaded to Cloudflare.

Note

When using `compatible` or `modern`, a selection might be done on the intermediates you provide at upload time, meaning it is not guaranteed all of them will make it to the final chain. If you must ensure the chain you upload is the one used, select `user-defined`.

## Methodologies

### Compatible

Compatible is the default methodology and uses common and well distributed intermediate certificates to complete the chain. This ensures that the resulting bundle is compatible with as many clients as possible.

The related value for the `bundle_method` parameter when using the [API](https://developers.cloudflare.com/api/resources/custom_certificates/methods/create/) is `ubiquitous`.

### Modern

Modern consists of attempts to make the chain as efficient as possible, often by using newer or fewer intermediate certificates.

The related value for the `bundle_method` parameter when using the [API](https://developers.cloudflare.com/api/resources/custom_certificates/methods/create/) is `optimal`.

### User-defined

User-defined allows you to paste your own certificate chain and present that bundle to clients. If you are using a self-signed certificate (not recommended), you must use this mode.

The related value for the `bundle_method` parameter when using the [API](https://developers.cloudflare.com/api/resources/custom_certificates/methods/create/) is `force`.

[PreviousRenewal and expiration](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/renewing/)[NextRemove key file password](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/remove-file-key-password/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/custom-certificates/bundling-methodologies.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
