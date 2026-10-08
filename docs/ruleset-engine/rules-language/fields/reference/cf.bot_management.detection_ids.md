---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.detection_ids/
title: cf.bot_management.detection_ids \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:02.609959+00:00
---

# cf.bot_management.detection_ids · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.detection_ids/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Bot_management.Detection_ids



# cf.bot_management.detection_ids

`cf.bot_management.detection_ids``Array<Number>`

List of IDs that correlate to the Bot Management heuristic detections made on a request.

Use this field to explicitly match a specific heuristic or to exclude a heuristic in a rule. You can have multiple heuristic detections on the same request.

Requires a Cloudflare Enterprise plan with [Bot Management](https://developers.cloudflare.com/bots/plans/bm-subscription/) enabled.

Example usage:
    
    
    any(cf.bot_management.detection_ids[*] eq 33554817)

Categories: 

  * Request
  * Bots



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
