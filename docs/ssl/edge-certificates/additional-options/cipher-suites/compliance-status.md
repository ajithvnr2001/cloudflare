---
url: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/compliance-status/
title: Cipher suites compliance standards \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:38.001365+00:00
---

# Cipher suites compliance standards · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/compliance-status/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)Additional options

  4. /[Cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/)
  5. /Compliance standards



# Compliance standards

Last updated Jun 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/compliance-status/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPCI DSSFIPS-140-3

Consider the following recommendations on custom [cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/) for when your organization needs to comply with regulatory standards.

Refer to [Customize cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/) to learn how to specify cipher suites at zone level or per hostname.

Caution

Also [enable TLS 1.3](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/tls-13/#enable-tls-13) on your zone and, when opting for PCI DSS, make sure to up your [Minimum TLS version](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/minimum-tls/) to `1.2`. Refer to [Cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/) and [TLS protocols](https://developers.cloudflare.com/ssl/reference/protocols/) to learn more.

## PCI DSS

Recommended cipher suites for compliance with the [Payment Card Industry Data Security Standard (PCI DSS) ↗︎](https://www.pcisecuritystandards.org/standards/pci-dss/). Enhances payment card data security.

Cipher suites list

`AEAD-AES128-GCM-SHA256`1, `AEAD-AES256-GCM-SHA384`2, `AEAD-CHACHA20-POLY1305-SHA256`3, `ECDHE-ECDSA-AES128-GCM-SHA256`, `ECDHE-RSA-AES128-GCM-SHA256`, `ECDHE-ECDSA-AES256-GCM-SHA384`, `ECDHE-RSA-AES256-GCM-SHA384`, `ECDHE-ECDSA-CHACHA20-POLY1305`, `ECDHE-RSA-CHACHA20-POLY1305`

If you are customizing cipher suites via API, refer to [Steps and API examples](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/#steps-and-api-examples) for a snippet you can copy with the formatted array.

## FIPS-140-3

Recommended cipher suites for compliance with the [Federal Information Processing Standard (140-3) ↗︎](https://csrc.nist.gov/pubs/fips/140-3/final). Used to approve cryptographic modules.

Cipher suites list

`AES128-GCM-SHA256`, `AES128-SHA`, `AES128-SHA256`, `AES256-SHA`, `AES256-SHA256`, `DES-CBC3-SHA`, `ECDHE-ECDSA-AES128-GCM-SHA256`, `ECDHE-ECDSA-AES128-SHA`, `ECDHE-ECDSA-AES128-SHA256`, `ECDHE-ECDSA-AES256-GCM-SHA384`, `ECDHE-ECDSA-AES256-SHA384`, `ECDHE-RSA-AES128-GCM-SHA256`, `ECDHE-RSA-AES128-SHA`, `ECDHE-RSA-AES128-SHA256`, `ECDHE-RSA-AES256-GCM-SHA384`, `ECDHE-RSA-AES256-SHA`, `ECDHE-RSA-AES256-SHA384`

If you are customizing cipher suites via API, refer to [Steps and API examples](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/#steps-and-api-examples) for a snippet you can copy with the formatted array.

## Footnotes

  1. Same as `TLS_AES_128_GCM_SHA256`. Refer to [TLS 1.3 cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details. ↩

  2. Same as `TLS_AES_256_GCM_SHA384`. Refer to [TLS 1.3 cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details. ↩

  3. Same as `TLS_CHACHA20_POLY1305_SHA256`. Refer to [TLS 1.3 cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details. ↩




[PreviousSecurity levels](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/recommendations/)[NextSupported cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/supported-cipher-suites/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/additional-options/cipher-suites/compliance-status.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
