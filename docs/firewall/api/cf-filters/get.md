---
url: https://developers.cloudflare.com/firewall/api/cf-filters/get/
title: GET examples - Filters \u00b7 Cloudflare Firewall Rules (deprecated) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:15.870288+00:00
---

# GET examples - Filters · Cloudflare Firewall Rules (deprecated) docs

> Source: https://developers.cloudflare.com/firewall/api/cf-filters/get/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Firewall Rules (deprecated)](https://developers.cloudflare.com/firewall/)
  3. /…

[Manage rules via the APIs](https://developers.cloudflare.com/firewall/api/)

  4. /[Cloudflare Filters API](https://developers.cloudflare.com/firewall/api/cf-filters/)
  5. /GET examples



# GET examples

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/firewall/api/cf-filters/get/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGet all filtersGet by filter ID

## Get all filters

This example returns all filters in zone with ID `{zone_id}`.

Requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/{zone_id}/filters" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>"

Responsejson
    
    
    {
      "result": [
        {
          "id": "<FILTER_ID_1>",
          "paused": false,
          "description": "Login from office",
          "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"
        },
        {
          "id": "<FILTER_ID_2>",
          "paused": false,
          "description": "Login",
          "expression": "(http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"
        },
        {
          "id": "<FILTER_ID_3>",
          "paused": false,
          "description": "not /api",
          "expression": "not http.request.uri.path matches \"^/api/.*$\""
        },
        {
          "id": "<FILTER_ID_4>",
          "paused": false,
          "description": "/api",
          "expression": "http.request.uri.path matches \"^/api/.*$\""
        },
        {
          "id": "<FILTER_ID_5>",
          "paused": false,
          "expression": "ip.src eq 93.184.216.0"
        }
      ],
      "success": true,
      "errors": [],
      "messages": [],
      "result_info": {
        "page": 1,
        "per_page": 25,
        "count": 5,
        "total_count": 5,
        "total_pages": 1
      }
    }

## Get by filter ID

This example returns the filter with ID `{filter_id}`.

Requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/{zone_id}/filters/{filter_id}" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>"

Responsejson
    
    
    {
      "result": {
        "id": "<FILTER_ID>",
        "paused": false,
        "description": "Login from office",
        "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"
      },
      "success": true,
      "errors": [],
      "messages": []
    }

[PreviousPOST example](https://developers.cloudflare.com/firewall/api/cf-filters/post/)[NextPUT examples](https://developers.cloudflare.com/firewall/api/cf-filters/put/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/firewall/api/cf-filters/get.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
