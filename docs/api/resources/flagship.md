---
url: https://developers.cloudflare.com/api/resources/flagship/
title: Flagship | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:42.209572+00:00
---

# Flagship | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/flagship/

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Flagship

#### FlagshipApps

##### [List apps](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/methods/list)

GET/accounts/{account_id}/flagship/apps

##### [Get app](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/methods/get)

GET/accounts/{account_id}/flagship/apps/{app_id}

##### [Create app](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/methods/create)

POST/accounts/{account_id}/flagship/apps

##### [Update app](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/methods/update)

PUT/accounts/{account_id}/flagship/apps/{app_id}

##### [Delete app](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/methods/delete)

DELETE/accounts/{account_id}/flagship/apps/{app_id}

##### ModelsExpand Collapse 

AppListResponse object { id, created_at, name, 2 more } 

id: string

created_at: string

name: string

updated_at: string

updated_by: string

Email of the actor who last modified the app, or `unknown` when unavailable.

AppGetResponse object { id, created_at, name, 2 more } 

id: string

created_at: string

name: string

updated_at: string

updated_by: string

Email of the actor who last modified the app, or `unknown` when unavailable.

AppCreateResponse object { id, created_at, name, 2 more } 

id: string

created_at: string

name: string

updated_at: string

updated_by: string

Email of the actor who last modified the app, or `unknown` when unavailable.

AppUpdateResponse object { id, created_at, name, 2 more } 

id: string

created_at: string

name: string

updated_at: string

updated_by: string

Email of the actor who last modified the app, or `unknown` when unavailable.

AppDeleteResponse object { id } 

id: string

#### FlagshipAppsFlags

##### [List flags](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/subresources/flags/methods/list)

GET/accounts/{account_id}/flagship/apps/{app_id}/flags

##### [Get flag](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/subresources/flags/methods/get)

GET/accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}

##### [Create flag](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/subresources/flags/methods/create)

POST/accounts/{account_id}/flagship/apps/{app_id}/flags

##### [Update flag](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/subresources/flags/methods/update)

PUT/accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}

##### [Delete flag](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/subresources/flags/methods/delete)

DELETE/accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}

##### ModelsExpand Collapse 

FlagListResponse object { default_variation, enabled, key, 6 more } 

default_variation: string

Variation the API serves when the flag is off, or when it’s on but no rule matches the context. Must be a key in `variations`.

minLength1

enabled: boolean

When false, the flag bypasses all rules and always serves `default_variation`.

key: string

Unique identifier for the flag within an app. Used in all evaluation and SDK calls.

maxLength64

minLength1

rules: array of object { conditions, priority, serve_variation, rollout } 

Targeting rules evaluated in ascending `priority`; the first matching rule wins. An empty array means the flag always serves `default_variation`.

conditions: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

Conditions the context must satisfy for this rule to match. An empty array matches all contexts.

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

priority: number

Evaluation order: the API evaluates rules with lower numbers first. Must be unique across the flag’s rules.

minimum1

serve_variation: string

Variation the API serves when this rule matches. Must be a key in `variations`.

minLength1

rollout: optional object { percentage, attribute } 

percentage: number

Percentage of matching traffic (0–100, up to 2 decimal places) served this variation. For multi-way splits, use cumulative upper bounds across rules (e.g. 30, 70, 100).

maximum100

minimum0

multipleOf0.01

attribute: optional string

Context attribute used for sticky bucketing. Defaults to `targetingKey`. If absent at evaluation time, bucketing is random per request.

maxLength64

minLength1

type: "boolean" or "string" or "number" or "json"

Server-inferred value type shared by all of the flag’s variations.

One of the following:

"boolean"

"string"

"number"

"json"

variations: map[string or number or boolean or 2 more]

Map of variation name to value. All values share the same type (boolean, string, number, or JSON object/array), and each serialized value stays within 10KB.

One of the following:

string

number

boolean

map[unknown]

array of unknown

description: optional string

Optional operator-facing description. It does not affect flag evaluation.

maxLength512

updated_at: optional string

updated_by: optional string

FlagGetResponse object { default_variation, enabled, key, 6 more } 

default_variation: string

Variation the API serves when the flag is off, or when it’s on but no rule matches the context. Must be a key in `variations`.

minLength1

enabled: boolean

When false, the flag bypasses all rules and always serves `default_variation`.

key: string

Unique identifier for the flag within an app. Used in all evaluation and SDK calls.

maxLength64

minLength1

rules: array of object { conditions, priority, serve_variation, rollout } 

Targeting rules evaluated in ascending `priority`; the first matching rule wins. An empty array means the flag always serves `default_variation`.

conditions: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

Conditions the context must satisfy for this rule to match. An empty array matches all contexts.

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

priority: number

Evaluation order: the API evaluates rules with lower numbers first. Must be unique across the flag’s rules.

minimum1

serve_variation: string

Variation the API serves when this rule matches. Must be a key in `variations`.

minLength1

rollout: optional object { percentage, attribute } 

percentage: number

Percentage of matching traffic (0–100, up to 2 decimal places) served this variation. For multi-way splits, use cumulative upper bounds across rules (e.g. 30, 70, 100).

maximum100

minimum0

multipleOf0.01

attribute: optional string

Context attribute used for sticky bucketing. Defaults to `targetingKey`. If absent at evaluation time, bucketing is random per request.

maxLength64

minLength1

type: "boolean" or "string" or "number" or "json"

Server-inferred value type shared by all of the flag’s variations.

One of the following:

"boolean"

"string"

"number"

"json"

variations: map[string or number or boolean or 2 more]

Map of variation name to value. All values share the same type (boolean, string, number, or JSON object/array), and each serialized value stays within 10KB.

One of the following:

string

number

boolean

map[unknown]

array of unknown

description: optional string

Optional operator-facing description. It does not affect flag evaluation.

maxLength512

updated_at: optional string

updated_by: optional string

FlagCreateResponse object { default_variation, enabled, key, 6 more } 

default_variation: string

Variation the API serves when the flag is off, or when it’s on but no rule matches the context. Must be a key in `variations`.

minLength1

enabled: boolean

When false, the flag bypasses all rules and always serves `default_variation`.

key: string

Unique identifier for the flag within an app. Used in all evaluation and SDK calls.

maxLength64

minLength1

rules: array of object { conditions, priority, serve_variation, rollout } 

Targeting rules evaluated in ascending `priority`; the first matching rule wins. An empty array means the flag always serves `default_variation`.

conditions: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

Conditions the context must satisfy for this rule to match. An empty array matches all contexts.

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

priority: number

Evaluation order: the API evaluates rules with lower numbers first. Must be unique across the flag’s rules.

minimum1

serve_variation: string

Variation the API serves when this rule matches. Must be a key in `variations`.

minLength1

rollout: optional object { percentage, attribute } 

percentage: number

Percentage of matching traffic (0–100, up to 2 decimal places) served this variation. For multi-way splits, use cumulative upper bounds across rules (e.g. 30, 70, 100).

maximum100

minimum0

multipleOf0.01

attribute: optional string

Context attribute used for sticky bucketing. Defaults to `targetingKey`. If absent at evaluation time, bucketing is random per request.

maxLength64

minLength1

type: "boolean" or "string" or "number" or "json"

Server-inferred value type shared by all of the flag’s variations.

One of the following:

"boolean"

"string"

"number"

"json"

variations: map[string or number or boolean or 2 more]

Map of variation name to value. All values share the same type (boolean, string, number, or JSON object/array), and each serialized value stays within 10KB.

One of the following:

string

number

boolean

map[unknown]

array of unknown

description: optional string

Optional operator-facing description. It does not affect flag evaluation.

maxLength512

updated_at: optional string

updated_by: optional string

FlagUpdateResponse object { default_variation, enabled, key, 6 more } 

default_variation: string

Variation the API serves when the flag is off, or when it’s on but no rule matches the context. Must be a key in `variations`.

minLength1

enabled: boolean

When false, the flag bypasses all rules and always serves `default_variation`.

key: string

Unique identifier for the flag within an app. Used in all evaluation and SDK calls.

maxLength64

minLength1

rules: array of object { conditions, priority, serve_variation, rollout } 

Targeting rules evaluated in ascending `priority`; the first matching rule wins. An empty array means the flag always serves `default_variation`.

conditions: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

Conditions the context must satisfy for this rule to match. An empty array matches all contexts.

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

priority: number

Evaluation order: the API evaluates rules with lower numbers first. Must be unique across the flag’s rules.

minimum1

serve_variation: string

Variation the API serves when this rule matches. Must be a key in `variations`.

minLength1

rollout: optional object { percentage, attribute } 

percentage: number

Percentage of matching traffic (0–100, up to 2 decimal places) served this variation. For multi-way splits, use cumulative upper bounds across rules (e.g. 30, 70, 100).

maximum100

minimum0

multipleOf0.01

attribute: optional string

Context attribute used for sticky bucketing. Defaults to `targetingKey`. If absent at evaluation time, bucketing is random per request.

maxLength64

minLength1

type: "boolean" or "string" or "number" or "json"

Server-inferred value type shared by all of the flag’s variations.

One of the following:

"boolean"

"string"

"number"

"json"

variations: map[string or number or boolean or 2 more]

Map of variation name to value. All values share the same type (boolean, string, number, or JSON object/array), and each serialized value stays within 10KB.

One of the following:

string

number

boolean

map[unknown]

array of unknown

description: optional string

Optional operator-facing description. It does not affect flag evaluation.

maxLength512

updated_at: optional string

updated_by: optional string

FlagDeleteResponse object { key } 

key: string

#### FlagshipAppsFlagsChangelog

##### [List flag changelog entries](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/subresources/flags/subresources/changelog/methods/list)

GET/accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}/changelog

##### ModelsExpand Collapse 

ChangelogListResponse = object { after, event, flag_key }  or object { after, event, flag_key }  or object { after, diff, event, flag_key } 

One of the following:

object { after, event, flag_key } 

after: object { default_variation, enabled, key, 6 more } 

default_variation: string

Variation the API serves when the flag is off, or when it’s on but no rule matches the context. Must be a key in `variations`.

minLength1

enabled: boolean

When false, the flag bypasses all rules and always serves `default_variation`.

key: string

Unique identifier for the flag within an app. Used in all evaluation and SDK calls.

maxLength64

minLength1

rules: array of object { conditions, priority, serve_variation, rollout } 

Targeting rules evaluated in ascending `priority`; the first matching rule wins. An empty array means the flag always serves `default_variation`.

conditions: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

Conditions the context must satisfy for this rule to match. An empty array matches all contexts.

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

priority: number

Evaluation order: the API evaluates rules with lower numbers first. Must be unique across the flag’s rules.

minimum1

serve_variation: string

Variation the API serves when this rule matches. Must be a key in `variations`.

minLength1

rollout: optional object { percentage, attribute } 

percentage: number

Percentage of matching traffic (0–100, up to 2 decimal places) served this variation. For multi-way splits, use cumulative upper bounds across rules (e.g. 30, 70, 100).

maximum100

minimum0

multipleOf0.01

attribute: optional string

Context attribute used for sticky bucketing. Defaults to `targetingKey`. If absent at evaluation time, bucketing is random per request.

maxLength64

minLength1

type: "boolean" or "string" or "number" or "json"

Server-inferred value type shared by all of the flag’s variations.

One of the following:

"boolean"

"string"

"number"

"json"

variations: map[string or number or boolean or 2 more]

Map of variation name to value. All values share the same type (boolean, string, number, or JSON object/array), and each serialized value stays within 10KB.

One of the following:

string

number

boolean

map[unknown]

array of unknown

description: optional string

Optional operator-facing description. It does not affect flag evaluation.

maxLength512

updated_at: optional string

updated_by: optional string

event: "create"

flag_key: string

object { after, event, flag_key } 

after: object { default_variation, enabled, key, 6 more } 

default_variation: string

Variation the API serves when the flag is off, or when it’s on but no rule matches the context. Must be a key in `variations`.

minLength1

enabled: boolean

When false, the flag bypasses all rules and always serves `default_variation`.

key: string

Unique identifier for the flag within an app. Used in all evaluation and SDK calls.

maxLength64

minLength1

rules: array of object { conditions, priority, serve_variation, rollout } 

Targeting rules evaluated in ascending `priority`; the first matching rule wins. An empty array means the flag always serves `default_variation`.

conditions: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

Conditions the context must satisfy for this rule to match. An empty array matches all contexts.

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

priority: number

Evaluation order: the API evaluates rules with lower numbers first. Must be unique across the flag’s rules.

minimum1

serve_variation: string

Variation the API serves when this rule matches. Must be a key in `variations`.

minLength1

rollout: optional object { percentage, attribute } 

percentage: number

Percentage of matching traffic (0–100, up to 2 decimal places) served this variation. For multi-way splits, use cumulative upper bounds across rules (e.g. 30, 70, 100).

maximum100

minimum0

multipleOf0.01

attribute: optional string

Context attribute used for sticky bucketing. Defaults to `targetingKey`. If absent at evaluation time, bucketing is random per request.

maxLength64

minLength1

type: "boolean" or "string" or "number" or "json"

Server-inferred value type shared by all of the flag’s variations.

One of the following:

"boolean"

"string"

"number"

"json"

variations: map[string or number or boolean or 2 more]

Map of variation name to value. All values share the same type (boolean, string, number, or JSON object/array), and each serialized value stays within 10KB.

One of the following:

string

number

boolean

map[unknown]

array of unknown

description: optional string

Optional operator-facing description. It does not affect flag evaluation.

maxLength512

updated_at: optional string

updated_by: optional string

event: "delete"

flag_key: string

object { after, diff, event, flag_key } 

after: object { default_variation, enabled, key, 6 more } 

default_variation: string

Variation the API serves when the flag is off, or when it’s on but no rule matches the context. Must be a key in `variations`.

minLength1

enabled: boolean

When false, the flag bypasses all rules and always serves `default_variation`.

key: string

Unique identifier for the flag within an app. Used in all evaluation and SDK calls.

maxLength64

minLength1

rules: array of object { conditions, priority, serve_variation, rollout } 

Targeting rules evaluated in ascending `priority`; the first matching rule wins. An empty array means the flag always serves `default_variation`.

conditions: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

Conditions the context must satisfy for this rule to match. An empty array matches all contexts.

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of object { attribute, operator, value }  or object { clauses, logical_operator } 

One of the following:

object { attribute, operator, value } 

attribute: string

maxLength64

minLength1

operator: "equals" or "not_equals" or "greater_than" or 10 more

One of the following:

"equals"

"not_equals"

"greater_than"

"less_than"

"greater_than_or_equals"

"less_than_or_equals"

"contains"

"starts_with"

"ends_with"

"in"

"not_in"

"has"

"not_has"

value: string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

object { clauses, logical_operator } 

clauses: array of string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

logical_operator: "AND" or "OR"

One of the following:

"AND"

"OR"

priority: number

Evaluation order: the API evaluates rules with lower numbers first. Must be unique across the flag’s rules.

minimum1

serve_variation: string

Variation the API serves when this rule matches. Must be a key in `variations`.

minLength1

rollout: optional object { percentage, attribute } 

percentage: number

Percentage of matching traffic (0–100, up to 2 decimal places) served this variation. For multi-way splits, use cumulative upper bounds across rules (e.g. 30, 70, 100).

maximum100

minimum0

multipleOf0.01

attribute: optional string

Context attribute used for sticky bucketing. Defaults to `targetingKey`. If absent at evaluation time, bucketing is random per request.

maxLength64

minLength1

type: "boolean" or "string" or "number" or "json"

Server-inferred value type shared by all of the flag’s variations.

One of the following:

"boolean"

"string"

"number"

"json"

variations: map[string or number or boolean or 2 more]

Map of variation name to value. All values share the same type (boolean, string, number, or JSON object/array), and each serialized value stays within 10KB.

One of the following:

string

number

boolean

map[unknown]

array of unknown

description: optional string

Optional operator-facing description. It does not affect flag evaluation.

maxLength512

updated_at: optional string

updated_by: optional string

diff: map[object { from, to } ]

from: optional string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

to: optional string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

event: "update"

flag_key: string

#### FlagshipAppsEvaluate

##### [Evaluate flag from query context](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/subresources/evaluate/methods/get)

GET/accounts/{account_id}/flagship/apps/{app_id}/evaluate

##### ModelsExpand Collapse 

EvaluateGetResponse object { flagKey, reason, variant, value } 

flagKey: string

Key of the evaluated flag.

reason: "STATIC" or "TARGETING_MATCH" or "DEFAULT" or 2 more

Reason the evaluator selected this variation.

One of the following:

"STATIC"

"TARGETING_MATCH"

"DEFAULT"

"DISABLED"

"SPLIT"

variant: string

Name of the variation that supplied the resolved value.

value: optional string or number or boolean or 2 more

One of the following:

string

number

boolean

map[unknown]

array of unknown

[ Previous

* * *

DNS ](https://developers.cloudflare.com/api/resources/email_sending/subresources/subdomains/subresources/dns)[ Next

* * *

Apps ](https://developers.cloudflare.com/api/resources/flagship/subresources/apps)
