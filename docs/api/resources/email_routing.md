---
url: https://developers.cloudflare.com/api/resources/email_routing/
title: Email Routing | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:38.753463+00:00
---

# Email Routing | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/email_routing/

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Email Routing

##### [Get Email Routing settings](https://developers.cloudflare.com/api/resources/email_routing/methods/get)

GET/zones/{zone_id}/email/routing

##### [Update Email Routing settings](https://developers.cloudflare.com/api/resources/email_routing/methods/edit)

PATCH/zones/{zone_id}/email/routing

##### [Apply Email Routing settings](https://developers.cloudflare.com/api/resources/email_routing/methods/update)

PUT/zones/{zone_id}/email/routing

##### [Disable Email Routing](https://developers.cloudflare.com/api/resources/email_routing/methods/disable)

Deprecated

POST/zones/{zone_id}/email/routing/disable

##### [Enable Email Routing](https://developers.cloudflare.com/api/resources/email_routing/methods/enable)

Deprecated

POST/zones/{zone_id}/email/routing/enable

##### [Unlock Email Routing](https://developers.cloudflare.com/api/resources/email_routing/methods/unlock)

Deprecated

POST/zones/{zone_id}/email/routing/unlock

##### ModelsExpand Collapse 

Settings object { id, enabled, name, 6 more } 

id: string

Email Routing settings identifier.

maxLength32

enabled: true or false

State of the zone settings for Email Routing.

One of the following:

true

false

name: string

Domain of your zone.

created: optional string

The date and time the settings have been created.

formatdate-time

modified: optional string

The date and time the settings have been modified.

formatdate-time

skip_wizard: optional true or false

Flag to check if the user skipped the configuration wizard.

One of the following:

true

false

status: optional "ready" or "unconfigured" or "misconfigured" or 2 more

Show the state of your account, and the type or configuration error.

One of the following:

"ready"

"unconfigured"

"misconfigured"

"misconfigured/locked"

"unlocked"

support_subaddress: optional true or false

Whether subaddressing (plus-addressing) is honored when matching incoming mail against routing rules.

One of the following:

true

false

Deprecatedtag: optional string

Email Routing settings tag. (Deprecated, replaced by Email Routing settings identifier)

maxLength32

#### Email RoutingDNS

##### [Email Routing - DNS settings](https://developers.cloudflare.com/api/resources/email_routing/subresources/dns/methods/get)

GET/zones/{zone_id}/email/routing/dns

##### [Enable Email Routing](https://developers.cloudflare.com/api/resources/email_routing/subresources/dns/methods/create)

POST/zones/{zone_id}/email/routing/dns

##### [Unlock Email Routing DNS records](https://developers.cloudflare.com/api/resources/email_routing/subresources/dns/methods/edit)

PATCH/zones/{zone_id}/email/routing/dns

##### [Disable Email Routing](https://developers.cloudflare.com/api/resources/email_routing/subresources/dns/methods/delete)

DELETE/zones/{zone_id}/email/routing/dns

##### ModelsExpand Collapse 

DNSRecord object { content, name, priority, 2 more } 

List of records needed to enable an Email Routing zone.

content: optional string

DNS record content.

name: optional string

DNS record name (or @ for the zone apex).

maxLength255

priority: optional number

Required for MX, SRV and URI records. Unused by other record types. Records with lower priorities are preferred.

maximum65535

minimum0

ttl: optional number or 1

Time to live, in seconds, of the DNS record. Must be between 60 and 86400, or 1 for ‘automatic’.

One of the following:

number

1

Time to live, in seconds, of the DNS record. Must be between 60 and 86400, or 1 for ‘automatic’.

type: optional "A" or "AAAA" or "CNAME" or 15 more

DNS record type.

One of the following:

"A"

"AAAA"

"CNAME"

"HTTPS"

"TXT"

"SRV"

"LOC"

"MX"

"NS"

"CERT"

"DNSKEY"

"DS"

"NAPTR"

"SMIMEA"

"SSHFP"

"SVCB"

"TLSA"

"URI"

DNSGetResponse = array of [DNSRecord](https://developers.cloudflare.com/api/resources/email_routing#\(resource\)%20email_routing.dns%20%3E%20\(model\)%20dns_record%20%3E%20\(schema\)) { content, name, priority, 2 more } 

content: optional string

DNS record content.

name: optional string

DNS record name (or @ for the zone apex).

maxLength255

priority: optional number

Required for MX, SRV and URI records. Unused by other record types. Records with lower priorities are preferred.

maximum65535

minimum0

ttl: optional number or 1

Time to live, in seconds, of the DNS record. Must be between 60 and 86400, or 1 for ‘automatic’.

One of the following:

number

1

Time to live, in seconds, of the DNS record. Must be between 60 and 86400, or 1 for ‘automatic’.

type: optional "A" or "AAAA" or "CNAME" or 15 more

DNS record type.

One of the following:

"A"

"AAAA"

"CNAME"

"HTTPS"

"TXT"

"SRV"

"LOC"

"MX"

"NS"

"CERT"

"DNSKEY"

"DS"

"NAPTR"

"SMIMEA"

"SSHFP"

"SVCB"

"TLSA"

"URI"

#### Email RoutingRules

##### [List account or zone routing rules](https://developers.cloudflare.com/api/resources/email_routing/subresources/rules/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/email/routing/rules

##### [Get routing rule](https://developers.cloudflare.com/api/resources/email_routing/subresources/rules/methods/get)

GET/zones/{zone_id}/email/routing/rules/{rule_identifier}

##### [Create routing rule](https://developers.cloudflare.com/api/resources/email_routing/subresources/rules/methods/create)

POST/zones/{zone_id}/email/routing/rules

##### [Update routing rule](https://developers.cloudflare.com/api/resources/email_routing/subresources/rules/methods/update)

PUT/zones/{zone_id}/email/routing/rules/{rule_identifier}

##### [Delete routing rule](https://developers.cloudflare.com/api/resources/email_routing/subresources/rules/methods/delete)

DELETE/zones/{zone_id}/email/routing/rules/{rule_identifier}

##### ModelsExpand Collapse 

Action object { type, value } 

Actions pattern.

type: "drop" or "forward" or "worker"

Type of supported action.

One of the following:

"drop"

"forward"

"worker"

value: optional array of string

List of values for the action. Currently limited to a single value.

EmailRoutingRule object { id, actions, enabled, 5 more } 

id: optional string

Routing rule identifier.

maxLength32

actions: optional array of [Action](https://developers.cloudflare.com/api/resources/email_routing#\(resource\)%20email_routing.rules%20%3E%20\(model\)%20action%20%3E%20\(schema\)) { type, value } 

List actions patterns.

type: "drop" or "forward" or "worker"

Type of supported action.

One of the following:

"drop"

"forward"

"worker"

value: optional array of string

List of values for the action. Currently limited to a single value.

enabled: optional true or false

Routing rule status.

One of the following:

true

false

matchers: optional array of [Matcher](https://developers.cloudflare.com/api/resources/email_routing#\(resource\)%20email_routing.rules%20%3E%20\(model\)%20matcher%20%3E%20\(schema\)) { type, field, value } 

Matching patterns to forward to your actions.

type: "all" or "literal"

Type of matcher.

One of the following:

"all"

"literal"

field: optional "to"

Field for type matcher.

value: optional string

Value for matcher.

maxLength90

name: optional string

Routing rule name.

maxLength256

priority: optional number

Priority of the routing rule.

minimum0

source: optional "api" or "wrangler"

Who manages the rule. `api` covers dashboard, generic API, and Terraform; `wrangler` means the rule is managed by a Worker’s wrangler.jsonc. Defaults to `api` when omitted on write.

One of the following:

"api"

"wrangler"

Deprecatedtag: optional string

Routing rule tag. (Deprecated, replaced by routing rule identifier)

maxLength32

Matcher object { type, field, value } 

Matching pattern to forward your actions.

type: "all" or "literal"

Type of matcher.

One of the following:

"all"

"literal"

field: optional "to"

Field for type matcher.

value: optional string

Value for matcher.

maxLength90

#### Email RoutingRulesCatch Alls

##### [Get catch-all rule](https://developers.cloudflare.com/api/resources/email_routing/subresources/rules/subresources/catch_alls/methods/get)

GET/zones/{zone_id}/email/routing/rules/catch_all

##### [Update catch-all rule](https://developers.cloudflare.com/api/resources/email_routing/subresources/rules/subresources/catch_alls/methods/update)

PUT/zones/{zone_id}/email/routing/rules/catch_all

##### ModelsExpand Collapse 

CatchAllAction object { type, value } 

Action for the catch-all routing rule.

type: "drop" or "forward" or "worker"

Type of action for catch-all rule.

One of the following:

"drop"

"forward"

"worker"

value: optional array of string

List of values for the action. Currently limited to a single value.

CatchAllMatcher object { type } 

Matcher for catch-all routing rule.

type: "all"

Type of matcher. Default is ‘all’.

CatchAllGetResponse object { id, actions, enabled, 4 more } 

id: optional string

Routing rule identifier.

maxLength32

actions: optional array of [CatchAllAction](https://developers.cloudflare.com/api/resources/email_routing#\(resource\)%20email_routing.rules.catch_alls%20%3E%20\(model\)%20catch_all_action%20%3E%20\(schema\)) { type, value } 

List actions for the catch-all routing rule.

type: "drop" or "forward" or "worker"

Type of action for catch-all rule.

One of the following:

"drop"

"forward"

"worker"

value: optional array of string

List of values for the action. Currently limited to a single value.

enabled: optional true or false

Routing rule status.

One of the following:

true

false

matchers: optional array of [CatchAllMatcher](https://developers.cloudflare.com/api/resources/email_routing#\(resource\)%20email_routing.rules.catch_alls%20%3E%20\(model\)%20catch_all_matcher%20%3E%20\(schema\)) { type } 

List of matchers for the catch-all routing rule.

type: "all"

Type of matcher. Default is ‘all’.

name: optional string

Routing rule name.

maxLength256

source: optional "api" or "wrangler"

Who manages the rule. `api` covers dashboard, generic API, and Terraform; `wrangler` means the rule is managed by a Worker’s wrangler.jsonc. Defaults to `api` when omitted on write.

One of the following:

"api"

"wrangler"

Deprecatedtag: optional string

Routing rule tag. (Deprecated, replaced by routing rule identifier)

maxLength32

CatchAllUpdateResponse object { id, actions, enabled, 4 more } 

id: optional string

Routing rule identifier.

maxLength32

actions: optional array of [CatchAllAction](https://developers.cloudflare.com/api/resources/email_routing#\(resource\)%20email_routing.rules.catch_alls%20%3E%20\(model\)%20catch_all_action%20%3E%20\(schema\)) { type, value } 

List actions for the catch-all routing rule.

type: "drop" or "forward" or "worker"

Type of action for catch-all rule.

One of the following:

"drop"

"forward"

"worker"

value: optional array of string

List of values for the action. Currently limited to a single value.

enabled: optional true or false

Routing rule status.

One of the following:

true

false

matchers: optional array of [CatchAllMatcher](https://developers.cloudflare.com/api/resources/email_routing#\(resource\)%20email_routing.rules.catch_alls%20%3E%20\(model\)%20catch_all_matcher%20%3E%20\(schema\)) { type } 

List of matchers for the catch-all routing rule.

type: "all"

Type of matcher. Default is ‘all’.

name: optional string

Routing rule name.

maxLength256

source: optional "api" or "wrangler"

Who manages the rule. `api` covers dashboard, generic API, and Terraform; `wrangler` means the rule is managed by a Worker’s wrangler.jsonc. Defaults to `api` when omitted on write.

One of the following:

"api"

"wrangler"

Deprecatedtag: optional string

Routing rule tag. (Deprecated, replaced by routing rule identifier)

maxLength32

#### Email RoutingAccount Rules

##### [List account or zone routing rules](https://developers.cloudflare.com/api/resources/email_routing/subresources/account_rules/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/email/routing/rules

##### ModelsExpand Collapse 

AccountRule object { id, actions, enabled, 6 more } 

id: optional string

Routing rule identifier.

maxLength32

actions: optional array of [Action](https://developers.cloudflare.com/api/resources/email_routing#\(resource\)%20email_routing.rules%20%3E%20\(model\)%20action%20%3E%20\(schema\)) { type, value } 

List actions patterns.

type: "drop" or "forward" or "worker"

Type of supported action.

One of the following:

"drop"

"forward"

"worker"

value: optional array of string

List of values for the action. Currently limited to a single value.

enabled: optional true or false

Routing rule status.

One of the following:

true

false

matchers: optional array of [Matcher](https://developers.cloudflare.com/api/resources/email_routing#\(resource\)%20email_routing.rules%20%3E%20\(model\)%20matcher%20%3E%20\(schema\)) { type, field, value } 

Matching patterns to forward to your actions.

type: "all" or "literal"

Type of matcher.

One of the following:

"all"

"literal"

field: optional "to"

Field for type matcher.

value: optional string

Value for matcher.

maxLength90

name: optional string

Routing rule name.

maxLength256

priority: optional number

Priority of the routing rule.

minimum0

source: optional "api" or "wrangler"

Who manages the rule. `api` covers dashboard, generic API, and Terraform; `wrangler` means the rule is managed by a Worker’s wrangler.jsonc. Defaults to `api` when omitted on write.

One of the following:

"api"

"wrangler"

Deprecatedtag: optional string

Routing rule tag. (Deprecated, replaced by routing rule identifier)

maxLength32

zone: optional object { name, tag } 

Zone information for the routing rule.

name: optional string

Zone name.

tag: optional string

Zone tag.

maxLength32

#### Email RoutingAddresses

##### [List destination addresses](https://developers.cloudflare.com/api/resources/email_routing/subresources/addresses/methods/list)

GET/accounts/{account_id}/email/routing/addresses

##### [Get a destination address](https://developers.cloudflare.com/api/resources/email_routing/subresources/addresses/methods/get)

GET/accounts/{account_id}/email/routing/addresses/{destination_address_identifier}

##### [Create a destination address](https://developers.cloudflare.com/api/resources/email_routing/subresources/addresses/methods/create)

POST/accounts/{account_id}/email/routing/addresses

##### [Update destination address](https://developers.cloudflare.com/api/resources/email_routing/subresources/addresses/methods/edit)

PATCH/accounts/{account_id}/email/routing/addresses/{destination_address_identifier}

##### [Delete destination address](https://developers.cloudflare.com/api/resources/email_routing/subresources/addresses/methods/delete)

DELETE/accounts/{account_id}/email/routing/addresses/{destination_address_identifier}

##### ModelsExpand Collapse 

Address object { id, created, email, 3 more } 

id: optional string

Destination address identifier.

maxLength32

created: optional string

The date and time the destination address has been created.

formatdate-time

email: optional string

The contact email address of the user.

maxLength90

modified: optional string

The date and time the destination address was last modified.

formatdate-time

Deprecatedtag: optional string

Destination address tag. (Deprecated, replaced by destination address identifier)

maxLength32

verified: optional string

The date and time the destination address has been verified. Null means not verified yet.

formatdate-time

[ Previous

* * *

Objects ](https://developers.cloudflare.com/api/resources/durable_objects/subresources/namespaces/subresources/objects)[ Next

* * *

DNS ](https://developers.cloudflare.com/api/resources/email_routing/subresources/dns)
