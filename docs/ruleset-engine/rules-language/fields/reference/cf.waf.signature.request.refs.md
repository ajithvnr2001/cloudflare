---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.signature.request.refs/
title: cf.waf.signature.request.refs \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:33.438175+00:00
---

# cf.waf.signature.request.refs · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.signature.request.refs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Waf.Signature.Request.Refs



# cf.waf.signature.request.refs

`cf.waf.signature.request.refs``Array<String>`

An array containing up to 10 Refs for attack signatures that matched the request.

Each Ref is the same value as the corresponding Cloudflare Managed Rules public Rule ID.

Available to customers with [Attack Signature Detection](https://developers.cloudflare.com/waf/detections/attack-signature-detection/) in Security Analytics and Custom Rules. Contact your Cloudflare account team to request Early Access.

Example value:
    
    
    ["d68f8101f6e14e25aefcaea69c530a29"]

Example usage:
    
    
    any(cf.waf.signature.request.refs[*] eq "d68f8101f6e14e25aefcaea69c530a29")

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
