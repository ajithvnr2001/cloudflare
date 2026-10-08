---
url: https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/override-ddos-rule-sensitivity/
title: Adjust the sensitivity of an HTTP DDoS rule to Low \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:01.971182+00:00
---

# Adjust the sensitivity of an HTTP DDoS rule to Low · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/override-ddos-rule-sensitivity/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Work with managed rulesets](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/)

  4. /[Override examples](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/)
  5. /Adjust the sensitivity of an HTTP DDoS rule to Low



# Adjust the sensitivity of an HTTP DDoS rule to Low

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/override-ddos-rule-sensitivity/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExample

Follow the steps below to override the sensitivity of a specific rule of the Cloudflare HTTP DDoS Attack Protection managed ruleset.

  1. [Add a rule](https://developers.cloudflare.com/ruleset-engine/basic-operations/deploy-rulesets/) to a phase to deploy the Cloudflare HTTP DDoS Attack Protection managed ruleset. You only need to deploy this specific ruleset when you wish to define one or more overrides, since it is enabled by default.
  2. [Configure a rule override](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-managed-ruleset/) that sets the `sensitivity_level` of a specific rule.



## Example

The following example uses the [Update a zone entry point ruleset](https://developers.cloudflare.com/ruleset-engine/rulesets-api/update/) operation to execute the two steps in a single `PUT` request.

  * Set the rules in the `ddos_l7` phase entry point ruleset to a single rule that executes the Cloudflare HTTP DDoS Attack Protection managed ruleset (with ID `<HTTP_DDOS_RULESET_ID>`).
  * Create an override for the rule with ID `<RULE_ID>` and set the rule sensitivity to `low`. All other rules use the default sensitivity defined by Cloudflare.



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
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/phases/ddos_l7/entrypoint" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"rules": [
    				{
    						"action": "execute",
    						"expression": "true",
    						"action_parameters": {
    								"id": "<HTTP_DDOS_RULESET_ID>",
    								"overrides": {
    										"rules": [
    												{
    														"id": "<RULE_ID>",
    														"sensitivity_level": "low"
    												}
    										]
    								}
    						}
    				}
    		]
    	}'

[PreviousDeploy a managed ruleset with ruleset, tag, and rule overrides](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-examples/override-ruleset-tag-rule/)[NextAdjust an L3/4 DDoS rule ↗︎](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/configure-api/#configure-an-override-for-the-network-layer-ddos-attack-protection-managed-ruleset)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ruleset-engine/managed-rulesets/override-examples/override-ddos-rule-sensitivity.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
