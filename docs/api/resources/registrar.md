---
url: https://developers.cloudflare.com/api/resources/registrar/
title: Registrar | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:19:09.757389+00:00
---

# Registrar | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/registrar/

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Registrar

Registrar API for searching, checking, registering, and managing domains through Cloudflare Registrar.

## Prerequisites

Before using this API, ensure:

  1. **Cloudflare account** — the caller must have a valid Cloudflare account.
  2. **Billing profile** — the account must have a billing profile with a valid, current default payment method (credit card or other accepted method). This cannot be set up via API — the account owner must configure billing at `https://dash.cloudflare.com/{account_id}/billing/payment-info` before calling `POST /registrations`.
  3. **API authentication** — use an API token or API key with the appropriate Registrar permissions for the operations you are calling.



## Terminology: domain extension

Throughout this API, “extension” refers to the domain extension part of a fully qualified domain name — the portion after the registrable label. For example, in `example.co.uk`, the extension is `co.uk` (not just `uk`). This covers both top-level domains like `com` and multi-level extensions like `co.uk`. This is distinct from other uses of the word “extension” (e.g., EPP extensions).

## Supported extensions

This API supports programmatic registration for all extensions supported by the dashboard experience, with the following exceptions:

`giving`, `mom`, `inc`, `lol`, `sh`, `link`, `cc`, `new`

Cloudflare Registrar supports 400+ extensions in the dashboard. Extensions listed above can be registered at `https://dash.cloudflare.com/{account_id}/domains/registrations`.

## Typical workflow

  1. **Search** — call `GET /domain-search?q={keyword}` to discover available domains.
  2. **Check** — call `POST /domain-check` with candidate domains to verify real-time availability and pricing.
  3. **Review the response** — if `registrable: false`, inspect `reason` to understand whether the domain is unavailable, the extension is not supported by this API, the extension is not supported by Cloudflare Registrar at all, or the extension’s registry has frozen new registrations.
  4. **Handle premium domains** — if `tier: premium`, premium registration is not currently supported by this API. Surface the premium pricing to the user, but do not proceed to `POST /registrations` for that domain.
  5. **Observe the registration schema** — call `GET /extensions/:extension_name` to discover the required values for registering this extension.
  6. **Register** — call `POST /registrations` with the chosen domain name for supported non-premium registrations.
  7. **Confirm completion** — if the response is `201 Created`, registration completed within the default timeout and no polling is needed.
  8. **Poll when needed** — if the response is `202 Accepted`, poll `links.self` from the workflow response.
  9. **Stop for user action** — if `state: action_required`, stop polling and surface `context.action` to the user. The workflow will not resolve on its own.
  10. **Continue when blocked** — if `state: blocked`, continue polling and inform the user that a third party, such as the extension registry or losing registrar, is delaying progress.
  11. **Review failures before retrying** — if `state: failed`, review `error.code` and `error.message`, then decide whether user action or a new Check call is needed.



**All successful domain registrations are non-refundable.** Once the registration workflow completes with `state: succeeded`, the charge cannot be reversed. Confirm pricing and domain choice with the user before calling `POST /registrations`.

## Default behavior for mutating operations

By default, mutating operations such as create and update hold the connection for a bounded, server-defined amount of time while the operation completes. In most cases, the response contains a completed workflow status and no polling is required.

  * **Completed within the synchronous wait window:** Returns `201` (create) or `200` (update) with a `workflow_status` where `state: succeeded` and `completed: true`.
  * **Still processing after the synchronous wait window:** Returns `202 Accepted` with a `workflow_status` where `completed: false`. Use the `links.self` URL to poll for completion.



## Non-blocking mode

To receive an immediate `202 Accepted` response without waiting, send the `Prefer: respond-async` request header (RFC 7240). The server will acknowledge it with a `Preference-Applied: respond-async` response header.

## Polling

When the response is `202`, poll the workflow status endpoint indicated by `links.self` in the response body until the workflow reaches a terminal state or requires user action.

##### [Search for available domains](https://developers.cloudflare.com/api/resources/registrar/methods/search)

GET/accounts/{account_id}/registrar/domain-search

##### [Check domain availability](https://developers.cloudflare.com/api/resources/registrar/methods/check)

POST/accounts/{account_id}/registrar/domain-check

##### [Check domain transfer eligibility](https://developers.cloudflare.com/api/resources/registrar/methods/transfer_check)

POST/accounts/{account_id}/registrar/domain-transfer-check

##### ModelsExpand Collapse 

Registration object { auto_renew, created_at, domain_name, 4 more } 

A domain registration resource representing the current state of a registered domain.

auto_renew: boolean

Whether automatic renewal occurs before expiration.

created_at: string

When the domain was registered. Present when the registration resource exists.

formatdate-time

domain_name: string

Provides a fully qualified domain name (FQDN), including the extension (e.g., `example.com`, `mybrand.app`). The domain name uniquely identifies a registration. Cloudflare permits only one registration per domain, making the domain name a natural idempotency key for registration requests.

expires_at: string

When the domain registration expires. Ready registrations include this value; only `registration_pending` and `transfer_pending` may return null.

formatdate-time

locked: boolean

Whether the domain is locked for transfer.

privacy_mode: "off" or "redaction"

Current WHOIS privacy mode for the registration.

One of the following:

"off"

"redaction"

status: "active" or "registration_pending" or "transfer_pending" or 4 more

Current registration status.

  * `active`: The domain operates with an active registration.
  * `registration_pending`: Registration remains in progress.
  * `transfer_pending`: Domain transfer is in progress.
  * `expired`: The domain registration expired.
  * `suspended`: The registry suspended the domain.
  * `redemption_period`: The domain entered the redemption grace period.
  * `pending_delete`: The registry scheduled the domain for deletion.



One of the following:

"active"

"registration_pending"

"transfer_pending"

"expired"

"suspended"

"redemption_period"

"pending_delete"

WorkflowStatus object { completed, created_at, links, 4 more } 

Status of an async registration workflow.

completed: boolean

Indicates whether the workflow reached a terminal state. A `succeeded` or `failed` state returns `true`; `pending`, `in_progress`, `action_required`, and `blocked` return `false`.

created_at: string

formatdate-time

links: object { self, resource } 

self: string

URL to this status resource.

resource: optional string

URL to the domain resource.

state: "pending" or "in_progress" or "action_required" or 3 more

Describes the workflow lifecycle state.

  * `pending`: The workflow awaits processing.
  * `in_progress`: Processing started. Continue polling `links.self`. An internal deadline limits the duration of this state.
  * `action_required`: The workflow pauses for user action. See `context.action` for details. Stop automated polling until the user completes the required action.
  * `blocked`: A third party, such as the domain extension’s registry or a losing registrar, prevents progress. Continue polling because the block may resolve when the third party responds.
  * `succeeded`: Terminal state. The operation completed successfully. `completed` equals `true`. For registrations, `context.registration` contains the resulting registration resource.
  * `failed`: Terminal state. The operation failed. `completed` equals `true`. See `error.code` and `error.message` for the reason. Require user review before retrying.



One of the following:

"pending"

"in_progress"

"action_required"

"blocked"

"succeeded"

"failed"

updated_at: string

formatdate-time

context: optional map[unknown]

Provides workflow-specific data.

For domain-centric workflows, `context.domain_name` identifies the workflow subject.

error: optional object { code, message } 

Provides error details when a workflow reaches the `failed` state. The workflow type (registration, update, etc.) and underlying registry response determine the specific codes and messages. Workflow error codes differ from immediate HTTP error `errors[].code` values in non-2xx responses. Surface `error.message` to the user for context.

code: string

Machine-readable error code identifying the failure reason.

message: string

Human-readable explanation of the failure. May include registry-specific details.

RegistrarSearchResponse object { domains } 

Contains the search results.

domains: array of object { name, registrable, pricing, 2 more } 

Lists domain suggestions in relevance order. An empty array indicates that the search criteria matched zero domains.

name: string

The fully qualified domain name (FQDN) in punycode format for internationalized domain names (IDNs).

registrable: boolean

Indicates domain availability according to potentially stale, non-authoritative search data.

  * `true`: The domain appears available. Use POST /domain-check to confirm before registration.
  * `false`: Search results mark the domain ineligible for registration through this API. See `reason` for details.



pricing: optional object { currency, registration_cost, renewal_cost } 

Provides annual pricing information for a given domain. The API returns all per-year prices as strings to preserve decimal precision.

`renewal_cost` and `registration_cost` or `transfer_cost` are frequently the same value, but may differ due to premium rates for certain domains.

For a multi-year operations, the operation’s cost applies to the first year and `renewal_cost` applies to each subsequent year. The values reflect the current registry rate, which can change over time.

currency: string

ISO-4217 currency code for the prices (e.g., “USD”, “EUR”, “GBP”).

registration_cost: string

The first-year cost to register this domain.

renewal_cost: string

Per-year renewal cost for this domain. Applied to each year beyond the first year of a multi-year registration, and to each annual auto-renewal thereafter. May differ from `registration_cost`, especially for premium domains where initial registration often costs more than renewals.

reason: optional "extension_not_supported_via_api" or "extension_not_supported" or "extension_disallows_registration" or 2 more

Appears only when `registrable` is `false` and explains the advisory search result. Use POST /domain-check for authoritative status.

  * `extension_not_supported_via_api`: Cloudflare Registrar supports this extension in the dashboard but currently excludes it from programmatic registration through this API.
  * `extension_not_supported`: Cloudflare Registrar excludes this extension entirely.
  * `extension_disallows_registration`: The extension’s registry temporarily or permanently freezes new registrations.
  * `domain_premium`: The domain carries premium pricing. This API currently supports standard registrations only.
  * `domain_unavailable`: The domain appears unavailable.



One of the following:

"extension_not_supported_via_api"

"extension_not_supported"

"extension_disallows_registration"

"domain_premium"

"domain_unavailable"

tier: optional "standard" or "premium"

The pricing tier for this domain. A `registrable` value of `true` always includes this field, which defaults to `standard` for most domains. A `registrable` value of `false` may omit it.

  * `standard`: Standard registry pricing.
  * `premium`: Premium domain with higher pricing from the registry.



One of the following:

"standard"

"premium"

RegistrarCheckResponse object { domains } 

Contains the availability check results.

domains: array of object { name, registrable, pricing, 2 more } 

Array of domain availability results. Results for unsupported extensions contain `registrable: false` and a `reason` field. The response may omit malformed domain names.

name: string

The fully qualified domain name (FQDN) in punycode format for internationalized domain names (IDNs).

registrable: boolean

Indicates programmatic registration eligibility according to a real-time registry check.

  * `true`: The domain is available for registration. The response includes the `pricing` object.
  * `false`: A restriction prevents registration. See the `reason` field for details. Some results, such as premium domains, may still include `tier`.



pricing: optional object { currency, registration_cost, renewal_cost } 

Provides annual pricing information for a given domain. The API returns all per-year prices as strings to preserve decimal precision.

`renewal_cost` and `registration_cost` or `transfer_cost` are frequently the same value, but may differ due to premium rates for certain domains.

For a multi-year operations, the operation’s cost applies to the first year and `renewal_cost` applies to each subsequent year. The values reflect the current registry rate, which can change over time.

currency: string

ISO-4217 currency code for the prices (e.g., “USD”, “EUR”, “GBP”).

registration_cost: string

The first-year cost to register this domain.

renewal_cost: string

Per-year renewal cost for this domain. Applied to each year beyond the first year of a multi-year registration, and to each annual auto-renewal thereafter. May differ from `registration_cost`, especially for premium domains where initial registration often costs more than renewals.

reason: optional "extension_not_supported_via_api" or "extension_not_supported" or "extension_disallows_registration" or 2 more

Appears only when `registrable` is `false` and explains the result.

  * `extension_not_supported_via_api`: Cloudflare Registrar supports this extension in the dashboard but currently excludes it from programmatic registration through this API. The user can register via `https://dash.cloudflare.com/{account_id}/domains/registrations`.
  * `extension_not_supported`: Cloudflare Registrar excludes this extension entirely.
  * `extension_disallows_registration`: The extension’s registry temporarily or permanently freezes new registrations. Registrars currently cannot register domains on this extension.
  * `domain_premium`: The domain carries premium pricing. This API currently supports standard registrations only.
  * `domain_unavailable`: An existing registration, reservation, or other registry restriction makes the domain unavailable on a supported extension.



One of the following:

"extension_not_supported_via_api"

"extension_not_supported"

"extension_disallows_registration"

"domain_premium"

"domain_unavailable"

tier: optional "standard" or "premium"

The pricing tier for this domain. A `registrable` value of `true` always includes this field, which defaults to `standard` for most domains. A `registrable` value of `false` may omit it.

  * `standard`: Standard registry pricing.
  * `premium`: Premium domain with higher pricing from the registry.



One of the following:

"standard"

"premium"

RegistrarTransferCheckResponse object { domains } 

Contains the transfer eligibility results.

domains: map[object { pricing, transferable, name, reasons }  or object { transferable, name, pricing, reasons } ]

Maps domain names to transfer eligibility results. Each value contains `name`, `transferable`, and `reasons`.

One of the following:

TransferableResult object { pricing, transferable, name, reasons } 

pricing: object { currency, renewal_cost, transfer_cost } 

Provides annual pricing information for a given domain. The API returns all per-year prices as strings to preserve decimal precision.

`renewal_cost` and `registration_cost` or `transfer_cost` are frequently the same value, but may differ due to premium rates for certain domains.

For a multi-year operations, the operation’s cost applies to the first year and `renewal_cost` applies to each subsequent year. The values reflect the current registry rate, which can change over time.

currency: string

ISO-4217 currency code for the prices (e.g., “USD”, “EUR”, “GBP”).

renewal_cost: string

Per-year renewal cost for this domain. Applied to each year beyond the first year of a multi-year registration, and to each annual auto-renewal thereafter. May differ from `registration_cost`, especially for premium domains where initial registration often costs more than renewals.

transfer_cost: string

The first-year cost to transfer this domain.

transferable: true

name: optional string

The check evaluates this domain name.

reasons: optional array of object { code } 

code: "extension_not_supported_via_api" or "extension_not_supported" or "domain_premium" or 14 more

Transfer eligibility reason code.

  * `extension_not_supported_via_api`: This API excludes the extension; dashboard flows support it.
  * `extension_not_supported`: Cloudflare Registrar excludes the extension.
  * `domain_premium`: This API currently excludes premium transfers.
  * `extension_disallows_transfer`: Extension currently blocks transfer operations.
  * `domain_not_exists`: No registration record exists for the domain.
  * `domain_on_cloudflare`: Cloudflare already serves as the domain’s registrar.
  * `domain_locked`: Losing registrar reports transfer-prohibited lock status.
  * `registry_status`: Registry status currently blocks transfer (for example, pending transfer or deletion state).
  * `domain_outside_transfer_window`: Domain is within a transfer wait window (for example, recently registered).
  * `domain_max_term`: Completing transfer would exceed the registry maximum term.
  * `invalid_auth_code`: The provided auth code is incorrect.
  * `invalid_auth_code_format`: Auth code fails Base64 validation.
  * `dnssec_enabled`: DNSSEC is enabled. It must be disabled before transfer.
  * `zone_not_found`: The target account lacks a Cloudflare zone for the domain.
  * `zone_status_invalid`: The Cloudflare zone cannot transfer in its current state.
  * `invalid_zone_plan`: The zone plan fails transfer requirements.
  * `domain_unsupported`: This endpoint rejects the domain name format.



One of the following:

"extension_not_supported_via_api"

"extension_not_supported"

"domain_premium"

"extension_disallows_transfer"

"domain_not_exists"

"domain_on_cloudflare"

"domain_locked"

"registry_status"

"domain_outside_transfer_window"

"domain_max_term"

"invalid_auth_code"

"invalid_auth_code_format"

"dnssec_enabled"

"zone_not_found"

"zone_status_invalid"

"invalid_zone_plan"

"domain_unsupported"

NonTransferableResult object { transferable, name, pricing, reasons } 

transferable: false

name: optional string

The check evaluates this domain name.

pricing: optional object { currency, renewal_cost, transfer_cost } 

Provides annual pricing information for a given domain. The API returns all per-year prices as strings to preserve decimal precision.

`renewal_cost` and `registration_cost` or `transfer_cost` are frequently the same value, but may differ due to premium rates for certain domains.

For a multi-year operations, the operation’s cost applies to the first year and `renewal_cost` applies to each subsequent year. The values reflect the current registry rate, which can change over time.

currency: string

ISO-4217 currency code for the prices (e.g., “USD”, “EUR”, “GBP”).

renewal_cost: string

Per-year renewal cost for this domain. Applied to each year beyond the first year of a multi-year registration, and to each annual auto-renewal thereafter. May differ from `registration_cost`, especially for premium domains where initial registration often costs more than renewals.

transfer_cost: string

The first-year cost to transfer this domain.

reasons: optional array of object { code } 

code: "extension_not_supported_via_api" or "extension_not_supported" or "domain_premium" or 14 more

Transfer eligibility reason code.

  * `extension_not_supported_via_api`: This API excludes the extension; dashboard flows support it.
  * `extension_not_supported`: Cloudflare Registrar excludes the extension.
  * `domain_premium`: This API currently excludes premium transfers.
  * `extension_disallows_transfer`: Extension currently blocks transfer operations.
  * `domain_not_exists`: No registration record exists for the domain.
  * `domain_on_cloudflare`: Cloudflare already serves as the domain’s registrar.
  * `domain_locked`: Losing registrar reports transfer-prohibited lock status.
  * `registry_status`: Registry status currently blocks transfer (for example, pending transfer or deletion state).
  * `domain_outside_transfer_window`: Domain is within a transfer wait window (for example, recently registered).
  * `domain_max_term`: Completing transfer would exceed the registry maximum term.
  * `invalid_auth_code`: The provided auth code is incorrect.
  * `invalid_auth_code_format`: Auth code fails Base64 validation.
  * `dnssec_enabled`: DNSSEC is enabled. It must be disabled before transfer.
  * `zone_not_found`: The target account lacks a Cloudflare zone for the domain.
  * `zone_status_invalid`: The Cloudflare zone cannot transfer in its current state.
  * `invalid_zone_plan`: The zone plan fails transfer requirements.
  * `domain_unsupported`: This endpoint rejects the domain name format.



One of the following:

"extension_not_supported_via_api"

"extension_not_supported"

"domain_premium"

"extension_disallows_transfer"

"domain_not_exists"

"domain_on_cloudflare"

"domain_locked"

"registry_status"

"domain_outside_transfer_window"

"domain_max_term"

"invalid_auth_code"

"invalid_auth_code_format"

"dnssec_enabled"

"zone_not_found"

"zone_status_invalid"

"invalid_zone_plan"

"domain_unsupported"

#### RegistrarRegistrations

##### [Create Registration](https://developers.cloudflare.com/api/resources/registrar/subresources/registrations/methods/create)

POST/accounts/{account_id}/registrar/registrations

##### [List Registrations](https://developers.cloudflare.com/api/resources/registrar/subresources/registrations/methods/list)

GET/accounts/{account_id}/registrar/registrations

##### [Get Registration](https://developers.cloudflare.com/api/resources/registrar/subresources/registrations/methods/get)

GET/accounts/{account_id}/registrar/registrations/{domain_name}

##### [Update Registration](https://developers.cloudflare.com/api/resources/registrar/subresources/registrations/methods/edit)

PATCH/accounts/{account_id}/registrar/registrations/{domain_name}

#### RegistrarRegistration Status

##### [Get Registration Status](https://developers.cloudflare.com/api/resources/registrar/subresources/registration_status/methods/get)

GET/accounts/{account_id}/registrar/registrations/{domain_name}/registration-status

#### RegistrarUpdate Status

##### [Get Update Status](https://developers.cloudflare.com/api/resources/registrar/subresources/update_status/methods/get)

GET/accounts/{account_id}/registrar/registrations/{domain_name}/update-status

#### RegistrarExtensions

##### [List extensions](https://developers.cloudflare.com/api/resources/registrar/subresources/extensions/methods/list)

GET/accounts/{account_id}/registrar/extensions

##### [Get extension](https://developers.cloudflare.com/api/resources/registrar/subresources/extensions/methods/get)

GET/accounts/{account_id}/registrar/extensions/{extension}

##### ModelsExpand Collapse 

ExtensionListResponse object { metadata, registration_schema, transfer_schema } 

Extension entry with metadata and JSON Schema documents for registration and transfer operations.

metadata: object { name, tld } 

Extension metadata.

name: string

The full name of the extension. For example, “co.uk”, or “uk”.

tld: string

The TLD of the extension. For example, for “co.uk”, it is “uk”. For “uk”, it is “uk”.

registration_schema: unknown

JSON Schema describing the expected input structure for registration operations on this extension.

transfer_schema: unknown

JSON Schema describing the expected input structure for transfer operations on this extension.

ExtensionGetResponse object { metadata, registration_schema, transfer_schema } 

Extension entry with metadata and JSON Schema documents for registration and transfer operations.

metadata: object { name, tld } 

Extension metadata.

name: string

The full name of the extension. For example, “co.uk”, or “uk”.

tld: string

The TLD of the extension. For example, for “co.uk”, it is “uk”. For “uk”, it is “uk”.

registration_schema: unknown

JSON Schema describing the expected input structure for registration operations on this extension.

transfer_schema: unknown

JSON Schema describing the expected input structure for transfer operations on this extension.

#### RegistrarTransfer In

##### [Initiate Transfer](https://developers.cloudflare.com/api/resources/registrar/subresources/transfer_in/methods/create)

POST/accounts/{account_id}/registrar/registrations/{domain_name}/transfer-in

#### RegistrarTransfer In Status

##### [Get Transfer Status](https://developers.cloudflare.com/api/resources/registrar/subresources/transfer_in_status/methods/get)

GET/accounts/{account_id}/registrar/registrations/{domain_name}/transfer-in-status

[ Previous

* * *

Tenant Custom Nameservers ](https://developers.cloudflare.com/api/resources/tenant_custom_nameservers)[ Next

* * *

Registrations ](https://developers.cloudflare.com/api/resources/registrar/subresources/registrations)
