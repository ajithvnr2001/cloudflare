---
url: https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/
title: Suppressions | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:28:07.356771+00:00
---

# Suppressions | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/

[API Reference](https://developers.cloudflare.com/api)

[Email Sending](https://developers.cloudflare.com/api/resources/email_sending)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Suppressions

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

[ Previous

* * *

Email Sending ](https://developers.cloudflare.com/api/resources/email_sending)[ Next

* * *

Subdomains ](https://developers.cloudflare.com/api/resources/email_sending/subresources/subdomains)
