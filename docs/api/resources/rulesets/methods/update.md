---
url: https://developers.cloudflare.com/api/resources/rulesets/methods/update/
title: Update an account or zone ruleset | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:55.146652+00:00
---

# Update an account or zone ruleset | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/rulesets/methods/update/

[API Reference](https://developers.cloudflare.com/api)

[Rulesets](https://developers.cloudflare.com/api/resources/rulesets)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Update an account or zone ruleset

PUT/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}

Updates an account or zone ruleset, creating a new version.

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

`Mass URL Redirects Write``Magic Firewall Write``L4 DDoS Managed Ruleset Write``Transform Rules Write``Select Configuration Write``Account WAF Write``Account Rulesets Write``Logs Write`

##### Path ParametersExpand Collapse 

ruleset_id: string

The unique ID of the ruleset.

account_id: optional string

The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

zone_id: optional string

The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

##### Query ParametersExpand Collapse 

dry_run: optional boolean

Validates the request without persisting changes when set to `true`. Responses that normally return 200 return `result: null`; endpoints that normally return 204 continue to return 204.

##### Body ParametersJSONExpand Collapse 

description: optional string

An informative description of the ruleset.

kind: optional [Kind](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets%20%3E%20\(model\)%20kind%20%3E%20\(schema\))

The kind of the ruleset.

One of the following:

"managed"

"custom"

"root"

"zone"

name: optional string

The human-readable name of the ruleset.

minLength1

phase: optional [Phase](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets%20%3E%20\(model\)%20phase%20%3E%20\(schema\))

The phase of the ruleset.

One of the following:

"ddos_l4"

"ddos_l7"

"http_config_settings"

"http_custom_errors"

"http_log_custom_fields"

"http_ratelimit"

"http_request_cache_settings"

"http_request_dynamic_redirect"

"http_request_firewall_custom"

"http_request_firewall_managed"

"http_request_late_transform"

"http_request_origin"

"http_request_redirect"

"http_request_sanitize"

"http_request_sbfm"

"http_request_transform"

"http_response_cache_settings"

"http_response_compression"

"http_response_firewall_managed"

"http_response_headers_transform"

"magic_transit"

"magic_transit_ids_managed"

"magic_transit_managed"

"magic_transit_ratelimit"

rules: optional array of [BlockRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20block_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more }  or object { last_updated, version, id, 10 more }  or [CompressResponseRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20compress_response_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more }  or 18 more

The list of rules in the ruleset.

One of the following:

BlockRule object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "block"

The action to perform when the rule matches.

action_parameters: optional object { response } 

The parameters configuring the rule’s action.

response: optional object { content, content_type, status_code } 

The response to show when the block is applied.

content: string

The content to return.

minLength1

content_type: string

The type of the content to return.

minLength1

status_code: number

The status code to return.

maximum499

minimum400

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

Whether the rule should be executed.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

Challenge object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "challenge"

The action to perform when the rule matches.

action_parameters: optional unknown

The parameters configuring the rule’s action.

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

Whether the rule should be executed.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

CompressResponseRule object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "compress_response"

The action to perform when the rule matches.

action_parameters: optional object { algorithms } 

The parameters configuring the rule’s action.

algorithms: array of object { name } 

Custom order for compression algorithms.

name: optional "none" or "auto" or "default" or 3 more

Name of the compression algorithm to enable.

One of the following:

"none"

"auto"

"default"

"gzip"

"brotli"

"zstd"

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

Whether the rule should be executed.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

DDoSDynamicRule object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "ddos_dynamic"

The action to perform when the rule matches.

action_parameters: optional unknown

The parameters configuring the rule’s action.

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

Whether the rule should be executed.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

ExecuteRule object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "execute"

The action to perform when the rule matches.

action_parameters: optional object { id, matched_data, overrides } 

The parameters configuring the rule’s action.

id: string

The ID of the ruleset to execute.

matched_data: optional object { public_key } 

The configuration to use for matched data logging.

public_key: string

The public key to encrypt matched data logs with.

minLength1

overrides: optional object { action, categories, enabled, 2 more } 

A set of overrides to apply to the target ruleset.

action: optional string

An action to override all rules with. This option has lower precedence than rule and category overrides.

categories: optional array of object { category, action, enabled, sensitivity_level } 

A list of category-level overrides. This option has the second-highest precedence after rule-level overrides.

category: string

The name of the category to override.

minLength1

action: optional string

The action to override rules in the category with.

enabled: optional boolean

Whether to enable execution of rules in the category.

sensitivity_level: optional "default" or "medium" or "low" or "eoff"

The sensitivity level to use for rules in the category. This option is only applicable for DDoS phases.

One of the following:

"default"

"medium"

"low"

"eoff"

enabled: optional boolean

Whether to enable execution of all rules. This option has lower precedence than rule and category overrides.

rules: optional array of object { id, action, enabled, 2 more } 

A list of rule-level overrides. This option has the highest precedence.

id: string

The ID of the rule to override.

action: optional string

The action to override the rule with.

enabled: optional boolean

Whether to enable execution of the rule.

score_threshold: optional number

The score threshold to use for the rule.

sensitivity_level: optional "default" or "medium" or "low" or "eoff"

The sensitivity level to use for the rule. This option is only applicable for DDoS phases.

One of the following:

"default"

"medium"

"low"

"eoff"

sensitivity_level: optional "default" or "medium" or "low" or "eoff"

A sensitivity level to set for all rules. This option has lower precedence than rule and category overrides and is only applicable for DDoS phases.

One of the following:

"default"

"medium"

"low"

"eoff"

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

Whether the rule should be executed.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

ForceConnectionCloseRule object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "force_connection_close"

The action to perform when the rule matches.

action_parameters: optional unknown

The parameters configuring the rule’s action.

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

Whether the rule should be executed.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

JSChallenge object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "js_challenge"

The action to perform when the rule matches.

action_parameters: optional unknown

The parameters configuring the rule’s action.

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

Whether the rule should be executed.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

LogRule object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "log"

The action to perform when the rule matches.

action_parameters: optional unknown

The parameters configuring the rule’s action.

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

Whether the rule should be executed.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

LogCustomFieldRule object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "log_custom_field"

The action to perform when the rule matches.

action_parameters: optional object { cookie_fields, raw_response_fields, request_fields, 2 more } 

The parameters configuring the rule’s action.

cookie_fields: optional array of object { name } 

The cookie fields to log.

name: string

The name of the cookie.

minLength1

raw_response_fields: optional array of object { name, preserve_duplicates } 

The raw response fields to log.

name: string

The name of the response header.

minLength1

preserve_duplicates: optional boolean

Whether to log duplicate values of the same header.

request_fields: optional array of object { name } 

The raw request fields to log.

name: string

The name of the header.

minLength1

response_fields: optional array of object { name, preserve_duplicates } 

The transformed response fields to log.

name: string

The name of the response header.

minLength1

preserve_duplicates: optional boolean

Whether to log duplicate values of the same header.

transformed_request_fields: optional array of object { name } 

The transformed request fields to log.

name: string

The name of the header.

minLength1

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

Whether the rule should be executed.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

ManagedChallengeRule object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "managed_challenge"

The action to perform when the rule matches.

action_parameters: optional unknown

The parameters configuring the rule’s action.

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

Whether the rule should be executed.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

RedirectRule object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "redirect"

The action to perform when the rule matches.

action_parameters: optional object { from_list, from_value } 

The parameters configuring the rule’s action.

from_list: optional object { key, name } 

A redirect based on a bulk list lookup.

key: string

An expression that evaluates to the list lookup key.

minLength1

name: string

The name of the list to match against.

from_value: optional object { target_url, preserve_query_string, status_code } 

A redirect based on the request properties.

target_url: object { expression, value } 

A URL to redirect the request to.

expression: optional string

An expression that evaluates to a URL to redirect the request to.

minLength1

value: optional string

A URL to redirect the request to.

minLength1

preserve_query_string: optional boolean

Whether to keep the query string of the original request.

status_code: optional 301 or 302 or 303 or 2 more

The status code to use for the redirect.

One of the following:

301

302

303

307

308

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

Whether the rule should be executed.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

RewriteRule object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "rewrite"

The action to perform when the rule matches.

action_parameters: optional object { headers, uri } 

The parameters configuring the rule’s action.

headers: optional map[object { operation, value }  or object { expression, operation }  or object { operation, value }  or 2 more]

A map of headers to rewrite.

One of the following:

AddStaticHeader object { operation, value } 

A header with a static value to add.

operation: "add"

The operation to perform on the header.

value: string

A static value for the header.

minLength1

AddDynamicHeader object { expression, operation } 

A header with a dynamic value to add.

expression: string

An expression that evaluates to a value for the header.

minLength1

operation: "add"

The operation to perform on the header.

SetStaticHeader object { operation, value } 

A header with a static value to set.

operation: "set"

The operation to perform on the header.

value: string

A static value for the header.

minLength1

SetDynamicHeader object { expression, operation } 

A header with a dynamic value to set.

expression: string

An expression that evaluates to a value for the header.

minLength1

operation: "set"

The operation to perform on the header.

RemoveHeader object { operation } 

A header to remove.

operation: "remove"

The operation to perform on the header.

uri: optional object { path, origin }  or object { query, origin } 

A URI path rewrite.

One of the following:

URIPath object { path, origin } 

A URI path rewrite.

path: object { expression, value } 

A URI path rewrite.

expression: optional string

An expression that evaluates to a value to rewrite the URI path to.

minLength1

value: optional string

A value to rewrite the URI path to.

minLength1

origin: optional boolean

Whether to propagate the rewritten URI to origin.

URIQuery object { query, origin } 

A URI query rewrite.

query: object { expression, value } 

A URI query rewrite.

expression: optional string

An expression that evaluates to a value to rewrite the URI query to.

minLength1

value: optional string

A value to rewrite the URI query to.

origin: optional boolean

Whether to propagate the rewritten URI to origin.

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

Whether the rule should be executed.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

RouteRule object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "route"

The action to perform when the rule matches.

action_parameters: optional object { host_header, origin, sni } 

The parameters configuring the rule’s action.

host_header: optional string

A value to rewrite the HTTP host header to.

minLength1

origin: optional object { host, port } 

An origin to route to.

host: optional string

A resolved host to route to.

minLength1

port: optional number

A destination port to route to.

maximum65535

minimum1

sni: optional object { value } 

A Server Name Indication (SNI) override.

value: string

A value to override the SNI to.

minLength1

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

Whether the rule should be executed.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

ScoreRule object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "score"

The action to perform when the rule matches.

action_parameters: optional object { increment } 

The parameters configuring the rule’s action.

increment: number

A delta to change the score by, which can be either positive or negative.

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

ServeErrorRule object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "serve_error"

The action to perform when the rule matches.

action_parameters: optional object { content, content_type, status_code }  or object { asset_name, content_type, status_code } 

The parameters configuring the rule’s action.

One of the following:

ActionParametersContent object { content, content_type, status_code } 

content: string

The response content.

minLength1

content_type: optional "application/json" or "text/html" or "text/plain" or "text/xml"

The content type header to set with the error response.

One of the following:

"application/json"

"text/html"

"text/plain"

"text/xml"

status_code: optional number

The status code to use for the error.

maximum999

minimum400

ActionParametersAsset object { asset_name, content_type, status_code } 

asset_name: string

The name of a custom asset to serve as the error response.

minLength1

content_type: optional "application/json" or "text/html" or "text/plain" or "text/xml"

The content type header to set with the error response.

One of the following:

"application/json"

"text/html"

"text/plain"

"text/xml"

status_code: optional number

The status code to use for the error.

maximum999

minimum400

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

SetCacheControl object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "set_cache_control"

The action to perform when the rule matches.

action_parameters: optional object { immutable, "max-age", "must-revalidate", 10 more } 

The parameters configuring the rule’s action.

immutable: optional object { operation, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration.

One of the following:

SetDirective object { operation, cloudflare_only } 

Set the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"max-age": optional object { operation, value, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration that accepts a duration value in seconds.

One of the following:

SetDirective object { operation, value, cloudflare_only } 

Set the directive with a duration value in seconds.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

value: number

The duration value in seconds for the directive.

minimum0

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"must-revalidate": optional object { operation, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration.

One of the following:

SetDirective object { operation, cloudflare_only } 

Set the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"must-understand": optional object { operation, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration.

One of the following:

SetDirective object { operation, cloudflare_only } 

Set the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"no-cache": optional object { operation, cloudflare_only, qualifiers }  or object { operation, cloudflare_only } 

A cache-control directive configuration that accepts optional qualifiers (header names).

One of the following:

SetDirective object { operation, cloudflare_only, qualifiers } 

Set the directive with optional qualifiers.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

qualifiers: optional array of string

Optional list of header names to qualify the directive (e.g., for “private” or “no-cache” directives).

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"no-store": optional object { operation, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration.

One of the following:

SetDirective object { operation, cloudflare_only } 

Set the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"no-transform": optional object { operation, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration.

One of the following:

SetDirective object { operation, cloudflare_only } 

Set the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

private: optional object { operation, cloudflare_only, qualifiers }  or object { operation, cloudflare_only } 

A cache-control directive configuration that accepts optional qualifiers (header names).

One of the following:

SetDirective object { operation, cloudflare_only, qualifiers } 

Set the directive with optional qualifiers.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

qualifiers: optional array of string

Optional list of header names to qualify the directive (e.g., for “private” or “no-cache” directives).

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"proxy-revalidate": optional object { operation, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration.

One of the following:

SetDirective object { operation, cloudflare_only } 

Set the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

public: optional object { operation, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration.

One of the following:

SetDirective object { operation, cloudflare_only } 

Set the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"s-maxage": optional object { operation, value, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration that accepts a duration value in seconds.

One of the following:

SetDirective object { operation, value, cloudflare_only } 

Set the directive with a duration value in seconds.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

value: number

The duration value in seconds for the directive.

minimum0

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"stale-if-error": optional object { operation, value, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration that accepts a duration value in seconds.

One of the following:

SetDirective object { operation, value, cloudflare_only } 

Set the directive with a duration value in seconds.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

value: number

The duration value in seconds for the directive.

minimum0

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"stale-while-revalidate": optional object { operation, value, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration that accepts a duration value in seconds.

One of the following:

SetDirective object { operation, value, cloudflare_only } 

Set the directive with a duration value in seconds.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

value: number

The duration value in seconds for the directive.

minimum0

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

SetCacheSettingsRule object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "set_cache_settings"

The action to perform when the rule matches.

action_parameters: optional object { additional_cacheable_ports, browser_ttl, cache, 14 more } 

The parameters configuring the rule’s action.

additional_cacheable_ports: optional array of number

A list of additional ports that caching should be enabled on.

browser_ttl: optional object { mode, default } 

How long client browsers should cache the response. Cloudflare cache purge will not purge content cached on client browsers, so high browser TTLs may lead to stale content.

mode: "respect_origin" or "bypass_by_default" or "override_origin" or "bypass"

The browser TTL mode.

One of the following:

"respect_origin"

"bypass_by_default"

"override_origin"

"bypass"

default: optional number

The browser TTL (in seconds) if you choose the “override_origin” mode.

minimum0

cache: optional boolean

Whether the request’s response from the origin is eligible for caching. Caching itself will still depend on the cache control header and your other caching configurations.

cache_key: optional object { cache_by_device_type, cache_deception_armor, custom_key, ignore_query_strings_order } 

Which components of the request are included in or excluded from the cache key Cloudflare uses to store the response in cache.

cache_by_device_type: optional boolean

Whether to separate cached content based on the visitor’s device type.

cache_deception_armor: optional boolean

Whether to protect from web cache deception attacks, while allowing static assets to be cached.

custom_key: optional object { cookie, header, host, 2 more } 

Which components of the request are included or excluded from the cache key.

cookie: optional object { check_presence, include } 

Which cookies to include in the cache key.

check_presence: optional array of string

A list of cookies to check for the presence of. The presence of these cookies is included in the cache key.

include: optional array of string

A list of cookies to include in the cache key.

header: optional object { check_presence, contains, exclude_origin, include } 

Which headers to include in the cache key.

check_presence: optional array of string

A list of headers to check for the presence of. The presence of these headers is included in the cache key.

contains: optional map[array of string]

A mapping of header names to a list of values. If a header is present in the request and contains any of the values provided, its value is included in the cache key.

exclude_origin: optional boolean

Whether to exclude the origin header in the cache key.

include: optional array of string

A list of headers to include in the cache key.

host: optional object { resolved } 

How to use the host in the cache key.

resolved: optional boolean

Whether to use the resolved host in the cache key.

query_string: optional object { exclude, include } 

Which query string parameters to include in or exclude from the cache key.

exclude: optional object { all, list } 

Which query string parameters to exclude from the cache key.

all: optional true

Whether to exclude all query string parameters from the cache key.

list: optional array of string

A list of query string parameters to exclude from the cache key.

include: optional object { all, list } 

Which query string parameters to include in the cache key.

all: optional true

Whether to include all query string parameters in the cache key.

list: optional array of string

A list of query string parameters to include in the cache key.

user: optional object { device_type, geo, lang } 

How to use characteristics of the request user agent in the cache key.

device_type: optional boolean

Whether to use the user agent’s device type in the cache key.

geo: optional boolean

Whether to use the user agents’s country in the cache key.

lang: optional boolean

Whether to use the user agent’s language in the cache key.

ignore_query_strings_order: optional boolean

Whether to treat requests with the same query parameters the same, regardless of the order those query parameters are in.

cache_reserve: optional object { eligible, minimum_file_size } 

Settings to determine whether the request’s response from origin is eligible for Cache Reserve (requires a Cache Reserve add-on plan).

eligible: boolean

Whether Cache Reserve is enabled. If this is true and a request meets eligibility criteria, Cloudflare will write the resource to Cache Reserve.

minimum_file_size: optional number

The minimum file size eligible for storage in Cache Reserve.

minimum0

edge_ttl: optional object { mode, default, status_code_ttl } 

How long the Cloudflare edge network should cache the response.

mode: "respect_origin" or "bypass_by_default" or "override_origin"

The edge TTL mode.

One of the following:

"respect_origin"

"bypass_by_default"

"override_origin"

default: optional number

The edge TTL (in seconds) if you choose the “override_origin” mode.

minimum0

status_code_ttl: optional array of object { value, status_code, status_code_range } 

A list of TTLs to apply to specific status codes or status code ranges.

value: number

The time to cache the response for (in seconds). A value of 0 is equivalent to setting the cache control header with the value “no-cache”. A value of -1 is equivalent to setting the cache control header with the value of “no-store”.

status_code: optional number

A single status code to apply the TTL to.

maximum999

minimum100

status_code_range: optional object { from, to } 

A range of status codes to apply the TTL to.

from: optional number

The lower bound of the range.

maximum999

minimum100

to: optional number

The upper bound of the range.

maximum999

minimum100

origin_cache_control: optional boolean

Whether Cloudflare will aim to strictly adhere to RFC 7234.

origin_error_page_passthru: optional boolean

Whether to generate Cloudflare error pages for issues from the origin server.

origin_range_requests: optional object { mode } 

Controls whether Cloudflare fetches a large asset from the origin as a series of range requests instead of one whole-body request.

mode: "on" or "off" or "default"

Whether to use range requests. `default` is the behaviour the zone gets without this rule.

One of the following:

"on"

"off"

"default"

read_timeout: optional number

A timeout value between two successive read operations to use for your origin server. Historically, the timeout value between two read options from Cloudflare to an origin server is 100 seconds. If you are attempting to reduce HTTP 524 errors because of timeouts from an origin server, try increasing this timeout value.

maximum6000

minimum100

respect_strong_etags: optional boolean

Whether Cloudflare should respect strong ETag (entity tag) headers. If false, Cloudflare converts strong ETag headers to weak ETag headers.

serve_stale: optional object { disable_stale_while_updating } 

When to serve stale content from cache.

disable_stale_while_updating: optional boolean

Whether Cloudflare should disable serving stale content while getting the latest content from the origin.

shared_dictionary: optional object { match_pattern } 

Configuration for shared dictionary compression. When set, Cloudflare injects Use-As-Dictionary headers on matching cacheable responses.

match_pattern: string

URL pattern for the Use-As-Dictionary match field. This pattern specifies which URLs can use this response as a dictionary.

maxLength1024

minLength1

strip_etags: optional boolean

Whether to strip ETag headers from the origin response before caching.

strip_last_modified: optional boolean

Whether to strip Last-Modified headers from the origin response before caching.

strip_set_cookie: optional boolean

Whether to strip Set-Cookie headers from the origin response before caching.

vary: optional object { default, headers } 

Controls how cached responses vary based on request headers. `default` is required by the API and applies to any Vary response header that does not have a per-header override.

default: optional object { action } 

Controls how response Vary headers without a per-header override contribute to the cache key.

action: "bypass" or "passthrough" or "normalize"

How the header value is treated when building the cache key.

One of the following:

"bypass"

"passthrough"

"normalize"

headers: optional map[object { action, languages, media_types } ]

A mapping of lowercase request header names to their vary configuration.

action: "bypass" or "passthrough" or "normalize"

How the header value is treated when building the cache key.

One of the following:

"bypass"

"passthrough"

"normalize"

languages: optional array of string

The set of languages to normalize against. Only valid for the `accept-language` header.

media_types: optional array of string

The set of media types to normalize against. Only valid for the `accept` header.

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

SetCacheTags object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "set_cache_tags"

The action to perform when the rule matches.

action_parameters: optional object { operation, values }  or object { expression, operation }  or object { operation, values }  or 3 more

The parameters configuring the rule’s action.

One of the following:

AddCacheTagsValues object { operation, values } 

Add cache tags using a list of values.

operation: "add" or "remove" or "set"

The operation to perform on the cache tags.

One of the following:

"add"

"remove"

"set"

values: array of string

A list of cache tag values.

AddCacheTagsExpression object { expression, operation } 

Add cache tags using an expression.

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

operation: "add" or "remove" or "set"

The operation to perform on the cache tags.

One of the following:

"add"

"remove"

"set"

RemoveCacheTagsValues object { operation, values } 

Remove cache tags using a list of values.

operation: "add" or "remove" or "set"

The operation to perform on the cache tags.

One of the following:

"add"

"remove"

"set"

values: array of string

A list of cache tag values.

RemoveCacheTagsExpression object { expression, operation } 

Remove cache tags using an expression.

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

operation: "add" or "remove" or "set"

The operation to perform on the cache tags.

One of the following:

"add"

"remove"

"set"

SetCacheTagsValues object { operation, values } 

Set cache tags using a list of values.

operation: "add" or "remove" or "set"

The operation to perform on the cache tags.

One of the following:

"add"

"remove"

"set"

values: array of string

A list of cache tag values.

SetCacheTagsExpression object { expression, operation } 

Set cache tags using an expression.

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

operation: "add" or "remove" or "set"

The operation to perform on the cache tags.

One of the following:

"add"

"remove"

"set"

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

SetConfigRule object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "set_config"

The action to perform when the rule matches.

action_parameters: optional object { automatic_https_rewrites, autominify, bic, 21 more } 

The parameters configuring the rule’s action.

automatic_https_rewrites: optional boolean

Whether to enable Automatic HTTPS Rewrites.

autominify: optional object { css, html, js } 

Which file extensions to minify automatically.

css: optional boolean

Whether to minify CSS files.

html: optional boolean

Whether to minify HTML files.

js: optional boolean

Whether to minify JavaScript files.

bic: optional boolean

Whether to enable Browser Integrity Check (BIC).

content_converter: optional boolean

Whether to enable content conversion (e.g., HTML to Markdown).

Deprecateddisable_apps: optional true

Cloudflare Apps are deprected.

Whether to disable Cloudflare Apps.

disable_pay_per_crawl: optional true

Whether to disable Pay Per Crawl.

disable_rum: optional true

Whether to disable Real User Monitoring (RUM).

disable_zaraz: optional true

Whether to disable Zaraz.

email_obfuscation: optional boolean

Whether to enable Email Obfuscation.

fonts: optional boolean

Whether to enable Cloudflare Fonts.

hotlink_protection: optional boolean

Whether to enable Hotlink Protection.

Deprecatedmirage: optional boolean

Mirage is deprecated. More information at <https://developers.cloudflare.com/speed/optimization/images/mirage/>.

Whether to enable Mirage.

opportunistic_encryption: optional boolean

Whether to enable Opportunistic Encryption.

polish: optional "off" or "lossless" or "lossy" or "webp"

The Polish level to configure.

One of the following:

"off"

"lossless"

"lossy"

"webp"

redirects_for_ai_training: optional boolean

Whether to redirect verified AI training crawlers to canonical URLs found in the HTML response.

request_body_buffering: optional "none" or "standard" or "full"

The request body buffering mode.

One of the following:

"none"

"standard"

"full"

response_body_buffering: optional "none" or "standard"

The response body buffering mode.

One of the following:

"none"

"standard"

rocket_loader: optional boolean

Whether to enable Rocket Loader.

security_level: optional "off" or "essentially_off" or "low" or 3 more

The Security Level to configure.

One of the following:

"off"

"essentially_off"

"low"

"medium"

"high"

"under_attack"

server_side_excludes: optional boolean

Whether to enable Server-Side Excludes.

ssl: optional "off" or "flexible" or "full" or 2 more

The SSL level to configure.

One of the following:

"off"

"flexible"

"full"

"strict"

"origin_pull"

Deprecatedsxg: optional boolean

Signed Exchanges (SXG) is deprecated.

Whether to enable Signed Exchanges (SXG).

webmcp_enabled: optional boolean

Whether to serve the WebMCP bridge script, which exposes the page’s tools to browser AI agents.

webmcp_packs: optional array of string

Bundled WebMCP tool packs to activate for matching requests. An empty array disables all packs. Omitting this parameter leaves the pack selection unchanged. Does not enable the WebMCP bridge itself. Non-empty selections require the WebMCP Configuration Rules entitlement.

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

SkipRule object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "skip"

The action to perform when the rule matches.

action_parameters: optional object { phase, phases, products, 3 more } 

The parameters configuring the rule’s action.

phase: optional "current"

A phase to skip the execution of. This option is only compatible with the products option.

phases: optional array of [Phase](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets%20%3E%20\(model\)%20phase%20%3E%20\(schema\))

A list of phases to skip the execution of. This option is incompatible with the rulesets option.

One of the following:

"ddos_l4"

"ddos_l7"

"http_config_settings"

"http_custom_errors"

"http_log_custom_fields"

"http_ratelimit"

"http_request_cache_settings"

"http_request_dynamic_redirect"

"http_request_firewall_custom"

"http_request_firewall_managed"

"http_request_late_transform"

"http_request_origin"

"http_request_redirect"

"http_request_sanitize"

"http_request_sbfm"

"http_request_transform"

"http_response_cache_settings"

"http_response_compression"

"http_response_firewall_managed"

"http_response_headers_transform"

"magic_transit"

"magic_transit_ids_managed"

"magic_transit_managed"

"magic_transit_ratelimit"

products: optional array of "bic" or "hot" or "rateLimit" or 4 more

A list of legacy security products to skip the execution of.

One of the following:

"bic"

"hot"

"rateLimit"

"securityLevel"

"uaBlock"

"waf"

"zoneLockdown"

rules: optional map[array of string]

A mapping of ruleset IDs to a list of rule IDs in that ruleset to skip the execution of. This option is incompatible with the ruleset option.

ruleset: optional "current"

A ruleset to skip the execution of. This option is incompatible with the rulesets option.

rulesets: optional array of string

A list of ruleset IDs to skip the execution of. This option is incompatible with the ruleset and phases options.

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

TransformResponseHTML object { last_updated, version, id, 10 more } 

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

version: string

The version of the rule.

id: optional string

The unique ID of the rule.

action: optional "transform_response_html"

The action to perform when the rule matches.

action_parameters: optional object { link_maze } 

The parameters configuring the rule’s action.

link_maze: unknown

Enables the link maze transformation on the response.

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

enabled: optional boolean

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

expression: optional string

The expression defining which traffic will match the rule.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

##### ReturnsExpand Collapse 

errors: array of object { message, code, source } 

A list of error messages.

message: string

A text description of this message.

minLength1

code: optional number

A unique code for this message.

source: optional object { pointer } 

The source of this message.

pointer: string

A JSON pointer to the field that is the source of the message.

minLength1

messages: array of object { message, code, source } 

A list of warning messages.

message: string

A text description of this message.

minLength1

code: optional number

A unique code for this message.

source: optional object { pointer } 

The source of this message.

pointer: string

A JSON pointer to the field that is the source of the message.

minLength1

result: object { id, kind, last_updated, 5 more }  or unknown

A result.

One of the following:

Ruleset object { id, kind, last_updated, 5 more } 

A ruleset object.

id: string

The unique ID of the ruleset.

kind: [Kind](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets%20%3E%20\(model\)%20kind%20%3E%20\(schema\))

The kind of the ruleset.

One of the following:

"managed"

"custom"

"root"

"zone"

last_updated: string

The timestamp of when the ruleset was last modified.

formatdate-time

name: string

The human-readable name of the ruleset.

minLength1

phase: [Phase](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets%20%3E%20\(model\)%20phase%20%3E%20\(schema\))

The phase of the ruleset.

One of the following:

"ddos_l4"

"ddos_l7"

"http_config_settings"

"http_custom_errors"

"http_log_custom_fields"

"http_ratelimit"

"http_request_cache_settings"

"http_request_dynamic_redirect"

"http_request_firewall_custom"

"http_request_firewall_managed"

"http_request_late_transform"

"http_request_origin"

"http_request_redirect"

"http_request_sanitize"

"http_request_sbfm"

"http_request_transform"

"http_response_cache_settings"

"http_response_compression"

"http_response_firewall_managed"

"http_response_headers_transform"

"magic_transit"

"magic_transit_ids_managed"

"magic_transit_managed"

"magic_transit_ratelimit"

rules: array of [BlockRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20block_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more }  or object { id, action, enabled, 10 more }  or [CompressResponseRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20compress_response_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more }  or 18 more

The list of rules in the ruleset.

One of the following:

BlockRule = [BlockRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20block_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more } 

id: string

action: string

enabled: boolean

expression: string

ref: string

ChallengeRule object { id, action, enabled, 10 more } 

id: string

The unique ID of the rule.

action: "challenge"

The action to perform when the rule matches.

enabled: boolean

Whether the rule should be executed.

expression: string

The expression defining which traffic will match the rule.

minLength1

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

version: string

The version of the rule.

action_parameters: optional unknown

The parameters configuring the rule’s action.

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

ResponseCompressionRule = [CompressResponseRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20compress_response_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more } 

id: string

action: string

enabled: boolean

expression: string

ref: string

DDoSDynamicRule = [DDoSDynamicRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20ddos_dynamic_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more } 

id: string

action: string

enabled: boolean

expression: string

ref: string

ExecuteRule = [ExecuteRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20execute_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more } 

id: string

action: string

enabled: boolean

expression: string

ref: string

ForceConnectionCloseRule = [ForceConnectionCloseRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20force_connection_close_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more } 

id: string

action: string

enabled: boolean

expression: string

ref: string

JavaScriptChallengeRule object { id, action, enabled, 10 more } 

id: string

The unique ID of the rule.

action: "js_challenge"

The action to perform when the rule matches.

enabled: boolean

Whether the rule should be executed.

expression: string

The expression defining which traffic will match the rule.

minLength1

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

version: string

The version of the rule.

action_parameters: optional unknown

The parameters configuring the rule’s action.

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

LogRule = [LogRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20log_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more } 

id: string

action: string

enabled: boolean

expression: string

ref: string

LogCustomFieldRule = [LogCustomFieldRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20log_custom_field_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more } 

id: string

action: string

enabled: boolean

expression: string

ref: string

ManagedChallengeRule = [ManagedChallengeRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20managed_challenge_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more } 

id: string

action: string

enabled: boolean

expression: string

ref: string

RedirectRule = [RedirectRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20redirect_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more } 

id: string

action: string

enabled: boolean

expression: string

ref: string

RewriteRule = [RewriteRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20rewrite_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more } 

id: string

action: string

enabled: boolean

expression: string

ref: string

RouteRule = [RouteRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20route_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more } 

id: string

action: string

enabled: boolean

expression: string

ref: string

ScoreRule = [ScoreRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20score_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more } 

id: string

action: string

enabled: boolean

expression: string

ref: string

ServeErrorRule = [ServeErrorRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20serve_error_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more } 

id: string

action: string

enabled: boolean

expression: string

ref: string

SetCacheControlRule object { id, action, enabled, 10 more } 

id: string

The unique ID of the rule.

action: "set_cache_control"

The action to perform when the rule matches.

enabled: boolean

expression: string

The expression defining which traffic will match the rule.

minLength1

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

version: string

The version of the rule.

action_parameters: optional object { immutable, "max-age", "must-revalidate", 10 more } 

The parameters configuring the rule’s action.

immutable: optional object { operation, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration.

One of the following:

SetDirective object { operation, cloudflare_only } 

Set the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"max-age": optional object { operation, value, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration that accepts a duration value in seconds.

One of the following:

SetDirective object { operation, value, cloudflare_only } 

Set the directive with a duration value in seconds.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

value: number

The duration value in seconds for the directive.

minimum0

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"must-revalidate": optional object { operation, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration.

One of the following:

SetDirective object { operation, cloudflare_only } 

Set the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"must-understand": optional object { operation, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration.

One of the following:

SetDirective object { operation, cloudflare_only } 

Set the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"no-cache": optional object { operation, cloudflare_only, qualifiers }  or object { operation, cloudflare_only } 

A cache-control directive configuration that accepts optional qualifiers (header names).

One of the following:

SetDirective object { operation, cloudflare_only, qualifiers } 

Set the directive with optional qualifiers.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

qualifiers: optional array of string

Optional list of header names to qualify the directive (e.g., for “private” or “no-cache” directives).

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"no-store": optional object { operation, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration.

One of the following:

SetDirective object { operation, cloudflare_only } 

Set the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"no-transform": optional object { operation, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration.

One of the following:

SetDirective object { operation, cloudflare_only } 

Set the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

private: optional object { operation, cloudflare_only, qualifiers }  or object { operation, cloudflare_only } 

A cache-control directive configuration that accepts optional qualifiers (header names).

One of the following:

SetDirective object { operation, cloudflare_only, qualifiers } 

Set the directive with optional qualifiers.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

qualifiers: optional array of string

Optional list of header names to qualify the directive (e.g., for “private” or “no-cache” directives).

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"proxy-revalidate": optional object { operation, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration.

One of the following:

SetDirective object { operation, cloudflare_only } 

Set the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

public: optional object { operation, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration.

One of the following:

SetDirective object { operation, cloudflare_only } 

Set the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"s-maxage": optional object { operation, value, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration that accepts a duration value in seconds.

One of the following:

SetDirective object { operation, value, cloudflare_only } 

Set the directive with a duration value in seconds.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

value: number

The duration value in seconds for the directive.

minimum0

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"stale-if-error": optional object { operation, value, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration that accepts a duration value in seconds.

One of the following:

SetDirective object { operation, value, cloudflare_only } 

Set the directive with a duration value in seconds.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

value: number

The duration value in seconds for the directive.

minimum0

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

"stale-while-revalidate": optional object { operation, value, cloudflare_only }  or object { operation, cloudflare_only } 

A cache-control directive configuration that accepts a duration value in seconds.

One of the following:

SetDirective object { operation, value, cloudflare_only } 

Set the directive with a duration value in seconds.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

value: number

The duration value in seconds for the directive.

minimum0

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

RemoveDirective object { operation, cloudflare_only } 

Remove the directive.

operation: "set" or "remove"

The operation to perform on the cache-control directive.

One of the following:

"set"

"remove"

cloudflare_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

SetCacheSettingsRule = [SetCacheSettingsRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20set_cache_settings_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more } 

id: string

action: string

enabled: boolean

expression: string

ref: string

SetCacheTagsRule object { id, action, enabled, 10 more } 

id: string

The unique ID of the rule.

action: "set_cache_tags"

The action to perform when the rule matches.

enabled: boolean

expression: string

The expression defining which traffic will match the rule.

minLength1

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

version: string

The version of the rule.

action_parameters: optional object { operation, values }  or object { expression, operation }  or object { operation, values }  or 3 more

The parameters configuring the rule’s action.

One of the following:

AddCacheTagsValues object { operation, values } 

Add cache tags using a list of values.

operation: "add" or "remove" or "set"

The operation to perform on the cache tags.

One of the following:

"add"

"remove"

"set"

values: array of string

A list of cache tag values.

AddCacheTagsExpression object { expression, operation } 

Add cache tags using an expression.

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

operation: "add" or "remove" or "set"

The operation to perform on the cache tags.

One of the following:

"add"

"remove"

"set"

RemoveCacheTagsValues object { operation, values } 

Remove cache tags using a list of values.

operation: "add" or "remove" or "set"

The operation to perform on the cache tags.

One of the following:

"add"

"remove"

"set"

values: array of string

A list of cache tag values.

RemoveCacheTagsExpression object { expression, operation } 

Remove cache tags using an expression.

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

operation: "add" or "remove" or "set"

The operation to perform on the cache tags.

One of the following:

"add"

"remove"

"set"

SetCacheTagsValues object { operation, values } 

Set cache tags using a list of values.

operation: "add" or "remove" or "set"

The operation to perform on the cache tags.

One of the following:

"add"

"remove"

"set"

values: array of string

A list of cache tag values.

SetCacheTagsExpression object { expression, operation } 

Set cache tags using an expression.

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

operation: "add" or "remove" or "set"

The operation to perform on the cache tags.

One of the following:

"add"

"remove"

"set"

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

SetConfigurationRule = [SetConfigRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20set_config_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more } 

id: string

action: string

enabled: boolean

expression: string

ref: string

SkipRule = [SkipRule](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20skip_rule%20%3E%20\(schema\)) { last_updated, version, id, 10 more } 

id: string

action: string

enabled: boolean

expression: string

ref: string

TransformResponseHTMLRule object { id, action, enabled, 10 more } 

id: string

The unique ID of the rule.

action: "transform_response_html"

The action to perform when the rule matches.

enabled: boolean

expression: string

The expression defining which traffic will match the rule.

minLength1

last_updated: string

The timestamp of when the rule was last modified.

formatdate-time

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

version: string

The version of the rule.

action_parameters: optional object { link_maze } 

The parameters configuring the rule’s action.

link_maze: unknown

Enables the link maze transformation on the response.

categories: optional array of string

The categories of the rule.

description: optional string

An informative description of the rule.

exposed_credential_check: optional object { password_expression, username_expression } 

Configuration for exposed credential checking.

password_expression: string

An expression that selects the password used in the credentials check.

minLength1

username_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

logging: optional [Logging](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets.rules%20%3E%20\(model\)%20logging%20%3E%20\(schema\)) { enabled } 

An object configuring the rule’s logging behavior.

enabled: boolean

Whether to generate a log when the rule matches.

ratelimit: optional object { characteristics, period, counting_expression, 5 more } 

An object configuring the rule’s rate limit behavior.

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

period: number

Period in seconds over which the counter is being incremented.

minimum0

counting_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

mitigation_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

requests_per_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

requests_to_origin: optional boolean

Whether counting is only performed when an origin is reached.

score_per_period: optional number

The score threshold per period for which the action will be executed the first time.

score_response_header_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

version: string

The version of the ruleset.

description: optional string

An informative description of the ruleset.

unknown

Returned when dry_run is true.

success: true

Whether the API call was successful.

### Update an account or zone ruleset

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
    
    
    curl https://api.cloudflare.com/client/v4/$ACCOUNTS_OR_ZONES/$ACCOUNT_OR_ZONE_ID/rulesets/$RULESET_ID \
        -X PUT \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{
              "description": "A description for my ruleset.",
              "kind": "root",
              "name": "My ruleset",
              "phase": "http_request_firewall_custom"
            }'

200 example
    
    
    {
      "errors": [
        {
          "message": "something bad happened",
          "code": 10000,
          "source": {
            "pointer": "/rules/0/action"
          }
        }
      ],
      "messages": [
        {
          "message": "something bad happened",
          "code": 10000,
          "source": {
            "pointer": "/rules/0/action"
          }
        }
      ],
      "result": {
        "id": "2f2feab2026849078ba485f918791bdc",
        "kind": "root",
        "last_updated": "2000-01-01T00:00:00Z",
        "name": "My ruleset",
        "phase": "http_request_firewall_custom",
        "rules": [
          {
            "last_updated": "2000-01-01T00:00:00Z",
            "version": "1",
            "id": "id",
            "action": "action",
            "action_parameters": {
              "response": {
                "content": "{\n  \"success\": false,\n  \"error\": \"you have been blocked\"\n}",
                "content_type": "application/json",
                "status_code": 400
              }
            },
            "categories": [
              "directory-traversal"
            ],
            "description": "Block the request.",
            "enabled": true,
            "exposed_credential_check": {
              "password_expression": "url_decode(http.request.body.form[\\\"password\\\"][0])",
              "username_expression": "url_decode(http.request.body.form[\\\"username\\\"][0])"
            },
            "expression": "expression",
            "logging": {
              "enabled": true
            },
            "ratelimit": {
              "characteristics": [
                "cf.colo.id"
              ],
              "period": 60,
              "counting_expression": "http.request.body.raw eq \"abcd\"",
              "mitigation_timeout": 600,
              "requests_per_period": 1000,
              "requests_to_origin": true,
              "score_per_period": 400,
              "score_response_header_name": "my-score"
            },
            "ref": "ref"
          }
        ],
        "version": "1",
        "description": "A description for my ruleset."
      },
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "errors": [
        {
          "message": "something bad happened",
          "code": 10000,
          "source": {
            "pointer": "/rules/0/action"
          }
        }
      ],
      "messages": [
        {
          "message": "something bad happened",
          "code": 10000,
          "source": {
            "pointer": "/rules/0/action"
          }
        }
      ],
      "result": {
        "id": "2f2feab2026849078ba485f918791bdc",
        "kind": "root",
        "last_updated": "2000-01-01T00:00:00Z",
        "name": "My ruleset",
        "phase": "http_request_firewall_custom",
        "rules": [
          {
            "last_updated": "2000-01-01T00:00:00Z",
            "version": "1",
            "id": "id",
            "action": "action",
            "action_parameters": {
              "response": {
                "content": "{\n  \"success\": false,\n  \"error\": \"you have been blocked\"\n}",
                "content_type": "application/json",
                "status_code": 400
              }
            },
            "categories": [
              "directory-traversal"
            ],
            "description": "Block the request.",
            "enabled": true,
            "exposed_credential_check": {
              "password_expression": "url_decode(http.request.body.form[\\\"password\\\"][0])",
              "username_expression": "url_decode(http.request.body.form[\\\"username\\\"][0])"
            },
            "expression": "expression",
            "logging": {
              "enabled": true
            },
            "ratelimit": {
              "characteristics": [
                "cf.colo.id"
              ],
              "period": 60,
              "counting_expression": "http.request.body.raw eq \"abcd\"",
              "mitigation_timeout": 600,
              "requests_per_period": 1000,
              "requests_to_origin": true,
              "score_per_period": 400,
              "score_response_header_name": "my-score"
            },
            "ref": "ref"
          }
        ],
        "version": "1",
        "description": "A description for my ruleset."
      },
      "success": true
    }
