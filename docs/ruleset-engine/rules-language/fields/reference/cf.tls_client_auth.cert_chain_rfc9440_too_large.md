---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440_too_large/
title: cf.tls_client_auth.cert_chain_rfc9440_too_large \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:05.940048+00:00
---

# cf.tls_client_auth.cert_chain_rfc9440_too_large · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440_too_large/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Tls_client_auth.Cert_chain_rfc9440_too_large



# cf.tls_client_auth.cert_chain_rfc9440_too_large

`cf.tls_client_auth.cert_chain_rfc9440_too_large``Boolean`

Returns `true` when the RFC 9440 encoded client certificate chain exceeds the 16 KiB size limit.

When `true`, [`cf.tls_client_auth.cert_chain_rfc9440`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440/) contains an empty string instead of the encoded certificate chain.

This field defaults to `false` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Categories: 

  * Request
  * mTLS



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
