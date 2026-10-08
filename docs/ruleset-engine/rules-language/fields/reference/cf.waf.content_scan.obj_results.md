---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.obj_results/
title: cf.waf.content_scan.obj_results \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:08.099460+00:00
---

# cf.waf.content_scan.obj_results · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.obj_results/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Waf.Content_scan.Obj_results



# cf.waf.content_scan.obj_results

`cf.waf.content_scan.obj_results``Array<String>`

An array of scan results in the order the content objects were detected in the request.

The possible values are: `clean`, `suspicious`, `infected`, and `not scanned`.

Requires a Cloudflare Enterprise plan with [malicious uploads detection](https://developers.cloudflare.com/waf/detections/malicious-uploads/).

Example usage:
    
    
    # Check if requests to a specific endpoint contain any suspicious or infected content objects
    any(cf.waf.content_scan.obj_results[*] in {"suspicious" "infected"}) and http.request.uri.path eq "/upload"

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
