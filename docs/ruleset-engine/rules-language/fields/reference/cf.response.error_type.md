---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.response.error_type/
title: cf.response.error_type \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:35.156431+00:00
---

# cf.response.error_type · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.response.error_type/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Response.Error_type



# cf.response.error_type

`cf.response.error_type``String`

A string with the type of error in the response being returned.

The default value is an empty string (`""`).

The available values are the following:

  * `"managed_challenge"`
  * `"iuam"`
  * `"legacy_challenge"`
  * `"ip_ban"`
  * `"waf"`
  * `"5xx"`
  * `"1xxx"`
  * `"always_online"`
  * `"country_challenge"`
  * `"ratelimit"`



You can use this field to customize the response for a specific type of error (for example, all 1XXX errors or all WAF block actions).

**Note** : This field is only available in [Response Header Transform Rules](https://developers.cloudflare.com/rules/transform/response-header-modification/) and [Custom Errors](https://developers.cloudflare.com/rules/custom-errors/).

Categories: 

  * Response



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
