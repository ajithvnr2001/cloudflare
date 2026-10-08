---
url: https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/
title: Block traffic by geographical location \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:38.236184+00:00
---

# Block traffic by geographical location · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)

  4. /Common use cases
  5. /Block traffic by geographical location



# Block traffic by geographical location

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOther resources

This example [custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) blocks requests by autonomous system number (ASN), continent, or country of origin.

  * **When incoming requests match** :

Field | Operator | Value | Logic  
---|---|---|---  
AS Num | equals | `131279` | Or  
Continent | equals | `Asia` | Or  
Country | equals | `Korea, North` |   
  
If you are using the expression editor:  
`(ip.src.asnum eq 131279) or (ip.src.continent eq "AS") or (ip.src.country eq "KP")`

  * **Then take action** : _Block_




## Other resources

  * [Use case: Block traffic from specific countries](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-traffic-from-specific-countries/)
  * [Use case: Allow traffic from specific countries only](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-specific-countries/)
  * [Fields reference: Geolocation](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/?field-category=Geolocation)



[PreviousBlock requests by attack score](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-attack-score/)[NextBlock traffic from specific countries](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-traffic-from-specific-countries/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/use-cases/block-by-geographical-location.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
