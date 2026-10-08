---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs/
title: Audit Logs \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:11.412667+00:00
---

# Audit Logs · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /Audit Logs



# Audit Logs

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewActionResultActionTypeActorEmailActorIDActorIPActorTypeIDInterfaceMetadataNewValueOldValueOwnerIDResourceIDResourceTypeWhen

The descriptions below detail the fields available for `audit_logs`.

## ActionResult

Type: `bool`

Whether the action was successful.

## ActionType

Type: `string`

Type of action taken.

## ActorEmail

Type: `string`

Email of the actor.

## ActorID

Type: `string`

Unique identifier of the actor in Cloudflare's system.

## ActorIP

Type: `string`

Physical network address of the actor.

## ActorType

Type: `string`

Type of user that started the audit trail.

## ID

Type: `string`

Unique identifier of an audit log.

## Interface

Type: `string`

Entry point or interface of the audit log.

## Metadata

Type: `object`

Additional audit log-specific information. Metadata is organized in key:value pairs. Key and Value formats can vary by ResourceType.

## NewValue

Type: `object`

Contains the new value for the audited item.

## OldValue

Type: `object`

Contains the old value for the audited item.

## OwnerID

Type: `string`

The identifier of the user that was acting or was acted on behalf of. If a user did the action themselves, this value will be the same as the ActorID.

## ResourceID

Type: `string`

Unique identifier of the resource within Cloudflare's system.

## ResourceType

Type: `string`

The type of resource that was changed.

## When

Type: `int or string`

When the change happened.

[PreviousAccount Abuse Protection Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/account_abuse_protection_events/)[NextAudit Logs V2](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs_v2/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/audit_logs.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
