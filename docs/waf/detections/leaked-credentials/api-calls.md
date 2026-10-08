---
url: https://developers.cloudflare.com/waf/detections/leaked-credentials/api-calls/
title: Common API calls \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:41.930260+00:00
---

# Common API calls · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/leaked-credentials/api-calls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Traffic detections](https://developers.cloudflare.com/waf/detections/)

  4. /[Leaked credentials](https://developers.cloudflare.com/waf/detections/leaked-credentials/)
  5. /Common API calls



# Common API calls

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/leaked-credentials/api-calls/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGeneral operations Turn on leaked credentials detection Turn off leaked credentials detection Get status of leaked credentials detectionCustom detection location operations Add a custom detection location Get existing custom detection locations Delete a custom detection location

The following examples address common scenarios of using the Cloudflare API to manage and configure leaked credentials detection.

If you are using Terraform, refer to [Terraform configuration examples](https://developers.cloudflare.com/waf/detections/leaked-credentials/terraform-examples/).

## General operations

The following API examples cover basic operations such as enabling and disabling the leaked credentials detection.

### Turn on leaked credentials detection

To turn on leaked credentials detection, use a `POST` request similar to the following:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`
  * `Account WAF Write`

Update the Leaked Credential Checks status for a zone.bash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/leaked-credential-checks" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"enabled": true
    	}'

### Turn off leaked credentials detection

To turn off leaked credentials detection, use a `POST` request similar to the following:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`
  * `Account WAF Write`

Update the Leaked Credential Checks status for a zone.bash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/leaked-credential-checks" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"enabled": false
    	}'

### Get status of leaked credentials detection

To obtain the current status of the leaked credentials detection, use a `GET` request similar to the following:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`
  * `Zone WAF Read`
  * `Account WAF Write`
  * `Account WAF Read`

Get the Leaked Credential Checks status for a zone.bash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/leaked-credential-checks" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
    
    
    {
    	"result": {
    		"enabled": true
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

## Custom detection location operations

The following API examples cover operations on [custom detection locations](https://developers.cloudflare.com/waf/detections/leaked-credentials/#custom-detection-locations) for leaked credentials detection.

### Add a custom detection location

To add a custom detection location, use a `POST` request similar to the following:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`
  * `Account WAF Write`

Create a custom detection location for a zone.bash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/leaked-credential-checks/detections" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"username": "lookup_json_string(http.request.body.raw, \"user\")",
    		"password": "lookup_json_string(http.request.body.raw, \"secret\")"
    	}'

### Get existing custom detection locations

To get a list of existing custom detection locations, use a `GET` request similar to the following:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`
  * `Zone WAF Read`
  * `Account WAF Write`
  * `Account WAF Read`

List the custom detection locations of a zone.bash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/leaked-credential-checks/detections" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
    
    
    {
    	"result": [
    		{
    			"id": "<DETECTION_ID>",
    			"username": "lookup_json_string(http.request.body.raw, \"user\")",
    			"password": "lookup_json_string(http.request.body.raw, \"secret\")"
    		}
    		// (...)
    	],
    	"success": true,
    	"errors": [],
    	"messages": []
    }

### Delete a custom detection location

To delete a custom detection location, use a `DELETE` request similar to the following:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`
  * `Account WAF Write`

Delete a custom detection location from a zone.bash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/leaked-credential-checks/detections/$DETECTION_ID" \
    	--request DELETE \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

[PreviousGet started](https://developers.cloudflare.com/waf/detections/leaked-credentials/get-started/)[NextTerraform examples](https://developers.cloudflare.com/waf/detections/leaked-credentials/terraform-examples/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/leaked-credentials/api-calls.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
