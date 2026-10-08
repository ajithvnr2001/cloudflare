---
url: https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/enable-selected-rules/
title: Use rulesets and rule overrides to only enable selected rules \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:01.820027+00:00
---

# Use rulesets and rule overrides to only enable selected rules · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/enable-selected-rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Work with managed rulesets](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/)

  4. /[Override examples](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/)
  5. /Enable only selected rules



# Enable only selected rules

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/enable-selected-rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewZone-level exampleAccount-level example

Use a ruleset override and a rule override in a phase entry point ruleset to execute only selected rules in a managed ruleset.

  1. [Add a rule](https://developers.cloudflare.com/ruleset-engine/basic-operations/deploy-rulesets/) to a phase entry point ruleset that executes a managed ruleset.
  2. [Configure a ruleset override](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-managed-ruleset/) that disables all rules in the managed ruleset.
  3. [Configure a rule override](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-managed-ruleset/) to set an action for the rules you want to execute.



## Zone-level example

The following `PUT` request uses the [Update a zone entry point ruleset](https://developers.cloudflare.com/ruleset-engine/rulesets-api/update/) operation to define a configuration that executes only two rules from a managed ruleset in the `http_request_firewall_managed` phase.

In this example:

  * `"id": "<MANAGED_RULESET_ID>"` defines the managed ruleset to execute for requests in the specified zone (`$ZONE_ID`).
  * `"enabled": false` defines an override at the ruleset level to disable all rules in the managed ruleset.
  * `"rules": [{"id": "<RULE_ID_1>", "action": "block", "enabled": true}, {"id": "<RULE_ID_2>", "action": "log", "enabled": true}]` defines a list of overrides at the rule level to enable two individual rules.



Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Response Compression Write`
  * `Config Settings Write`
  * `Dynamic URL Redirects Write`
  * `Cache Settings Write`
  * `Custom Errors Write`
  * `Origin Write`
  * `Managed headers Write`
  * `Zone Transform Rules Write`
  * `Mass URL Redirects Write`
  * `Magic Firewall Write`
  * `L4 DDoS Managed Ruleset Write`
  * `HTTP DDoS Managed Ruleset Write`
  * `Sanitize Write`
  * `Transform Rules Write`
  * `Select Configuration Write`
  * `Bot Management Write`
  * `Zone WAF Write`
  * `Account WAF Write`
  * `Account Rulesets Write`
  * `Logs Write`
  * `Logs Write`

Update a zone entry point rulesetbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/phases/http_request_firewall_managed/entrypoint" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"rules": [
    				{
    						"action": "execute",
    						"expression": "true",
    						"action_parameters": {
    								"id": "<MANAGED_RULESET_ID>",
    								"overrides": {
    										"enabled": false,
    										"rules": [
    												{
    														"id": "<RULE_ID_1>",
    														"action": "block",
    														"enabled": true
    												},
    												{
    														"id": "<RULE_ID_2>",
    														"action": "log",
    														"enabled": true
    												}
    										]
    								}
    						}
    				}
    		]
    	}'

## Account-level example

The following `PUT` request uses the [Update an account entry point ruleset](https://developers.cloudflare.com/ruleset-engine/rulesets-api/update/) operation to define a configuration that executes only two rules from a managed ruleset in the `http_request_firewall_managed` phase.

In this example:

  * `"id": "<MANAGED_RULESET_ID>"` defines the managed ruleset to execute for requests addressed to `example.com`.
  * `"enabled": false` defines an override at the ruleset level to disable all rules in the managed ruleset.
  * `"rules": [{"id": "<RULE_ID_1>", "action": "block", "enabled": true}, {"id": "<RULE_ID_2>", "action": "log", "enabled": true}]` defines a list of overrides at the rule level to enable two individual rules.



Note

At the account level, the rule expression of an `execute` rule must end with `and cf.zone.plan eq "ENT"` so that it only applies to zones on an Enterprise plan.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Mass URL Redirects Write`
  * `Magic Firewall Write`
  * `L4 DDoS Managed Ruleset Write`
  * `Transform Rules Write`
  * `Select Configuration Write`
  * `Account WAF Write`
  * `Account Rulesets Write`
  * `Logs Write`

Update an account entry point rulesetbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/rulesets/phases/http_request_firewall_managed/entrypoint" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"rules": [
    				{
    						"action": "execute",
    						"expression": "cf.zone.name eq \"example.com\" and cf.zone.plan eq \"ENT\"",
    						"action_parameters": {
    								"id": "<MANAGED_RULESET_ID>",
    								"overrides": {
    										"enabled": false,
    										"rules": [
    												{
    														"id": "<RULE_ID_1>",
    														"action": "block",
    														"enabled": true
    												},
    												{
    														"id": "<RULE_ID_2>",
    														"action": "log",
    														"enabled": true
    												}
    										]
    								}
    						}
    				}
    		]
    	}'

[PreviousEnable only Joomla rules](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/deploy-cmr-joomla-only/)[NextDeploy a managed ruleset with ruleset, tag, and rule overrides](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/override-ruleset-tag-rule/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ruleset-engine/managed-rulesets/override-examples/enable-selected-rules.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
