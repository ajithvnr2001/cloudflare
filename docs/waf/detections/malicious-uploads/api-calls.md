---
url: https://developers.cloudflare.com/waf/detections/malicious-uploads/api-calls/
title: Common API calls for content scanning \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:42.063091+00:00
---

# Common API calls for content scanning · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/malicious-uploads/api-calls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Traffic detections](https://developers.cloudflare.com/waf/detections/)

  4. /[Malicious uploads](https://developers.cloudflare.com/waf/detections/malicious-uploads/)
  5. /Common API calls



# Common API calls

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/malicious-uploads/api-calls/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGeneral operations Enable WAF content scanning Disable WAF content scanning Get WAF content scanning statusCustom expression operations Get existing custom scan expressions Add a custom scan expression Delete a custom scan expression

The following examples address common scenarios of using the Cloudflare API to manage and configure WAF content scanning.

If you are using Terraform, refer to [Terraform configuration examples](https://developers.cloudflare.com/waf/detections/malicious-uploads/terraform-examples/).

## General operations

The following API examples cover basic operations such as enabling and disabling WAF content scanning.

### Enable WAF content scanning

To enable content scanning, use a `POST` request similar to the following:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`
  * `Account WAF Write`

Enable Content Scanning for a zone.bash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/content-upload-scan/enable" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

### Disable WAF content scanning

To disable content scanning, use a `POST` request similar to the following:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`
  * `Account WAF Write`

Disable Content Scanning for a zone.bash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/content-upload-scan/disable" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

### Get WAF content scanning status

To obtain the current status of the content scanning feature, use a `GET` request similar to the following:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`
  * `Zone WAF Read`
  * `Account WAF Write`
  * `Account WAF Read`

Get the Content Scanning status for a zone.bash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/content-upload-scan/settings" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

## Custom expression operations

The following API examples cover operations on custom scan expressions for content scanning.

### Get existing custom scan expressions

To get a list of existing custom scan expressions, use a `GET` request similar to the following:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`
  * `Zone WAF Read`
  * `Account WAF Write`
  * `Account WAF Read`

List the Content Scanning custom expressions of a zone.bash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/content-upload-scan/payloads" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
    
    
    {
    	"result": [
    		{
    			"id": "<EXPRESSION_ID>",
    			"payload": "lookup_json_string(http.request.body.raw, \"file\")"
    		}
    	],
    	"success": true,
    	"errors": [],
    	"messages": []
    }

### Add a custom scan expression

Use a `POST` request similar to the following:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`
  * `Account WAF Write`

Create Content Scanning custom expressions for a zone.bash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/content-upload-scan/payloads" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '[
    		{
    				"payload": "lookup_json_string(http.request.body.raw, \"file\")"
    		}
    	]'

### Delete a custom scan expression

Use a `DELETE` request similar to the following:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`
  * `Account WAF Write`

Delete a Content Scanning custom expression from a zone.bash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/content-upload-scan/payloads/$EXPRESSION_ID" \
    	--request DELETE \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

[PreviousExample rules](https://developers.cloudflare.com/waf/detections/malicious-uploads/example-rules/)[NextTerraform examples](https://developers.cloudflare.com/waf/detections/malicious-uploads/terraform-examples/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/malicious-uploads/api-calls.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
