---
url: https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/
title: Create WAF exceptions \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:45.610884+00:00
---

# Create WAF exceptions · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /[Managed rules](https://developers.cloudflare.com/waf/managed-rules/)
  4. /Create exceptions



# Create exceptions

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTypes of exceptionsScope and execution orderNext steps

Create an exception to skip the execution of WAF managed rulesets or some of their rules. The exception configuration includes an expression that defines the skip conditions, and the rules or rulesets to skip under those conditions.

## Types of exceptions

An exception can have one of the following behaviors (from highest to lowest priority):

  * Skip all remaining rules (belonging to WAF managed rulesets)
  * Skip one or more WAF managed rulesets
  * Skip one or more rules of WAF managed rulesets



For more information on exceptions, refer to [Create an exception](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/create-exception/) in the Ruleset Engine documentation.

## Scope and execution order

You can define exceptions at the account level and at the zone level. The scope of an exception determines which rules it affects:

  * An account-level exception only skips rules configured at the account level. It does not affect zone-level rules.
  * A zone-level exception only skips rules configured at the zone level. It does not affect account-level rules.



Within each phase, account-level rulesets run before zone-level rulesets. This means that if you deploy managed rules at both the account level and the zone level, a request is evaluated against account-level rules first. An exception defined at the zone level will not prevent a match at the account level.

For more information on how WAF features run in sequence, refer to [Security features interoperability](https://developers.cloudflare.com/waf/feature-interoperability/).

Note

Exceptions apply to WAF managed rulesets only. To skip other security features such as [Browser Integrity Check](https://developers.cloudflare.com/waf/tools/browser-integrity-check/) or [Zone Lockdown](https://developers.cloudflare.com/waf/tools/zone-lockdown/), create a custom rule with the [skip action](https://developers.cloudflare.com/waf/custom-rules/skip/) and select the specific products you want to skip.

## Next steps

Add exceptions [in the Cloudflare dashboard](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/define-dashboard/) or [via API](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/define-api/).

[PreviousTroubleshooting](https://developers.cloudflare.com/waf/managed-rules/troubleshooting/)[NextAdd an exception in the dashboard](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/define-dashboard/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/managed-rules/waf-exceptions/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
