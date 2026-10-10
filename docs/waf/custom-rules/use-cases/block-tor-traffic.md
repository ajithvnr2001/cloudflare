---
url: https://developers.cloudflare.com/waf/custom-rules/use-cases/block-tor-traffic/
title: Block Tor traffic \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T07:57:29.336969+00:00
---

# Block Tor traffic · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/use-cases/block-tor-traffic/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)

  4. /Common use cases
  5. /Block Tor traffic



# Block Tor traffic

Last updated Oct 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare identifies requests coming from Tor exit nodes with the continent code `T1`. If you do not want Tor traffic on your zone, this example [custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) blocks requests from the Tor network using the [`ip.src.continent`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.continent/) field.

  * **When incoming requests match** :

If you are using the expression editor:  
`(ip.src.continent eq "T1")`

  * **Then take action** : _Block_




If you prefer not to block Tor traffic outright, use the _Managed Challenge_ action instead.

Note

If you block or challenge Tor traffic, disable [Onion Routing](https://developers.cloudflare.com/network/onion-routing/) on your zone. Onion Routing improves the experience of visitors using the Tor Browser, which contradicts blocking Tor traffic.

[PreviousBlock requests by attack score](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-attack-score/)[NextBlock traffic by geographical location](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/use-cases/block-tor-traffic.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
