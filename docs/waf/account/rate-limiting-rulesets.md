---
url: https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/
title: Rate limiting rulesets \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:31.384478+00:00
---

# Rate limiting rulesets · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /[Account-level configuration](https://developers.cloudflare.com/waf/account/)
  4. /Rate limiting rulesets



# Rate limiting rulesets

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNext steps

[Rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/) allow you to define a rate limit for requests matching an [expression](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/), and the action to perform when that rate limit is reached. You can configure rate limiting rules for a single zone or at the account level.

Account-level rate limiting rulesets allow you to define rate limiting rules once and deploy them to multiple Enterprise zones. Instead of configuring the same rules in each zone, you create a ruleset at the account level and control which zones it applies to.

To apply a rate limiting ruleset at the account level:

  1. Create a rate limiting ruleset with one or more rate limiting rules.
  2. Deploy the ruleset to one or more zones on an Enterprise plan.



For more information on how Cloudflare calculates request rates, refer to [Request rate calculation](https://developers.cloudflare.com/waf/rate-limiting-rules/request-rate/).

## Next steps

For instructions on creating and deploying a rate limiting ruleset, refer to the following pages:

  * [Create a rate limiting ruleset in the dashboard](https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/create-dashboard/)
  * [Create a rate limiting ruleset using the API](https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/create-api/)



For Terraform examples, refer to [Rate limiting rules configuration using Terraform](https://developers.cloudflare.com/terraform/additional-configurations/rate-limiting-rules/).

[PreviousUse Terraform ↗︎](https://developers.cloudflare.com/terraform/additional-configurations/waf-custom-rules/#create-and-deploy-a-custom-ruleset)[NextCreate in the dashboard](https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/create-dashboard/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/account/rate-limiting-rulesets/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
