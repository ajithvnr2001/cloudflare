---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/mnm_flow_logs/
title: Magic Network Monitoring Flow Logs \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:12.917639+00:00
---

# Magic Network Monitoring Flow Logs · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/mnm_flow_logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /Magic Network Monitoring Flow Logs



# Magic Network Monitoring Flow Logs

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/mnm_flow_logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAWSVPCFlowJSONBitsDestinationASDestinationAddressDestinationPortDeviceIDEgressBitsEgressPacketsEthertypeFlowProtocolFlowTimestampNumFlowsPacketIDPacketsProtocolRuleIDsSampleRateSampleRateTypeSamplerAddressSourceASSourceAddressSourcePortTcpFlagsTimestamp

The descriptions below detail the fields available for `mnm_flow_logs`.

## AWSVPCFlowJSON

Type: `string`

AWS VPC Flow Logs JSON data. Only set if the flow protocol is AWS_VPC.

## Bits

Type: `int`

The number of bits transmitted.

## DestinationAS

Type: `int`

The autonomous system number of the destination.

## DestinationAddress

Type: `string`

The destination IP address.

## DestinationPort

Type: `int`

The destination port number.

## DeviceID

Type: `string`

The ID of the network device (such as a router or switch) that originated the flow.

## EgressBits

Type: `int`

The number of egress bits transmitted.

## EgressPackets

Type: `int`

The number of egress packets transmitted.

## Ethertype

Type: `int`

The ethertype of the packet (for example, 2048 for IPv4, 34525 for IPv6).

## FlowProtocol

Type: `string`

The flow protocol (for example, 'AWS_VPC', 'IPFIX', 'SFLOW_5', 'NETFLOW_V9').

## FlowTimestamp

Type: `int or string`

The timestamp of the flow. To specify the timestamp format, refer to [Output types](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/#output-types).

## NumFlows

Type: `int`

The number of flows.

## PacketID

Type: `string`

The packet ID.

## Packets

Type: `int`

The number of packets transmitted.

## Protocol

Type: `int`

The protocol number (for example, 6 for TCP, 17 for UDP).

## RuleIDs

Type: `string`

Comma-separated list of Magic Network Monitoring rule IDs associated with the flow, if any.

## SampleRate

Type: `int`

The sample rate of the flow set by the sampler (1, 100, 1000, 1024, 2000 are common).

## SampleRateType

Type: `string`

The type of sample rate (for example, 'flow', 'default', 'propagated').

## SamplerAddress

Type: `string`

The sampler IP address.

## SourceAS

Type: `int`

The autonomous system number of the source.

## SourceAddress

Type: `string`

The source IP address.

## SourcePort

Type: `int`

The source port number.

## TcpFlags

Type: `int`

The TCP flags.

## Timestamp

Type: `int or string`

The date and time of the event. To specify the timestamp format, refer to [Output types](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/#output-types).

[PreviousMagic IDS Detections](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_ids_detections/)[NextMCP Portal Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/mcp_portal_logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/mnm_flow_logs.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
