---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/nel_reports/
title: NEL reports \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:14.108727+00:00
---

# NEL reports · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/nel_reports/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Zone-scoped datasets
  5. /NEL reports



# NEL reports

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/nel_reports/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewClientIPASNClientIPASNDescriptionClientIPCountryLastKnownGoodColoCodePhaseTimestampType

The descriptions below detail the fields available for `nel_reports`.

## ClientIPASN

Type: `int`

Client ASN.

## ClientIPASNDescription

Type: `string`

Client ASN description.

## ClientIPCountry

Type: `string`

Client country.

## LastKnownGoodColoCode

Type: `string`

IATA airport code of colo client connected to.

## Phase

Type: `string`

The phase of connection the error occurred in; _dns_ | _connection_ | _application_ | _unknown_.

## Timestamp

Type: `int or string`

Timestamp for error report.

## Type

Type: `string`

The type of error in the phase.

[PreviousHTTP requests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/)[NextPage Shield events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/page_shield_events/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/zone/nel_reports.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
