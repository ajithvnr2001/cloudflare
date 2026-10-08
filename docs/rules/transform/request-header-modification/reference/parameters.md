---
url: https://developers.cloudflare.com/rules/transform/request-header-modification/reference/parameters/
title: API parameter reference \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:57.601019+00:00
---

# API parameter reference · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/request-header-modification/reference/parameters/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)[Modify request headers](https://developers.cloudflare.com/rules/transform/request-header-modification/)

  4. /Reference
  5. /API parameter reference



# API parameter reference

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/request-header-modification/reference/parameters/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewStatic header value parametersDynamic header value parametersHeader removal parametersDifferent header modifications in the same rule

To set an HTTP request header via API, set the following parameters in the `action_parameters` field:

  * **operation** : `set`

  * Include one of the following parameters to define a static or dynamic value:

    * **value** : Specifies a static value for the HTTP request header.
    * **expression** : Specifies the expression that defines a value for the HTTP request header.



To remove an HTTP request header via API, set the following parameter in the `action_parameters` field:

  * **operation** : `remove`



For step-by-step instructions, refer to [Create a request header transform rule via API](https://developers.cloudflare.com/rules/transform/request-header-modification/create-api/).

## Static header value parameters

The full syntax of the `action_parameters` field to define a static HTTP request header value is the following:
    
    
    "action_parameters": {
      "headers": {
        "<HEADER_NAME>": {
          "operation": "set",
          "value": "<URI_PATH_VALUE>"
        }
      }
    }

## Dynamic header value parameters

The full syntax of the `action_parameters` field to define a dynamic HTTP request header value using an expression is the following:
    
    
    "action_parameters": {
      "headers": {
        "<HEADER_NAME>": {
          "operation": "set",
          "expression": "<EXPRESSION>"
        }
      }
    }

Note

Check the [available fields and functions](https://developers.cloudflare.com/rules/transform/request-header-modification/reference/fields-functions/) you can use in an expression.

## Header removal parameters

The full syntax of the `action_parameters` field to remove an HTTP request header is the following:
    
    
    "action_parameters": {
      "headers": {
        "<HEADER_NAME>": {
          "operation": "remove"
        }
      }
    }

## Different header modifications in the same rule

The same rule can modify different HTTP request headers using different operations (set or remove a header). For example, a single rule can set the value of a header and remove a different header. The syntax of such a rule could be the following:
    
    
    "action_parameters": {
      "headers": {
        "<HEADER_NAME_1>": {
          "operation": "set",
          "value": "<HEADER_VALUE_1>"
        },
        "<HEADER_NAME_2>": {
          "operation": "remove"
        }
      }
    }

[PreviousAvailable fields and functions](https://developers.cloudflare.com/rules/transform/request-header-modification/reference/fields-functions/)[NextOverview](https://developers.cloudflare.com/rules/transform/response-header-modification/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/request-header-modification/reference/parameters.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
