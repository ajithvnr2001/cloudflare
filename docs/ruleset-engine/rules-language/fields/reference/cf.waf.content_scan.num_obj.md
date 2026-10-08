---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.num_obj/
title: cf.waf.content_scan.num_obj \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:08.027072+00:00
---

# cf.waf.content_scan.num_obj · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.num_obj/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Waf.Content_scan.Num_obj



# cf.waf.content_scan.num_obj

`cf.waf.content_scan.num_obj``Integer`

The number of content objects detected in the request (zero or greater).

Requires a Cloudflare Enterprise plan with [malicious uploads detection](https://developers.cloudflare.com/waf/detections/malicious-uploads/).

Example usage:
    
    
    # Check if requests to a specific endpoint contain more than two content objects
    cf.waf.content_scan.num_obj > 2 and http.request.uri.path eq "/upload"

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
