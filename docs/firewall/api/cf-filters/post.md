---
url: https://developers.cloudflare.com/firewall/api/cf-filters/post/
title: POST examples - Filters \u00b7 Cloudflare Firewall Rules (deprecated) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:15.988162+00:00
---

# POST examples - Filters · Cloudflare Firewall Rules (deprecated) docs

> Source: https://developers.cloudflare.com/firewall/api/cf-filters/post/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Firewall Rules (deprecated)](https://developers.cloudflare.com/firewall/)
  3. /…

[Manage rules via the APIs](https://developers.cloudflare.com/firewall/api/)

  4. /[Cloudflare Filters API](https://developers.cloudflare.com/firewall/api/cf-filters/)
  5. /POST example



# POST example

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/firewall/api/cf-filters/post/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This example creates several filters using a single API call.

Requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/{zone_id}/filters" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>" \
    --header "Content-Type: application/json" \
    --data '[
      {
        "expression": "ip.src eq 93.184.216.0"
      },
      {
        "expression": "http.request.uri.path matches \"^/api/.*$\"",
        "description": "/api"
      },
      {
        "expression": "not http.request.uri.path matches \"^/api/.*$\"",
        "description": "not /api"
      },
      {
        "expression": "(http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")",
        "description": "Login"
      },
      {
        "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")",
        "description": "Login from office"
      }
    ]'

Responsejson
    
    
    {
      "result": [
        {
          "id": "<FILTER_ID_1>",
          "paused": false,
          "expression": "ip.src eq 93.184.216.0"
        },
        {
          "id": "<FILTER_ID_2>",
          "paused": false,
          "description": "/api",
          "expression": "http.request.uri.path matches \"^/api/.*$\""
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
          "description": "Login",
          "expression": "(http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"
        },
        {
          "id": "<FILTER_ID_5>",
          "paused": false,
          "description": "Login from office",
          "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"
        }
      ],
      "success": true,
      "errors": [],
      "messages": []
    }

[PreviousEndpoints](https://developers.cloudflare.com/firewall/api/cf-filters/endpoints/)[NextGET examples](https://developers.cloudflare.com/firewall/api/cf-filters/get/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/firewall/api/cf-filters/post.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
