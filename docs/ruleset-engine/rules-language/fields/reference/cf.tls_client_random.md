---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_random/
title: cf.tls_client_random \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:07.656040+00:00
---

# cf.tls_client_random · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_random/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Tls_client_random



# cf.tls_client_random

`cf.tls_client_random``String`

The value of the 32-byte random value provided by the client in a [TLS handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake), encoded in Base64.

For more details, refer to [RFC 8446](https://datatracker.ietf.org/doc/html/rfc8446#section-4.1.2).

Example value:
    
    
    "YWJjZA=="

Categories: 

  * Request
  * SSL/TLS



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
