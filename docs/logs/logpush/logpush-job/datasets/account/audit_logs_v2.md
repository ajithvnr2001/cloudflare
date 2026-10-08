---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs_v2/
title: Audit Logs V2 \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:11.507105+00:00
---

# Audit Logs V2 · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs_v2/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /Audit Logs V2



# Audit Logs V2

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs_v2/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAccountIDAccountNameActionDescriptionActionResultActionTimestampActionTypeActorContextActorEmailActorIDActorIPAddressActorTokenDetailsActorTypeAuditLogIDRawResourceIDResourceProductResourceRequestResourceResponseResourceScopeResourceTypeResourceValueZoneIDZoneName

The descriptions below detail the fields available for `audit_logs_v2`.

## AccountID

Type: `string`

The Cloudflare account ID.

## AccountName

Type: `string`

The Cloudflare account name.

## ActionDescription

Type: `string`

Description of action taken.

## ActionResult

Type: `string`

Whether the action was successful.

## ActionTimestamp

Type: `int or string`

When the change happened.

## ActionType

Type: `string`

Type of action taken.

## ActorContext

Type: `string`

Context of the actor.

## ActorEmail

Type: `string`

Email of the actor.

## ActorID

Type: `string`

Unique identifier of the actor in Cloudflare's system.

## ActorIPAddress

Type: `string`

Physical network address of the actor.

## ActorTokenDetails

Type: `object`

Details of how the actor is authenticated.

## ActorType

Type: `string`

Type of user that started the audit trail.

## AuditLogID

Type: `string`

Unique identifier of an audit log.

## Raw

Type: `object`

Raw data.

## ResourceID

Type: `string`

Unique identifier of the resource within Cloudflare's system.

## ResourceProduct

Type: `string`

Resource product.

## ResourceRequest

Type: `object`

Resource request.

## ResourceResponse

Type: `object`

Resource response.

## ResourceScope

Type: `string`

Resource scope.

## ResourceType

Type: `string`

The type of resource that was changed.

## ResourceValue

Type: `object`

Resource value.

## ZoneID

Type: `string`

The Cloudflare zone ID.

## ZoneName

Type: `string`

The Cloudflare zone name.

[PreviousAudit Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs/)[NextBrowser Isolation User Actions](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/biso_user_actions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/audit_logs_v2.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
