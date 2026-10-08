---
url: https://developers.cloudflare.com/ssl/origin-configuration/cipher-suites/
title: Cipher suites \u2014 Origin \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:44.488104+00:00
---

# Cipher suites — Origin · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/origin-configuration/cipher-suites/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /Origin server
  4. /Cipher suites



# Cipher suites

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/origin-configuration/cipher-suites/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSupported cipher suites by protocol TLS 1.3 cipher suitesMatch on origin

Refer to the following list to know what cipher suites Cloudflare presents to origin servers during an SSL/TLS handshake.

Note

Refer to [cipher suites supported at Cloudflare's global network](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/supported-cipher-suites/) to know what cipher suites Cloudflare presents to browsers and other user agents.

The list order is based on how the cipher suites appear in the [ClientHello ↗︎](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/#:~:text=client%20hello), communicating Cloudflare's preference.

## Supported cipher suites by protocol

Cipher name | TLS 1.0 | TLS 1.1 | TLS 1.2 | TLS 1.3  
---|---|---|---|---  
AEAD-AES128-GCM-SHA256 1 | ❌ | ❌ | ❌ | ✅  
AEAD-AES256-GCM-SHA384 1 | ❌ | ❌ | ❌ | ✅  
AEAD-CHACHA20-POLY1305-SHA256 1 | ❌ | ❌ | ❌ | ✅  
ECDHE-ECDSA-AES128-GCM-SHA256 | ❌ | ❌ | ✅ | ❌  
ECDHE-RSA-AES128-GCM-SHA256 | ❌ | ❌ | ✅ | ❌  
ECDHE-RSA-AES128-SHA | ✅ | ✅ | ✅ | ❌  
AES128-GCM-SHA256 | ❌ | ❌ | ✅ | ❌  
AES128-SHA | ✅ | ✅ | ✅ | ❌  
ECDHE-ECDSA-AES256-GCM-SHA384 | ❌ | ❌ | ✅ | ❌  
ECDHE-RSA-AES256-GCM-SHA384 | ❌ | ❌ | ✅ | ❌  
ECDHE-RSA-AES256-SHA384 | ❌ | ❌ | ✅ | ❌  
AES256-SHA | ✅ | ✅ | ✅ | ❌  
DES-CBC3-SHA | ✅ | ❌ | ❌ | ❌  
  
### TLS 1.3 cipher suites

Although TLS 1.3 uses the same cipher suite space as previous versions of TLS, TLS 1.3 cipher suites are defined differently, only specifying the symmetric ciphers, and cannot be used for TLS 1.2 ([RFC 8446 ↗︎](https://www.rfc-editor.org/rfc/rfc8446.html)).

Similarly, TLS 1.2 and lower cipher suites cannot be used with TLS 1.3. BoringSSL also hard-codes cipher preferences in the order above for TLS 1.3.

Based on BoringSSL, Cloudflare system will return the names listed above. However, the corresponding names defined in [RFC 8446 ↗︎](https://www.rfc-editor.org/rfc/rfc8446.html) are the following:

  * `TLS_AES_128_GCM_SHA256`
  * `TLS_AES_256_GCM_SHA384`
  * `TLS_CHACHA20_POLY1305_SHA256`



## Match on origin

Cloudflare will present the cipher suites to your origin and your server will select whichever cipher suite it prefers.

However, if you want to ensure that your origin server supports the same cipher suites that Cloudflare supports at our global network and you use [NGINX ↗︎](https://en.wikipedia.org/wiki/Nginx) for TLS termination on your origin, you can apply the following configuration:
    
    
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
    ssl_ecdh_curve X25519:P-256:P-384;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-CHACHA20-POLY1305:ECDHE+AES128:RSA+AES128:ECDHE+AES256:RSA+AES256:ECDHE+3DES:RSA+3DES;
    ssl_prefer_server_ciphers on;

## Footnotes

  1. Refer to TLS 1.3 cipher suites for details. ↩ ↩2 ↩3




[PreviousCustom Origin Trust Store](https://developers.cloudflare.com/ssl/origin-configuration/custom-origin-trust-store/)[NextOverview](https://developers.cloudflare.com/ssl/client-certificates/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/origin-configuration/cipher-suites.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
