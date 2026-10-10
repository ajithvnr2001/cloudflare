---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_issuer_dn_rfc2253/
title: cf.tls_client_auth.cert_issuer_dn_rfc2253 \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:34.406183+00:00
---

# cf.tls_client_auth.cert_issuer_dn_rfc2253 · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_issuer_dn_rfc2253/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Tls_client_auth.Cert_issuer_dn_rfc2253



# cf.tls_client_auth.cert_issuer_dn_rfc2253

`cf.tls_client_auth.cert_issuer_dn_rfc2253``String`

The Distinguished Name (DN) of the Certificate Authority (CA) that issued the mTLS client certificate in [RFC 2253](https://datatracker.ietf.org/doc/html/rfc2253) format.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:
    
    
    "CN=Access Testing CA,OU=TX,O=Access Testing,L=Austin,ST=Texas,C=US"

Categories: 

  * Request
  * mTLS



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
