---
url: https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list/
title: Filter and list events | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:27:14.344562+00:00
---

# Filter and list events | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[Cloudforce One](https://developers.cloudflare.com/api/resources/cloudforce_one)

[Threat Events](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Filter and list events

GET/accounts/{account_id}/cloudforce-one/events

Use one standalone `datasetId` scope value: ‘all’/’*’ or ‘operational’ for readable intelligence datasets (isAnalytics=false), or ‘analytics’ for readable analytics datasets (isAnalytics=true). Scope values query at most 50 datasets and must be used alone. When `datasetId` is unspecified, events are listed from the default Cloudforce One Threat Events dataset. To list existing datasets, use the [`List Datasets`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/list/) endpoint.

##### Security

API Token

The preferred authorization scheme for interacting with the Cloudflare API. [Create a token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

**Example:**`Authorization: Bearer Sn3lZJTBX6kkg7OdcBUAxOO963GEIyGQqnFTOFYY`

##### Accepted Permissions (at least one required)

`Cloudforce One Write``Cloudforce One Read`

##### Path ParametersExpand Collapse 

account_id: string

Account ID.

##### Query ParametersExpand Collapse 

cache: optional "from-graph"

Cache strategy. ‘from-graph’ serves results from the graph-node KV cache when all requested UUIDs are cached; falls back to normal path on partial/zero hit.

cursor: optional string

Cursor for pagination. When provided, filters are embedded in the cursor so you only need to pass cursor and pageSize. Returned in the previous response’s result_info.cursor field. Use cursor-based pagination for deep pagination (beyond 100,000 records) or for optimal performance.

datasetId: optional array of string

Dataset UUIDs to query, or one standalone scope value: ‘all’/’*’ or ‘operational’ for readable intelligence datasets (isAnalytics=false), or ‘analytics’ for readable analytics datasets (isAnalytics=true). Scope values query at most 50 datasets. If not provided, uses the default dataset.

forceRefresh: optional boolean

format: optional "json" or "stix2" or "taxii"

One of the following:

"json"

"stix2"

"taxii"

order: optional "asc" or "desc"

One of the following:

"asc"

"desc"

orderBy: optional string

page: optional number

Page number (1-indexed) for offset-based pagination. Limited to offset of 100,000 records. For deep pagination, use cursor-based pagination instead.

pageSize: optional number

Number of results per page. Maximum 25,000.

search: optional array of object { field, op, value }  or object { field, op, value }  or object { field, op, value }  or 3 more

One of the following:

object { field, op, value } 

field: "attacker" or "attackerCountry" or "category" or 12 more

One of the following:

"attacker"

"attackerCountry"

"category"

"createdAt"

"date"

"event"

"indicator"

"indicatorType"

"mitreAttack"

"mitreCapec"

"tags"

"targetCountry"

"targetIndustry"

"tlp"

"uuid"

op: "equals" or "not" or "gt" or 8 more

One of the following:

"equals"

"not"

"gt"

"gte"

"lt"

"lte"

"like"

"contains"

"startsWith"

"endsWith"

"find"

value: string

maxLength512

minLength1

object { field, op, value } 

field: "attacker" or "attackerCountry" or "category" or 12 more

One of the following:

"attacker"

"attackerCountry"

"category"

"createdAt"

"date"

"event"

"indicator"

"indicatorType"

"mitreAttack"

"mitreCapec"

"tags"

"targetCountry"

"targetIndustry"

"tlp"

"uuid"

op: "in"

value: array of string

object { field, op, value } 

field: "killChain"

op: "equals" or "not" or "gt" or 3 more

One of the following:

"equals"

"not"

"gt"

"gte"

"lt"

"lte"

value: number or string

One of the following:

number

string

object { field, op, value } 

field: "killChain"

op: "in"

value: array of number or string

One of the following:

number

string

object { field, op, value } 

field: "hasChildren"

op: "equals" or "not" or "gt" or 3 more

One of the following:

"equals"

"not"

"gt"

"gte"

"lt"

"lte"

value: unknown or boolean

One of the following:

unknown

boolean

object { field, op, value } 

field: "hasChildren"

op: "in"

value: array of unknown or boolean

One of the following:

unknown

boolean

searchBranches: optional array of array of object { field, op, value }  or object { field, op, value }  or object { field, op, value }  or 3 more

JSON-encoded. OR branches of structured search filters. Filters within a branch are AND’d, branches are OR’d, and the result is AND’d with `search`: `AND(search) AND OR(AND(branch 1), ...)`. Max 8 branches of 1-10 conditions each. Not supported for analytics datasets, and `indicator` filters are not yet supported inside branches. Cursor pages carry the original branches, so do not resend them with `cursor`.

One of the following:

object { field, op, value } 

field: "attacker" or "attackerCountry" or "category" or 12 more

One of the following:

"attacker"

"attackerCountry"

"category"

"createdAt"

"date"

"event"

"indicator"

"indicatorType"

"mitreAttack"

"mitreCapec"

"tags"

"targetCountry"

"targetIndustry"

"tlp"

"uuid"

op: "equals" or "not" or "gt" or 8 more

One of the following:

"equals"

"not"

"gt"

"gte"

"lt"

"lte"

"like"

"contains"

"startsWith"

"endsWith"

"find"

value: string

maxLength512

minLength1

object { field, op, value } 

field: "attacker" or "attackerCountry" or "category" or 12 more

One of the following:

"attacker"

"attackerCountry"

"category"

"createdAt"

"date"

"event"

"indicator"

"indicatorType"

"mitreAttack"

"mitreCapec"

"tags"

"targetCountry"

"targetIndustry"

"tlp"

"uuid"

op: "in"

value: array of string

object { field, op, value } 

field: "killChain"

op: "equals" or "not" or "gt" or 3 more

One of the following:

"equals"

"not"

"gt"

"gte"

"lt"

"lte"

value: number or string

One of the following:

number

string

object { field, op, value } 

field: "killChain"

op: "in"

value: array of number or string

One of the following:

number

string

object { field, op, value } 

field: "hasChildren"

op: "equals" or "not" or "gt" or 3 more

One of the following:

"equals"

"not"

"gt"

"gte"

"lt"

"lte"

value: unknown or boolean

One of the following:

unknown

boolean

object { field, op, value } 

field: "hasChildren"

op: "in"

value: array of unknown or boolean

One of the following:

unknown

boolean

##### ReturnsExpand Collapse 

attacker: string

attackerCountry: string

attackerCountryAlpha3: string

category: string

datasetId: string

date: string

event: string

hasChildren: boolean

indicator: string

indicatorType: string

indicatorTypeId: number

killChain: number

mitreAttack: array of string

mitreCapec: array of string

numReferenced: number

numReferences: number

rawId: string

referenced: array of string

referencedIds: array of number

references: array of string

referencesIds: array of number

tags: array of string

targetCountry: string

targetCountryAlpha3: string

targetIndustry: string

tlp: string

uuid: string

insight: optional string

releasabilityId: optional string

### Filter and list events

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cloudforce-one/events \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    [
      {
        "attacker": "Flying Yeti",
        "attackerCountry": "CN",
        "attackerCountryAlpha3": "CHN",
        "category": "Domain Resolution",
        "datasetId": "dataset-example-id",
        "date": "2022-04-01T00:00:00Z",
        "event": "An attacker registered the domain domain.com",
        "hasChildren": true,
        "indicator": "domain.com",
        "indicatorType": "domain",
        "indicatorTypeId": 5,
        "killChain": 0,
        "mitreAttack": [
          " "
        ],
        "mitreCapec": [
          " "
        ],
        "numReferenced": 0,
        "numReferences": 0,
        "rawId": "453gw34w3",
        "referenced": [
          " "
        ],
        "referencedIds": [
          0
        ],
        "references": [
          " "
        ],
        "referencesIds": [
          0
        ],
        "tags": [
          "malware"
        ],
        "targetCountry": "US",
        "targetCountryAlpha3": "USA",
        "targetIndustry": "Agriculture",
        "tlp": "amber",
        "uuid": "12345678-1234-1234-1234-1234567890ab",
        "insight": "insight",
        "releasabilityId": "releasabilityId"
      }
    ]

##### Returns Examples

200 example
    
    
    [
      {
        "attacker": "Flying Yeti",
        "attackerCountry": "CN",
        "attackerCountryAlpha3": "CHN",
        "category": "Domain Resolution",
        "datasetId": "dataset-example-id",
        "date": "2022-04-01T00:00:00Z",
        "event": "An attacker registered the domain domain.com",
        "hasChildren": true,
        "indicator": "domain.com",
        "indicatorType": "domain",
        "indicatorTypeId": 5,
        "killChain": 0,
        "mitreAttack": [
          " "
        ],
        "mitreCapec": [
          " "
        ],
        "numReferenced": 0,
        "numReferences": 0,
        "rawId": "453gw34w3",
        "referenced": [
          " "
        ],
        "referencedIds": [
          0
        ],
        "references": [
          " "
        ],
        "referencesIds": [
          0
        ],
        "tags": [
          "malware"
        ],
        "targetCountry": "US",
        "targetCountryAlpha3": "USA",
        "targetIndustry": "Agriculture",
        "tlp": "amber",
        "uuid": "12345678-1234-1234-1234-1234567890ab",
        "insight": "insight",
        "releasabilityId": "releasabilityId"
      }
    ]
