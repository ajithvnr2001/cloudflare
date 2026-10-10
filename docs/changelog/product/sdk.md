---
url: https://developers.cloudflare.com/changelog/product/sdk/
title: SDK Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:04.719814+00:00
---

# SDK Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/sdk/

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



Apr 30, 2026

## [Cloudflare Python SDK v5.0.0 Released](https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-python-v5.0.0/)

[SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)

Full Changelog: [v4.3.1...v5.0.0 ↗︎](https://github.com/cloudflare/cloudflare-python/compare/v4.3.1...v5.0.0)

This is a major release of the Cloudflare Python SDK. It drops support for Python 3.8, adds 11 new API services, introduces optional aiohttp backend support for improved async concurrency, and includes hundreds of type and method updates across the entire API surface.

**Please review the breaking changes below before upgrading.** A migration guide is available at [v5.0.0 Migration Guide ↗︎](https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md).

#### Breaking Changes

  * **Python 3.8 is no longer supported.** The minimum required version is now Python 3.9.
  * **`typing-extensions` minimum version bumped** from `>=4.10` to `>=4.14`.



The following resources have breaking changes. See the [v5.0.0 Migration Guide ↗︎](https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md) for detailed migration instructions.

  * `abusereports`
  * `acm.totaltls`
  * `apigateway.configurations`
  * `cloudforceone.threatevents`
  * `d1.database`
  * `intel.indicatorfeeds`
  * `logpush.edge`
  * `origintlsclientauth.hostnames`
  * `queues.consumers`
  * `radar.bgp`
  * `rulesets.rules`
  * `schemavalidation.schemas`
  * `snippets`
  * `zerotrust.dlp`
  * `zerotrust.networks`



#### Features

#### aiohttp Backend Support

The async client now supports an optional `aiohttp` HTTP backend for improved concurrency performance. Install with `pip install cloudflare[aiohttp]` and use `DefaultAioHttpClient()` as the `http_client` parameter.

#### Python 3.13 and 3.14 Support

Python 3.13 and 3.14 are now tested and supported.

#### New Services

The following top-level resources are new in this release:

Resource | Client Path | Description  
---|---|---  
AI Search | `aisearch` | AI-powered search capabilities  
Connectivity | `connectivity` | Connectivity testing and diagnostics  
Email Sending | `email_sending` | Email send and send_raw endpoints  
Fraud | `fraud` | Fraud detection and prevention  
Google Tag Gateway | `google_tag_gateway` | Google Tag Gateway management  
Organizations | `organizations` | Organization audit logs and management  
R2 Data Catalog | `r2_data_catalog` | R2 Data Catalog operations  
Realtime Kit | `realtime_kit` | Realtime communication (Calls/TURN)  
Resource Tagging | `resource_tagging` | Resource tagging and labeling  
Token Validation | `token_validation` | Token validation configuration and rules  
Vulnerability Scanner | `vulnerability_scanner` | Vulnerability scanning, credential sets, and target environments  
  
#### New Endpoints on Existing Services

  * **api_gateway** : Labels endpoints
  * **billing** : Billable usage PayGo endpoint
  * **brand_protection** : v2 endpoints
  * **browser_rendering** : DevTools methods
  * **cache** : Origin cloud regions resource
  * **custom_origin_trust_store** : Custom origin trust store
  * **dns** : `dns_records/usage` endpoints
  * **email_security** : Phishguard reports endpoint
  * **iam** : User groups and user group members resources
  * **radar** : Botnet Threat Feed and Post-Quantum endpoints
  * **workers** : Observability Destinations resources
  * **zero_trust** : Access Users, DEX rules, Device IP Profile, Device Subnet, WARP Connector connections and failover, WARP Subnet, Gateway PAC files
  * **zones** : Zone environments endpoints



#### Bug Fixes

  * Fixed `polymorphic_serialization` parameter in `model_dump` overrides
  * Added `BaseModel` base to response `SchemaFieldStruct`/`SchemaFieldList` stubs in Pipelines
  * Added missing `model_rebuild`/`update_forward_refs` for `SharedEntryCustomEntry` classes in DLP
  * Made `RunQueryParametersNeedleValue` a `BaseModel` with `arbitrary_types_allowed` in Workers
  * Removed duplicate `notification_url` field in webhook response types for Stream
  * Resolved pre-existing codegen type errors
  * Fixed `type: ignore[call-arg]` placement for mypy compatibility in Radar



#### Deprecations

Resources with `@deprecated` annotations on some methods include: `accounts`, `addressing`, `ai-gateway`, `aisearch`, `api-gateway`, `billing`, `cloudforce-one`, `dns`, `email-routing`, `email-security`, `filters`, `firewall`, `images`, `intel`, `kv`, `logpush`, `origin-tls-client-auth`, `pages`, `pipelines`, `radar`, `rate-limits`, `registrar`, `rulesets`, `ssl`, `user`, `workers`, `workers-for-platforms`, `zero-trust`, `zones`

#### Get started

  * [Download Python SDK v5.0.0 ↗︎](https://github.com/cloudflare/cloudflare-python/releases/tag/v5.0.0)
  * [Python SDK documentation ↗︎](https://developers.cloudflare.com/api/sdks/python/)
  * [Migration Guide ↗︎](https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md)



Apr 30, 2026

## [Cloudflare TypeScript SDK v6.0.0 Released](https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-typescript-v6.0.0/)

[SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)

Full Changelog: [v6.0.0-beta.2...v6.0.0 ↗︎](https://github.com/cloudflare/cloudflare-typescript/compare/v6.0.0-beta.2...v6.0.0)

This is a major version release of the Cloudflare TypeScript SDK. It includes 11 entirely new top-level API resources, new sub-resources and methods across 50+ existing resources, SDK infrastructure improvements, and breaking changes to the generated API surface from the v5.x line.

**Please ensure you read through the list of changes below before moving to this version** \- this will help you understand any down or upstream issues it may cause to your environments.

#### Breaking Changes

#### SDK Infrastructure

  * **Retry-After handling changed** : The SDK now respects any server-specified `Retry-After` value for rate-limited requests. Previously, values over 60 seconds were ignored and a default backoff was used instead.
  * **Empty response handling** : Responses with `content-length: 0` now return `undefined` instead of attempting to parse the body.
  * **Environment variable reading** : Empty string env vars (for example, `CLOUDFLARE_API_TOKEN=""`) are now treated as unset.
  * **Path query parameter merging** : URL search params embedded in endpoint paths are now extracted and merged into the query object.



#### Removed Endpoints (17)

17 HTTP endpoints were removed from the SDK, affecting `abuse-reports`, `cloudforce-one`, `dlp/profiles/predefined`, `email-security/investigate`, `email-security/settings`, and `intel/ip-list`.

#### Method Signature Changes

  * `client.ai.toMarkdown.transform(file, \{ ...params \})` -> `client.ai.toMarkdown.transform(\{ ...params \})` \-- `file` moved from positional arg into params body
  * `client.radar.ai.toMarkdown.create(body, \{ ...params \})` -> `client.radar.ai.toMarkdown.create(\{ ...params \})` \-- `body` moved from positional arg into params
  * `client.abuseReports.create(reportType, \{ ...params \})` -> `client.abuseReports.create(reportParam, \{ ...params \})` \-- positional arg renamed
  * `client.iam.userGroups.members.create(userGroupId, [ ...body ])` -> `client.iam.userGroups.members.create(userGroupId, [ ...members ])` \-- body array param renamed



#### Renamed Client Paths

  * `client.originTLSClientAuth.hostnames.certificates` -> `client.originTLSClientAuth.zoneCertificates`
  * `client.radar.netflows` -> `client.radar.netFlows` (casing change)



#### Return Type Changes (179)

  * **133 methods now return`null`** instead of a typed response object. This primarily affects delete operations across `accounts`, `cache`, `d1`, `filters`, `firewall`, `hyperdrive`, `iam`, `kv`, `logpush`, `logs`, `r2`, `stream`, `workers`, `zero-trust`, `zones`, and others.
  * **17 methods changed pagination type** (for example, `KeysCursorPaginationAfter` -> `KeysCursorLimitPagination`).
  * **29 methods changed to a different named type** (for example, `CloudflaredCreateResponse` -> `CloudflareTunnel`).



#### Removed Types (43)

24 shared types removed from root namespace (`ASN`, `AuditLog`, `Member`, `Permission`, `Role`, `Subscription`, `Token`, etc.). 19 response types consolidated or renamed.

#### Resource Restructuring

19 resources were restructured from single files to directories. Public API client paths are unchanged, but deep imports may break.

#### New Top-Level Resources

11 entirely new resources added to the client:

Resource | Client Path | Methods | Description  
---|---|---|---  
AI Search | `client.aiSearch` | 46 | Instances, namespaces, tokens, and items  
Connectivity | `client.connectivity` | 5 | Directory service APIs  
Email Sending | `client.emailSending` | 7 | Send and send_raw endpoints  
Fraud | `client.fraud` | 2 | Fraud detection API  
Google Tag Gateway | `client.googleTagGateway` | 2 | Google Tag Gateway management  
Organizations | `client.organizations` | 8 | Organization profiles and audit logs  
R2 Data Catalog | `client.r2DataCatalog` | 11 | R2 Data Catalog routes  
Realtime Kit | `client.realtimeKit` | 54 | Realtime Kit APIs  
Resource Tagging | `client.resourceTagging` | 9 | Resource tagging routes  
Token Validation | `client.tokenValidation` | 13 | Token validation rules  
Vulnerability Scanner | `client.vulnerabilityScanner` | 21 | Vulnerability scanning  
  
#### New Sub-Resources on Existing Resources

  * **browser-rendering** : `crawl`, `devtools` \- Crawl endpoints and DevTools methods
  * **cache** : `origin-cloud-regions` \- Origin cloud regions resource
  * **dns** : `usage` \- DNS records usage endpoints
  * **d1** : `time-travel` \- Time travel get_bookmark and restore
  * **email-security** : `phishguard` \- Phishguard reports endpoint
  * **pipelines** : `sinks`, `streams` \- Pipelines restructure
  * **radar** : `agent-readiness`, `geolocations`, `post-quantum` \- New analytics endpoints
  * **workers** : `observability` \- Observability destinations
  * **zones** : `environments` \- Zone environments endpoints
  * **api-gateway** : `labels` \- Labels endpoints
  * **brand-protection** : `v2` \- V2 endpoints
  * **alerting** : `silences` \- Alert silencing API
  * **billing** : `usage` \- Billable usage PayGo endpoint
  * **iam** : `sso` \- SSO Connectors resource
  * **queues** : `getMetrics` method - Queues metrics endpoint
  * **registrar** : `registration-status`, `update-status` \- Registrar API convergence
  * **zero-trust** : DLP settings, DEX rules, Access Users, WARP Connector, WARP Subnets, Gateway PAC files, Gateway tenants



#### Bug Fixes

  * Resolved type errors from codegen overwriting manual fixes
  * Fixed `post()` usage for to-markdown endpoints to resolve async type error
  * Added least-privilege permissions to all workflow jobs
  * Reverted erroneous removal of rulesets resource methods and types
  * Resolved prettier formatting errors in codegen output



#### Deprecations

The following resources now include `@deprecated` annotations on some methods:

`accounts`, `addressing`, `ai-gateway`, `aisearch`, `api-gateway`, `billing`, `cloudforce-one`, `custom-nameservers`, `dns`, `email-routing`, `email-security`, `filters`, `firewall`, `images`, `intel`, `keyless-certificates`, `kv`, `logpush`, `origin-tls-client-auth`, `page-shield`, `pages`, `pipelines`, `radar`, `rate-limits`, `registrar`, `rulesets`, `ssl`, `user`, `workers`, `workers-for-platforms`, `zero-trust`, `zones`

#### Get started

  * [Download TypeScript SDK v6.0.0 ↗︎](https://github.com/cloudflare/cloudflare-typescript/releases/tag/v6.0.0)
  * [TypeScript SDK documentation ↗︎](https://developers.cloudflare.com/api/sdks/typescript/)
  * [Full Changelog ↗︎](https://github.com/cloudflare/cloudflare-typescript/blob/main/CHANGELOG.md)



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



Feb 13, 2026

## [Cloudflare Python SDK v5.0.0-beta.1 now available](https://developers.cloudflare.com/changelog/post/2026-02-13-cloudflare-python-v5.0.0-beta.1/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)

> **Disclaimer:** Please note that v5.0.0-beta.1 is in Beta and we are still testing it for stability.

Full Changelog: [v4.3.1...v5.0.0-beta.1 ↗︎](https://github.com/cloudflare/cloudflare-python/compare/v4.3.1...v5.0.0-beta.1)

In this release, you'll see a large number of breaking changes. This is primarily due to a change in OpenAPI definitions, which our libraries are based off of, and codegen updates that we rely on to read those OpenAPI definitions and produce our SDK libraries. As the codegen is always evolving and improving, so are our code bases.

There may be changes that are not captured in this changelog. Feel free to open an issue to report any inaccuracies, and we will make sure it gets into the changelog before the v5.0.0 release.

Most of the breaking changes below are caused by improvements to the accuracy of the base OpenAPI schemas, which sometimes translates to breaking changes in downstream clients that depend on those schemas.

Please ensure you read through the list of changes below and the migration guide before moving to this version - this will help you understand any down or upstream issues it may cause to your environments.

#### Breaking Changes

**The following resources have breaking changes. See the[v5 Migration Guide ↗︎](https://github.com/cloudflare/cloudflare-python/blob/main/docs/v5-migration-guide.md) for detailed migration instructions.**

  * `abusereports`
  * `acm.totaltls`
  * `apigateway.configurations`
  * `cloudforceone.threatevents`
  * `d1.database`
  * `intel.indicatorfeeds`
  * `logpush.edge`
  * `origintlsclientauth.hostnames`
  * `queues.consumers`
  * `radar.bgp`
  * `rulesets.rules`
  * `schemavalidation.schemas`
  * `snippets`
  * `zerotrust.dlp`
  * `zerotrust.networks`



#### Features

#### New API Resources

  * `abusereports` \- Abuse report management
  * `abusereports.mitigations` \- Abuse report mitigation actions
  * `ai.tomarkdown` \- AI-powered markdown conversion
  * `aigateway.dynamicrouting` \- AI Gateway dynamic routing configuration
  * `aigateway.providerconfigs` \- AI Gateway provider configurations
  * `aisearch` \- AI-powered search functionality
  * `aisearch.instances` \- AI Search instance management
  * `aisearch.tokens` \- AI Search authentication tokens
  * `alerting.silences` \- Alert silence management
  * `brandprotection.logomatches` \- Brand protection logo match detection
  * `brandprotection.logos` \- Brand protection logo management
  * `brandprotection.matches` \- Brand protection match results
  * `brandprotection.queries` \- Brand protection query management
  * `cloudforceone.binarystorage` \- CloudForce One binary storage
  * `connectivity.directory` \- Connectivity directory services
  * `d1.database` \- D1 database management
  * `diagnostics.endpointhealthchecks` \- Endpoint health check diagnostics
  * `fraud` \- Fraud detection and prevention
  * `iam.sso` \- IAM Single Sign-On configuration
  * `loadbalancers.monitorgroups` \- Load balancer monitor groups
  * `organizations` \- Organization management
  * `organizations.organizationprofile` \- Organization profile settings
  * `origintlsclientauth.hostnamecertificates` \- Origin TLS client auth hostname certificates
  * `origintlsclientauth.hostnames` \- Origin TLS client auth hostnames
  * `origintlsclientauth.zonecertificates` \- Origin TLS client auth zone certificates
  * `pipelines` \- Data pipeline management
  * `pipelines.sinks` \- Pipeline sink configurations
  * `pipelines.streams` \- Pipeline stream configurations
  * `queues.subscriptions` \- Queue subscription management
  * `r2datacatalog` \- R2 Data Catalog integration
  * `r2datacatalog.credentials` \- R2 Data Catalog credentials
  * `r2datacatalog.maintenanceconfigs` \- R2 Data Catalog maintenance configurations
  * `r2datacatalog.namespaces` \- R2 Data Catalog namespaces
  * `radar.bots` \- Radar bot analytics
  * `radar.ct` \- Radar certificate transparency data
  * `radar.geolocations` \- Radar geolocation data
  * `realtimekit.activesession` \- Real-time Kit active session management
  * `realtimekit.analytics` \- Real-time Kit analytics
  * `realtimekit.apps` \- Real-time Kit application management
  * `realtimekit.livestreams` \- Real-time Kit live streaming
  * `realtimekit.meetings` \- Real-time Kit meeting management
  * `realtimekit.presets` \- Real-time Kit preset configurations
  * `realtimekit.recordings` \- Real-time Kit recording management
  * `realtimekit.sessions` \- Real-time Kit session management
  * `realtimekit.webhooks` \- Real-time Kit webhook configurations
  * `tokenvalidation.configuration` \- Token validation configuration
  * `tokenvalidation.rules` \- Token validation rules
  * `workers.beta` \- Workers beta features



#### New Endpoints (Existing Resources)

#### `acm.totaltls`

  * `edit()`
  * `update()`



#### `cloudforceone.threatevents`

  * `list()`



#### `contentscanning`

  * `create()`
  * `get()`
  * `update()`



#### `dns.records`

  * `scan_list()`
  * `scan_review()`
  * `scan_trigger()`



#### `intel.indicatorfeeds`

  * `create()`
  * `delete()`
  * `list()`



#### `leakedcredentialchecks.detections`

  * `get()`



#### `queues.consumers`

  * `list()`



#### `radar.ai`

  * `summary()`
  * `timeseries()`
  * `timeseries_groups()`



#### `radar.bgp`

  * `changes()`
  * `snapshot()`



#### `workers.subdomains`

  * `delete()`



#### `zerotrust.networks`

  * `create()`
  * `delete()`
  * `edit()`
  * `get()`
  * `list()`



#### General Fixes and Improvements

#### Type System & Compatibility

  * **Type inference improvements** : Allow Pyright to properly infer TypedDict types within SequenceNotStr
  * **Type completeness** : Add missing types to method arguments and response models
  * **Pydantic compatibility** : Ensure compatibility with Pydantic versions prior to 2.8.0 when using additional fields



#### Request/Response Handling

  * **Multipart form data** : Correctly handle sending multipart/form-data requests with JSON data
  * **Header handling** : Do not send headers with default values set to omit
  * **GET request headers** : Don't send Content-Type header on GET requests
  * **Response body model accuracy** : Broad improvements to the correctness of models



#### Parsing & Data Processing

  * **Discriminated unions** : Correctly handle nested discriminated unions in response parsing
  * **Extra field types** : Parse extra field types correctly
  * **Empty metadata** : Ignore empty metadata fields during parsing
  * **Singularization rules** : Update resource name singularization rules for better consistency



Jan 20, 2026

## [Cloudflare Typescript SDK v6.0.0-beta.1 now available](https://developers.cloudflare.com/changelog/post/2026-01-20-cloudflare-typescript-v6.0.0-beta.1/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)

> **Disclaimer:** Please note that v6.0.0-beta.1 is in Beta and we are still testing it for stability.

Full Changelog: [v5.2.0...v6.0.0-beta.1 ↗︎](https://github.com/cloudflare/cloudflare-typescript/compare/v5.2.0...v6.0.0-beta.1)

In this release, you'll see a large number of breaking changes. This is primarily due to a change in OpenAPI definitions, which our libraries are based off of, and codegen updates that we rely on to read those OpenAPI definitions and produce our SDK libraries. As the codegen is always evolving and improving, so are our code bases.

Some breaking changes were introduced due to bug fixes, also listed below.

Please ensure you read through the list of changes below before moving to this version - this will help you understand any down or upstream issues it may cause to your environments.

* * *

#### Breaking Changes

#### Addressing - Parameter Requirements Changed

  * `BGPPrefixCreateParams.cidr`: optional → **required**
  * `PrefixCreateParams.asn`: `number | null` → `number`
  * `PrefixCreateParams.loa_document_id`: required → **optional**
  * `ServiceBindingCreateParams.cidr`: optional → **required**
  * `ServiceBindingCreateParams.service_id`: optional → **required**



#### API Gateway

  * `ConfigurationUpdateResponse` removed
  * `PublicSchema` → `OldPublicSchema`
  * `SchemaUpload` → `UserSchemaCreateResponse`
  * `ConfigurationUpdateParams.properties` removed; use `normalize`



#### CloudforceOne - Response Type Changes

  * `ThreatEventBulkCreateResponse`: `number` → complex object with counts and errors



#### D1 Database - Query Parameters

  * `DatabaseQueryParams`: simple interface → union type (`D1SingleQuery | MultipleQueries`)
  * `DatabaseRawParams`: same change
  * Supports batch queries via `batch` array



#### DNS Records - Type Renames (21 types)

All record type interfaces renamed from `*Record` to short names:

  * `RecordResponse.ARecord` → `RecordResponse.A`
  * `RecordResponse.AAAARecord` → `RecordResponse.AAAA`
  * `RecordResponse.CNAMERecord` → `RecordResponse.CNAME`
  * `RecordResponse.MXRecord` → `RecordResponse.MX`
  * `RecordResponse.NSRecord` → `RecordResponse.NS`
  * `RecordResponse.PTRRecord` → `RecordResponse.PTR`
  * `RecordResponse.TXTRecord` → `RecordResponse.TXT`
  * `RecordResponse.CAARecord` → `RecordResponse.CAA`
  * `RecordResponse.CERTRecord` → `RecordResponse.CERT`
  * `RecordResponse.DNSKEYRecord` → `RecordResponse.DNSKEY`
  * `RecordResponse.DSRecord` → `RecordResponse.DS`
  * `RecordResponse.HTTPSRecord` → `RecordResponse.HTTPS`
  * `RecordResponse.LOCRecord` → `RecordResponse.LOC`
  * `RecordResponse.NAPTRRecord` → `RecordResponse.NAPTR`
  * `RecordResponse.SMIMEARecord` → `RecordResponse.SMIMEA`
  * `RecordResponse.SRVRecord` → `RecordResponse.SRV`
  * `RecordResponse.SSHFPRecord` → `RecordResponse.SSHFP`
  * `RecordResponse.SVCBRecord` → `RecordResponse.SVCB`
  * `RecordResponse.TLSARecord` → `RecordResponse.TLSA`
  * `RecordResponse.URIRecord` → `RecordResponse.URI`
  * `RecordResponse.OpenpgpkeyRecord` → `RecordResponse.Openpgpkey`



#### IAM Resource Groups

  * `ResourceGroupCreateResponse.scope`: optional single → **required array**
  * `ResourceGroupCreateResponse.id`: optional → **required**



#### Origin CA Certificates - Parameter Requirements Changed

  * `OriginCACertificateCreateParams.csr`: optional → **required**
  * `OriginCACertificateCreateParams.hostnames`: optional → **required**
  * `OriginCACertificateCreateParams.request_type`: optional → **required**



#### Pages

  * Renamed: `DeploymentsSinglePage` → `DeploymentListResponsesV4PagePaginationArray`
  * Domain response fields: many optional → **required**



#### Pipelines - v0 to v1 Migration

  * Entire v0 API deprecated; use v1 methods (`createV1`, `listV1`, etc.)
  * New sub-resources: `Sinks`, `Streams`



#### R2

  * `EventNotificationUpdateParams.rules`: optional → **required**
  * Super Slurper: `bucket`, `secret` now required in source params



#### Radar

  * `dataSource`: `string` → typed enum (23 values)
  * `eventType`: `string` → typed enum (6 values)
  * V2 methods require `dimension` parameter (breaking signature change)



#### Resource Sharing

  * Removed: `status_message` field from all recipient response types



#### Schema Validation

  * Consolidated `SchemaCreateResponse`, `SchemaListResponse`, `SchemaEditResponse`, `SchemaGetResponse` → `PublicSchema`
  * Renamed: `SchemaListResponsesV4PagePaginationArray` → `PublicSchemasV4PagePaginationArray`



#### Spectrum

  * Renamed union members: `AppListResponse.UnionMember0` → `SpectrumConfigAppConfig`
  * Renamed union members: `AppListResponse.UnionMember1` → `SpectrumConfigPaygoAppConfig`



#### Workers

  * Removed: `WorkersBindingKindTailConsumer` type (all occurrences)
  * Renamed: `ScriptsSinglePage` → `ScriptListResponsesSinglePage`
  * Removed: `DeploymentsSinglePage`



#### Zero-Trust DLP

  * `datasets.create()`, `update()`, `get()` return types changed
  * `PredefinedGetResponse` union members renamed to `UnionMember0-5`



#### Zero-Trust Tunnels

  * Removed: `CloudflaredCreateResponse`, `CloudflaredListResponse`, `CloudflaredDeleteResponse`, `CloudflaredEditResponse`, `CloudflaredGetResponse`
  * Removed: `CloudflaredListResponsesV4PagePaginationArray`



* * *

#### Features

#### Abuse Reports (`client.abuseReports`)

  * **Reports** : `create`, `list`, `get`
  * **Mitigations** : sub-resource for abuse mitigations



#### AI Search (`client.aisearch`)

  * **Instances** : `create`, `update`, `list`, `delete`, `read`, `stats`
  * **Items** : `list`, `get`
  * **Jobs** : `create`, `list`, `get`, `logs`
  * **Tokens** : `create`, `update`, `list`, `delete`, `read`



#### Connectivity (`client.connectivity`)

  * **Directory Services** : `create`, `update`, `list`, `delete`, `get`
  * Supports IPv4, IPv6, dual-stack, and hostname configurations



#### Organizations (`client.organizations`)

  * **Organizations** : `create`, `update`, `list`, `delete`, `get`
  * **OrganizationProfile** : `update`, `get`
  * Hierarchical organization support with parent/child relationships



#### R2 Data Catalog (`client.r2DataCatalog`)

  * **Catalog** : `list`, `enable`, `disable`, `get`
  * **Credentials** : `create`
  * **MaintenanceConfigs** : `update`, `get`
  * **Namespaces** : `list`
  * **Tables** : `list`, maintenance config management
  * Apache Iceberg integration



#### Realtime Kit (`client.realtimeKit`)

  * **Apps** : `get`, `post`
  * **Meetings** : `create`, `get`, participant management
  * **Livestreams** : 10+ methods for streaming
  * **Recordings** : start, pause, stop, get
  * **Sessions** : transcripts, summaries, chat
  * **Webhooks** : full CRUD
  * **ActiveSession** : polls, kick participants
  * **Analytics** : organization analytics



#### Token Validation (`client.tokenValidation`)

  * **Configuration** : `create`, `list`, `delete`, `edit`, `get`
  * **Credentials** : `update`
  * **Rules** : `create`, `list`, `delete`, `bulkCreate`, `bulkEdit`, `edit`, `get`
  * JWT validation with RS256/384/512, PS256/384/512, ES256, ES384



#### Alerting Silences (`client.alerting.silences`)

  * `create`, `update`, `list`, `delete`, `get`



#### IAM SSO (`client.iam.sso`)

  * `create`, `update`, `list`, `delete`, `get`, `beginVerification`



#### Pipelines v1 (`client.pipelines`)

  * **Sinks** : `create`, `list`, `delete`, `get`
  * **Streams** : `create`, `update`, `list`, `delete`, `get`



#### Zero-Trust AI Controls / MCP (`client.zeroTrust.access.aiControls.mcp`)

  * **Portals** : `create`, `update`, `list`, `delete`, `read`
  * **Servers** : `create`, `update`, `list`, `delete`, `read`, `sync`



#### Accounts

  * `managed_by` field with `parent_org_id`, `parent_org_name`



#### Addressing LOA Documents

  * `auto_generated` field on `LOADocumentCreateResponse`



#### Addressing Prefixes

  * `delegate_loa_creation`, `irr_validation_state`, `ownership_validation_state`, `ownership_validation_token`, `rpki_validation_state`



#### AI

  * Added `toMarkdown.supported()` method to get all supported conversion formats



#### AI Gateway

  * `zdr` field added to all responses and params



#### Alerting

  * New alert type: `abuse_report_alert`
  * `type` field added to PolicyFilter



#### Browser Rendering

  * `ContentCreateParams`: refined to discriminated union (`Variant0 | Variant1`)
  * Split into URL-based and HTML-based parameter variants for better type safety



#### Client Certificates

  * `reactivate` parameter in edit



#### CloudforceOne

  * `ThreatEventCreateParams.indicatorType`: required → optional
  * `hasChildren` field added to all threat event response types
  * `datasetIds` query parameter on `AttackerListParams`, `CategoryListParams`, `TargetIndustryListParams`
  * `categoryUuid` field on `TagCreateResponse`
  * `indicators` array for multi-indicator support per event
  * `uuid` and `preserveUuid` fields for UUID preservation in bulk create
  * `format` query parameter (`'json' | 'stix2'`) on `ThreatEventListParams`
  * `createdAt`, `datasetId` fields on `ThreatEventEditParams`



#### Content Scanning

  * Added `create()`, `update()`, `get()` methods



#### Custom Pages

  * New page types: `basic_challenge`, `under_attack`, `waf_challenge`



#### D1

  * `served_by_colo` \- colo that handled query
  * `jurisdiction` \- `'eu' | 'fedramp'`
  * **Time Travel** (`client.d1.database.timeTravel`): `getBookmark()`, `restore()` \- point-in-time recovery



#### Email Security

  * New fields on `InvestigateListResponse`/`InvestigateGetResponse`: `envelope_from`, `envelope_to`, `postfix_id_outbound`, `replyto`
  * New detection classification: `'outbound_ndr'`
  * Enhanced `Finding` interface with `attachment`, `detection`, `field`, `portion`, `reason`, `score`
  * Added `cursor` query parameter to `InvestigateListParams`



#### Gateway Lists

  * New list types: `CATEGORY`, `LOCATION`, `DEVICE`



#### Intel

  * New issue type: `'configuration_suggestion'`
  * `payload` field: `unknown` → typed `Payload` interface with `detection_method`, `zone_tag`



#### Leaked Credential Checks

  * Added `detections.get()` method



#### Logpush

  * New datasets: `dex_application_tests`, `dex_device_state_events`, `ipsec_logs`, `warp_config_changes`, `warp_toggle_changes`



#### Load Balancers

  * `Monitor.port`: `number` → `number | null`
  * `Pool.load_shedding`: `LoadShedding` → `LoadShedding | null`
  * `Pool.origin_steering`: `OriginSteering` → `OriginSteering | null`



#### Magic Transit

  * `license_key` field on connectors
  * `provision_license` parameter for auto-provisioning
  * IPSec: `custom_remote_identities` with FQDN support
  * Snapshots: Bond interface, `probed_mtu` field



#### Pages

  * New response types: `ProjectCreateResponse`, `ProjectListResponse`, `ProjectEditResponse`, `ProjectGetResponse`
  * Deployment methods return specific response types instead of generic `Deployment`



#### Queues

  * Added `subscriptions.get()` method
  * Enhanced `SubscriptionGetResponse` with typed event source interfaces
  * New event source types: Images, KV, R2, Vectorize, Workers AI, Workers Builds, Workflows



#### R2

  * Sippy: new provider `s3` (S3-compatible endpoints)
  * Sippy: `bucketUrl` field for S3-compatible sources
  * Super Slurper: `keys` field on source response schemas (specify specific keys to migrate)
  * Super Slurper: `pathPrefix` field on source schemas
  * Super Slurper: `region` field on S3 source params



#### Radar

  * Added `geolocations.list()`, `geolocations.get()` methods
  * Added V2 dimension-based methods (`summaryV2`, `timeseriesGroupsV2`) to radar sub-resources



#### Resource Sharing

  * Added `terminal` boolean field to Resource Error interfaces



#### Rules

  * Added `id` field to `ItemDeleteParams.Item`



#### Rulesets

  * New buffering fields on `SetConfigRule`: `request_body_buffering`, `response_body_buffering`



#### Secrets Store

  * New scopes: `'dex'`, `'access'` (in addition to `'workers'`, `'ai_gateway'`)



#### SSL Certificate Packs

  * Response types now proper interfaces (was `unknown`)
  * Fields now required: `id`, `certificates`, `hosts`, `status`, `type`



#### Security Center

  * `payload` field: `unknown` → typed `Payload` interface with `detection_method`, `zone_tag`



#### Shared Types

  * Added: `CloudflareTunnelsV4PagePaginationArray` pagination class



#### Workers

  * Added `subdomains.delete()` method
  * `Worker.references` \- track external dependencies (domains, Durable Objects, queues)
  * `Worker.startup_time_ms` \- startup timing
  * `Script.observability` \- observability settings with logging
  * `Script.tag`, `Script.tags` \- immutable ID and tags
  * Placement: support for region, hostname, host-based placement
  * `tags`, `tail_consumers` now accept `| null`
  * Telemetry: `traces` field, `$containers` event info, `durableObjectId`, `transactionName`, `abr_level` fields



#### Workers for Platforms

  * `ScriptUpdateResponse`: new fields `entry_point`, `observability`, `tag`, `tags`
  * `placement` field now union of 4 variants (smart mode, region, hostname, host)
  * `tags`, `tail_consumers` now nullable
  * `TagUpdateParams.body` now accepts `null`



#### Workflows

  * `instance_retention`: `unknown` → typed `InstanceRetention` interface with `error_retention`, `success_retention`
  * New status option: `'restart'` added to `StatusEditParams.status`



#### Zero-Trust Devices

  * External emergency disconnect settings (4 new fields)
  * `antivirus` device posture check type
  * `os_version_extra` documentation improvements



#### Zones

  * New response types: `SubscriptionCreateResponse`, `SubscriptionUpdateResponse`, `SubscriptionGetResponse`



#### Zero-Trust Access Applications

  * New `ApplicationType` values: `'mcp'`, `'mcp_portal'`, `'proxy_endpoint'`
  * New destination type: `ViaMcpServerPortalDestination` for MCP server access



#### Zero-Trust Gateway

  * Added `rules.listTenant()` method



#### Zero-Trust Gateway - Proxy Endpoints

  * `ProxyEndpoint`: interface → discriminated union (`ZeroTrustGatewayProxyEndpointIP | ZeroTrustGatewayProxyEndpointIdentity`)
  * `ProxyEndpointCreateParams`: interface → union type
  * Added `kind` field: `'ip' | 'identity'`



#### Zero-Trust Tunnels

  * `WARPConnector*Response`: union type → interface



* * *

#### Deprecations

  * **API Gateway** : `UserSchemas`, `Settings`, `SchemaValidation` resources
  * **Audit Logs** : `auditLogId.not` (use `id.not`)
  * **CloudforceOne** : `ThreatEvents.get()`, `IndicatorTypes.list()`
  * **Devices** : `public_ip` field (use DEX API)
  * **Email Security** : `item_count` field in Move responses
  * **Pipelines** : v0 methods (use v1)
  * **Radar** : old `summary()` and `timeseriesGroups()` methods (use V2)
  * **Rulesets** : `disable_apps`, `mirage` fields
  * **WARP Connector** : `connections` field
  * **Workers** : `environment` parameter in Domains
  * **Zones** : `ResponseBuffering` page rule



* * *

#### Bug Fixes

  * **mcp:** correct code tool API endpoint ([599703c ↗︎](https://github.com/cloudflare/cloudflare-typescript/commit/599703c45672dc899455d74b124018efd4b75095))
  * **mcp:** return correct lines on typescript errors ([5d6f999 ↗︎](https://github.com/cloudflare/cloudflare-typescript/commit/5d6f9998ed9999aaa95e1bda8cf50929f3555cf1))
  * **organization_profile:** fix bad reference ([d84ea77 ↗︎](https://github.com/cloudflare/cloudflare-typescript/commit/d84ea77094400055c06554812b84c2f0c8d00cc4))
  * **schema_validation:** correctly reflect model to openapi mapping ([bb86151 ↗︎](https://github.com/cloudflare/cloudflare-typescript/commit/bb861516774b159d80e0f46a5f3abc5a4c9f9d49))
  * **workers:** fix tests ([2ee37f7 ↗︎](https://github.com/cloudflare/cloudflare-typescript/commit/2ee37f7adf5a4637d65f61fc225e135eec2579fc))



* * *

#### Documentation

  * Added deprecation notices with migration paths
  * **api_gateway:** deprecate API Shield Schema Validation resources ([8a4b20f ↗︎](https://github.com/cloudflare/cloudflare-typescript/commit/8a4b20f7a572422f74179fbdb4f1c4fb555e3e40))
  * Improved JSDoc examples across all resources
  * **workers:** expose subdomain delete documentation ([4f7cc1f ↗︎](https://github.com/cloudflare/cloudflare-typescript/commit/4f7cc1f2b8861a5b8abc193d287f78264a425062))


