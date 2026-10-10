---
url: https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-python-v5.0.0/
title: Cloudflare Python SDK v5.0.0 Released \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:39.251461+00:00
---

# Cloudflare Python SDK v5.0.0 Released · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-python-v5.0.0/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 30, 2026

## Cloudflare Python SDK v5.0.0 Released

[SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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


