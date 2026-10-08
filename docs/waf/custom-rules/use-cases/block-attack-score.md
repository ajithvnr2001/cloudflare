---
url: https://developers.cloudflare.com/waf/custom-rules/use-cases/block-attack-score/
title: Block requests by attack score \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:38.169765+00:00
---

# Block requests by attack score · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/use-cases/block-attack-score/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)

  4. /Common use cases
  5. /Block requests by attack score



# Block requests by attack score

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-attack-score/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [attack score](https://developers.cloudflare.com/waf/detections/attack-score/) helps identify variations of known attacks and their malicious payloads.

This example [custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) blocks requests based on country code ([ISO 3166-1 Alpha 2 ↗︎](https://www.iso.org/obp/ui/#search/code/) format), from requests with an attack score lower than 20. For more information, refer to [WAF attack score](https://developers.cloudflare.com/waf/detections/attack-score/).

  * **When incoming requests match** :

Field | Operator | Value | Logic  
---|---|---|---  
Country | is in | `China`, `Taiwan`, `United Kingdom`, `United States` | And  
WAF Attack Score | less than | `20` |   
  
If you are using the expression editor:  
`(ip.src.country in {"CN" "TW" "US" "GB"} and cf.waf.score lt 20)`

  * **Then take action** : _Block_




[PreviousBlock Microsoft Exchange Autodiscover requests](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-ms-exchange-autodiscover/)[NextBlock traffic by geographical location](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/use-cases/block-attack-score.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
