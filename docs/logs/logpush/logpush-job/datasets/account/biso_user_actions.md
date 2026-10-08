---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/biso_user_actions/
title: Browser Isolation User Actions \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:11.536491+00:00
---

# Browser Isolation User Actions · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/biso_user_actions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /Browser Isolation User Actions



# Browser Isolation User Actions

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/biso_user_actions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAccountIDDecisionDomainNameMetadataTimestampTypeURLUserEmailUserID

The descriptions below detail the fields available for `biso_user_actions`.

## AccountID

Type: `string`

The Cloudflare account ID.

## Decision

Type: `string`

The decision applied ('allow' or 'block').

## DomainName

Type: `string`

The domain name in the URL.

## Metadata

Type: `string`

Additional information specific to a user action (JSON string).

## Timestamp

Type: `int or string`

The date and time.

## Type

Type: `string`

The user action type (for example, 'copy', 'paste', 'download').

## URL

Type: `string`

The URL of the webpage where a user action was performed.

## UserEmail

Type: `string`

The user email.

## UserID

Type: `string`

The user ID.

[PreviousAudit Logs V2](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs_v2/)[NextCASB Findings](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/casb_findings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/biso_user_actions.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
