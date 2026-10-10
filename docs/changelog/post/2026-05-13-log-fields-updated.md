---
url: https://developers.cloudflare.com/changelog/post/2026-05-13-log-fields-updated/
title: New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:38.163977+00:00
---

# New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-13-log-fields-updated/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 13, 2026

## New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### New datasets

  * **Email Security Post-Delivery Events** : A new dataset with fields including `AlertID`, `CompletedAt`, `Destination`, `FinalDisposition`, `Folder`, `From`, `FromName`, `MessageID`, `MessageTimestamp`, `MicrosoftTenantID`, `Operation`, `PostfixID`, `Reasons`, `Recipient`, `RequestedAt`, `RequestedBy`, `RequestedDisposition`, `Status`, `Subject`, `Success`, and `To`.
  * **Magic Network Monitoring Flow Logs** : A new dataset with fields including `AWSVPCFlowJSON`, `Bits`, `DestinationAS`, `DestinationAddress`, `DestinationPort`, `DeviceID`, `EgressBits`, `EgressPackets`, `Ethertype`, `FlowProtocol`, `FlowTimestamp`, `NumFlows`, `PacketID`, `Packets`, `Protocol`, `RuleIDs`, `SampleRate`, `SampleRateType`, `SamplerAddress`, `SourceAS`, `SourceAddress`, `SourcePort`, `TcpFlags`, and `Timestamp`.



#### Updated fields in existing datasets

  * **Firewall events** (added): `AISecurityInjectionScore`, `AISecurityPIICategories`, `AISecurityTokenCount`, and `AISecurityUnsafeTopicCategories`.
  * **HTTP requests** (added): `AISecurityInjectionScore`, `AISecurityPIICategories`, `AISecurityTokenCount`, `AISecurityUnsafeTopicCategories`, and `Subrequests`.



For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).
