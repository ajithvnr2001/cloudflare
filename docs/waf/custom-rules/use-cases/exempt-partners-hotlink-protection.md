---
url: https://developers.cloudflare.com/waf/custom-rules/use-cases/exempt-partners-hotlink-protection/
title: Exempt partners from Hotlink Protection \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:38.983260+00:00
---

# Exempt partners from Hotlink Protection · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/use-cases/exempt-partners-hotlink-protection/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)

  4. /Common use cases
  5. /Exempt partners from Hotlink Protection



# Exempt partners from Hotlink Protection

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/exempt-partners-hotlink-protection/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAllow requests from partners using custom rulesAllow requests from partners using Configuration Rules

When enabled, [Cloudflare Hotlink Protection](https://developers.cloudflare.com/waf/tools/scrape-shield/hotlink-protection/) blocks all HTTP referrers that are not part of your domain or zone. That presents a problem if you allow partners to use inline links to your assets.

## Allow requests from partners using custom rules

You can use custom rules to protect against hotlinking while allowing inline links from your partners. In this case, you will need to disable [Hotlink Protection](https://developers.cloudflare.com/waf/tools/scrape-shield/hotlink-protection/) so that partner referrals are not blocked by that feature.

This example [custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) uses the [`http.referer`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.referer/) field to target HTTP referrals from partner sites.

The `not` operator matches HTTP referrals that are not from partner sites, and the action blocks them:

  * **When incoming requests match** :

Use the expression editor:  
`not (http.referer contains "example.com" or http.referer eq "www.example.net" or http.referer eq "www.cloudflare.com")`

  * **Then take action** : _Block_




## Allow requests from partners using Configuration Rules

Alternatively, you can [create a configuration rule](https://developers.cloudflare.com/rules/configuration-rules/create-dashboard/) to exclude HTTP referrals from partner sites from Hotlink Protection. In this case, you would keep the Hotlink Protection feature enabled.

[PreviousConfigure token authentication](https://developers.cloudflare.com/waf/custom-rules/use-cases/configure-token-authentication/)[NextIssue challenge for admin user in JWT claim based on attack score](https://developers.cloudflare.com/waf/custom-rules/use-cases/check-jwt-claim-to-protect-admin-user/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/use-cases/exempt-partners-hotlink-protection.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
