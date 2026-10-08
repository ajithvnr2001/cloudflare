---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/page_shield_events/
title: Page Shield events \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:14.147113+00:00
---

# Page Shield events · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/page_shield_events/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Zone-scoped datasets
  5. /Page Shield events



# Page Shield events

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/page_shield_events/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewActionCSPDirectiveHostPageURLPolicyIDResourceTypeTimestampURLURLContainsCDNCGIPath (deprecated)URLHost

The descriptions below detail the fields available for `page_shield_events`.

## Action

Type: `string`

The action which was taken against the violation.   
Possible values are _log_ | _allow_.

## CSPDirective

Type: `string`

The violated directive in the report.

## Host

Type: `string`

The host where the resource was seen on.

## PageURL

Type: `string`

The page URL the violation was seen on.

## PolicyID

Type: `string`

The ID of the policy which was violated.

## ResourceType

Type: `string`

The resource type of the violated directive. Possible values are 'script', 'connection', or 'other' for unmonitored resource types.

## Timestamp

Type: `int or string`

The timestamp of when the report was received.

## URL

Type: `string`

The resource URL.

## URLContainsCDNCGIPath (deprecated)

Type: `bool`

Whether the resource URL contains the '/cdn-cgi/' path.

## URLHost

Type: `string`

The domain host of the URL.

[PreviousNEL reports](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/nel_reports/)[NextSpectrum events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/spectrum_events/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/zone/page_shield_events.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
