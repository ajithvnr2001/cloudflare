---
url: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/recommendations/
title: Cipher suite recommendations \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:38.341002+00:00
---

# Cipher suite recommendations · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/recommendations/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)Additional options

  4. /[Cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/)
  5. /Security levels



# Security levels

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/recommendations/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewModernCompatibleLegacy (default)

Refer to the sections below for three different security levels and how Cloudflare recommends that you set them up if you need to restrict the [cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/) used between Cloudflare and clients that access your website or application.

Refer to [Customize cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/) to learn how to specify cipher suites at zone level or per hostname.

Caution

Before opting for compatible or modern, review the [related SSL/TLS settings](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/#related-ssltls-settings)1.

## Modern

Offers the best security and performance, limiting your range of clients to modern devices and browsers. Supports TLS 1.2-1.3 cipher suites. All suites are forward-secret and support authenticated encryption (AEAD).

Cipher suites list

`AEAD-AES128-GCM-SHA256`2, `AEAD-AES256-GCM-SHA384`3, `AEAD-CHACHA20-POLY1305-SHA256`4,`ECDHE-ECDSA-AES128-GCM-SHA256`, `ECDHE-ECDSA-CHACHA20-POLY1305`, `ECDHE-RSA-AES128-GCM-SHA256`, `ECDHE-RSA-CHACHA20-POLY1305`, `ECDHE-ECDSA-AES256-GCM-SHA384`, `ECDHE-RSA-AES256-GCM-SHA384`

If you are customizing cipher suites via API, refer to [Steps and API examples](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/#steps-and-api-examples) for a snippet you can copy with the formatted array.

## Compatible

Provides broader compatibility with somewhat weaker security. Supports TLS 1.2-1.3 cipher suites. All suites are forward-secret.

Cipher suites list

`AEAD-AES128-GCM-SHA256`2, `AEAD-AES256-GCM-SHA384`3, `AEAD-CHACHA20-POLY1305-SHA256`4, `ECDHE-ECDSA-AES128-GCM-SHA256`, `ECDHE-ECDSA-CHACHA20-POLY1305`, `ECDHE-RSA-AES128-GCM-SHA256`, `ECDHE-RSA-CHACHA20-POLY1305`, `ECDHE-ECDSA-AES256-GCM-SHA384`, `ECDHE-RSA-AES256-GCM-SHA384`, `ECDHE-ECDSA-AES128-SHA256`, `ECDHE-RSA-AES128-SHA256`, `ECDHE-ECDSA-AES256-SHA384`, `ECDHE-RSA-AES256-SHA384`

If you are customizing cipher suites via API, refer to [Steps and API examples](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/#steps-and-api-examples) for a snippet you can copy with the formatted array.

## Legacy (default)

Includes all cipher suites that Cloudflare supports today. Broadest compatibility with the weakest security. Supports TLS 1.0-1.3 cipher suites.

Cipher suites list

`AEAD-AES128-GCM-SHA256`2, `AEAD-AES256-GCM-SHA384`3, `AEAD-CHACHA20-POLY1305-SHA256`4, `ECDHE-ECDSA-AES128-GCM-SHA256`, `ECDHE-ECDSA-CHACHA20-POLY1305`, `ECDHE-RSA-AES128-GCM-SHA256`, `ECDHE-RSA-CHACHA20-POLY1305`, `ECDHE-ECDSA-AES256-GCM-SHA384`, `ECDHE-RSA-AES256-GCM-SHA384`, `ECDHE-ECDSA-AES128-SHA256`, `ECDHE-RSA-AES128-SHA256`, `ECDHE-ECDSA-AES256-SHA384`, `ECDHE-RSA-AES256-SHA384`, `ECDHE-ECDSA-AES128-SHA`, `ECDHE-RSA-AES128-SHA`, `AES128-GCM-SHA256`, `AES128-SHA256`, `AES128-SHA`, `ECDHE-RSA-AES256-SHA`, `AES256-GCM-SHA384`, `AES256-SHA256`, `AES256-SHA`, `DES-CBC3-SHA`

To reset your option to the default, [use an empty array](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/#reset-to-default-values).

## Footnotes

  1. Although configured independently, cipher suites interact with **Minimum TLS version** and **TLS 1.3**. ↩

  2. Same as `TLS_AES_128_GCM_SHA256`. Refer to [TLS 1.3 cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details. ↩ ↩2 ↩3

  3. Same as `TLS_AES_256_GCM_SHA384`. Refer to [TLS 1.3 cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details. ↩ ↩2 ↩3

  4. Same as `TLS_CHACHA20_POLY1305_SHA256`. Refer to [TLS 1.3 cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details. ↩ ↩2 ↩3




[PreviousUse the API](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/)[NextCompliance standards](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/compliance-status/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/additional-options/cipher-suites/recommendations.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
