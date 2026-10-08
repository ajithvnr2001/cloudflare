---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ipsec_logs/
title: IPSec Logs \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:12.541281+00:00
---

# IPSec Logs · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ipsec_logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /IPSec Logs



# IPSec Logs

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ipsec_logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLevelLocalIPLocalPortMessageRemoteIPRemotePortTimestamp

The descriptions below detail the fields available for `ipsec_logs`.

## Level

Type: `string`

The level of the log.

## LocalIP

Type: `string`

The local IP address associated with the log.

## LocalPort

Type: `int`

The local port associated with the log.

## Message

Type: `string`

The log message. IKEv2 ciphersuite is logged here for handshake messages.

## RemoteIP

Type: `string`

The remote IP address associated with the log.

## RemotePort

Type: `int`

The remote port associated with the log.

## Timestamp

Type: `int or string`

Timestamp at which the log occurred.

[PreviousGateway Network](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_network/)[NextMagic BGP Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_bgp_logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/ipsec_logs.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
