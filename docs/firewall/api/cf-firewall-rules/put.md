---
url: https://developers.cloudflare.com/firewall/api/cf-firewall-rules/put/
title: PUT examples - Firewall rules \u00b7 Cloudflare Firewall Rules (deprecated) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:16.789408+00:00
---

# PUT examples - Firewall rules · Cloudflare Firewall Rules (deprecated) docs

> Source: https://developers.cloudflare.com/firewall/api/cf-firewall-rules/put/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Firewall Rules (deprecated)](https://developers.cloudflare.com/firewall/)
  3. /…

[Manage rules via the APIs](https://developers.cloudflare.com/firewall/api/)

  4. /[Firewall Rules API](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/)
  5. /PUT examples



# PUT examples

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/put/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUpdate multiple rulesUpdate a single rule

## Update multiple rules

This example updates several firewall rules using a single API call.

You can include up to 25 rules in the JSON object array (`-d` flag) to update as a batch. The batch is handled as a transaction.

Requestbash
    
    
    curl --request PUT \
    "https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>" \
    --header "Content-Type: application/json" \
    --data '[
      {
        "id": "<RULE_ID>",
        "paused": false,
        "description": "Challenge site",
        "action": "challenge",
        "priority": null,
        "filter": {
          "id": "<FILTER_ID>",
          "expression": "not http.request.uri.path matches \"^/api/.*$\"",
          "paused": false,
          "description": "not /api"
        }
      }
    ]'

Note

`PUT` does not update the filter specified. It only looks at the filter ID (`<FILTER_ID>`) to update the rule with a new filter.

To update the filter, use the [Filters API](https://developers.cloudflare.com/firewall/api/cf-filters/).

Responsejson
    
    
    {
    	"result": [
    		{
    			"id": "<RULE_ID>",
    			"paused": false,
    			"description": "Challenge site",
    			"action": "challenge",
    			"priority": null,
    			"filter": {
    				"id": "<FILTER_ID>",
    				"expression": "not http.request.uri.path matches \"^/api/.*$\"",
    				"paused": false,
    				"description": "not /api"
    			}
    		}
    	],
    	"success": true,
    	"errors": [],
    	"messages": []
    }

## Update a single rule

This example updates the firewall rule with ID `{rule_id}`.

You must include the following fields in the request body:

  * `id`
  * `action`
  * `filter.id`



All other fields are optional.

Requestbash
    
    
    curl --request PUT \
    "https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules/{rule_id}" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>" \
    --header "Content-Type: application/json" \
    --data '{
      "id": "<RULE_ID>",
      "paused": false,
      "description": "Do not challenge login from office IPv6",
      "action": "allow",
      "priority": null,
      "filter": {
        "id": "<FILTER_ID>",
        "expression": "ip.src in {2400:cb00::/32 2803:f800::/32 2c0f:f248::/32 2a06:98c0::/29} and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")",
        "paused": false,
        "description": "Login from office"
      }
    }'

Responsejson
    
    
    {
    	"result": {
    		"id": "<RULE_ID>",
    		"paused": false,
    		"description": "Do not challenge login from office IPv6",
    		"action": "allow",
    		"priority": null,
    		"filter": {
    			"id": "<FILTER_ID>",
    			"expression": "ip.src in {2400:cb00::/32 2803:f800::/32 2c0f:f248::/32 2a06:98c0::/29} and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")",
    			"paused": false,
    			"description": "Login from office"
    		}
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

Note

`PUT` overwrites fields that are not explicitly passed in the request.

For example, if the request omits `description`, any previously existing `description` value will be erased.

To preserve existing values, issue a `GET` request and based on the response, determine which fields (and respective values) to include in your `PUT` request.

[PreviousGET examples](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/get/)[NextDELETE examples](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/delete/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/firewall/api/cf-firewall-rules/put.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
