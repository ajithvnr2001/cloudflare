---
url: https://developers.cloudflare.com/changelog/product/logs/
title: Logs Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:06.536104+00:00
---

# Logs Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/logs/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Sep 30, 2026

## [Logpush is now available on all plans with usage-based pricing](https://developers.cloudflare.com/changelog/post/2026-09-30-logpush-usage-based-pricing/)

[Logpush](https://developers.cloudflare.com/logs/logpush/)[Logs](https://developers.cloudflare.com/logs/)

Cloudflare Logpush is now available on Free, Pro, Business, and Enterprise plans with usage-based pricing. Free, Pro, and Business customers can enable Logpush through self-service. Enterprise customers continue to work with their account team. Logpush Transformers are also now generally available.

Each account receives included monthly usage before charges apply:

  * **Internal exports** : 25 GB per month, then $0.03 per additional GB.
  * **External exports** : 25 GB per month, then $0.10 per additional GB.
  * **Transformations** : 1 GB per month, then $0.04 per additional GB.



R2 and Pipelines use the internal destination rate. All other destinations use the external destination rate.

Existing Enterprise contracts retain their current Logpush pricing through renewal. Workers Logpush for Workers Trace Events retains request-based pricing, and OpenTelemetry destinations retain event-based Workers Observability pricing.

For complete rates, measurement details, and billing examples, refer to [Logpush pricing](https://developers.cloudflare.com/logs/logpush/pricing/).

Sep 30, 2026

## [Transformers are now generally available](https://developers.cloudflare.com/changelog/post/2026-09-30-transformers-ga/)

[Logpush](https://developers.cloudflare.com/logs/logpush/)[Logs](https://developers.cloudflare.com/logs/)

Transformers are now generally available for supported Logpush datasets on Free, Pro, Business, and Enterprise plans. Use SQL to filter records, reshape fields, redact sensitive values, compute new fields, or add metadata before Logpush delivers each batch.

Create and preview Transformers in Transformer Studio or through the Cloudflare API, then attach them to eligible account-scoped or zone-scoped Logpush jobs that use NDJSON output. Cloudflare validates each query against the dataset schema before saving it.

Each account includes 1 GB of transformation input per month. Additional input costs $0.04 per GB. For setup instructions, supported SQL, limits, and examples, refer to [Transformers](https://developers.cloudflare.com/logs/logpush/transformers/). For billing details, refer to [Logpush pricing](https://developers.cloudflare.com/logs/logpush/pricing/).

Sep 18, 2026

## [Filter DDoS attack traffic from Logpush jobs](https://developers.cloudflare.com/changelog/post/2026-09-18-filter-ddos-attack-traffic/)

[Logpush](https://developers.cloudflare.com/logs/logpush/)[Logs](https://developers.cloudflare.com/logs/)

Logpush jobs can now exclude identified distributed denial-of-service (DDoS) attack traffic. This option reduces attack traffic in delivered logs.

It supports the `http_requests`, `firewall_events`, and `network_analytics_logs` datasets.

In the dashboard, select **Exclude DDoS attack traffic** under **Advanced Options**. With the API, add this field to a job request:
    
    
    {
    	"filter_attack_traffic": true
    }

For more information, refer to [API configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#ddos-attack-traffic).

Aug 26, 2026

## [Azure Functions-based Microsoft Sentinel connector deprecation](https://developers.cloudflare.com/changelog/post/2026-08-26-sentinel-functions-connector-deprecation/)

[Logpush Connectors](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/)[Logs](https://developers.cloudflare.com/logs/)

Cloudflare Enterprise customers using the [Azure Functions-based Microsoft Sentinel connector ↗︎](https://marketplace.microsoft.com/en-us/product/cloudflare.cloudflare_sentinel?tab=Overview) must migrate to the [Cloudflare for Microsoft Sentinel Codeless Connector Framework (CCF) connector ↗︎](https://marketplace.microsoft.com/en-us/product/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview) by 2026-09-14.

Microsoft is deprecating the Azure Monitor HTTP Data Collector API. Support for the API ends on 2026-09-14. As a result, Cloudflare will no longer maintain the Azure Functions-based connector after that date.

To migrate, follow the [Microsoft Sentinel integration setup guide](https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/).

#### Additional resources

  * [Download Cloudflare's CCF Sentinel Solution ↗︎](https://marketplace.microsoft.com/en-us/product/azure-application/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview)
  * [Microsoft Sentinel data lake overview ↗︎](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview)
  * [About the CCF platform ↗︎](https://learn.microsoft.com/en-us/azure/sentinel/create-codeless-connector)



For more information, refer to Microsoft's [Azure Monitor HTTP Data Collector API deprecation notice ↗︎](https://learn.microsoft.com/en-us/previous-versions/azure/azure-monitor/logs/data-collector-api?tabs=powershell).

Aug 20, 2026

## [New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs](https://developers.cloudflare.com/changelog/post/2026-08-20-log-fields-updated/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### New datasets

  * **Account Abuse Protection Events** : A new dataset with fields including `AuthenticationIdentityProvider`, `AuthenticationMethod`, `AuthenticationStatus`, `BotScore`, `ClientASN`, `ClientCity`, `ClientCountry`, `ClientIP`, `Email`, `EphemeralID`, `EventSource`, `EventType`, `FraudEmailRisk`, `Host`, `JA4`, `RayID`, `Timestamp`, `UserAgent`, and `UserID`.
  * **Magic BGP Logs** : A new dataset with fields including `Direction`, `EventData`, `EventKind`, `EventTimestamp`, `TunnelID`, and `TunnelName`.



#### Updated fields in existing datasets

  * **Firewall events** (added): `AISecurityCustomTopicCategories`, `WAFRequestSignatureCategories`, and `WAFRequestSignatureRefs`.
  * **Gateway HTTP** (added): `ExperimentalFeatures` and `PackageInfo`.
  * **HTTP requests** (added): `AISecurityCustomTopicCategories`, `ClientTLSKeyExchangeGroup`, `WAFRequestSignatureCategories`, and `WAFRequestSignatureRefs`.



For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

Aug 20, 2026

## [Per-zone post-quantum visibility in Logpush and Log Explorer](https://developers.cloudflare.com/changelog/post/2026-08-20-pqc-key-exchange-visibility/)

[Logs](https://developers.cloudflare.com/logs/)[Log Explorer](https://developers.cloudflare.com/log-explorer/)

[Cloudflare Radar ↗︎](https://radar.cloudflare.com/post-quantum) publishes global statistics on post-quantum key agreement adoption across all Cloudflare traffic, but until now customers had no way to see the same measurement scoped to their own zones. This is now possible because the [`http_requests`](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/) Logpush dataset — also queryable in [Log Explorer](https://developers.cloudflare.com/log-explorer/) — includes a new `ClientTLSKeyExchangeGroup` field.

The field reports the TLS key exchange group negotiated on the client-to-Cloudflare connection, by group name. Post-quantum connections appear as `X25519MLKEM768`, and classical connections appear as `X25519`, `P-256`, or another named group. A value of `UNK` means the group could not be determined, and `NONE` means either RSA key exchange was used or TLS was not used.

With this field, you can build per-zone reports showing what percentage of your inbound HTTPS traffic is protected by post-quantum key agreement, break the number down by hostname, path, user agent, or country, and push the data into your SIEM via any [Logpush destination](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/).

Jul 7, 2026

## [New WebSocket Analytics Logpush dataset](https://developers.cloudflare.com/changelog/post/2026-07-07-websocket-analytics-dataset/)

[Logs](https://developers.cloudflare.com/logs/)

Enterprise customers can now push per-connection WebSocket analytics to any [Logpush destination](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/) using the new `websocket_analytics` dataset. Each log record is emitted when a WebSocket connection closes and includes fields that were previously only available to Cloudflare engineers via internal tooling.

Key fields include:

  * **`ConnectionCloseReason`** — why the connection ended: `peerReset`, `peerNoError`, `timedOut`, `upstreamReset`, `protocolViolation`, `unspecifiedError`, or `none`.
  * **`ConnectionCloseSource`** — which side initiated the close: `upstream`, `downstream`, `me`, or `both`.
  * **`ConnectionTransportCloseCode`** — the TLS alert code or TCP-level close code for additional precision.
  * **`RayID`** — correlate WebSocket connection events with your existing HTTP Request logs.



The dataset also includes directional byte counts (`BytesSentClient`, `BytesReceivedClient`, `BytesSentOrigin`, `BytesReceivedOrigin`), connection timestamps, client IP, colo code, and request metadata from the original WebSocket upgrade.

This data lets you build alerts on connection close patterns — for example, detecting spikes in TCP resets (`ConnectionCloseReason == "peerReset"`) grouped by host and data center — directly in your existing log analysis tools.

For the full list of available fields, refer to [WebSocket Analytics](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/websocket_analytics/).

Jul 2, 2026

## [Updated fields across multiple Logpush datasets in Cloudflare Logs](https://developers.cloudflare.com/changelog/post/2026-07-02-log-fields-updated/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### Updated fields in existing datasets

  * **Gateway DNS** (added): `AppliedMaxTTL` and `UpstreamRecordTTLs`.
  * **Gateway HTTP** (added): `Warnings`.
  * **HTTP requests** (added): `CacheLockWaitedMs`.



For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

Jun 30, 2026

## [Account-scoped firewall events dataset in Logpush](https://developers.cloudflare.com/changelog/post/2026-06-30-account-level-firewall-events/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare Logpush now supports [firewall events as an account-scoped dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/firewall_events/). Configure a single Logpush job at the account level to receive firewall events for every zone in the account, instead of creating and maintaining a separate job per zone.

The dataset includes a new [`ZoneName`](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/firewall_events/#zonename) field so you can identify which zone each event came from when consuming logs in your downstream pipeline.

#### What's available

  * A new account-scoped `firewall_events` dataset, configurable via the [Logpush API](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/) or the Cloudflare dashboard.
  * The same fields and filter expressions supported by the existing [zone-scoped firewall events dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/firewall_events/), plus the new `ZoneName` field.
  * Support for all existing Logpush destinations.



Jun 24, 2026

## [New WebSocket Analytics Logpush dataset and updated fields](https://developers.cloudflare.com/changelog/post/2026-06-24-log-fields-updated/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### New datasets

  * **WebSocket Analytics** : A new dataset with fields including `BytesReceivedClient`, `BytesReceivedOrigin`, `BytesSentClient`, `BytesSentOrigin`, `ClientASN`, `ClientIP`, `ClientRequestHost`, `ClientRequestPath`, `ClientRequestUserAgent`, `ColoCode`, `ConnectionCloseReason`, `ConnectionCloseSource`, `ConnectionID`, `ConnectionTransportCloseCode`, `EdgeEndTimestamp`, `EdgeStartTimestamp`, and `RayID`.



#### Updated fields in existing datasets

  * **Firewall events** (added): `ZoneName`. The Firewall events dataset is now also available for [account-scope Logpush](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/firewall_events/), in addition to the existing zone scope.
  * **Email Security Alerts** (added): `BCC`, `DKIMResult`, `DMARCPolicy`, `DMARCResult`, and `SPFResult`.



For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

Jun 1, 2026

## [New Turnstile Events Logpush dataset in Cloudflare Logs](https://developers.cloudflare.com/changelog/post/2026-06-01-log-fields-updated/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### New datasets

  * **Turnstile Events** : A new dataset with fields including `ASN`, `Action`, `BrowserMajor`, `BrowserName`, `ClientIP`, `CountryCode`, `EventType`, `Hostname`, `OSMajor`, `OSName`, `Sitekey`, `Timestamp`, and `UserAgent`.



For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

May 29, 2026

## [Updated fields across multiple Logpush datasets in Cloudflare Logs](https://developers.cloudflare.com/changelog/post/2026-05-29-log-fields-updated/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### Updated fields in existing datasets

  * **DEX Device State Events** (added): `DeviceRegistrationProfileID`.
  * **Gateway HTTP** (added): `AddedHeaders`, `DeletedHeaders`, and `SetHeaders`.
  * **HTTP requests** (added): `MatchedRules`.



For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

May 13, 2026

## [New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs](https://developers.cloudflare.com/changelog/post/2026-05-13-log-fields-updated/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### New datasets

  * **Email Security Post-Delivery Events** : A new dataset with fields including `AlertID`, `CompletedAt`, `Destination`, `FinalDisposition`, `Folder`, `From`, `FromName`, `MessageID`, `MessageTimestamp`, `MicrosoftTenantID`, `Operation`, `PostfixID`, `Reasons`, `Recipient`, `RequestedAt`, `RequestedBy`, `RequestedDisposition`, `Status`, `Subject`, `Success`, and `To`.
  * **Magic Network Monitoring Flow Logs** : A new dataset with fields including `AWSVPCFlowJSON`, `Bits`, `DestinationAS`, `DestinationAddress`, `DestinationPort`, `DeviceID`, `EgressBits`, `EgressPackets`, `Ethertype`, `FlowProtocol`, `FlowTimestamp`, `NumFlows`, `PacketID`, `Packets`, `Protocol`, `RuleIDs`, `SampleRate`, `SampleRateType`, `SamplerAddress`, `SourceAS`, `SourceAddress`, `SourcePort`, `TcpFlags`, and `Timestamp`.



#### Updated fields in existing datasets

  * **Firewall events** (added): `AISecurityInjectionScore`, `AISecurityPIICategories`, `AISecurityTokenCount`, and `AISecurityUnsafeTopicCategories`.
  * **HTTP requests** (added): `AISecurityInjectionScore`, `AISecurityPIICategories`, `AISecurityTokenCount`, `AISecurityUnsafeTopicCategories`, and `Subrequests`.



For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

Apr 21, 2026

## [Logpush subrequest merging for HTTP requests](https://developers.cloudflare.com/changelog/post/2026-04-21-logpush-subrequests-merging/)

[Logs](https://developers.cloudflare.com/logs/)

When a Cloudflare Worker intercepts a visitor request, it can dispatch additional outbound fetch calls called subrequests. By default, each subrequest generates its own log entry in Logpush, resulting in multiple log lines per visitor request. With subrequest merging enabled, subrequest data is embedded as a nested array field on the parent log record instead.

#### What's new

  * New subrequest_merging field on Logpush jobs — Set "merge_subrequests": true when creating or updating an http_requests Logpush job to enable the feature.
  * New Subrequests log field — When subrequest merging is enabled, a Subrequests field (`array\<object\>`) is added to each parent request log record. Each element in the array contains the standard http_requests fields for that subrequest.



#### Limitations

  * Applies to the http_requests (zone-scoped) dataset only.
  * A maximum of 50 subrequests are merged per parent request. Subrequests beyond this limit are passed through unmodified as individual log entries.
  * Subrequests must complete within 5 minutes of the visitor request. Subrequests that exceed this window are passed through unmodified.
  * Subrequests that do not qualify appear as separate log entries — no data is lost.
  * Subrequest merging is being gradually rolled out and is not yet available on all zones. Contact your account team for concerns or to ensure it is enabled for your zone.
  * For more information, refer to [Subrequests](https://developers.cloudflare.com/logs/logpush/logpush-job/subrequests/).



Apr 20, 2026

## [Cloudflare Pipelines as a Logpush destination](https://developers.cloudflare.com/changelog/post/2026-04-20-pipelines-logpush-destination/)

[Logs](https://developers.cloudflare.com/logs/)[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)

Logpush has traditionally been great at delivering Cloudflare logs to a variety of destinations in JSON format. While JSON is flexible and easily readable, it can be inefficient to store and query at scale.

With this release, you can now send your logs directly to [Pipelines](https://developers.cloudflare.com/basin-pipelines/) to ingest, transform, and store your logs in [R2](https://developers.cloudflare.com/r2/) as Parquet files or Apache Iceberg tables managed by [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/). This makes the data footprint more compact and more efficient at querying your logs instantly with [R2 SQL](https://developers.cloudflare.com/basin-sql/) or any other query engine that supports Apache Iceberg or Parquet.

#### Transform logs before storage

Pipelines SQL runs on each log record in-flight, so you can reshape your data before it is written. For example, you can drop noisy fields, redact sensitive values, or derive new columns:
    
    
    INSERT INTO http_logs_sink
    SELECT
      ClientIP,
      EdgeResponseStatus,
      to_timestamp_micros(EdgeStartTimestamp) AS event_time,
      upper(ClientRequestMethod) AS method,
      sha256(ClientIP) AS hashed_ip
    FROM http_logs_stream
    WHERE EdgeResponseStatus >= 400;

Pipelines SQL supports string functions, regex, hashing, JSON extraction, timestamp conversion, conditional expressions, and more. For the full list, refer to the [Pipelines SQL reference](https://developers.cloudflare.com/basin-pipelines/sql-reference/).

#### Get started

To configure Pipelines as a Logpush destination, refer to [Enable Cloudflare Pipelines](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/pipelines/).

Apr 15, 2026

## [New TenantID and Firewall for AI fields in Logpush datasets](https://developers.cloudflare.com/changelog/post/2026-04-15-logpush-new-fields/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has added new fields to multiple [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### TenantID field

The following Gateway and Zero Trust datasets now include a `TenantID` field:

  * **[Gateway DNS](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_dns/#tenantid)** : Identifies the tenant ID of the DNS request, if it exists.
  * **[Gateway HTTP](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_http/#tenantid)** : Identifies the tenant ID of the HTTP request, if it exists.
  * **[Gateway Network](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_network/#tenantid)** : Identifies the tenant ID of the network session, if it exists.
  * **[Zero Trust Network Sessions](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/#tenantid)** : Identifies the tenant ID of the network session, if it exists.



#### Firewall for AI fields

The following datasets now include [Firewall for AI](https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/#firewall-for-ai) fields:

  * **[Firewall Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/firewall_events/)** :

    * `FirewallForAIInjectionScore`: The score indicating the likelihood of a prompt injection attack in the request.
    * `FirewallForAIPIICategories`: List of PII categories detected in the request.
    * `FirewallForAITokenCount`: The number of tokens in the request.
    * `FirewallForAIUnsafeTopicCategories`: List of unsafe topic categories detected in the request.
  * **[HTTP Requests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/)** :

    * `FirewallForAIInjectionScore`: The score indicating the likelihood of a prompt injection attack in the request.
    * `FirewallForAIPIICategories`: List of PII categories detected in the request.
    * `FirewallForAITokenCount`: The number of tokens in the request.
    * `FirewallForAIUnsafeTopicCategories`: List of unsafe topic categories detected in the request.



For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

Apr 14, 2026

## [Logpush to BigQuery — Cloudflare dashboard support](https://developers.cloudflare.com/changelog/post/2026-04-14-bigquery-dashboard-support/)

[Logpush](https://developers.cloudflare.com/logs/logpush/)[Logs](https://developers.cloudflare.com/logs/)

You can now configure Logpush jobs to Google BigQuery directly from the Cloudflare dashboard, in addition to the existing API-based setup.

Previously, setting up a BigQuery Logpush destination required using the Logpush API. Now you can create and manage BigQuery Logpush jobs from the **Logpush** page in the Cloudflare dashboard by selecting **Google BigQuery** as the destination and entering your Google Cloud project ID, dataset ID, table ID, and service account credentials.

For more information, refer to [Enable Logpush to Google BigQuery](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/bigquery/).

Apr 6, 2026

## [New ResponseTimeMs field in Gateway DNS Logpush dataset](https://developers.cloudflare.com/changelog/post/2026-04-06-gateway-dns-response-time-ms/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has added a new field to the [Gateway DNS](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_dns/#responsetimems) Logpush dataset:

  * **ResponseTimeMs** : Total response time of the DNS request in milliseconds.



For the complete field definitions, refer to [Gateway DNS dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_dns/).

Apr 2, 2026

## [BigQuery as Logpush destination](https://developers.cloudflare.com/changelog/post/2026-04-02-bigquery-destination/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare Logpush now supports **BigQuery** as a native destination.

Logs from Cloudflare can be sent to [Google Cloud BigQuery ↗︎](https://cloud.google.com/bigquery) via [Logpush](https://developers.cloudflare.com/logs/logpush/). The destination can be configured through the Logpush UI in the Cloudflare dashboard or by using the [Logpush API](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/).

For more information, refer to the [Destination Configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/bigquery/) documentation.

Mar 25, 2026

## [Logpush — More granular timestamps](https://developers.cloudflare.com/changelog/post/2026-03-25-logpush-granular-timestamps/)

[Logpush](https://developers.cloudflare.com/logs/logpush/)[Logs](https://developers.cloudflare.com/logs/)

Logpush now supports higher-precision timestamp formats for log output. You can configure jobs to output timestamps at millisecond or nanosecond precision. This is available in both the Logpush UI in the Cloudflare dashboard and the [Logpush API](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/).

To use the new formats, set `timestamp_format` in your Logpush job's `output_options`:

  * `rfc3339ms` — `2024-02-17T23:52:01.123Z`
  * `rfc3339ns` — `2024-02-17T23:52:01.123456789Z`



Default timestamp formats apply unless explicitly set. The dashboard defaults to `rfc3339` and the API defaults to `unixnano`.

For more information, refer to the [Log output options](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/) documentation.

Mar 9, 2026

## [New MCP Portal Logs dataset and new fields across multiple Logpush datasets in Cloudflare Logs](https://developers.cloudflare.com/changelog/post/2026-03-09-log-fields-updated/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has added new fields across multiple [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### New dataset

  * **MCP Portal Logs** : A new dataset with fields including `ClientCountry`, `ClientIP`, `ColoCode`, `Datetime`, `Error`, `Method`, `PortalAUD`, `PortalID`, `PromptGetName`, `ResourceReadURI`, `ServerAUD`, `ServerID`, `ServerResponseDurationMs`, `ServerURL`, `SessionID`, `Success`, `ToolCallName`, `UserEmail`, and `UserID`.



#### New fields in existing datasets

  * **DEX Application Tests** : `HTTPRedirectEndMs`, `HTTPRedirectStartMs`, `HTTPResponseBody`, and `HTTPResponseHeaders`.
  * **DEX Device State Events** : `ExperimentalExtra`.
  * **Firewall Events** : `FraudUserID`.
  * **Gateway HTTP** : `AppControlInfo` and `ApplicationStatuses`.
  * **Gateway DNS** : `InternalDNSDurationMs`.
  * **HTTP Requests** : `FraudEmailRisk`, `FraudUserID`, and `PayPerCrawlStatus`.
  * **Network Analytics Logs** : `DNSQueryName`, `DNSQueryType`, and `PFPCustomTag`.
  * **WARP Toggle Changes** : `UserEmail`.
  * **WARP Config Changes** : `UserEmail`.
  * **Zero Trust Network Session Logs** : `SNI`.



For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

Dec 11, 2025

## [SentinelOne as Logpush destination](https://developers.cloudflare.com/changelog/post/2025-12-11-sentinelone-destination/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare Logpush now supports **SentinelOne** as a native destination.

Logs from Cloudflare can be sent to [SentinelOne AI SIEM ↗︎](https://www.sentinelone.com/) via [Logpush](https://developers.cloudflare.com/logs/logpush/). The destination can be configured through the Logpush UI in the Cloudflare dashboard or by using the [Logpush API](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/).

For more information, refer to the [Destination Configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/sentinelone/) documentation.

Nov 11, 2025

## [Logpush Health Dashboards](https://developers.cloudflare.com/changelog/post/2025-11-11-health-dashboards/)

[Logs](https://developers.cloudflare.com/logs/)

We’re excited to introduce **Logpush Health Dashboards** , giving customers real-time visibility into the status, reliability, and performance of their [Logpush](https://developers.cloudflare.com/logs/logpush/) jobs. Health dashboards make it easier to detect delivery issues, monitor job stability, and track performance across destinations. The dashboards are divided into two sections:

  * **Upload Health** : See how much data was successfully uploaded, where drops occurred, and how your jobs are performing overall. This includes data completeness, success rate, and upload volume.

  * **Upload Reliability** – Diagnose issues impacting stability, retries, or latency, and monitor key metrics such as retry counts, upload duration, and destination availability.


![Health Dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1333,height=334,format=webp/_astro/Health-Dashboard.CP0mV0IW.gif)

Health Dashboards can be accessed from the Logpush page in the Cloudflare dashboard at the account or zone level, under the Health tab. For more details, refer to our [**Logpush Health Dashboards**](https://developers.cloudflare.com/logs/logpush/logpush-health) documentation, which includes a comprehensive troubleshooting guide to help interpret and resolve common issues.

Nov 5, 2025

## [Logpush Permission Update for Zero Trust Datasets](https://developers.cloudflare.com/changelog/post/2025-11-05-logpush-permissions-update/)

[Logs](https://developers.cloudflare.com/logs/)

[Permissions](https://developers.cloudflare.com/logs/logpush/permissions/) for managing Logpush jobs related to [Zero Trust datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/) (Access, Gateway, and DEX) have been updated to improve data security and enforce appropriate access controls.

To view, create, update, or delete Logpush jobs for Zero Trust datasets, users must now have both of the following permissions:

  * Logs Edit
  * Zero Trust: PII Read



Note

Update your UI, API or Terraform configurations to include the new permissions. Requests to Zero Trust datasets will fail due to insufficient access without the additional permission.

Oct 27, 2025

## [Azure Sentinel Connector](https://developers.cloudflare.com/changelog/post/2025-10-27-Sentinel-connector/)

[Logs](https://developers.cloudflare.com/logs/)

Logpush now supports integration with [Microsoft Sentinel ↗︎](https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-sentinel).The new Azure Sentinel Connector built on Microsoft’s Codeless Connector Framework (CCF), is now available. This solution replaces the previous Azure Functions-based connector, offering significant improvements in security, data control, and ease of use for customers. Logpush customers can send logs to Azure Blob Storage and configure this new Sentinel Connector to ingest those logs directly into Microsoft Sentinel.

This upgrade significantly streamlines log ingestion, improves security, and provides greater control:

  * Simplified Implementation: Easier for engineering teams to set up and maintain.
  * Cost Control: New support for Data Collection Rules (DCRs) allows you to filter and transform logs at ingestion time, offering potential cost savings.
  * Enhanced Security: CCF provides a higher level of security compared to the older Azure Functions connector.
  * Data Lake Integration: Includes native integration with Data Lake.



Find the new solution [here ↗︎](https://marketplace.microsoft.com/en-us/product/azure-application/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview) and refer to the [Cloudflare's developer documentation ↗︎](https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/#supported-logs:~:text=WorkBook%20fields,-Analytic%20rules)for more information on the connector, including setup steps, supported logs and Microsoft's resources.

← Prev

1[2](https://developers.cloudflare.com/changelog/product/logs/2/)

[Next →](https://developers.cloudflare.com/changelog/product/logs/2/)
