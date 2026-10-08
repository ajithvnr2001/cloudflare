---
url: https://developers.cloudflare.com/rules/snippets/create-api/
title: Configure Snippets via API \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:52.451078+00:00
---

# Configure Snippets via API · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/create-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Snippets](https://developers.cloudflare.com/rules/snippets/)
  4. /Configure via API



# Configure Snippets via API

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/create-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRequired permissionsEndpointsExample API calls Create/update code snippet Create/update/delete snippet rules

You can create Snippets using the [Cloudflare API](https://developers.cloudflare.com/fundamentals/api/).

## Required permissions

The [API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) used in API requests to manage Snippets must have at least the following permission:

  * _Zone_ > _Snippets_ > _Edit_



Note

A token with this permission is only valid for the Snippets endpoints described in this page. You cannot use it to interact with the `http_request_snippets` phase via [Rulesets API](https://developers.cloudflare.com/ruleset-engine/rulesets-api/).

## Endpoints

To obtain the complete endpoint, append the Snippets endpoints listed below to the Cloudflare API base URL:
    
    
    https://api.cloudflare.com/client/v4

The `{zone_id}` argument is the [zone ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) (a hexadecimal string). You can find this value in the Cloudflare dashboard.

The following table summarizes the available operations.

Operation | Verb + Endpoint  
---|---  
List all code snippets | `GET /zones/{zone_id}/snippets`  
Create/update code snippet | `PUT /zones/{zone_id}/snippets/{snippet_name}`  
Get code snippet details | `GET /zones/{zone_id}/snippets/{snippet_name}`  
Get code snippet content | `GET /zones/{zone_id}/snippets/{snippet_name}/content`  
Delete code snippet | `DELETE /zones/{zone_id}/snippets/{snippet_name}`  
List snippet rules | `GET /zones/{zone_id}/snippets/snippet_rules`  
Create/update/delete snippet rules | `PUT /zones/{zone_id}/snippets/snippet_rules`  
Delete all snippet rules | `DELETE /zones/{zone_id}/snippets/snippet_rules`  
  
## Example API calls

### Create/update code snippet

To create or update a Snippet, use the following `PUT` request. The snippet is named `$SNIPPET_NAME` and the body contains the JavaScript code.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Snippets Write`

Update a zone snippetbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/snippets/$SNIPPET_NAME" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--form "files=@example.js" \
    	--form "metadata={\"main_module\": \"example.js\"}"

The name of a snippet can only contain the characters `a-z`, `0-9`, and `_` (underscore). The name must be unique in the context of the zone. You cannot change the snippet name after creating the snippet.

The required body parameters are:

  * `files`: The file with your JavaScript code.
  * `metadata`: Object containing `main_module`, which must match the filename of the uploaded file.



To make this example work, save your JavaScript code in a file named `example.js`, and then execute `curl` command with a `PUT` request from the folder where `example.js` is located.

Example responsejson
    
    
    {
    	"errors": [],
    	"messages": [],
    	"success": true,
    	"result": {
    		"created_on": "2023-07-24-00:00:00",
    		"modified_on": "2023-07-24-00:00:00",
    		"snippet_name": "snippet_name_01"
    	}
    }

To deploy a new snippet you must create a snippet rule. The expression of the snippet rule defines when the snippet code will run.

### Create/update/delete snippet rules

Caution

When using this endpoint to create a new rule and keep existing rules, you must include all rules in the request body. Omitting an existing rule will delete the corresponding rule.

Once you have created a code snippet, you can link it to rules. This is done via the following `PUT` request to the `snippet_rules` endpoint.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Snippets Write`

Update zone snippet rulesbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/snippets/snippet_rules" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"rules": [
    				{
    						"description": "Trigger snippet on specific cookie",
    						"enabled": true,
    						"expression": "http.cookie eq \"a=b\"",
    						"snippet_name": "snippet_name_01"
    				}
    		]
    	}'

[PreviousCreate in the dashboard](https://developers.cloudflare.com/rules/snippets/create-dashboard/)[NextConfigure using Terraform](https://developers.cloudflare.com/rules/snippets/create-terraform/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/create-api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
