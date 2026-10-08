---
url: https://developers.cloudflare.com/firewall/api/cf-firewall-rules/get/
title: GET examples - Firewall rules \u00b7 Cloudflare Firewall Rules (deprecated) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:16.376487+00:00
---

# GET examples - Firewall rules · Cloudflare Firewall Rules (deprecated) docs

> Source: https://developers.cloudflare.com/firewall/api/cf-firewall-rules/get/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Firewall Rules (deprecated)](https://developers.cloudflare.com/firewall/)
  3. /…

[Manage rules via the APIs](https://developers.cloudflare.com/firewall/api/)

  4. /[Firewall Rules API](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/)
  5. /GET examples



# GET examples

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/get/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGet all rulesGet rule by ID

## Get all rules

This example returns all the firewall rules in the zone with ID `{zone_id}`.

Requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>"

Responsejson
    
    
    {
      "result": [
        {
          "id": "<RULE_ID_1>",
          "paused": false,
          "description": "allow API traffic without challenge",
          "action": "allow",
          "priority": null,
          "filter": {
            "id": "<FILTER_ID_1>",
            "expression": "http.request.uri.path matches \"^/api/.*$\"",
            "paused": false,
            "description": "/api"
          }
        },
        {
          "id": "<RULE_ID_2>",
          "paused": false,
          "description": "do not challenge login from office",
          "action": "allow",
          "priority": null,
          "filter": {
            "id": "<FILTER_ID_2>",
            "expression": "ip.src in {2400:cb00::/32 2803:f800::/32 2c0f:f248::/32 2a06:98c0::/29} and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")",
            "paused": false,
            "description": "Login from office"
          }
        },
        {
          "id": "<RULE_ID_3>",
          "paused": false,
          "description": "challenge login",
          "action": "challenge",
          "priority": null,
          "filter": {
            "id": "<FILTER_ID_3>",
            "expression": "(http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")",
            "paused": false,
            "description": "Login"
          }
        },
        {
          "id": "<RULE_ID_4>",
          "paused": false,
          "description": "Non-interactive challenge site",
          "action": "js_challenge",
          "priority": null,
          "filter": {
            "id": "<FILTER_ID_4>",
            "expression": "not http.request.uri.path matches \"^/api/.*$\"",
            "paused": false,
            "description": "not /api"
          }
        }
      ],
      "success": true,
      "errors": [],
      "messages": [],
      "result_info": {
        "page": 1,
        "per_page": 25,
        "count": 4,
        "total_count": 4,
        "total_pages": 1
      }
    }

## Get rule by ID

This example returns the firewall rule with ID `{rule_id}`.

Requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules/{rule_id}" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>"

Responsejson
    
    
    {
      "result": {
        "id": "<RULE_ID>",
        "paused": false,
        "description": "do not challenge login from office",
        "action": "allow",
        "priority": null,
        "filter": {
          "id": "<FILTER_ID>",
          "expression": "ip.src in {2400:cb00::/32 2803:f800::/32 2c0f:f248::/32 2a06:98c0::/29} and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")",
          "paused": false,
          "description": "Login from office"
        }
      },
      "success": true,
      "errors": [],
      "messages": []
    }

[PreviousPOST example](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/post/)[NextPUT examples](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/put/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/firewall/api/cf-firewall-rules/get.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
