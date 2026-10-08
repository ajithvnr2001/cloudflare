---
url: https://developers.cloudflare.com/turnstile/get-started/widget-management/api/
title: Create and manage widgets using Cloudflare API \u00b7 Cloudflare Turnstile docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:07.934390+00:00
---

# Create and manage widgets using Cloudflare API · Cloudflare Turnstile docs

> Source: https://developers.cloudflare.com/turnstile/get-started/widget-management/api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Turnstile](https://developers.cloudflare.com/turnstile/)
  3. /…

[Get started](https://developers.cloudflare.com/turnstile/get-started/)

  4. /Widget management
  5. /API



# Create and manage widgets using Cloudflare API

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/turnstile/get-started/widget-management/api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites Create a widget via the API Manage widgets via the API

Use the [Cloudflare API](https://developers.cloudflare.com/api/resources/turnstile/) for programmatic widget management and automation.

## Prerequisites

Before you begin, you must have:

  * A Cloudflare API token with `Account:Turnstile:Edit` permissions
  * An account ID found in your Cloudflare dashboard



### Create a widget via the API

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Turnstile Sites Write`
  * `Account Settings Write`

Create a Turnstile Widgetbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/challenges/widgets" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"domains": [
    				"example.com"
    		],
    		"mode": "managed",
    		"name": "My Example Turnstile Widget"
    	}'

### Manage widgets via the API

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Turnstile Sites Write`
  * `Turnstile Sites Read`
  * `Account Settings Write`
  * `Account Settings Read`

List Turnstile Widgetsbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/challenges/widgets" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Turnstile Sites Write`
  * `Turnstile Sites Read`
  * `Account Settings Write`
  * `Account Settings Read`

Turnstile Widget Detailsbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/challenges/widgets/$SITEKEY" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Turnstile Sites Write`
  * `Account Settings Write`

Update a Turnstile Widgetbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/challenges/widgets/$SITEKEY" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"domains": [
    				"203.0.113.1",
    				"cloudflare.com",
    				"blog.example.com"
    		],
    		"mode": "invisible",
    		"name": "blog.cloudflare.com login form",
    		"clearance_level": "interactive"
    	}'

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Turnstile Sites Write`
  * `Account Settings Write`

Rotate Secret for a Turnstile Widgetbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/challenges/widgets/$SITEKEY/rotate_secret" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"invalidate_immediately": false
    	}'

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Turnstile Sites Write`
  * `Account Settings Write`

Delete a Turnstile Widgetbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/challenges/widgets/$SITEKEY" \
    	--request DELETE \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

[PreviousCloudflare dashboard](https://developers.cloudflare.com/turnstile/get-started/widget-management/dashboard/)[NextTerraform](https://developers.cloudflare.com/turnstile/get-started/widget-management/terraform/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/turnstile/get-started/widget-management/api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
