---
url: https://developers.cloudflare.com/speed/optimization/content/troubleshooting/disable-auto-minify/
title: Turn off Auto Minify via API \u00b7 Cloudflare Speed docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:35.253995+00:00
---

# Turn off Auto Minify via API · Cloudflare Speed docs

> Source: https://developers.cloudflare.com/speed/optimization/content/troubleshooting/disable-auto-minify/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Speed](https://developers.cloudflare.com/speed/)
  3. /…

SettingsContent optimizations

  4. /Troubleshooting
  5. /Turn off Auto Minify



# Turn off Auto Minify via API

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/speed/optimization/content/troubleshooting/disable-auto-minify/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you begin(Optional) Check zone statusTurn off Auto Minify using the API

If your site is still using deprecated features for [Auto Minify](https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#2024-08-05), turn off Auto Minify via API.

## Before you begin

You will need an [API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with the following permissions:

  * _Zone_ > _Zone Settings_ > _Edit_
  * _Zone_ > _Zone Settings_ > _Read_



## (Optional) Check zone status

To check your zone's Auto Minify status, send a `GET` request to the `/zones/{zone_id}/settings/minify` endpoint.
    
    
    curl "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/minify" \
    --header "Authorization: Bearer <API_TOKEN>"
    
    
    {
    	"result": {
    		"id": "minify",
    		"value": { "css": "off", "html": "off", "js": "off" },
    		"modified_on": null,
    		"editable": true
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

If any of the values in the highlighted line are `"on"`, then you need to turn them off.

## Turn off Auto Minify using the API

To turn off Auto Minify for your zone, send a `PATCH` request to the `/zones/{zone_id}/settings/minify` endpoint. The value for `success` in the response should be `true`.
    
    
    curl --request PATCH \
    "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/minify" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{ "value": { "css": "off","html": "off","js": "off" } }'
    
    
    {
    	"result": {
    		"id": "minify",
    		"value": { "js": "off", "css": "off", "html": "off" },
    		"modified_on": "2024-11-15T19:32:20.882640Z",
    		"editable": true
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

[PreviousContent encoding issues](https://developers.cloudflare.com/speed/optimization/content/troubleshooting/content-encoding-issues/)[NextHTTP/2](https://developers.cloudflare.com/speed/optimization/protocol/http2/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/speed/optimization/content/troubleshooting/disable-auto-minify.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
