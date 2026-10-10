---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_fingerprint_sha256/
title: cf.tls_client_auth.cert_fingerprint_sha256 \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:34.525093+00:00
---

# cf.tls_client_auth.cert_fingerprint_sha256 · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_fingerprint_sha256/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Tls_client_auth.Cert_fingerprint_sha256



# cf.tls_client_auth.cert_fingerprint_sha256

`cf.tls_client_auth.cert_fingerprint_sha256``String`

The SHA-256 fingerprint of the mTLS client certificate.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:
    
    
    "af363dc85bc942a892d3cee9796190fdb36d89cd588a4f1cb17c74a943439714"

Categories: 

  * Request
  * mTLS



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
