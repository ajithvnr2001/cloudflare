---
url: https://developers.cloudflare.com/firewall/api/cf-filters/put/
title: PUT examples - Filters \u00b7 Cloudflare Firewall Rules (deprecated) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:15.960064+00:00
---

# PUT examples - Filters · Cloudflare Firewall Rules (deprecated) docs

> Source: https://developers.cloudflare.com/firewall/api/cf-filters/put/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Firewall Rules (deprecated)](https://developers.cloudflare.com/firewall/)
  3. /…

[Manage rules via the APIs](https://developers.cloudflare.com/firewall/api/)

  4. /[Cloudflare Filters API](https://developers.cloudflare.com/firewall/api/cf-filters/)
  5. /PUT examples



# PUT examples

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/firewall/api/cf-filters/put/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUpdate multiple filtersUpdate a single filter

## Update multiple filters

This example updates two filters with IDs `<FILTER_ID_1>` and `<FILTER_ID_2>` using a single API call.

Requestbash
    
    
    curl --request PUT \
    "https://api.cloudflare.com/client/v4/zones/{zone_id}/filters" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>" \
    --header "Content-Type: application/json" \
    --data '[
      {
        "id": "<FILTER_ID_1>",
        "paused": false,
        "expression": "ip.src eq 93.184.216.0",
        "description": "IP of example.org"
      },
      {
        "id": "<FILTER_ID_2>",
        "expression": "http.request.uri.path matches \"^/api/.*$\"",
        "description": "/api"
      }
    ]'

Responsejson
    
    
    {
      "result": [
        {
          "id": "<FILTER_ID>",
          "paused": false,
          "description": "IP of example.org",
          "expression": "ip.src eq 93.184.216.0"
        },
        {
          "id": "<FILTER_ID_2>",
          "paused": false,
          "description": "/api",
          "expression": "http.request.uri.path matches \"^/api/.*$\""
        }
      ],
      "success": true,
      "errors": [],
      "messages": []
    }

## Update a single filter

This example updates the filter with ID `{filter_id}`.

Requestbash
    
    
    curl --request PUT \
    "https://api.cloudflare.com/client/v4/zones/{zone_id}/filters/{filter_id}" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>" \
    --header "Content-Type: application/json" \
    --data '{
      "id": "<FILTER_ID>",
      "paused": false,
      "description": "Login from office",
      "expression": "ip.src in {2400:cb00::/32 2a06:98c0::/29} and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"
    }'

Responsejson
    
    
    {
      "result": {
        "id": "<FILTER_ID>",
        "paused": false,
        "description": "Login from office",
        "expression": "ip.src in {2400:cb00::/32 2a06:98c0::/29} and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"
      },
      "success": true,
      "errors": [],
      "messages": []
    }

[PreviousGET examples](https://developers.cloudflare.com/firewall/api/cf-filters/get/)[NextDELETE examples](https://developers.cloudflare.com/firewall/api/cf-filters/delete/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/firewall/api/cf-filters/put.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
