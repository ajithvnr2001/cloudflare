---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.signature.request.confidence/
title: cf.waf.signature.request.confidence \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:33.326263+00:00
---

# cf.waf.signature.request.confidence · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.signature.request.confidence/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Waf.Signature.Request.Confidence



# cf.waf.signature.request.confidence

`cf.waf.signature.request.confidence``Array<String>`

An array of confidence values associated with attack signatures that matched the request.

Supported values are `high` and `low`.

Available to customers with [Attack Signature Detection](https://developers.cloudflare.com/waf/detections/attack-signature-detection/) in Security Analytics and Custom Rules. Contact your Cloudflare account team to request Early Access.

Example value:
    
    
    ["high"]

Example usage:
    
    
    any(cf.waf.signature.request.confidence[*] eq "high")

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
