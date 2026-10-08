---
url: https://developers.cloudflare.com/waf/custom-rules/use-cases/block-traffic-from-specific-countries/
title: Block traffic from specific countries \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:38.582766+00:00
---

# Block traffic from specific countries · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/use-cases/block-traffic-from-specific-countries/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)

  4. /Common use cases
  5. /Block traffic from specific countries



# Block traffic from specific countries

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-traffic-from-specific-countries/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOther resources

This example [custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) blocks requests based on country code using the [`ip.src.country`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.country/) field.

  * **When incoming requests match** :

Field | Operator | Value  
---|---|---  
Country | is in | `Korea, North`  
  
If you are using the expression editor:  
`(ip.src.country in {"KP"})`

  * **Then take action** : _Block_




## Other resources

  * [Use case: Block traffic by geographical location](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/)
  * [Use case: Allow traffic from specific countries only](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-specific-countries/)



[PreviousBlock traffic by geographical location](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/)[NextBlock Worker subrequests from other zones](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-worker-subrequests/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/use-cases/block-traffic-from-specific-countries.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
