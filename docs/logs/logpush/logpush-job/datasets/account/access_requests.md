---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/access_requests/
title: Access requests \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:11.354159+00:00
---

# Access requests · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/access_requests/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /Access requests



# Access requests

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/access_requests/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewActionAllowedAppDomainAppUUIDConnectionCountryCreatedAtEmailIPAddressPurposeJustificationPromptPurposeJustificationResponseRayIDTemporaryAccessApproversTemporaryAccessDurationUserUID

The descriptions below detail the fields available for `access_requests`.

## Action

Type: `string`

What type of record is this. _login_ | _logout_.

## Allowed

Type: `bool`

If request was allowed or denied.

## AppDomain

Type: `string`

The domain of the Application that Access is protecting.

## AppUUID

Type: `string`

Access Application UUID.

## Connection

Type: `string`

Identity provider used for the login.

## Country

Type: `string`

Request's country of origin.

## CreatedAt

Type: `int or string`

The date and time the corresponding access request was made (for example, '2021-07-27T00:01:07Z').

## Email

Type: `string`

Email of the user who logged in.

## IPAddress

Type: `string`

The IP address of the client.

## PurposeJustificationPrompt

Type: `string`

Message prompted to the client when accessing the application.

## PurposeJustificationResponse

Type: `string`

Justification given by the client when accessing the application.

## RayID

Type: `string`

Identifier of the request.

## TemporaryAccessApprovers

Type: `array[string]`

List of approvers for this access request.

## TemporaryAccessDuration

Type: `int`

Approved duration for this access request.

## UserUID

Type: `string`

The uid of the user who logged in.

[PreviousZaraz Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/zaraz_events/)[NextAccount Abuse Protection Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/account_abuse_protection_events/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/access_requests.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
