---
url: https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/configure-api/
title: Configure exposed credentials checks via API \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:43.291817+00:00
---

# Configure exposed credentials checks via API · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/configure-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Managed rules](https://developers.cloudflare.com/waf/managed-rules/)

  4. /[Check for exposed credentials](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/)
  5. /Configure via API



# Configure exposed credentials checks via API

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/configure-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a custom rule checking for exposed credentials Example A Example B

Deprecation notice

Exposed credentials check has been deprecated.

Switch from exposed credentials check to [leaked credentials detection](https://developers.cloudflare.com/waf/detections/leaked-credentials/) for improved security. To upgrade your current configuration, refer to the [upgrade guide](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/).

Configure exposed credentials checks using the [Rulesets API](https://developers.cloudflare.com/ruleset-engine/rulesets-api/). You can do the following:

  * [Deploy the Cloudflare Exposed Credentials Check Managed Ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/exposed-credentials-check/#configure-via-api).
  * Create custom rules that check for exposed credentials.



If you are using Terraform, refer to [Configure exposed credentials checks using Terraform](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/configure-terraform/).

## Create a custom rule checking for exposed credentials

Note

This feature requires [account-level WAF configuration](https://developers.cloudflare.com/waf/account/), which is available to Enterprise customers with a paid add-on.

You can create rules that check for exposed credentials using the [Rulesets API](https://developers.cloudflare.com/ruleset-engine/rulesets-api/). Include these rules in a custom ruleset, which you must create at the account level, and then deploy the custom ruleset to a phase.

A rule checking for exposed credentials has a match when both the rule expression and the result from the exposed credentials check are true.

To check for exposed credentials in a custom rule, include the `exposed_credential_check` object in the rule definition. This object must have the following properties:

  * `username_expression` — Expression that selects the user ID used in the credentials check. This property can have up to 1024 characters.
  * `password_expression` — Expression that selects the password used in the credentials check. This property can have up to 1024 characters.



Note

These properties have additional requirements:

  * Each expression must evaluate to a string.
  * You can only use the [`upper()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#upper), [`lower()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#lower), [`url_decode()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#url_decode), and [`lookup_json_string()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#lookup_json_string) functions, and you cannot nest these functions.



You can use the `exposed_credential_check` object in rules with one of the following actions: `rewrite`, `log`, `block`, `js_challenge` (Non-Interactive Challenge), or `challenge` (Interactive Challenge). Cloudflare recommends that you only use exposed credentials checks with the following actions: `rewrite` and `log`.

To create and deploy a custom ruleset, follow the workflow described in [Work with custom rulesets](https://developers.cloudflare.com/ruleset-engine/custom-rulesets/).

### Example A

This `POST` request example creates a new custom ruleset with a rule that checks for exposed credentials. The rule has a match if both the rule expression and the `exposed_credential_check` result are `true`. When there is a match, the rule will log the request with exposed credentials in the Cloudflare logs.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Account WAF Write`
  * `Account Rulesets Write`

Create an account rulesetbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/rulesets" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"name": "Custom Ruleset A",
    		"kind": "custom",
    		"description": "This ruleset includes a rule checking for exposed credentials.",
    		"rules": [
    				{
    						"action": "log",
    						"description": "Exposed credentials check on login.php page",
    						"expression": "http.request.method == \"POST\" && http.request.uri == \"/login.php\"",
    						"exposed_credential_check": {
    								"username_expression": "url_decode(http.request.body.form[\"username\"][0])",
    								"password_expression": "url_decode(http.request.body.form[\"password\"][0])"
    						}
    				}
    		],
    		"phase": "http_request_firewall_custom"
    	}'

The response returns the created ruleset. Note the presence of the `exposed_credential_check` object on the rule definition.
    
    
    {
    	"result": {
    		"id": "<CUSTOM_RULESET_ID>",
    		"name": "Custom Ruleset A",
    		"description": "This ruleset includes a rule checking for exposed credentials.",
    		"kind": "custom",
    		"version": "1",
    		"rules": [
    			{
    				"id": "<CUSTOM_RULE_ID>",
    				"version": "1",
    				"action": "log",
    				"description": "Exposed credentials check on login.php page",
    				"expression": "http.request.method == \"POST\" && http.request.uri == \"/login.php\"",
    				"exposed_credential_check": {
    					"username_expression": "url_decode(http.request.body.form[\"username\"][0])",
    					"password_expression": "url_decode(http.request.body.form[\"password\"][0])"
    				},
    				"last_updated": "2021-03-19T10:48:04.057775Z",
    				"ref": "<CUSTOM_RULE_REF>",
    				"enabled": true
    			}
    		],
    		"last_updated": "2021-03-19T10:48:04.057775Z",
    		"phase": "http_request_firewall_custom"
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

The example uses the `url_decode()` function because fields in the request body (available in `http.request.body.form`) are URL-encoded when the content type is `application/x-www-form-urlencoded`.

After creating the custom ruleset, deploy it to a phase so that it executes. You will need the ruleset ID to deploy the custom ruleset. For more information, refer to [Deploy a custom ruleset](https://developers.cloudflare.com/ruleset-engine/custom-rulesets/deploy-custom-ruleset/).

### Example B

This `POST` request example creates a new custom ruleset with a rule that checks for exposed credentials in JSON responses. The rule has a match if both the rule expression and the `exposed_credential_check` result are `true`. When there is a match, the rule will add an `Exposed-Credential-Check` HTTP header to the request with value `1`.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Account WAF Write`
  * `Account Rulesets Write`

Create an account rulesetbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/rulesets" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"name": "Custom Ruleset B",
    		"kind": "custom",
    		"description": "This ruleset includes a rule checking for exposed credentials.",
    		"rules": [
    				{
    						"action": "rewrite",
    						"action_parameters": {
    								"headers": {
    										"Exposed-Credential-Check": {
    												"operation": "set",
    												"value": "1"
    										}
    								}
    						},
    						"description": "Exposed credentials check on login endpoint with JSON body",
    						"expression": "http.request.method == \"POST\" && http.request.uri == \"/login.php\" && any(http.request.headers[\"content-type\"][*] == \"application/json\")",
    						"exposed_credential_check": {
    								"username_expression": "lookup_json_string(http.request.body.raw, \"username\")",
    								"password_expression": "lookup_json_string(http.request.body.raw, \"password\")"
    						}
    				}
    		],
    		"phase": "http_request_firewall_custom"
    	}'

The response returns the created ruleset. Note the presence of the following elements in the rule definition:

  * The `rewrite` action.
  * The `action_parameters` object configuring the HTTP header added to requests with exposed credentials.
  * The `exposed_credential_check` object.


    
    
    {
    	"result": {
    		"id": "<CUSTOM_RULESET_ID>",
    		"name": "Custom Ruleset B",
    		"description": "This ruleset includes a rule checking for exposed credentials.",
    		"kind": "custom",
    		"version": "1",
    		"rules": [
    			{
    				"id": "<CUSTOM_RULE_ID>",
    				"version": "1",
    				"action": "rewrite",
    				"action_parameters": {
    					"headers": {
    						"Exposed-Credential-Check": {
    							"operation": "set",
    							"value": "1"
    						}
    					}
    				},
    				"description": "Exposed credentials check on login endpoint with JSON body",
    				"expression": "http.request.method == \"POST\" && http.request.uri == \"/login.php\" && any(http.request.headers[\"content-type\"][*] == \"application/json\")",
    				"exposed_credential_check": {
    					"username_expression": "lookup_json_string(http.request.body.raw, \"username\")",
    					"password_expression": "lookup_json_string(http.request.body.raw, \"password\")"
    				},
    				"last_updated": "2022-03-19T12:48:04.057775Z",
    				"ref": "<CUSTOM_RULE_REF>",
    				"enabled": true
    			}
    		],
    		"last_updated": "2022-03-19T12:48:04.057775Z",
    		"phase": "http_request_firewall_custom"
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

After creating the custom ruleset, deploy it to a phase so that it executes. You will need the ruleset ID to deploy the custom ruleset. For more information, refer to [Deploy a custom ruleset](https://developers.cloudflare.com/ruleset-engine/custom-rulesets/deploy-custom-ruleset/).

[PreviousHow it works](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/how-checks-work/)[NextConfigure using Terraform](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/configure-terraform/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/managed-rules/check-for-exposed-credentials/configure-api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
