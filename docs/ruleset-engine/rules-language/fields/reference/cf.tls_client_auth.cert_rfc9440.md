---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_rfc9440/
title: cf.tls_client_auth.cert_rfc9440 \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:34.448790+00:00
---

# cf.tls_client_auth.cert_rfc9440 · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_rfc9440/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Tls_client_auth.Cert_rfc9440



# cf.tls_client_auth.cert_rfc9440

`cf.tls_client_auth.cert_rfc9440``String`

The mTLS client certificate encoded as a Structured Fields Byte Sequence per [RFC 9440](https://datatracker.ietf.org/doc/html/rfc9440).

Contains the DER-encoded, Base64-wrapped client leaf certificate formatted as an [RFC 9440](https://datatracker.ietf.org/doc/html/rfc9440#name-client-cert-http-header-fie) `Client-Cert` HTTP header value. The value is a Structured Fields Byte Sequence (the Base64 data prefixed and suffixed by `:`).

This field is populated regardless of the certificate validation result. Before using this value, verify the certificate status by checking [`cf.tls_client_auth.cert_verified`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_verified/) and [`cf.tls_client_auth.cert_revoked`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_revoked/).

Returns `""` if no client certificate was presented or if the encoded value exceeds the 10 KiB size limit. Refer to [`cf.tls_client_auth.cert_rfc9440_too_large`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_rfc9440_too_large/) to distinguish between these cases.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:
    
    
    ":MIIBqDCCAU6g......:"

Categories: 

  * Request
  * mTLS



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
