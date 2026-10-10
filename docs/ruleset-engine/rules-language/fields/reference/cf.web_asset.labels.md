---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.web_asset.labels/
title: cf.web_asset.labels \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:33.392129+00:00
---

# cf.web_asset.labels · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.web_asset.labels/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Web_asset.Labels



# cf.web_asset.labels

`cf.web_asset.labels``Array<String>`

An array of labels associated with the operation matched by the request.

Use this field to create rules based on labels applied to operations in Web Assets, including API endpoints. For more information, refer to [Label operations](https://developers.cloudflare.com/security/web-assets/label-operations/).

Example value:
    
    
    ["cf-log-in"]

Example usage:
    
    
    any(cf.web_asset.labels[*] == "cf-log-in")

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
