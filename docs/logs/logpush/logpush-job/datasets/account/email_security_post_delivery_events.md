---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/email_security_post_delivery_events/
title: Email Security Post-Delivery Events \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:12.083087+00:00
---

# Email Security Post-Delivery Events · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/email_security_post_delivery_events/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /Email Security Post-Delivery Events



# Email Security Post-Delivery Events

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/email_security_post_delivery_events/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAlertIDCompletedAtDestinationFinalDispositionFolderFromFromNameMessageIDMessageTimestampMicrosoftTenantIDOperationPostfixIDReasonsRecipientRequestedAtRequestedByRequestedDispositionStatusSubjectSuccessTo

The descriptions below detail the fields available for `email_security_post_delivery_events`.

## AlertID

Type: `string`

Email Security alert ID for the original message.

## CompletedAt

Type: `int or string`

The timestamp when the post-delivery action completed. To specify the timestamp format, refer to [Output types](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/#output-types).

## Destination

Type: `string`

Target folder for MOVE operations (for example, 'RecoverableItemsPurges').

## FinalDisposition

Type: `string`

Threat disposition of the original message.   
Possible values are _unset_ | _none_ | _malicious_ | _suspicious_ | _spam_ | _spoof_ | _bulk_.

## Folder

Type: `string`

Resolved folder name after a successful MOVE.

## From

Type: `string`

From header address of the original message (for example, '[firstlast@cloudflare.com](mailto:firstlast@cloudflare.com)').

## FromName

Type: `string`

From header display name of the original message (for example, 'First Last').

## MessageID

Type: `string`

RFC Message-ID header of the original message.

## MessageTimestamp

Type: `int or string`

The timestamp of the original message. To specify the timestamp format, refer to [Output types](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/#output-types).

## MicrosoftTenantID

Type: `string`

Microsoft 365 tenant identifier.

## Operation

Type: `string`

Post-delivery action type.   
Possible values are _move_ | _submission_ | _quarantineRelease_.

## PostfixID

Type: `string`

Email Security postfix queue identifier for the original message.

## Reasons

Type: `array[string]`

Detection findings that prompted the post-delivery action (for example, 'Malicious URL').

## Recipient

Type: `string`

Email address of the targeted mailbox (for example, '[firstlast@cloudflare.com](mailto:firstlast@cloudflare.com)').

## RequestedAt

Type: `int or string`

The timestamp when the post-delivery action was requested. To specify the timestamp format, refer to [Output types](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/#output-types).

## RequestedBy

Type: `string`

Identity that requested the post-delivery action; expected format is an email address.

## RequestedDisposition

Type: `string`

Requested disposition for SUBMISSION operations.

## Status

Type: `string`

Status message returned by the post-delivery provider (for example, 'OK').

## Subject

Type: `string`

Subject header of the original message.

## Success

Type: `bool`

Whether the post-delivery action succeeded.

## To

Type: `array[string]`

Recipient addresses of the original message (for example, '[firstlast@cloudflare.com](mailto:firstlast@cloudflare.com)').

[PreviousEmail Security Alerts](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/email_security_alerts/)[NextFirewall events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/firewall_events/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/email_security_post_delivery_events.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
