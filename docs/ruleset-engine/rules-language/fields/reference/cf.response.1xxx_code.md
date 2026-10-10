---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.response.1xxx_code/
title: cf.response.1xxx_code \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:35.358513+00:00
---

# cf.response.1xxx_code · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.response.1xxx_code/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Response.1xxx_code



# cf.response.1xxx_code

`cf.response.1xxx_code``Integer`

Contains the specific code for 1XXX Cloudflare errors.

Use this field to differentiate between 1XXX errors associated with the same HTTP status code. The default value is `0`.

For a list of 1XXX errors, refer to [Troubleshooting Cloudflare 1XXX errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/).

**Note** : This field is only available in [Response Header Transform Rules](https://developers.cloudflare.com/rules/transform/response-header-modification/) and [Custom Errors](https://developers.cloudflare.com/rules/custom-errors/).

Example value:
    
    
    1020

Categories: 

  * Response



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
