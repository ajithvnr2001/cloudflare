---
url: https://developers.cloudflare.com/rules/configuration-rules/create-api/
title: Create a configuration rule via API \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:47.674044+00:00
---

# Create a configuration rule via API · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/configuration-rules/create-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/)
  4. /Create a rule via API



# Create a configuration rule via API

Last updated Aug 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/configuration-rules/create-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBasic rule settingsProcedureExample requestsRequired API token permissions

Use the [Rulesets API](https://developers.cloudflare.com/ruleset-engine/rulesets-api/) to create configuration rules via API.

## Basic rule settings

When creating a configuration rule via API, make sure you:

  * Set the rule action to `set_config`.
  * Define the parameters in the `action_parameters` field according to the [settings](https://developers.cloudflare.com/rules/configuration-rules/settings/) you wish to override for matching requests.
  * Deploy the rule to the `http_config_settings` phase at the zone level.



## Procedure

Follow this workflow to create a configuration rule for a given zone via API:

  1. Use the [List zone rulesets](https://developers.cloudflare.com/api/resources/rulesets/methods/list/) operation to check if there is already a ruleset for the `http_config_settings` phase at the zone level.

  2. If the phase ruleset does not exist, create it using the [Create a zone ruleset](https://developers.cloudflare.com/api/resources/rulesets/methods/create/) operation. In the new ruleset properties, set the following values:

     * **kind** : `zone`
     * **phase** : `http_config_settings`
  3. Use the [Update a zone ruleset](https://developers.cloudflare.com/api/resources/rulesets/methods/update/) operation to add a configuration rule to the list of ruleset rules. Alternatively, include the rule in the [Create a zone ruleset](https://developers.cloudflare.com/api/resources/rulesets/methods/create/) request mentioned in the previous step.




Make sure your API token has the required permissions to perform the API operations.

## Example requests

Example: Add a rule that enables Email Obfuscation and Browser Integrity Check

The following example sets the rules of an existing phase ruleset (`{ruleset_id}`) to a single configuration rule — enabling Email Obfuscation and Browser Integrity Check for the contacts page — using the [Update a zone ruleset](https://developers.cloudflare.com/api/resources/rulesets/methods/update/) operation:

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

Update a zone rulesetbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/$RULESET_ID" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"rules": [
    				{
    						"ref": "enable_email_obfuscation_bic",
    						"expression": "starts_with(http.request.uri.path, \"/contact-us/\")",
    						"description": "Obfuscates email addresses and enables BIC in contacts page",
    						"action": "set_config",
    						"action_parameters": {
    								"email_obfuscation": true,
    								"bic": true
    						}
    				}
    		]
    	}'

Use the `ref` field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to [Troubleshooting](https://developers.cloudflare.com/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications) in the Terraform documentation.

Example: Add a rule that turns on Under Attack mode for the admin area

The following example sets the rules of an existing phase ruleset (`{ruleset_id}`) to a single configuration rule — turning on Under Attack mode for the administration area — using the [Update a zone ruleset](https://developers.cloudflare.com/api/resources/rulesets/methods/update/) operation:

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

Update a zone rulesetbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/$RULESET_ID" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"rules": [
    				{
    						"ref": "enable_under_attack_in_admin",
    						"expression": "http.host eq \"admin.example.com\"",
    						"description": "Turn on Under Attack mode for admin area",
    						"action": "set_config",
    						"action_parameters": {
    								"security_level": "under_attack"
    						}
    				}
    		]
    	}'

Use the `ref` field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to [Troubleshooting](https://developers.cloudflare.com/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications) in the Terraform documentation.

* * *

## Required API token permissions

The API token used in API requests to manage configuration rules must have at least the following permission:

  * _Zone_ > _Config Rules_ > _Edit_



[PreviousCreate a rule in the dashboard](https://developers.cloudflare.com/rules/configuration-rules/create-dashboard/)[NextAvailable settings](https://developers.cloudflare.com/rules/configuration-rules/settings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/configuration-rules/create-api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
