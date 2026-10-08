---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.truncated/
title: cf.waf.content_scan.truncated \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:08.333638+00:00
---

# cf.waf.content_scan.truncated · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.truncated/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Waf.Content_scan.Truncated



# cf.waf.content_scan.truncated

`cf.waf.content_scan.truncated``Boolean`

Indicates whether the request body exceeded the size limit for content scanning and was truncated before scanning.

Requires a Cloudflare Enterprise plan with [malicious uploads detection](https://developers.cloudflare.com/waf/detections/malicious-uploads/).

When this field is true, the scan results may be incomplete. Refer to [Size limit](https://developers.cloudflare.com/waf/detections/malicious-uploads/#size-limit).

Example usage:
    
    
    # Block requests to a specific endpoint whose content was not fully scanned
    cf.waf.content_scan.truncated and http.request.uri.path eq "/upload"

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
