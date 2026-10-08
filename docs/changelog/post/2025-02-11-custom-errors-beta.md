---
url: https://developers.cloudflare.com/changelog/post/2025-02-11-custom-errors-beta/
title: Custom Errors (beta): Stored Assets & Account-level Rules \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:02.874114+00:00
---

# Custom Errors (beta): Stored Assets & Account-level Rules · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-02-11-custom-errors-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 11, 2025

## Custom Errors (beta): Stored Assets & Account-level Rules

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-11-custom-errors-beta/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We're introducing [Custom Errors](https://developers.cloudflare.com/rules/custom-errors/) (beta), which builds on our existing Custom Error Responses feature with new asset storage capabilities.

This update allows you to store externally hosted error pages on Cloudflare and reference them in custom error rules, eliminating the need to supply inline content.

This brings the following new capabilities:

  * **Custom error assets** – Fetch and store external error pages at the edge for use in error responses.
  * **Account-Level custom errors** – Define error handling rules and assets at the account level for consistency across multiple zones. Zone-level rules take precedence over account-level ones, and assets are not shared between levels.



You can use Cloudflare API to upload your existing assets for use with Custom Errors:
    
    
    curl "https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_pages/assets" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header 'Content-Type: application/json' \
    --data '{
      "name": "maintenance",
      "description": "Maintenance template page",
      "url": "https://example.com/"
    }'

You can then reference the stored asset in a Custom Error rule:
    
    
    curl --request PUT \
    "https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/http_custom_errors/entrypoint" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header 'Content-Type: application/json' \
    --data '{
      "rules": [
    		{
    			"action": "serve_error",
    			"action_parameters": {
    				"asset_name": "maintenance",
    				"content_type": "text/html",
    				"status_code": 503
    			},
    			"enabled": true,
    			"expression": "http.request.uri.path contains \"error\""
    		}
    	]
    }'
