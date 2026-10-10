---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.full_uri/
title: http.request.full_uri \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:32.786255+00:00
---

# http.request.full_uri · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.full_uri/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Full_uri



# http.request.full_uri

`http.request.full_uri``String`

The full URI as received by the web server.

The value will not include the `#fragment` part, which is not sent to web servers.

Example value:
    
    
    "https://www.example.org/articles/index?section=539061&expand=comments"

Categories: 

  * Request
  * URI



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
