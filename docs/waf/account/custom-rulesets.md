---
url: https://developers.cloudflare.com/waf/account/custom-rulesets/
title: Custom rulesets (account level) \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:23.667856+00:00
---

# Custom rulesets (account level) · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/account/custom-rulesets/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /[Account-level configuration](https://developers.cloudflare.com/waf/account/)
  4. /Custom rulesets



# Custom rulesets (account level)

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/account/custom-rulesets/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNext steps

Custom rulesets are collections of custom rules that you can deploy at the account or [zone level](https://developers.cloudflare.com/waf/custom-rules/custom-rulesets/).

Like [custom rules](https://developers.cloudflare.com/waf/custom-rules/) at the zone level, custom rulesets allow you to control incoming traffic by filtering requests.

Account-level custom rulesets allow you to define a set of custom rules once and apply them across multiple Enterprise zones in your account. Instead of configuring each zone individually, you create a ruleset at the account level and use expressions to control which zones and traffic it applies to.

At the zone level, all customers can create and deploy custom rulesets. Custom rulesets at the account level require an Enterprise plan. For more details, refer to [Availability](https://developers.cloudflare.com/waf/custom-rules/#availability).

## Next steps

Refer to the following pages for more information on working with custom rulesets:

  * [Work with custom rulesets in the dashboard](https://developers.cloudflare.com/waf/account/custom-rulesets/create-dashboard/)
  * [Work with custom rulesets using the API](https://developers.cloudflare.com/waf/account/custom-rulesets/create-api/)



For Terraform examples, refer to [WAF custom rules configuration using Terraform](https://developers.cloudflare.com/terraform/additional-configurations/waf-custom-rules/#create-and-deploy-a-custom-ruleset).

[PreviousOverview](https://developers.cloudflare.com/waf/account/)[NextUse the dashboard](https://developers.cloudflare.com/waf/account/custom-rulesets/create-dashboard/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/account/custom-rulesets/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
