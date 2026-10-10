---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score.class/
title: cf.waf.score.class \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:33.557091+00:00
---

# cf.waf.score.class · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score.class/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Waf.Score.Class



# cf.waf.score.class

`cf.waf.score.class``String`

The attack score class of the current request, based on the WAF attack score.

Can have one of the following values: `attack`, `likely_attack`, `likely_clean`, `clean`.

Requires a Cloudflare Business plan or above. You must also enable [attack score detection](https://developers.cloudflare.com/waf/detections/attack-score/).

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
