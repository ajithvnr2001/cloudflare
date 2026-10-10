---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.host/
title: http.host \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:33.344466+00:00
---

# http.host · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.host/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Host



# http.host

`http.host``String`

The hostname used in the full request URI.

The `http.host` field contains the `Host` header from the original client request.

If you have configured [Origin Rules](https://developers.cloudflare.com/rules/origin-rules/) that change the hostname, this change is not reflected in the `http.host` value seen by other rule phases (such as custom rules, cache rules, or transform rules) or [Cloudflare Workers](https://developers.cloudflare.com/workers/). All rule phases and Workers evaluate against the original, unmodified host.

Example value:
    
    
    "www.example.org"

Categories: 

  * Request
  * URI



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
