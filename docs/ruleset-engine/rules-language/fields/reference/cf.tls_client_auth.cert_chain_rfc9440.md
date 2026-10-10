---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440/
title: cf.tls_client_auth.cert_chain_rfc9440 \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:34.604688+00:00
---

# cf.tls_client_auth.cert_chain_rfc9440 · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Tls_client_auth.Cert_chain_rfc9440



# cf.tls_client_auth.cert_chain_rfc9440

`cf.tls_client_auth.cert_chain_rfc9440``String`

The mTLS client certificate chain (excluding the leaf certificate) encoded as a structured field list per [RFC 9440](https://datatracker.ietf.org/doc/html/rfc9440).

Contains the DER-encoded, Base64-wrapped client certificate chain formatted as an [RFC 9440](https://datatracker.ietf.org/doc/html/rfc9440#name-client-cert-chain-http-head) `Client-Cert-Chain` HTTP header value. The value is a structured field list of byte sequences. The leaf certificate is not included in the chain (it is available in [`cf.tls_client_auth.cert_rfc9440`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_rfc9440/)). The chain reflects the certificates as sent by the client, without any reordering or validation.

This field is populated regardless of the certificate validation result. Before using this value, verify the certificate status by checking [`cf.tls_client_auth.cert_verified`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_verified/) and [`cf.tls_client_auth.cert_revoked`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_revoked/).

Returns `""` if the client did not send any intermediate certificates or if the encoded value exceeds the 16 KiB size limit. Refer to [`cf.tls_client_auth.cert_chain_rfc9440_too_large`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440_too_large/) to distinguish between these cases.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:
    
    
    ":MII.....=:, :MII....=:"

Categories: 

  * Request
  * mTLS



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
