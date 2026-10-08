---
url: https://developers.cloudflare.com/cache/how-to/cache-rules/create-api/
title: Create a cache rule via API \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:42.572926+00:00
---

# Create a cache rule via API · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/how-to/cache-rules/create-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /…

Cache configuration

  4. /[Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/)
  5. /Create a rule via API



# Create a rule via API

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/create-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBasic rule settingsProcedureExample requestsRequired API token permissions

Use the [Rulesets API](https://developers.cloudflare.com/ruleset-engine/rulesets-api/) to create a cache rule via API. To configure Cloudflare’s API refer to the [API documentation](https://developers.cloudflare.com/fundamentals/api/get-started/).

## Basic rule settings

When creating a cache rule via API, make sure you:

  * Set the rule action to `set_cache_settings`.
  * Define the parameters in the `action_parameters` field according to the [settings](https://developers.cloudflare.com/cache/how-to/cache-rules/settings/) you wish to override for matching requests.
  * Deploy the rule to the `http_request_cache_settings` phase entry point ruleset.



## Procedure

  1. Use the [List zone rulesets](https://developers.cloudflare.com/api/resources/rulesets/methods/list/) method to obtain the list of rules already present in the `http_request_cache_settings` phase entry point ruleset.
  2. If the phase ruleset does not exist, create it using the [Create a zone ruleset](https://developers.cloudflare.com/api/resources/rulesets/methods/create/) operation. In the new ruleset properties, set the following values: 
     * kind: `zone`
     * phase: `http_request_cache_settings`
  3. Use the [Update a zone ruleset](https://developers.cloudflare.com/api/resources/rulesets/methods/update/) operation to add a cache rule to the list of ruleset rules. Alternatively, include the rule in the [Create a zone ruleset](https://developers.cloudflare.com/api/resources/rulesets/methods/create/) request mentioned in the previous step.
  4. (Optional) To update an existing cache rule, use the [Update a zone ruleset rule](https://developers.cloudflare.com/api/resources/rulesets/methods/update/) operation. For an example, refer to the section below.



## Example requests

These examples are setting all the Cache Rules of a zone to a single rule, since using these examples directly will cause any existing rules to be deleted.

Example: Cache everything for example.com

Update a zone rulesetbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/$RULESET_ID" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"rules": [
    				{
    						"expression": "(http.host eq \"example.com\")",
    						"description": "cache everything for example.com",
    						"action": "set_cache_settings",
    						"action_parameters": {
    								"cache": true
    						}
    				}
    		]
    	}'

Example: Extend read timeout for Android clients

Update a zone rulesetbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/$RULESET_ID" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"rules": [
    				{
    						"expression": "(http.user_agent contains \"Android\")",
    						"description": "extend read timeout for android clients",
    						"action": "set_cache_settings",
    						"action_parameters": {
    								"cache": true,
    								"read_timeout": 300
    						}
    				}
    		]
    	}'

Example: Disable Cache Reserve for frequently updated assets

Update a zone rulesetbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/$RULESET_ID" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"rules": [
    				{
    						"expression": "(starts_with(http.request.uri, \"/feed/\"))",
    						"description": "disable cache reserve for frequently updated assets",
    						"action": "set_cache_settings",
    						"action_parameters": {
    								"cache": true,
    								"cache_reserve": {
    										"enabled": false
    								}
    						}
    				}
    		]
    	}'

Example: Turn on Origin Range Requests for large media files

Update a zone entry point rulesetbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/phases/http_request_cache_settings/entrypoint" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"rules": [
    				{
    						"expression": "(http.request.uri.path.extension in {\"mp4\" \"mov\" \"m4v\"})",
    						"description": "turn on origin range requests for large media files",
    						"action": "set_cache_settings",
    						"action_parameters": {
    								"cache": true,
    								"origin_range_requests": {
    										"mode": "on"
    								}
    						}
    				}
    		]
    	}'

Example: Turn off default Origin Range Requests

Update a zone entry point rulesetbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/phases/http_request_cache_settings/entrypoint" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"rules": [
    				{
    						"expression": "true",
    						"description": "turn off default Origin Range Requests",
    						"action": "set_cache_settings",
    						"action_parameters": {
    								"origin_range_requests": {
    										"mode": "off"
    								}
    						}
    				}
    		]
    	}'

Example: Turn off default cache TTLs

Update a zone rulesetbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/$RULESET_ID" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"rules": [
    				{
    						"expression": "(http.host eq \"example.com\")",
    						"description": "turn off default cache ttls",
    						"action": "set_cache_settings",
    						"action_parameters": {
    								"cache": true,
    								"edge_ttl": {
    										"mode": "bypass_by_default"
    								}
    						}
    				}
    		]
    	}'

Example: Cache expected Vary responses

Update a zone entry point rulesetbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/phases/http_request_cache_settings/entrypoint" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"rules": [
    				{
    						"expression": "(http.host eq \"example.com\")",
    						"description": "cache expected vary responses",
    						"action": "set_cache_settings",
    						"action_parameters": {
    								"cache": true,
    								"vary": {
    										"default": {
    												"action": "bypass"
    										},
    										"headers": {
    												"accept": {
    														"action": "normalize",
    														"media_types": [
    																"text/html",
    																"application/json"
    														]
    												},
    												"accept-language": {
    														"action": "normalize",
    														"languages": [
    																"en",
    																"fr",
    																"de"
    														]
    												}
    										}
    								}
    						}
    				}
    		]
    	}'

Example: Update the position of an existing rule

Update a zone ruleset rulebash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/$RULESET_ID/rules/$RULE_ID" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"expression": "(http.host eq \"example.com\")",
    		"description": "cache everything for example.com",
    		"action": "set_cache_settings",
    		"action_parameters": {
    				"cache": true
    		},
    		"enabled": true,
    		"position": {
    				"before": "da5e8e506c8e7877fe06cdf4c41add54"
    		}
    	}'

## Required API token permissions

The API token used in API requests to manage Cache Rules must have the following permissions:

  * _Zone_ > _Cache Rules_ > _Edit_
  * _Account Rulesets_ > _Edit_
  * _Account Filter Lists_ > _Edit_



[PreviousCreate a rule in the dashboard](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/)[NextTerraform example](https://developers.cloudflare.com/cache/how-to/cache-rules/terraform-example/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/how-to/cache-rules/create-api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
