---
url: https://developers.cloudflare.com/api/resources/alerting/subresources/available_alerts/methods/list/
title: Get Alert Types | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:34.105117+00:00
---

# Get Alert Types | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/alerting/subresources/available_alerts/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[Alerting](https://developers.cloudflare.com/api/resources/alerting)

[Available Alerts](https://developers.cloudflare.com/api/resources/alerting/subresources/available_alerts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Get Alert Types

GET/accounts/{account_id}/alerting/v3/available_alerts

Gets a list of all alert types for which an account is eligible.

##### Security

API Token

The preferred authorization scheme for interacting with the Cloudflare API. [Create a token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

**Example:**`Authorization: Bearer Sn3lZJTBX6kkg7OdcBUAxOO963GEIyGQqnFTOFYY`

API Email + API Key

The previous authorization scheme for interacting with the Cloudflare API, used in conjunction with a Global API key.

**Example:**`X-Auth-Email: user@example.com`

The previous authorization scheme for interacting with the Cloudflare API. When possible, use API tokens instead of Global API keys.

**Example:**`X-Auth-Key: 144c9defac04969c7bfad8efaa8ea194`

##### Accepted Permissions (at least one required)

`Zero Trust: PII Read``Notifications Write``Notifications Read``Account Settings Write``Account Settings Read`

##### Path ParametersExpand Collapse 

account_id: string

The account id

maxLength32

##### ReturnsExpand Collapse 

errors: array of object { message, code } 

message: string

code: optional number

minimum1000

messages: array of object { message, code } 

message: string

code: optional number

minimum1000

success: true

Whether the API call was successful

result: optional map[array of object { description, display_name, filter_options, type } ]

description: optional string

Describes the alert type.

display_name: optional string

Alert type name.

filter_options: optional array of unknown

Format of additional configuration options (filters) for the alert type. Data type of filters during policy creation: Array of strings.

type: optional string

Use this value when creating and updating a notification policy.

### Get Alert Types

HTTP

HTTP

HTTP

TypeScript

TypeScript

Python

Python

Go

Go

Terraform

Terraform
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/alerting/v3/available_alerts \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "errors": [
        {
          "message": "message",
          "code": 1000
        }
      ],
      "messages": [
        {
          "message": "message",
          "code": 1000
        }
      ],
      "success": true,
      "result": {
        "Origin Monitoring": [
          {
            "description": "High levels of 5xx HTTP errors at your origin.",
            "display_name": "Origin Error Rate Alert",
            "filter_options": [
              {
                "AvailableValues": null,
                "ComparisonOperator": "==",
                "Key": "zones",
                "Range": "1-n"
              },
              {
                "AvailableValues": [
                  {
                    "Description": "Service-Level Objective of 99.7",
                    "ID": "99.7"
                  },
                  {
                    "Description": "Service-Level Objective of 99.8",
                    "ID": "99.8"
                  }
                ],
                "ComparisonOperator": ">=",
                "Key": "slo",
                "Range": "0-1"
              }
            ],
            "type": "http_alert_origin_error"
          }
        ]
      }
    }

##### Returns Examples

200 example
    
    
    {
      "errors": [
        {
          "message": "message",
          "code": 1000
        }
      ],
      "messages": [
        {
          "message": "message",
          "code": 1000
        }
      ],
      "success": true,
      "result": {
        "Origin Monitoring": [
          {
            "description": "High levels of 5xx HTTP errors at your origin.",
            "display_name": "Origin Error Rate Alert",
            "filter_options": [
              {
                "AvailableValues": null,
                "ComparisonOperator": "==",
                "Key": "zones",
                "Range": "1-n"
              },
              {
                "AvailableValues": [
                  {
                    "Description": "Service-Level Objective of 99.7",
                    "ID": "99.7"
                  },
                  {
                    "Description": "Service-Level Objective of 99.8",
                    "ID": "99.8"
                  }
                ],
                "ComparisonOperator": ">=",
                "Key": "slo",
                "Range": "0-1"
              }
            ],
            "type": "http_alert_origin_error"
          }
        ]
      }
    }
