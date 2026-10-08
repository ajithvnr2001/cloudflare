---
url: https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/deploy-cmr-wordpress-block/
title: Use tag overrides to set WordPress rules to Block \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:01.903852+00:00
---

# Use tag overrides to set WordPress rules to Block · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/deploy-cmr-wordpress-block/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Work with managed rulesets](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/)

  4. /[Override examples](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/)
  5. /Set WordPress rules to Block



# Set WordPress rules to Block

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/deploy-cmr-wordpress-block/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewZone-level exampleAccount-level example

Follow the steps below to create a rule that executes a managed ruleset and defines an override for rules with a specific tag.

  1. [Add a rule](https://developers.cloudflare.com/ruleset-engine/basic-operations/deploy-rulesets/) to a phase entry point ruleset that executes a managed ruleset.
  2. [Configure a tag override](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-managed-ruleset/) that sets a specified action for all rules with a given tag.



## Zone-level example

This example uses the [Update a zone entry point ruleset](https://developers.cloudflare.com/ruleset-engine/rulesets-api/update/) operation to perform the following two steps in a single `PUT` request:

  * Set the list of rules in the `http_request_firewall_managed` phase entry point ruleset to a single rule that executes the [Cloudflare Managed Ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/cloudflare-managed-ruleset/).
  * Override rules with the `wordpress` tag to set the action to `block`. All other rules use the default action provided by the ruleset issuer.



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
    										"categories": [
    												{
    														"category": "wordpress",
    														"action": "block"
    												}
    										]
    								}
    						}
    				}
    		]
    	}'

## Account-level example

This example uses the [Update an account entry point ruleset](https://developers.cloudflare.com/ruleset-engine/rulesets-api/update/) operation to perform the following two steps in a single `PUT` request:

  * Set the list of rules in the `http_request_firewall_managed` phase entry point ruleset to a single rule that executes the [Cloudflare Managed Ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/cloudflare-managed-ruleset/) for the zone `example.com`.
  * Override rules with the `wordpress` tag to set the action to `block`. All other rules use the default action provided by the ruleset issuer.



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
    										"categories": [
    												{
    														"category": "wordpress",
    														"action": "block"
    												}
    										]
    								}
    						}
    				}
    		]
    	}'

[PreviousOverview](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/)[NextEnable only Joomla rules](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/deploy-cmr-joomla-only/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ruleset-engine/managed-rulesets/override-examples/deploy-cmr-wordpress-block.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
