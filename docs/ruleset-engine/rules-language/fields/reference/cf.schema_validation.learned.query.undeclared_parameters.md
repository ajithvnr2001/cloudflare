---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.learned.query.undeclared_parameters/
title: cf.schema_validation.learned.query.undeclared_parameters \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:04.633189+00:00
---

# cf.schema_validation.learned.query.undeclared_parameters · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.learned.query.undeclared_parameters/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Schema_validation.Learned.Query.Undeclared_parameters



# cf.schema_validation.learned.query.undeclared_parameters

`cf.schema_validation.learned.query.undeclared_parameters``Array<String>`

Names of query parameters detected in the request but [not declared in the learned schema](https://developers.cloudflare.com/waf/detections/application-profiles/fields/#undeclared-query-parameters).

Query parameter names are URL-decoded.

Example value:
    
    
    ["utm"]

Example usage:
    
    
    any(cf.schema_validation.learned.query.undeclared_parameters[*] == "utm")

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
