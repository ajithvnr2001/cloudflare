---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_not_after/
title: cf.tls_client_auth.cert_not_after \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:34.373514+00:00
---

# cf.tls_client_auth.cert_not_after · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_not_after/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Tls_client_auth.Cert_not_after



# cf.tls_client_auth.cert_not_after

`cf.tls_client_auth.cert_not_after``String`

The mTLS client certificate is not valid after this date.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:
    
    
    "Mar 21 13:35:00 2023 GMT"

Categories: 

  * Request
  * mTLS



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
