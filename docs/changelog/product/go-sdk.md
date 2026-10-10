---
url: https://developers.cloudflare.com/changelog/product/go-sdk/
title: Go SDK Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:07.138687+00:00
---

# Go SDK Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/go-sdk/

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

Apr 30, 2026

## [Go SDK v7.0.0 Released](https://developers.cloudflare.com/changelog/post/2026-04-30-go-sdk-v7.0.0/)

[SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)[Go SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)

Full Changelog: [v6.10.0...v7.0.0 ↗︎](https://github.com/cloudflare/cloudflare-go/compare/v6.10.0...v7.0.0)

This is a major version release that includes breaking changes to three packages: `ai_search`, `email_security`, and `workers`. These changes reflect upstream API specification updates that improve type correctness and consistency.

**Please ensure you read through the list of changes below before moving to this version** \- this will help you understand any down or upstream issues it may cause to your environments.

#### Breaking Changes

See the [v7.0.0 Migration Guide ↗︎](https://github.com/cloudflare/cloudflare-go/blob/main/docs/migration-guides/v7.0.0-migration-guide.md) for before/after code examples and actions needed for each change.

#### AI Search - SearchForAgents Metadata Removed

The `SearchForAgents` nested type has been removed from all instance metadata structs. This field is no longer part of the API specification.

**Removed Types:**

  * `InstanceNewResponseMetadataSearchForAgents`
  * `InstanceUpdateResponseMetadataSearchForAgents`
  * `InstanceListResponseMetadataSearchForAgents`
  * `InstanceDeleteResponseMetadataSearchForAgents`
  * `InstanceReadResponseMetadataSearchForAgents`
  * `InstanceNewParamsMetadataSearchForAgents`
  * `InstanceUpdateParamsMetadataSearchForAgents`
  * `NamespaceInstanceNewResponseMetadataSearchForAgents`
  * `NamespaceInstanceUpdateResponseMetadataSearchForAgents`
  * `NamespaceInstanceListResponseMetadataSearchForAgents`
  * `NamespaceInstanceDeleteResponseMetadataSearchForAgents`
  * `NamespaceInstanceReadResponseMetadataSearchForAgents`
  * `NamespaceInstanceNewParamsMetadataSearchForAgents`
  * `NamespaceInstanceUpdateParamsMetadataSearchForAgents`



#### Email Security - Path Parameter Type Changes

Multiple Email Security settings sub-resources have changed their path parameter types from `int64` to `string`:

  * `AllowPolicies` (`policyID int64` -> `policyID string`)
  * `BlockSenders` (`patternID int64` -> `patternID string`)
  * `Domains` (`domainID int64` -> `domainID string`)
  * `ImpersonationRegistry` (`displayNameID int64` -> `impersonationRegistryID string`)
  * `TrustedDomains` (`trustedDomainID int64` -> `trustedDomainID string`)



#### Email Security - Investigate Parameter Rename

The `Investigate.Get`, `Investigate.Move.New`, and `Investigate.Reclassify.New` methods now use `investigateID` instead of `postfixID` as the path parameter name.

#### Email Security - Domains BulkDelete Method Removed

The `SettingDomainService.BulkDelete` method and its associated types have been removed:

  * `SettingDomainBulkDeleteResponse`
  * `SettingDomainBulkDeleteParams`



#### Email Security - TrustedDomains Return Type Change

`SettingTrustedDomainService.New` now returns `*SettingTrustedDomainNewResponse` instead of `*SettingTrustedDomainNewResponseUnion`.

#### Email Security - Investigate.Move Return Type Change

`InvestigateMoveService.New` now returns `*pagination.SinglePage[InvestigateMoveNewResponse]` instead of `*[]InvestigateMoveNewResponse`.

#### Workers - Observability Telemetry Filter Restructuring

The observability telemetry filter parameter types have been restructured to support nested filter groups. New discriminated union types replace the previous flat filter arrays:

  * `ObservabilityTelemetryKeysParams.Filters` now accepts `FiltersObjectFilterUnion` (was `[]interface\{\}`)
  * `ObservabilityTelemetryQueryParams.Parameters.Filters` now accepts `FiltersObjectFilterUnion`
  * `ObservabilityTelemetryValuesParams.Filters` now accepts `FiltersObjectFilterUnion`



New types include `FiltersObjectFiltersObject` (for group filters with `FilterCombination`) and `FiltersWorkersObservabilityFilterLeaf` (for leaf filters with typed `Operation`, `Type`, and `Value` fields).

#### Features

#### Organizations - Audit Logs (`client.Organizations.Logs.Audit`)

**NEW SERVICE:** Query organization audit logs with cursor-based pagination.

  * `List()` \- Retrieve audit logs



#### Browser Rendering (`client.BrowserRendering`)

  * `client.BrowserRendering.Devtools.Browser.Targets.Close()` \- Close a specific browser target (tab, page) by ID



#### Queues (`client.Queues`)

  * `client.Queues.GetMetrics()` \- Retrieve queue metrics for a specific queue



#### AI Search (`client.AISearch`)

  * Added `WaitForCompletion` parameter to `NamespaceInstanceItemNewOrUpdateParams` and `NamespaceInstanceItemSyncParams` for synchronous indexing confirmation



#### Bug Fixes

  * **Magic Transit** : `ConnectorService.List` parameter name corrected from `query` to `params` (non-functional, affects generated documentation only)



#### Deprecations

None in this release.

#### Get started

  * [Download Go SDK v7.0.0 ↗︎](https://github.com/cloudflare/cloudflare-go/releases/tag/v7.0.0)
  * [Go SDK documentation ↗︎](https://developers.cloudflare.com/api/sdks/go/)
  * [Migration Guide ↗︎](https://github.com/cloudflare/cloudflare-go/blob/main/docs/migration-guides/v7.0.0-migration-guide.md)



Apr 23, 2026

## [Go SDK v6.10.0 Released](https://developers.cloudflare.com/changelog/post/2026-04-23-go-sdk-v6.10.0/)

[SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)[Go SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)

#### v6.10.0

In this release, you'll see a number of breaking changes. This is primarily due to changes in OpenAPI definitions, which our libraries are based off of, and codegen updates that we rely on to read those OpenAPI definitions and produce our SDK libraries.

**Please ensure you read through the list of changes below before moving to this version** \- this will help you understand any down or upstream issues it may cause to your environments.

#### Breaking Changes

See the [v6.10.0 Migration Guide ↗︎](https://github.com/cloudflare/cloudflare-go/blob/main/MIGRATION_GUIDE.md) for before/after code examples and actions needed for each change.

#### Abuse Reports - Registrar WHOIS Report Field Removals

Several fields have been removed from `AbuseReportNewParamsBodyAbuseReportsRegistrarWhoisReportRegWhoRequest`:

  * `RegWhoGoodFaithAffirmation`
  * `RegWhoLawfulProcessingAgreement`
  * `RegWhoLegalBasis`
  * `RegWhoRequestType`
  * `RegWhoRequestedDataElements`



#### AI Search - Instance Params Restructured

The `InstanceNewParams` and `InstanceUpdateParams` types have been significantly restructured. Many fields have been moved or removed:

  * `InstanceNewParams.TokenID`, `Type`, `CreatedFromAISearchWizard`, `WorkerDomain` removed
  * `InstanceUpdateParams` — most configuration fields removed (including `IndexMethod`, `IndexingOptions`, `MaxNumResults`, `Metadata`, `Paused`, `PublicEndpointParams`, `Reranking`, `RerankingModel`, `RetrievalOptions`, `RewriteModel`, `RewriteQuery`, `ScoreThreshold`, `SourceParams`, `Summarization`, `SummarizationModel`, `SystemPromptAISearch`, `SystemPromptIndexSummarization`, `SystemPromptRewriteQuery`, `TokenID`, `CreatedFromAISearchWizard`, `WorkerDomain`)
  * `InstanceSearchParams.Messages` field removed along with `InstanceSearchParamsMessage` and `InstanceSearchParamsMessagesRole` types



#### AI Search - InstanceItem Service Removed

The `InstanceItemService` type has been removed. The items sub-resource at `client.AISearch.Instances.Items` no longer exists in the non-namespace path. Use `client.AISearch.Namespaces.Instances.Items` instead.

#### AI Search - Token Types Removed

The following types have been removed from the `ai_search` package:

  * `TokenDeleteResponse`
  * `TokenListParams` (and associated `TokenListParamsOrderBy`, `TokenListParamsOrderByDirection`)



#### Email Security - Investigate Move Return Type Change

The `Investigate.Move.New()` method now returns a raw slice instead of a paginated wrapper:

  * `New()` returns `*[]InvestigateMoveNewResponse` instead of `*pagination.SinglePage[InvestigateMoveNewResponse]`
  * `NewAutoPaging()` method removed



#### Hyperdrive - Config Params Restructured

The `ConfigEditParams` type lost its `MTLS` and `Name` fields. The `HyperdriveMTLSParam` type lost `MTLS` and `Host` fields. The `Host` field on origin config changed from `param.Field[string]` to a plain `string`.

#### IAM - UserGroupMember Params and Return Types Changed

The `UserGroupMemberNewParams` struct has been restructured and the `New()` method now returns a paginated response:

  * `UserGroupMemberNewParams.Body` renamed to `UserGroupMemberNewParams.Members`
  * `UserGroupMemberNewParamsBody` renamed to `UserGroupMemberNewParamsMember`
  * `UserGroupMemberUpdateParams.Body` renamed to `UserGroupMemberUpdateParams.Members`
  * `UserGroupMemberUpdateParamsBody` renamed to `UserGroupMemberUpdateParamsMember`
  * `UserGroups.Members.New()` returns `*pagination.SinglePage[UserGroupMemberNewResponse]` instead of `*UserGroupMemberNewResponse`



#### IAM - UserGroup List Direction Type Changed

The `UserGroupListParams.Direction` field changed from `param.Field[string]` to `param.Field[UserGroupListParamsDirection]` (typed enum with `asc`/`desc` values).

#### Pipelines - Delete Methods Now Return Typed Responses

Several delete methods across Pipelines now return typed responses instead of bare error:

  * `Pipelines.DeleteV1()` returns `(*PipelineDeleteV1Response, error)` instead of `error`
  * `Pipelines.Sinks.Delete()` returns `(*SinkDeleteResponse, error)` instead of `error`
  * `Pipelines.Streams.Delete()` returns `(*StreamDeleteResponse, error)` instead of `error`



#### Queues - Message Response Types Removed

The following response envelope types have been removed:

  * `MessageBulkPushResponseSuccess`
  * `MessagePushResponseSuccess`
  * `MessageAckResponse` fields `RetryCount` and `Warnings` removed



#### Secrets Store - Pagination Wrapper Removal and Type Changes

Methods now return direct types instead of `SinglePage` wrappers, and several internal types have been removed. Associated `AutoPaging` methods have also been removed:

  * `Stores.New()` returns `*StoreNewResponse` instead of `*pagination.SinglePage[StoreNewResponse]`
  * `Stores.NewAutoPaging()` method removed
  * `Stores.Secrets.BulkDelete()` returns `*StoreSecretBulkDeleteResponse` instead of `*pagination.SinglePage[StoreSecretBulkDeleteResponse]`
  * `Stores.Secrets.BulkDeleteAutoPaging()` method removed
  * Removed types: `StoreDeleteResponse`, `StoreDeleteResponseEnvelopeResultInfo`, `StoreSecretDeleteResponse`, `StoreSecretDeleteResponseStatus`, `StoreSecretBulkDeleteResponse` (old shape), `StoreSecretBulkDeleteResponseStatus`, `StoreSecretDeleteResponseEnvelopeResultInfo`
  * `StoreNewParams` restructured (old `StoreNewParamsBody` removed)
  * `StoreSecretBulkDeleteParams` restructured



#### Stream - AudioTracks Return Type Change

The `AudioTracks.Get()` method now returns a dedicated response type instead of a paginated list. The `GetAutoPaging()` method has been removed:

  * `Get()` returns `*AudioTrackGetResponse` instead of `*pagination.SinglePage[Audio]`
  * `GetAutoPaging()` method removed



#### Stream - Clip Type Removal and Return Type Change

The `Clip.New()` method now returns the shared `Video` type. The following types have been entirely removed:

  * `Clip`, `ClipPlayback`, `ClipStatus`, `ClipWatermark`



#### Stream - Copy and Clip Params Field Removals

  * `ClipNewParams.MaxDurationSeconds`, `ThumbnailTimestampPct`, `Watermark` removed
  * `CopyNewParams.ThumbnailTimestampPct`, `Watermark` removed



#### Stream - Download and Webhook Changes

  * `DownloadNewResponseStatus` type removed
  * `WebhookUpdateResponse` and `WebhookGetResponse` changed from `interface{}` type aliases to full struct types



#### Zero Trust - Access AI Control MCP Portal Union Types Removed

The following union interface types have been removed:

  * `AccessAIControlMcpPortalListResponseServersUpdatedPromptsUnion`
  * `AccessAIControlMcpPortalListResponseServersUpdatedToolsUnion`
  * `AccessAIControlMcpPortalReadResponseServersUpdatedPromptsUnion`
  * `AccessAIControlMcpPortalReadResponseServersUpdatedToolsUnion`



#### Features

#### Vulnerability Scanner (`client.VulnerabilityScanner`)

**NEW SERVICE:** Full vulnerability scanning management

  * **CredentialSets** \- CRUD for credential sets (`New`, `Update`, `List`, `Delete`, `Edit`, `Get`)
  * **Credentials** \- Manage credentials within sets (`New`, `Update`, `List`, `Delete`, `Edit`, `Get`)
  * **Scans** \- Create and manage vulnerability scans (`New`, `List`, `Get`)
  * **TargetEnvironments** \- Manage scan target environments (`New`, `Update`, `List`, `Delete`, `Edit`, `Get`)



#### AI Search - Namespaces (`client.AISearch.Namespaces`)

**NEW SERVICE:** Namespace-scoped AI Search management

  * `New()`, `Update()`, `List()`, `Delete()`, `ChatCompletions()`, `Read()`, `Search()`
  * **Instances** \- Namespace-scoped instances (`New`, `Update`, `List`, `Delete`, `ChatCompletions`, `Read`, `Search`, `Stats`)
  * **Jobs** \- Instance job management (`New`, `Update`, `List`, `Get`, `Logs`)
  * **Items** \- Instance item management (`List`, `Delete`, `Chunks`, `NewOrUpdate`, `Download`, `Get`, `Logs`, `Sync`, `Upload`)



#### Browser Rendering - Devtools (`client.BrowserRendering.Devtools`)

**NEW SERVICE:** DevTools protocol browser control

  * **Session** \- List and get devtools sessions
  * **Browser** \- Browser lifecycle management (`New`, `Delete`, `Connect`, `Launch`, `Protocol`, `Version`)
  * **Page** \- Get page by target ID
  * **Targets** \- Manage browser targets (`New`, `List`, `Activate`, `Get`)



#### Registrar (`client.Registrar`)

**NEW:** Domain check and search endpoints

  * `Check()` \- `POST /accounts/{account_id}/registrar/domain-check`
  * `Search()` \- `GET /accounts/{account_id}/registrar/domain-search`



**NEW:** Registration management (`client.Registrar.Registrations`)

  * `New()`, `List()`, `Edit()`, `Get()`
  * `RegistrationStatus.Get()` \- Get registration workflow status
  * `UpdateStatus.Get()` \- Get update workflow status



#### Cache - Origin Cloud Regions (`client.Cache.OriginCloudRegions`)

**NEW SERVICE:** Manage origin cloud region configurations

  * `New()`, `List()`, `Delete()`, `BulkDelete()`, `BulkEdit()`, `Edit()`, `Get()`, `SupportedRegions()`



#### Zero Trust - DLP Settings (`client.ZeroTrust.DLP.Settings`)

**NEW SERVICE:** DLP settings management

  * `Update()`, `Delete()`, `Edit()`, `Get()`



#### Radar

  * `AgentReadiness.Summary()` \- Agent readiness summary by dimension
  * `AI.MarkdownForAgents.Summary()` \- Markdown-for-agents summary
  * `AI.MarkdownForAgents.Timeseries()` \- Markdown-for-agents timeseries



#### IAM (`client.IAM`)

  * `UserGroups.Members.Get()` \- Get details of a specific member in a user group
  * `UserGroups.Members.NewAutoPaging()` \- Auto-paging variant for adding members
  * `UserGroups.NewParams.Policies` changed from required to optional



#### Bot Management

  * `ContentBotsProtection` field added to `BotFightModeConfiguration` and `SubscriptionConfiguration` (`block`/`disabled`)



#### Deprecations

None in this release.

#### Get started

  * [Download Go SDK v6.10.0 ↗︎](https://github.com/cloudflare/cloudflare-go/releases/tag/v6.10.0)
  * [Go SDK documentation ↗︎](https://developers.cloudflare.com/api/sdks/go/)
  * [Migration Guide ↗︎](https://github.com/cloudflare/cloudflare-go/blob/main/MIGRATION_GUIDE.md)


