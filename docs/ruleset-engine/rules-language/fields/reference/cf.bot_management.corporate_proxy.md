---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.corporate_proxy/
title: cf.bot_management.corporate_proxy \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:02.391138+00:00
---

# cf.bot_management.corporate_proxy · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.corporate_proxy/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Bot_management.Corporate_proxy



# cf.bot_management.corporate_proxy

`cf.bot_management.corporate_proxy``Boolean`

Indicates whether the incoming request comes from an identified Enterprise-only cloud-based corporate proxy or secure web gateway.

Requires a Cloudflare Enterprise plan with [Bot Management](https://developers.cloudflare.com/bots/plans/bm-subscription/) enabled.

Example usage:
    
    
    not cf.bot_management.verified_bot
    and not cf.bot_management.static_resource
    and not cf.bot_management.corporate_proxy
    and cf.bot_management.score lt 30

Categories: 

  * Request
  * Bots



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
