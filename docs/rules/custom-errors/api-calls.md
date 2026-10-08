---
url: https://developers.cloudflare.com/rules/custom-errors/api-calls/
title: Common API calls for Custom Errors \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:48.197970+00:00
---

# Common API calls for Custom Errors · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/custom-errors/api-calls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Custom Errors](https://developers.cloudflare.com/rules/custom-errors/)
  4. /Common API calls



# Common API calls for Custom Errors

Last updated Sep 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/custom-errors/api-calls/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Create a custom error asset List custom error assets Update a custom error asset Get a custom error asset Delete a custom error asset Get error page Update error pageMore resources

The following sections provide examples of common API calls for managing custom error assets and Error Pages at the zone level.

To perform the same operations at the account level, use the corresponding account-level API endpoints.

### Create a custom error asset

The following `POST` request creates a new custom error asset in a zone based on the provided URL:
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_pages/assets" \
    --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    --json '{
      "name": "500_error_template",
      "description": "Standard 5xx error template page",
      "url": "https://example.com/errors/500_template.html"
    }'
    
    
    {
    	"result": {
    		"name": "500_error_template",
    		"description": "Standard 5xx error template page",
    		"url": "https://example.com/errors/500_template.html",
    		"last_updated": "2025-02-10T11:36:07.810215Z",
    		"size_bytes": 2048
    	},
    	"success": true
    }

To create an asset at the account level, use the account-level endpoint:
    
    
    https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/custom_pages/assets

### List custom error assets

The following `GET` request retrieves a list of custom error assets configured in the zone:
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_pages/assets" \
    --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
    
    
    {
    	"result": [
    		{
    			"name": "500_error_template",
    			"description": "Standard 5xx error template page",
    			"url": "https://example.com/errors/500_template.html",
    			"last_updated": "2025-02-10T11:36:07.810215Z",
    			"size_bytes": 2048
    		}
    		// ...
    	],
    	"success": true,
    	"errors": [],
    	"messages": [],
    	"result_info": {
    		"count": 2,
    		"page": 1,
    		"per_page": 20,
    		"total_count": 2,
    		"total_pages": 1
    	}
    }

To retrieve a list of assets at the account level, use the account-level endpoint:
    
    
    https://api.cloudflare.com/client/v4/accounts/$ZONE_ID/custom_pages/assets

### Update a custom error asset

The following `PUT` request updates the URL of an existing custom error asset at the zone level named `500_error_template`:
    
    
    curl --request PUT \
    "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_pages/assets/500_error_template" \
    --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    --json '{
      "description": "Standard 5xx error template page",
      "url": "https://example.com/errors/500_new_template.html"
    }'
    
    
    {
    	"result": {
    		"name": "500_error_template",
    		"description": "Standard 5xx error template page",
    		"url": "https://example.com/errors/500_new_template.html",
    		"last_updated": "2025-02-10T13:13:07.810215Z",
    		"size_bytes": 3145
    	},
    	"success": true
    }

You can update the asset description and URL. You cannot update the asset name after creation.

If you provide the same URL when updating an asset, Cloudflare will fetch the URL again, along with its resources.

To update an asset at the account level, use the account-level endpoint:
    
    
    https://api.cloudflare.com/client/v4/accounts/{account_id}/custom_pages/assets/{asset_name}

### Get a custom error asset

The following `GET` request retrieves the details of an existing custom error asset at the zone level named `500_error_template`:
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_pages/assets/500_error_template" \
    --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
    
    
    {
    	"result": {
    		"name": "500_error_template",
    		"description": "Standard 5xx error template page",
    		"url": "https://example.com/errors/500_new_template.html",
    		"last_updated": "2025-02-10T13:13:07.810215Z",
    		"size_bytes": 3145
    	},
    	"success": true
    }

To retrieve an asset at the account level, use the account-level endpoint:
    
    
    https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/custom_pages/assets/$ASSET_NAME

### Delete a custom error asset

The following `DELETE` request deletes an existing custom error asset at the zone level named `500_error_template`:
    
    
    curl --request DELETE \
    "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_pages/assets/500_error_template" \
    --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

If the request is successful, the response will have a `204` HTTP status code.

To delete an asset at the account level, use the account-level endpoint:
    
    
    https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/custom_pages/assets/$ASSET_NAME

### Get error page

This example obtains the current configuration for the `Rate limiting block` error page (with ID `ratelimit_block`).

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Custom Pages Write`
  * `Custom Pages Read`
  * `Zone Settings Write`
  * `Zone Settings Read`

Get a custom pagebash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_pages/ratelimit_block" \
    	--request GET \
    	--header "X-Auth-Email: $CLOUDFLARE_EMAIL" \
    	--header "X-Auth-Key: $CLOUDFLARE_API_KEY"
    
    
    {
    	"result": {
    		"id": "ratelimit_block",
    		"description": "Rate limit Block",
    		"required_tokens": [],
    		"preview_target": "block:rate-limit",
    		"created_on": "2025-06-03T08:33:17.091587Z",
    		"modified_on": "2025-06-03T08:33:17.091587Z",
    		"url": null,
    		"state": "default"
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

The response indicates that the page is currently set to the Cloudflare default page (`"state": "default"`).

For a list of error page identifiers, refer to [Error page types](https://developers.cloudflare.com/rules/custom-errors/reference/error-page-types/).

### Update error page

This example defines a custom error page for `Rate limiting block` errors (with ID `ratelimit_block`) based on the provided URL.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Custom Pages Write`
  * `Zone Settings Write`

Update a custom pagebash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_pages/ratelimit_block" \
    	--request PUT \
    	--header "X-Auth-Email: $CLOUDFLARE_EMAIL" \
    	--header "X-Auth-Key: $CLOUDFLARE_API_KEY" \
    	--json '{
    		"state": "customized",
    		"url": "https://example.com/rate_limiting_block_error_page.html"
    	}'
    
    
    {
    	"result": {
    		"id": "ratelimit_block",
    		"description": "Rate limit Block",
    		"required_tokens": [],
    		"preview_target": "block:rate-limit",
    		"created_on": "2025-06-03T08:33:17.091587Z",
    		"modified_on": "2025-06-03T08:35:32.639114Z",
    		"url": "https://example.com/rate_limiting_block_error_page.html",
    		"state": "customized"
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

To set the error page back to the default page, use `"state": "default"` in the request body.

For a list of error page identifiers, refer to [Error page types](https://developers.cloudflare.com/rules/custom-errors/reference/error-page-types/).

## More resources

  * [Custom Error Pages API reference](https://developers.cloudflare.com/api/resources/custom_pages/)



[PreviousExample rules](https://developers.cloudflare.com/rules/custom-errors/example-rules/)[NextParameters](https://developers.cloudflare.com/rules/custom-errors/reference/parameters/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/custom-errors/api-calls.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
