---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dlp_forensic_copies/
title: DLP Forensic Copies \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:11.989008+00:00
---

# DLP Forensic Copies · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dlp_forensic_copies/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /DLP Forensic Copies



# DLP Forensic Copies

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dlp_forensic_copies/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAccountIDDatetimeForensicCopyIDGatewayRequestIDHeadersPayloadPhaseTriggeredRuleID

The descriptions below detail the fields available for `dlp_forensic_copies`.

## AccountID

Type: `string`

Cloudflare account ID.

## Datetime

Type: `int or string`

The date and time the corresponding HTTP request was made.

## ForensicCopyID

Type: `string`

The unique ID for this particular forensic copy.

## GatewayRequestID

Type: `string`

Cloudflare request ID, as found in Gateway logs.

## Headers

Type: `object`

String key-value pairs for a selection of HTTP headers on the associated request/response.

## Payload

Type: `string`

Captured request/response data, base64-encoded.

## Phase

Type: `string`

Phase of the HTTP request this forensic copy was captured from (that is, "request" or "response").

## TriggeredRuleID

Type: `string`

The ID of the Gateway firewall rule that triggered this forensic copy.

[PreviousDEX Device State Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dex_device_state_events/)[NextDNS Firewall Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dns_firewall_logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/dlp_forensic_copies.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
