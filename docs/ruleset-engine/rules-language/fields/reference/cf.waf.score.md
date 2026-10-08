---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score/
title: cf.waf.score \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:08.829011+00:00
---

# cf.waf.score · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Waf.Score



# cf.waf.score

`cf.waf.score``Number`

A global score from 1–99 that combines the score of each WAF attack vector into a single score.

The special score `100` indicates that Cloudflare did not score the request.

This is the standard [WAF attack score](https://developers.cloudflare.com/waf/detections/attack-score/) to detect variants of attack patterns.

Requires a Cloudflare Enterprise plan. You must also enable [attack score detection](https://developers.cloudflare.com/waf/detections/attack-score/).

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
