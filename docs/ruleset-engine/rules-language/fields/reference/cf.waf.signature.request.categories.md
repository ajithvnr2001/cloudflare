---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.signature.request.categories/
title: cf.waf.signature.request.categories \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:08.899445+00:00
---

# cf.waf.signature.request.categories · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.signature.request.categories/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Waf.Signature.Request.Categories



# cf.waf.signature.request.categories

`cf.waf.signature.request.categories``Array<String>`

An array of categories associated with attack signatures that matched the request.

Available to customers with [Attack Signature Detection](https://developers.cloudflare.com/waf/detections/attack-signature-detection/) in Security Analytics and Custom Rules.

Contact your Cloudflare account team to request Early Access.

Example value:
    
    
    ["sqli", "cve-2025-55182"]

Example usage:
    
    
    any(cf.waf.signature.request.categories[*] eq "sqli")

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
