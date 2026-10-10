---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.obj_sizes/
title: cf.waf.content_scan.obj_sizes \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:33.731999+00:00
---

# cf.waf.content_scan.obj_sizes · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.obj_sizes/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Waf.Content_scan.Obj_sizes



# cf.waf.content_scan.obj_sizes

`cf.waf.content_scan.obj_sizes``Array<Integer>`

An array of file sizes in bytes, in the order the content objects were detected in the request.

Requires a Cloudflare Enterprise plan with [malicious uploads detection](https://developers.cloudflare.com/waf/detections/malicious-uploads/).

Example usage:
    
    
    # Check if requests to a specific endpoint contain any content objects larger than 500 KB (512,000 bytes)
    any(cf.waf.content_scan.obj_sizes[*] > 512000) and http.request.uri.path eq "/upload"

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
