---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.tags/
title: cf.bot_management.tags \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:03.130783+00:00
---

# cf.bot_management.tags · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.tags/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Bot_management.Tags



# cf.bot_management.tags

`cf.bot_management.tags``Array<String>`

Provides the tags associated with bot traffic.

Use this field to match requests associated with a specific bot tag.

Requires a Cloudflare Enterprise plan with [Bot Management](https://developers.cloudflare.com/bots/plans/bm-subscription/) enabled.

Example usage:
    
    
    any(cf.bot_management.tags[*] eq "API")

Categories: 

  * Request
  * Bots



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
