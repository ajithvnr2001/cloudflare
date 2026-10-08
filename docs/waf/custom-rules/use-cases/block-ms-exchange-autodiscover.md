---
url: https://developers.cloudflare.com/waf/custom-rules/use-cases/block-ms-exchange-autodiscover/
title: Block Microsoft Exchange Autodiscover requests \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:38.529408+00:00
---

# Block Microsoft Exchange Autodiscover requests · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/use-cases/block-ms-exchange-autodiscover/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)

  4. /Common use cases
  5. /Block Microsoft Exchange Autodiscover requests



# Block Microsoft Exchange Autodiscover requests

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-ms-exchange-autodiscover/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

In some cases, Microsoft Exchange Autodiscover service requests can be "noisy", triggering large numbers of `HTTP 404` (`Not found`) errors.

This example [custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) blocks requests for `autodiscover.xml` and `autodiscover.src`:

  * **When incoming requests match** :

Use the expression editor:  
`(ends_with(http.request.uri.path, "/autodiscover.xml") or ends_with(http.request.uri.path, "/autodiscover.src"))`

  * **Then take action** : _Block_




Alternatively, customers on a Business or Enterprise plan can use the `matches` [comparison operator](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#comparison-operators) for the same purpose. For this example, the expression would be the following:
    
    
    (http.request.uri.path matches "/autodiscover.(xml|src)$")

[PreviousAllow traffic from specific countries only](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-specific-countries/)[NextBlock requests by attack score](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-attack-score/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/use-cases/block-ms-exchange-autodiscover.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
