---
url: https://developers.cloudflare.com/waf/account/
title: Account-level WAF configuration \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:22.053899+00:00
---

# Account-level WAF configuration · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/account/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /Account-level configuration



# Account-level WAF configuration

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/account/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailability

The account-level Web Application Firewall (WAF) configuration allows you to define a configuration once and apply it to multiple Enterprise zones in your account. Instead of configuring each zone individually, you create rulesets at the account level and use expressions to control which zones and traffic they apply to.

For example, you can deploy a single ruleset that applies to `/admin/*` URI paths across both `example.com` and `example.net`. Rulesets can target all incoming traffic or a specific subset.

At the account level, WAF rules are grouped into rulesets. You can perform the following operations:

  * Create and deploy [custom rulesets](https://developers.cloudflare.com/waf/account/custom-rulesets/)
  * Create and deploy [rate limiting rulesets](https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/)
  * Deploy [managed rulesets](https://developers.cloudflare.com/waf/account/managed-rulesets/)



## Availability

Account-level WAF configuration requires an Enterprise plan.

| Custom rulesets | Rate limiting rulesets | Managed rulesets  
---|---|---|---  
Availability | Yes | Yes | Yes  
Maximum number of rulesets | 10 | 10 | Not applicable  
Maximum number of rules per ruleset | 100 | 10 | Not applicable  
  
The values in the table are the default limits. Your limits may vary based on the terms of your Enterprise contract.

Custom rulesets also have a total quota of 1,000 rules across all rulesets that a request traverses.

[PreviousValidation checks](https://developers.cloudflare.com/waf/tools/validation-checks/)[NextOverview](https://developers.cloudflare.com/waf/account/custom-rulesets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/account/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
