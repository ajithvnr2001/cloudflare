---
url: https://developers.cloudflare.com/rules/cloud-connector/create-api/
title: Configure a Cloud Connector rule via API \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:45.574057+00:00
---

# Configure a Cloud Connector rule via API · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/cloud-connector/create-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/)
  4. /Configure a rule via API



# Configure a Cloud Connector rule via API

Last updated Aug 18, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/cloud-connector/create-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRequired permissionsEndpointsExample API calls List of Cloud Connector rules Create/update/delete Cloud Connector rules

You can configure Cloud Connector rules using the [Cloudflare API](https://developers.cloudflare.com/fundamentals/api/).

## Required permissions

The [API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) used in API requests to manage Cloud Connector rules must have at least the following permission:

  * _Zone_ > _Cloud Connector_ > _Write_



Note

A token with this permission is only valid for the Cloud Connector endpoints described in this page. You cannot use it to interact with the `http_cloud_connector` phase via [Rulesets API](https://developers.cloudflare.com/ruleset-engine/rulesets-api/).

## Endpoints

To obtain the complete endpoint, append the Cloud Connector endpoints listed below to the Cloudflare API base URL:
    
    
    https://api.cloudflare.com/client/v4

The `{zone_id}` argument is the [zone ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) (a hexadecimal string). You can find this value in the Cloudflare dashboard.

The following table summarizes the available operations.

Operation | Verb + Endpoint  
---|---  
List Cloud Connector rules | `GET /zones/{zone_id}/cloud_connector/rules`  
Create/update/delete Cloud Connector rules | `PUT /zones/{zone_id}/cloud_connector/rules`  
  
## Example API calls

### List of Cloud Connector rules

The following example returns a list of existing Cloud Connector rules:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Cloud Connector Read`
  * `Cloud Connector Write`

Rulesbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/cloud_connector/rules" \
    	--request GET \
    	--header "X-Auth-Email: $CLOUDFLARE_EMAIL" \
    	--header "X-Auth-Key: $CLOUDFLARE_API_KEY"
    
    
    {
    	"result": [
    		{
    			"id": "<RULE_1_ID>",
    			"provider": "aws_s3",
    			"expression": "http.request.uri.path wildcard \"/images/*\"",
    			"description": "Connect to S3 bucket containing images",
    			"enabled": true,
    			"parameters": {
    				"host": "examplebucketwithimages.s3.north-eu.amazonaws.com"
    			}
    		}
    	],
    	"success": true,
    	"errors": [],
    	"messages": []
    }

### Create/update/delete Cloud Connector rules

Caution

To create a new rule and keep all existing rules, you must include them all in your request body. Omitting an existing rule in the request body will delete the corresponding Cloud Connector rule.

The following example request will replace all existing Cloud Connector rules with a single rule:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Cloud Connector Write`

Put Rulesbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/cloud_connector/rules" \
    	--request PUT \
    	--header "X-Auth-Email: $CLOUDFLARE_EMAIL" \
    	--header "X-Auth-Key: $CLOUDFLARE_API_KEY" \
    	--json '[
    		{
    				"expression": "http.request.uri.path wildcard \"/images/*\"",
    				"provider": "cloudflare_r2",
    				"description": "Connect to R2 bucket containing images",
    				"parameters": {
    						"host": "mybucketcustomdomain.example.com"
    				}
    		}
    	]'

The required body parameters for each rule are: `expression`, `provider`, and `parameters.host`.

The `provider` value must be one of the following: `cloudflare_r2`, `aws_s3`, `azure_storage`, `gcp_storage`, and `oci_storage`.

[PreviousConfigure a rule in the dashboard](https://developers.cloudflare.com/rules/cloud-connector/create-dashboard/)[NextConfigure rules using Terraform](https://developers.cloudflare.com/rules/cloud-connector/create-terraform/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/cloud-connector/create-api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
