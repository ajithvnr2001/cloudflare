---
url: https://developers.cloudflare.com/rules/origin-rules/examples/change-http-host-header/
title: Change the HTTP Host header and DNS record \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:49.621308+00:00
---

# Change the HTTP Host header and DNS record · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/origin-rules/examples/change-http-host-header/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Origin Rules](https://developers.cloudflare.com/rules/origin-rules/)

  4. /[Examples](https://developers.cloudflare.com/rules/origin-rules/examples/)
  5. /Change the HTTP Host header and DNS record



# Change the HTTP Host header and DNS record

Create an origin rule to change the HTTP `Host` header and DNS record.

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/origin-rules/examples/change-http-host-header/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following origin rule overrides the HTTP `Host` header to `hr-server.example.com` for all requests with a URI path starting with `/hr-app/`. It also overrides the DNS record to the same hostname.

The `Host` header override only updates the header value; the DNS record override will handle the rerouting of incoming requests. For more information on these overrides, refer to [Origin Rules settings](https://developers.cloudflare.com/rules/origin-rules/features/).

Expression when using the Expression Builder:

Field | Operator | Value  
---|---|---  
URI Path | starts with | `/hr-app/`  
  
Expression when using the Expression Editor:
    
    
    (starts_with(http.request.uri.path, "/hr-app/"))

Value after **Host Header** > **Rewrite to** :
    
    
    hr-server.example.com

Value after **DNS Record** > **Override to** :
    
    
    hr-server.example.com

The following example sets the rules of an existing phase ruleset (`$RULESET_ID`) to a single origin rule — overriding the `Host` header of incoming requests and the resolved DNS record — using the [Update a zone ruleset](https://developers.cloudflare.com/api/resources/rulesets/methods/update/) operation. The response will contain the complete definition of the ruleset you updated.

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
    						"ref": "hr_app_overrides",
    						"expression": "starts_with(http.request.uri.path, \"/hr-app/\")",
    						"description": "Origin rule for the company HR application",
    						"action": "route",
    						"action_parameters": {
    								"host_header": "hr-server.example.com",
    								"origin": {
    										"host": "hr-server.example.com"
    								}
    						}
    				}
    		]
    	}'
    
    
    {
    	"result": {
    		"id": "<RULESET_ID>",
    		"name": "Origin Rules ruleset",
    		"description": "Zone-level ruleset that will execute origin rules.",
    		"kind": "zone",
    		"version": "2",
    		"rules": [
    			{
    				"ref": "hr_app_overrides",
    				"id": "<RULE_ID>",
    				"version": "1",
    				"action": "route",
    				"action_parameters": {
    					"host_header": "hr-server.example.com",
    					"origin": {
    						"host": "hr-server.example.com"
    					}
    				},
    				"expression": "starts_with(http.request.uri.path, \"/hr-app/\")",
    				"description": "Origin rule for the company HR application",
    				"last_updated": "2022-06-03T14:42:04.219025Z",
    				"ref": "<RULE_REF>"
    			}
    		],
    		"last_updated": "2022-06-03T14:42:04.219025Z",
    		"phase": "http_request_origin"
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

Use the `ref` field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to [Troubleshooting](https://developers.cloudflare.com/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications) in the Terraform documentation.

[PreviousChange the destination port](https://developers.cloudflare.com/rules/origin-rules/examples/change-port/)[NextDefine a single origin rule using Terraform](https://developers.cloudflare.com/rules/origin-rules/examples/define-single-origin-terraform/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/origin-rules/examples/change-http-host-header.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
