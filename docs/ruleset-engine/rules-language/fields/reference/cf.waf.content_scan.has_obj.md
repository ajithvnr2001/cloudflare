---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.has_obj/
title: cf.waf.content_scan.has_obj \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:33.905838+00:00
---

# cf.waf.content_scan.has_obj · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.has_obj/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Waf.Content_scan.Has_obj



# cf.waf.content_scan.has_obj

`cf.waf.content_scan.has_obj``Boolean`

Indicates whether the request contains at least one content object.

Requires a Cloudflare Enterprise plan with [malicious uploads detection](https://developers.cloudflare.com/waf/detections/malicious-uploads/).

Example usage:
    
    
    # Check if requests to a specific endpoint include any content objects
    cf.waf.content_scan.has_obj and http.request.uri.path eq "/upload"

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
