---
url: https://developers.cloudflare.com/waf/custom-rules/use-cases/update-rules-customers-partners/
title: Update custom rules for customers or partners \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:39.619362+00:00
---

# Update custom rules for customers or partners · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/use-cases/update-rules-customers-partners/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)

  4. /Common use cases
  5. /Update custom rules for customers or partners



# Update custom rules for customers or partners

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/update-rules-customers-partners/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse ASN in custom rules Allow traffic by ASN Adjust rules by ASNUse IP addresses in custom rules Allow traffic by IP address Adjust rules by IP address

You may want to adjust your [custom rules](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) to increase access by customers or partners.

Potential examples include:

  * Removing rate limiting for an API
  * Sharing brand assets and marketing materials



Caution

The example custom rules in this page can bypass Cloudflare's security features and are generally not recommended. Use with caution.

## Use ASN in custom rules

If a customer or partner is large enough, you could set up a custom rule based on an [autonomous system number (ASN) ↗︎](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/).

### Allow traffic by ASN

This example uses:

  * The [`ip.src.asnum`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.asnum/) field to specify the general region.
  * The [`cf.bot_management.score`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.score/) field to ensure partner traffic does not come from bots.



Example custom rule:

  * **When incoming requests match** :

Field | Operator | Value | Logic  
---|---|---|---  
AS Num | equals | `64496` | And  
Bot Score | greater than | `30` |   
  
If you are using the expression editor:  
`(ip.src.asnum eq 64496 and cf.bot_management.score gt 30)`

  * **Then take action** : _Skip:_

    * _All remaining custom rules_



Note

Access to [Bot Management](https://developers.cloudflare.com/bots/plans/bm-subscription/) requires a Cloudflare Enterprise plan with Bot Management.

### Adjust rules by ASN

This example custom rule uses:

  * The [`ip.src.asnum`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.asnum/) field to specify the general region.
  * The [`cf.bot_management.score`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.score/) field to check if the request comes from a human.



If a request meets these criteria, the custom rule will skip [User Agent Blocking](https://developers.cloudflare.com/waf/tools/user-agent-blocking/) rules.

  * **When incoming requests match** :

Field | Operator | Value | Logic  
---|---|---|---  
AS Num | equals | `64496` | And  
Bot Score | greater than | `50` |   
  
If you are using the expression editor:  
`(ip.src.asnum eq 64496 and cf.bot_management.score gt 50)`

  * **Then take action** : _Skip:_

    * _User Agent Blocking_



## Use IP addresses in custom rules

For smaller organizations, you could set up custom rules based on IP addresses.

### Allow traffic by IP address

This example:

  * Specifies the source IP address and the host.
  * Uses the [`cf.bot_management.score`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.score/) field to ensure requests are not high-risk traffic.



Example custom rule:

  * **When incoming requests match** :

Field | Operator | Value | Logic  
---|---|---|---  
IP Source Address | equals | `203.0.113.1` | And  
Hostname | equals | `example.com` | And  
Bot Score | greater than | `30` |   
  
If you are using the expression editor:  
`(ip.src eq 203.0.113.1 and http.host eq "example.com" and cf.bot_management.score gt 30)`

  * **Then take action** : _Skip:_

    * _All remaining custom rules_



### Adjust rules by IP address

This example custom rule specifies the source IP address and the host.

If a request meets these criteria, the custom rule will skip [rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/).

  * **When incoming requests match** :

Field | Operator | Value | Logic  
---|---|---|---  
IP Source Address | equals | `203.0.113.1` | And  
Hostname | equals | `example.com` |   
  
If you are using the expression editor:  
`(ip.src eq 203.0.113.1 and http.host eq "example.com")`

  * **Then take action** : _Skip:_

    * _All remaining custom rules_



[PreviousStop R-U-Dead-Yet? (R.U.D.Y.) attacks](https://developers.cloudflare.com/waf/custom-rules/use-cases/stop-rudy-attacks/)[NextCustom rulesets](https://developers.cloudflare.com/waf/custom-rules/custom-rulesets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/use-cases/update-rules-customers-partners.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
