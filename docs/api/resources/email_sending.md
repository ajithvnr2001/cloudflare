---
url: https://developers.cloudflare.com/api/resources/email_sending/
title: Email Sending | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:39.723245+00:00
---

# Email Sending | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/email_sending/

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Email Sending

##### [Send an email](https://developers.cloudflare.com/api/resources/email_sending/methods/send)

POST/accounts/{account_id}/email/sending/send

##### [Send a raw MIME email](https://developers.cloudflare.com/api/resources/email_sending/methods/send_raw)

POST/accounts/{account_id}/email/sending/send_raw

##### ModelsExpand Collapse 

EmailSendingSendResponse object { delivered, message_id, permanent_bounces, 2 more } 

delivered: array of string

Email addresses to which the message was delivered immediately.

message_id: string

Message ID of the sent email.

permanent_bounces: array of string

Email addresses that permanently bounced.

queued: array of string

Email addresses for which delivery was queued for later.

suppressed_recipients: array of string

Email addresses dropped because they are on the suppression list. Returned when suppressed-recipient dropping is enabled for the sending subdomain; otherwise the request fails instead.

EmailSendingSendRawResponse object { delivered, message_id, permanent_bounces, 2 more } 

delivered: array of string

Email addresses to which the message was delivered immediately.

message_id: string

Message ID of the sent email.

permanent_bounces: array of string

Email addresses that permanently bounced.

queued: array of string

Email addresses for which delivery was queued for later.

suppressed_recipients: array of string

Email addresses dropped because they are on the suppression list. Returned when suppressed-recipient dropping is enabled for the sending subdomain; otherwise the request fails instead.

#### Email SendingSuppressions

##### [List account Email Sending suppressions](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/list)

GET/accounts/{account_id}/email/sending/suppressions

##### [Get account Email Sending suppression](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/get)

GET/accounts/{account_id}/email/sending/suppressions/{suppression_id}

##### [Create account Email Sending suppression](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/create)

POST/accounts/{account_id}/email/sending/suppressions

##### [Update account Email Sending suppression](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/edit)

PATCH/accounts/{account_id}/email/sending/suppressions/{suppression_id}

##### [Delete account Email Sending suppression](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/delete)

DELETE/accounts/{account_id}/email/sending/suppressions/{suppression_id}

##### [Bulk import account Email Sending suppressions](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/import)

POST/accounts/{account_id}/email/sending/suppressions/bulk

##### ModelsExpand Collapse 

SuppressionListResponse object { id, created_at, email, 5 more } 

id: string

Unique identifier for this suppression.

formatuuid

created_at: string

When the suppression was created.

formatdate-time

email: string

The suppressed email address.

formatemail

expires_at: string

When the suppression expires. Null for a permanent suppression.

formatdate-time

read_only: boolean

Whether clients may mutate this suppression. This is determined by the server and must not be inferred from `reason`.

reason: string

Why the address is suppressed: `manual`, `complaint`, `hard_bounce`, `soft_bounce`, or `policy`.

note: optional string

Advisory note for this suppression, if any.

scope: optional object { type }  or object { type, value } 

Where the suppression applies: `account` for every sending domain of the account, or `sending_domain` for one envelope MAIL FROM domain.

One of the following:

Type object { type } 

type: "account"

Blocks the recipient for every sending domain of the account.

object { type, value } 

type: "sending_domain"

Blocks the recipient only for mail whose envelope MAIL FROM uses `value`.

value: string

The sending domain: the domain part of the envelope MAIL FROM, lowercase, without a trailing dot.

maxLength1024

SuppressionGetResponse object { id, created_at, email, 5 more } 

id: string

Unique identifier for this suppression.

formatuuid

created_at: string

When the suppression was created.

formatdate-time

email: string

The suppressed email address.

formatemail

expires_at: string

When the suppression expires. Null for a permanent suppression.

formatdate-time

read_only: boolean

Whether clients may mutate this suppression. This is determined by the server and must not be inferred from `reason`.

reason: string

Why the address is suppressed: `manual`, `complaint`, `hard_bounce`, `soft_bounce`, or `policy`.

note: optional string

Advisory note for this suppression, if any.

scope: optional object { type }  or object { type, value } 

Where the suppression applies: `account` for every sending domain of the account, or `sending_domain` for one envelope MAIL FROM domain.

One of the following:

Type object { type } 

type: "account"

Blocks the recipient for every sending domain of the account.

object { type, value } 

type: "sending_domain"

Blocks the recipient only for mail whose envelope MAIL FROM uses `value`.

value: string

The sending domain: the domain part of the envelope MAIL FROM, lowercase, without a trailing dot.

maxLength1024

SuppressionCreateResponse object { id, scope } 

id: string

The suppression’s identifier.

formatuuid

scope: optional object { type }  or object { type, value } 

Where the suppression applies: `account` for every sending domain of the account, or `sending_domain` for one envelope MAIL FROM domain.

One of the following:

Type object { type } 

type: "account"

Blocks the recipient for every sending domain of the account.

object { type, value } 

type: "sending_domain"

Blocks the recipient only for mail whose envelope MAIL FROM uses `value`.

value: string

The sending domain: the domain part of the envelope MAIL FROM, lowercase, without a trailing dot.

maxLength1024

SuppressionEditResponse object { id, created_at, email, 5 more } 

id: string

Unique identifier for this suppression.

formatuuid

created_at: string

When the suppression was created.

formatdate-time

email: string

The suppressed email address.

formatemail

expires_at: string

When the suppression expires. Null for a permanent suppression.

formatdate-time

read_only: boolean

Whether clients may mutate this suppression. This is determined by the server and must not be inferred from `reason`.

reason: string

Why the address is suppressed: `manual`, `complaint`, `hard_bounce`, `soft_bounce`, or `policy`.

note: optional string

Advisory note for this suppression, if any.

scope: optional object { type }  or object { type, value } 

Where the suppression applies: `account` for every sending domain of the account, or `sending_domain` for one envelope MAIL FROM domain.

One of the following:

Type object { type } 

type: "account"

Blocks the recipient for every sending domain of the account.

object { type, value } 

type: "sending_domain"

Blocks the recipient only for mail whose envelope MAIL FROM uses `value`.

value: string

The sending domain: the domain part of the envelope MAIL FROM, lowercase, without a trailing dot.

maxLength1024

SuppressionDeleteResponse object { id, scope } 

id: string

The suppression’s identifier.

formatuuid

scope: optional object { type }  or object { type, value } 

Where the suppression applies: `account` for every sending domain of the account, or `sending_domain` for one envelope MAIL FROM domain.

One of the following:

Type object { type } 

type: "account"

Blocks the recipient for every sending domain of the account.

object { type, value } 

type: "sending_domain"

Blocks the recipient only for mail whose envelope MAIL FROM uses `value`.

value: string

The sending domain: the domain part of the envelope MAIL FROM, lowercase, without a trailing dot.

maxLength1024

SuppressionImportResponse object { deduplicated, errors, invalid, 4 more } 

deduplicated: number

Number of items dropped because their email address and scope repeated an earlier item in this request. Counted once and excluded from `items`.

errors: number

Number of items that failed to import due to an unexpected error.

invalid: number

Number of items with an invalid email address or sending domain.

items: array of object { index, status, id, 3 more } 

Per-item results, in the same order as the request body.

index: number

Zero-based index of this item in the request body.

status: "processed" or "invalid" or "error" or "skipped"

Outcome for this item.

One of the following:

"processed"

"invalid"

"error"

"skipped"

id: optional string

The created or promoted suppression’s identifier. Present when `status` is `processed`.

formatuuid

email: optional string

The submitted email address for this item.

formatemail

error: optional string

Human-readable error message. Present when `status` is `invalid`, `error`, or `skipped`.

scope: optional object { type }  or object { type, value } 

Where the suppression applies: `account` for every sending domain of the account, or `sending_domain` for one envelope MAIL FROM domain.

One of the following:

Type object { type } 

type: "account"

Blocks the recipient for every sending domain of the account.

object { type, value } 

type: "sending_domain"

Blocks the recipient only for mail whose envelope MAIL FROM uses `value`.

value: string

The sending domain: the domain part of the envelope MAIL FROM, lowercase, without a trailing dot.

maxLength1024

processed: number

Number of items successfully created or promoted.

skipped: number

Number of items skipped because the existing suppression is not customer-managed (for example, a read-only policy suppression).

total: number

Total number of items in the request body, including duplicates.

#### Email SendingSubdomains

##### [List sending subdomains](https://developers.cloudflare.com/api/resources/email_sending/subresources/subdomains/methods/list)

GET/zones/{zone_id}/email/sending/subdomains

##### [Get a sending subdomain](https://developers.cloudflare.com/api/resources/email_sending/subresources/subdomains/methods/get)

GET/zones/{zone_id}/email/sending/subdomains/{subdomain_id}

##### [Create a sending subdomain](https://developers.cloudflare.com/api/resources/email_sending/subresources/subdomains/methods/create)

POST/zones/{zone_id}/email/sending/subdomains

##### [Update a sending subdomain](https://developers.cloudflare.com/api/resources/email_sending/subresources/subdomains/methods/edit)

PATCH/zones/{zone_id}/email/sending/subdomains/{subdomain_id}

##### [Delete a sending subdomain](https://developers.cloudflare.com/api/resources/email_sending/subresources/subdomains/methods/delete)

DELETE/zones/{zone_id}/email/sending/subdomains/{subdomain_id}

##### ModelsExpand Collapse 

SubdomainListResponse object { enabled, name, tag, 6 more } 

enabled: boolean

Whether Email Sending is enabled on this subdomain.

name: string

The exact domain name or a leftmost wildcard such as `*.example.com`.

tag: string

Sending subdomain identifier.

maxLength32

created: optional string

The date and time the destination address has been created.

formatdate-time

dkim_selector: optional string

The DKIM selector used for email signing. Wildcard rows publish the selector and sign with `d=<base>`.

drop_suppressed_recipients: optional boolean

Whether a send request that includes a recipient suppressed on this subdomain drops that recipient and still delivers to the rest, instead of failing the entire request.

modified: optional string

The date and time the destination address was last modified.

formatdate-time

preview_enabled: optional boolean

Whether sent messages from this subdomain can be previewed in the activity log.

return_path_domain: optional string

The return-path domain used for bounce handling. Wildcard rows use `cf-bounce.<base>`.

SubdomainGetResponse object { enabled, name, tag, 6 more } 

enabled: boolean

Whether Email Sending is enabled on this subdomain.

name: string

The exact domain name or a leftmost wildcard such as `*.example.com`.

tag: string

Sending subdomain identifier.

maxLength32

created: optional string

The date and time the destination address has been created.

formatdate-time

dkim_selector: optional string

The DKIM selector used for email signing. Wildcard rows publish the selector and sign with `d=<base>`.

drop_suppressed_recipients: optional boolean

Whether a send request that includes a recipient suppressed on this subdomain drops that recipient and still delivers to the rest, instead of failing the entire request.

modified: optional string

The date and time the destination address was last modified.

formatdate-time

preview_enabled: optional boolean

Whether sent messages from this subdomain can be previewed in the activity log.

return_path_domain: optional string

The return-path domain used for bounce handling. Wildcard rows use `cf-bounce.<base>`.

SubdomainCreateResponse object { enabled, name, tag, 6 more } 

enabled: boolean

Whether Email Sending is enabled on this subdomain.

name: string

The exact domain name or a leftmost wildcard such as `*.example.com`.

tag: string

Sending subdomain identifier.

maxLength32

created: optional string

The date and time the destination address has been created.

formatdate-time

dkim_selector: optional string

The DKIM selector used for email signing. Wildcard rows publish the selector and sign with `d=<base>`.

drop_suppressed_recipients: optional boolean

Whether a send request that includes a recipient suppressed on this subdomain drops that recipient and still delivers to the rest, instead of failing the entire request.

modified: optional string

The date and time the destination address was last modified.

formatdate-time

preview_enabled: optional boolean

Whether sent messages from this subdomain can be previewed in the activity log.

return_path_domain: optional string

The return-path domain used for bounce handling. Wildcard rows use `cf-bounce.<base>`.

SubdomainEditResponse object { enabled, name, tag, 6 more } 

enabled: boolean

Whether Email Sending is enabled on this subdomain.

name: string

The exact domain name or a leftmost wildcard such as `*.example.com`.

tag: string

Sending subdomain identifier.

maxLength32

created: optional string

The date and time the destination address has been created.

formatdate-time

dkim_selector: optional string

The DKIM selector used for email signing. Wildcard rows publish the selector and sign with `d=<base>`.

drop_suppressed_recipients: optional boolean

Whether a send request that includes a recipient suppressed on this subdomain drops that recipient and still delivers to the rest, instead of failing the entire request.

modified: optional string

The date and time the destination address was last modified.

formatdate-time

preview_enabled: optional boolean

Whether sent messages from this subdomain can be previewed in the activity log.

return_path_domain: optional string

The return-path domain used for bounce handling. Wildcard rows use `cf-bounce.<base>`.

SubdomainDeleteResponse object { errors, messages, success } 

errors: array of object { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

messages: array of object { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

success: true

Whether the API call was successful.

#### Email SendingSubdomainsDNS

##### [Get sending subdomain DNS records](https://developers.cloudflare.com/api/resources/email_sending/subresources/subdomains/subresources/dns/methods/get)

GET/zones/{zone_id}/email/sending/subdomains/{subdomain_id}/dns

[ Previous

* * *

Addresses ](https://developers.cloudflare.com/api/resources/email_routing/subresources/addresses)[ Next

* * *

Suppressions ](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions)
