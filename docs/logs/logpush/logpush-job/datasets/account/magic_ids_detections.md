---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_ids_detections/
title: Magic IDS Detections \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:12.754251+00:00
---

# Magic IDS Detections · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_ids_detections/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /Magic IDS Detections



# Magic IDS Detections

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_ids_detections/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewActionColoCityColoCodeDestinationIPDestinationPortProtocolSignatureIDSignatureMessageSignatureRevisionSourceIPSourcePortTimestamp

The descriptions below detail the fields available for `magic_ids_detections`.

## Action

Type: `string`

What action was taken on the packet. Possible values are _pass_ | _block_.

## ColoCity

Type: `string`

The city where the detection occurred.

## ColoCode

Type: `string`

The IATA airport code corresponding to where the detection occurred.

## DestinationIP

Type: `string`

The destination IP of the packet which triggered the detection.

## DestinationPort

Type: `int`

The destination port of the packet which triggered the detection. It is set to 0 if the protocol field is set to _any_.

## Protocol

Type: `string`

The layer 4 protocol of the packet which triggered the detection. Possible values are _tcp_ | _udp_ | _any_. Variant _any_ means a detection occurred at a lower layer (such as IP).

## SignatureID

Type: `int`

The signature ID of the detection.

## SignatureMessage

Type: `string`

The signature message of the detection. Describes what the packet is attempting to do.

## SignatureRevision

Type: `int`

The signature revision of the detection.

## SourceIP

Type: `string`

The source IP of packet which triggered the detection.

## SourcePort

Type: `int`

The source port of the packet which triggered the detection. It is set to 0 if the protocol field is set to _any_.

## Timestamp

Type: `int or string`

A timestamp of when the detection occurred.

[PreviousMagic BGP Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_bgp_logs/)[NextMagic Network Monitoring Flow Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/mnm_flow_logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/magic_ids_detections.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
