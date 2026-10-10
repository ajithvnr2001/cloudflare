---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.uploaded.body.violated_parameters/
title: cf.schema_validation.uploaded.body.violated_parameters \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:35.093333+00:00
---

# cf.schema_validation.uploaded.body.violated_parameters · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.uploaded.body.violated_parameters/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Schema_validation.Uploaded.Body.Violated_parameters



# cf.schema_validation.uploaded.body.violated_parameters

`cf.schema_validation.uploaded.body.violated_parameters``Array<String>`

The JSON path of a detected request body [violation of the uploaded schema](https://developers.cloudflare.com/waf/detections/application-profiles/fields/#violated-parameters).

Body validation reports the first detected violation. A value of `$` identifies the body without a more specific path.

Example value:
    
    
    ["$"]

Example usage:
    
    
    any(cf.schema_validation.uploaded.body.violated_parameters[*] == "$")

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
