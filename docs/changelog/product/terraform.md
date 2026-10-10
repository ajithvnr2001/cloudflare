---
url: https://developers.cloudflare.com/changelog/product/terraform/
title: Terraform Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:04.155742+00:00
---

# Terraform Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/terraform/

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

Jun 12, 2026

## [Terraform v5.20.0 now available](https://developers.cloudflare.com/changelog/post/2026-06-12-terraform-v5.20.0-provider/)

[Terraform](https://developers.cloudflare.com/terraform/)

Cloudflare's Terraform v5 Provider makes it easy for developers to manage their Cloudflare infrastructure using a configuration as code approach. It releases every [2-3 weeks ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774) to ensure that you can always manage the latest features in the platform. This week, we launched Terraform v5.20.0, which adds 24 new resources, bumps the underlying Go SDK to cloudflare-go v7, and includes a range of bug fixes and state upgraders based on community feedback.

#### New resources

  * **cloudflare_ai_search_namespace:** Manage AI Search namespaces
  * **cloudflare_custom_csr:** Manage custom certificate signing requests
  * **cloudflare_dls_prefix_binding:** Manage DLS regional service prefix bindings
  * **cloudflare_flagship_app:** Manage Flagship feature flag apps
  * **cloudflare_flagship_flag:** Manage Flagship feature flags
  * **cloudflare_google_tag_gateway:** Manage Google Tag Gateway
  * **cloudflare_load_balancer_monitor_group:** Manage load balancer monitor groups
  * **cloudflare_oauth_client:** Manage IAM OAuth clients
  * **cloudflare_origin_cloud_region:** Manage origin cloud regions (v2 endpoints)
  * **cloudflare_secrets_store:** Manage Secrets Store instances
  * **cloudflare_secrets_store_secret:** Manage Secrets Store secrets
  * **cloudflare_share:** Manage resource shares
  * **cloudflare_share_recipient:** Manage share recipients
  * **cloudflare_share_resource:** Manage shared resources
  * **cloudflare_zero_trust_device_deployment_groups:** Manage Zero Trust device deployment groups
  * **cloudflare_zero_trust_dlp_data_class:** Manage DLP data classes
  * **cloudflare_zero_trust_dlp_data_tag:** Manage DLP data tags
  * **cloudflare_zero_trust_dlp_data_tag_category:** Manage DLP data tag categories
  * **cloudflare_zero_trust_dlp_sensitivity_group:** Manage DLP sensitivity groups
  * **cloudflare_zero_trust_dlp_sensitivity_level:** Manage DLP sensitivity levels
  * **cloudflare_zero_trust_dlp_sensitivity_level_order:** Manage DLP sensitivity level ordering
  * **cloudflare_zero_trust_resource_library_application:** Manage Zero Trust resource library applications
  * **cloudflare_zero_trust_resource_library_category:** Manage Zero Trust resource library categories
  * **cloudflare_zero_trust_tunnel_warp_connector_config:** Manage WARP connector tunnel configurations



#### Features

  * **cache:** add create (POST) method for smart_tiered_cache
  * **cache:** update OPCR config to v2 endpoints
  * **dlp:** promote classification Stainless config to main
  * **dlp:** add custom prompt topics endpoint
  * **email_security_block_sender:** state upgrader for v4 to v5 migration
  * **email_security_impersonation_registry:** state upgrader for v4 to v5 migration
  * **email_security_trusted_domains:** state upgrader for v4 to v5 migration
  * **snippets:** add Terraform `id_property` annotations for snippet and snippet_rules
  * bump Go SDK to cloudflare-go v7



#### Bug fixes

  * **account_member:** missing upgrade path from v5.0–v5.15
  * **authenticated_origin_pulls_settings:** nil pointer panic
  * **bot_management:** restore `content_bots_protection` handling in model.go
  * **dns_record:** prevent FQDN normalization from swallowing name shortening changes
  * **list:** nullify empty nested objects to prevent inconsistent result after apply
  * **load_balancer_pool:** accept early-v5 object-shape state at schema_version=0
  * **load_balancer_pool:** add `UseStateForUnknown` for `load_shedding` attribute to prevent drift
  * **r2_custom_domain:** restore degraded-response handling in resource.go
  * **regional_hostname:** update cloudflare-go imports from v6 to v7
  * **secrets_store:** fix model/schema parity and guard acceptance tests
  * **spectrum_application:** accept early-v5 object-shape state at schema_version=0
  * **worker:** preserve `observability.traces.propagation_policy` across reads
  * **worker:** add `propagation_policy` to observability defaults
  * **worker_version:** restore handwritten D1 `database_id` handling
  * **workers_custom_domain:** missing `CertId` field in state migration
  * **workers_script:** restore annotations Read workaround stripped by codegen
  * **zero_trust_access_identity_provider:** change `read_only` from computed to optional
  * **zero_trust_access_identity_provider:** add `UseStateForUnknown` to SAML-only config fields
  * **zero_trust_access_identity_provider:** use `UseNonNullStateForUnknown` on scim_config fields
  * **zero_trust_access_policy:** populate `account_id` when migrating zone-scoped v4 state
  * **zero_trust_access_policy:** missing `common_names` transform in migration
  * gracefully handle nil pointer dereference when config has `attributes_flat` during migration
  * set initial schema version to 500 for all new resources



#### Refactors

Extracted `MoveState` nil guard into shared helper

#### For more information

  * [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
  * [Version 5 Migration Guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration)
  * [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)
  * [List of stabilized resources ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)



Apr 24, 2026

## [Terraform v5.19.0 now available](https://developers.cloudflare.com/changelog/post/2026-04-24-terraform-v5.19.0-provider/)

[Terraform](https://developers.cloudflare.com/terraform/)

Terraform Provider v5.19.0 introduces 14 new resources spanning AI Gateway, Pipelines, R2 Data Catalog, User Groups, Vulnerability Scanner, Workers Observability, and Zero Trust capabilities. This release significantly improves the v4 to v5 migration experience with automatic state upgraders for 26 resources, working seamlessly with the new [tf-migrate CLI tool ↗︎](https://github.com/cloudflare/tf-migrate) to automate resource renames, attribute updates, and `moved` block generation. Together, these enhancements reduce manual migration effort and minimize risk when upgrading from v4 to v5.

**Note:** `cmd/migrate` is deprecated in favor of `tf-migrate` and will be removed in a future release ([#7062 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/pull/7062))

#### New Resources

  * **cloudflare_ai_gateway** : Manage AI Gateway instances
  * **cloudflare_certificate_authorities_hostname_associations** : Manage mTLS certificate hostname associations
  * **cloudflare_custom_page_asset** : Manage custom page assets
  * **cloudflare_pipeline** : Manage Cloudflare Pipelines
  * **cloudflare_r2_data_catalog** : Manage R2 Data Catalog
  * **cloudflare_user_group** : Manage user groups
  * **cloudflare_user_group_members** : Manage user group memberships
  * **cloudflare_vulnerability_scanner_credential** : Manage vulnerability scanner credentials
  * **cloudflare_vulnerability_scanner_credential_set** : Manage vulnerability scanner credential sets
  * **cloudflare_vulnerability_scanner_target_environment** : Manage vulnerability scanner target environments
  * **cloudflare_workers_observability_destination** : Manage Workers Observability destinations
  * **cloudflare_zero_trust_device_ip_profile** : Manage Zero Trust device IP profiles
  * **cloudflare_zero_trust_device_subnet** : Manage Zero Trust device subnets
  * **cloudflare_zero_trust_dlp_settings** : Manage Zero Trust DLP settings



#### Features

#### V4 to V5 Migration State Upgraders

State upgraders added for seamless migration from v4 to v5 for the following resources:

  * account
  * account_member
  * account_token
  * authenticated_origin_pulls
  * authenticated_origin_pulls_hostname_certificate
  * byo_ip_prefix
  * custom_hostname
  * custom_ssl
  * leaked_credential_check
  * leaked_credential_check_rule
  * logpush_ownership_challenge
  * mtls_certificate
  * observatory_scheduled_test
  * pages_domain
  * regional_tiered_cache
  * turnstile_widget
  * workers_custom_domain
  * zero_trust_device_custom_profile
  * zero_trust_device_default_profile
  * zero_trust_device_posture_integration
  * zero_trust_gateway_certificate
  * zero_trust_gateway_settings
  * zero_trust_organization
  * zero_trust_tunnel_cloudflared_virtual_network
  * zone_setting



#### Other Features

  * **ruleset** : Add `content_converter` and `redirects_for_ai_training` support to configuration rules
  * **zero_trust_gateway_logging** : Make importable



#### Bug Fixes

#### Migration & State Management

  * **account_member** : Add UseStateForUnknown to status field to prevent drift
  * **authenticated_origin_pulls_settings** : Fix no prior schema and no-op upgrade
  * **certificate_pack** : Initialize empty lists instead of null in state upgrader to prevent drift
  * **migrations** : Handle ambiguous schema_version state for v4/v5 coexistence
  * **zero_trust_access_policy** : Fix nil pointer panic in state upgrader; set PriorSchema nil for v4 state upgrade



#### Resource-Specific Fixes

  * **ai_search_instance** : Restore original defaults for cache and cache_threshold; conflict resolution
  * **apijson** : Return empty object from MarshalForPatch when no fields are serializable
  * **dlp_predefined_profile** : Eliminate perpetual entries and enabled_entries drift
  * **dns_record** : Avoid unnecessary drift for ipv4_only and ipv6_only attributes; remove private_routing default value
  * **drift** : Preserve prior state values for optional fields not returned by API
  * **healthcheck** : Use buildHealthcheckPlanChecks helper for correct plan checks per migration source; update assertions
  * **leaked_credential_check_rule** : Handle empty ID from v4 provider state migration
  * **list_item** : Remove context
  * **logpush_job** : Update model for migration
  * **ruleset** : Fix migration; add redirects_for_ai_training to SourceV4ActionParametersModel; fix duplicate model attribute
  * **worker** : Add UseStateForUnknown() plan modifiers and update tests for observability.traces
  * **workers_custom_domain** : Handle HTTP 200 no content header; update assertions
  * **workers_script** : Fix model drift
  * **zero_trust_access_identity_provider** : Fix boolean drifts
  * **zero_trust_device_managed_networks** : Upgrade resource state
  * **zero_trust_gateway_policy** : Make filters Computed+Optional to prevent drift
  * **zero_trust_gateway_settings** : Fix breaking changes; implement sweeper to reset account to clean defaults
  * **zone_setting** : Migration test improvements and fixes



#### Documentation

  * **healthcheck** : Update port description to clarify defaults
  * Add application-scoped access policy migration guidance
  * Update zone_settings_override migration guide for tf-migrate v2 workflow



#### For more information

  * [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
  * [Version 5 Migration Guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration)
  * [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)



Apr 24, 2026

## [Automate migration from Cloudflare's Terraform v4 to v5 provider](https://developers.cloudflare.com/changelog/post/2026-04-24-tf-migrate-tool-released/)

[Terraform](https://developers.cloudflare.com/terraform/)

We're excited to announce **tf-migrate** , a purpose-built CLI tool that simplifies migrating from Cloudflare Terraform Provider v4 to v5.

#### v5 is stable and ready for production

**Terraform Provider v5 is stable and actively receiving updates.** We encourage all users to migrate to v5 to take advantage of ongoing enhancements and new capabilities.

Cloudflare uses tf-migrate to migrate our own infrastructure — the same tool we're providing to the community — ensuring the best possible migration experience.

#### What tf-migrate does

**tf-migrate** automates the tedious and error-prone parts of the v4 to v5 migration process:

  * **Resource type renames** – Automatically updates `cloudflare_record` → `cloudflare_dns_record`, `cloudflare_access_application` → `cloudflare_zero_trust_access_application`, and 40+ other renamed resources
  * **Attribute transformations** – Updates field names (e.g., `value` → `content` for DNS records) and restructures nested blocks
  * **Moved block generation** – Creates Terraform 1.8+ `moved` blocks to prevent resource replacements and ensure zero-downtime migrations
  * **Cross-file reference updates** – Automatically finds and updates all references to renamed resources across your entire configuration
  * **Dry-run mode** – Preview all changes before applying them to ensure safety



Combined with the automatic state upgraders introduced in v5.19+, tf-migrate eliminates the manual work and risk that previously made v5 migrations challenging. Tf-migrate operates directly on the config, and the built-in state upgraders handle the rest.

#### Supported resources

Tf-migrate currently supports the most common Terraform resources our customers use. We are actively working to expand coverage, with the most commonly used resources prioritized first.

For the complete list of supported resources and their migration status, refer to the [v5 Stabilization Tracker ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237). This list is updated regularly as additional resources are stabilized and migration support is added.

Resources not yet supported by tf-migrate will need to be migrated manually using the [version 5 upgrade guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). The upgrade guide provides step-by-step instructions for handling resource renames, attribute changes, and state migrations.

#### Get started

  * [Download tf-migrate ↗︎](https://github.com/cloudflare/tf-migrate/releases)
  * [Version 5 Migration Guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration)
  * [Terraform Provider documentation ↗︎](https://developers.cloudflare.com/terraform/)
  * [v5 Stabilization Tracker ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)



We have been releasing Betas over the past month and a half while testing this tool. See the full changelog of those Betas here: [tf-migrate releases ↗︎](https://github.com/cloudflare/tf-migrate/releases).

Feb 12, 2026

## [Terraform v5.17.0 now available](https://developers.cloudflare.com/changelog/post/2026-02-12-terraform-v5.17.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

In January 2025, we announced the launch of the new Terraform v5 Provider. We greatly appreciate the proactive engagement and valuable feedback from the Cloudflare community following the v5 release. In response, we have established a consistent and rapid [2-3 week cadence ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774) for releasing targeted improvements, demonstrating our commitment to stability and reliability.

With the help of the community, we have a growing number of resources that we have marked as [stable ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237), with that list continuing to grow with every release. The most used [resources ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237) are on track to be stable by the end of March 2026, when we will also be releasing a new migration tool to help you migrate from v4 to v5 with ease.

This release brings new capabilities for AI Search, enhanced Workers Script placement controls, and numerous bug fixes based on community feedback. We also begun laying foundational work for improving the v4 to v5 migration process. Stay tuned for more details as we approach the March 2026 release timeline.

Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.

#### Features

  * **ai_search_instance:** add data source for querying AI Search instances
  * **ai_search_token:** add data source for querying AI Search tokens
  * **account:** add support for tenant unit management with new `unit` field
  * **account:** add automatic mapping from `managed_by.parent_org_id` to `unit.id`
  * **authenticated_origin_pulls_certificate:** add data source for querying authenticated origin pull certificates
  * **authenticated_origin_pulls_hostname_certificate:** add data source for querying hostname-specific authenticated origin pull certificates
  * **authenticated_origin_pulls_settings:** add data source for querying authenticated origin pull settings
  * **workers_kv:** add `value` field to data source to retrieve KV values directly
  * **workers_script:** add `script` field to data source to retrieve script content
  * **workers_script:** add support for `simple` rate limit binding
  * **workers_script:** add support for targeted placement mode with `placement.target` array for specifying placement targets (region, hostname, host)
  * **workers_script:** add `placement_mode` and `placement_status` computed fields
  * **zero_trust_dex_test:** add data source with filter support for finding specific tests
  * **zero_trust_dlp_predefined_profile:** add `enabled_entries` field for flexible entry management



#### Bug Fixes

  * **account:** map `managed_by.parent_org_id` to `unit.id` in unmarshall and add acceptance tests
  * **authenticated_origin_pulls_certificate:** add certificate normalization to prevent drift
  * **authenticated_origin_pulls:** handle array response and implement full lifecycle
  * **authenticated_origin_pulls_hostname_certificate:** fix resource and tests
  * **cloudforce_one_request_message:** use correct `request_id` field instead of `id` in API calls
  * **dns_zone_transfers_incoming:** use correct `zone_id` field instead of `id` in API calls
  * **dns_zone_transfers_outgoing:** use correct `zone_id` field instead of `id` in API calls
  * **email_routing_settings:** use correct `zone_id` field instead of `id` in API calls
  * **hyperdrive_config:** add proper handling for write-only fields to prevent state drift
  * **hyperdrive_config:** add normalization for empty `mtls` objects to prevent unnecessary diffs
  * **magic_network_monitoring_rule:** use correct `account_id` field instead of `id` in API calls
  * **mtls_certificates:** fix resource and test
  * **pages_project:** revert build_config to computed optional
  * **stream_key:** use correct `account_id` field instead of `id` in API calls
  * **total_tls:** use upsert pattern for singleton zone setting
  * **waiting_room_rules:** use correct `waiting_room_id` field instead of `id` in API calls
  * **workers_script:** add support for placement mode/status
  * **zero_trust_access_application:** update v4 version on migration tests
  * **zero_trust_device_posture_rule:** update tests to match API
  * **zero_trust_dlp_integration_entry:** use correct `entry_id` field instead of `id` in API calls
  * **zero_trust_dlp_predefined_entry:** use correct `entry_id` field instead of `id` in API calls
  * **zero_trust_organization:** fix plan issues



#### Chores

  * add state upgraders to 95+ resources to lay the foundation for replacing Grit (still under active development)
  * **certificate_pack:** add state migration handler for SDKv2 to Framework conversion
  * **custom_hostname_fallback_origin:** add comprehensive lifecycle test and migration support
  * **dns_record:** add state migration handler for SDKv2 to Framework conversion
  * **leaked_credential_check:** add import functionality and tests
  * **load_balancer_pool:** add state migration handler with detection for v4 vs v5 format
  * **pages_project:** add state migration handlers
  * **tiered_cache:** add state migration handlers
  * **zero_trust_dlp_predefined_profile:** deprecate `entries` field in favor of `enabled_entries`



#### For more information

  * [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
  * [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)
  * [List of stabilized resources ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)



Jan 20, 2026

## [Terraform v5.16.0 now available](https://developers.cloudflare.com/changelog/post/2026-01-20-terraform-v5.16.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

In January 2025, we announced the launch of the new Terraform v5 Provider. We greatly appreciate the proactive engagement and valuable feedback from the Cloudflare community following the v5 release. In response, we've established a consistent and rapid [2-3 week cadence ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774) for releasing targeted improvements, demonstrating our commitment to stability and reliability.

With the help of the community, we have a growing number of resources that we have marked as [stable ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237), with that list continuing to grow with every release. The most used [resources ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237) are on track to be stable by the end of March 2026, when we will also be releasing a new migration tool to you migrate from v4 to v5 with ease.

Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.

This release includes bug fixes, the stabilization of even more popular resources, and more.

#### Features

  * **custom_pages:** add "waf_challenge" as new supported error page type identifier in both resource and data source schemas
  * **list:** enhance CIDR validator to check for normalized CIDR notation requiring network address for IPv4 and IPv6
  * **magic_wan_gre_tunnel:** add automatic_return_routing attribute for automatic routing control
  * **magic_wan_gre_tunnel:** add BGP configuration support with new BGP model attribute
  * **magic_wan_gre_tunnel:** add bgp_status computed attribute for BGP connection status information
  * **magic_wan_gre_tunnel:** enhance schema with BGP-related attributes and validators
  * **magic_wan_ipsec_tunnel:** add automatic_return_routing attribute for automatic routing control
  * **magic_wan_ipsec_tunnel:** add BGP configuration support with new BGP model attribute
  * **magic_wan_ipsec_tunnel:** add bgp_status computed attribute for BGP connection status information
  * **magic_wan_ipsec_tunnel:** add custom_remote_identities attribute for custom identity configuration
  * **magic_wan_ipsec_tunnel:** enhance schema with BGP and identity-related attributes
  * **ruleset:** add request body buffering support
  * **ruleset:** enhance ruleset data source with additional configuration options
  * **workers_script:** add observability logs attributes to list data source model
  * **workers_script:** enhance list data source schema with additional configuration options



#### Bug Fixes

  * **account_member** : fix resource importability issues
  * **dns_record:** remove unnecessary fmt.Sprintf wrapper around LoadTestCase call in test configuration helper function
  * **load_balancer:** fix session_affinity_ttl type expectations to match Float64 in initial creation and Int64 after migration
  * **workers_kv:** handle special characters correctly in URL encoding



#### Documentation

  * **account_subscription:** update schema description for rate_plan.sets attribute to clarify it returns an array of strings
  * **api_shield:** add resource-level description for API Shield management of auth ID characteristics
  * **api_shield:** enhance auth_id_characteristics.name attribute description to include JWT token configuration format requirements
  * **api_shield:** specify JSONPath expression format for JWT claim locations
  * **hyperdrive_config:** add description attribute to name attribute explaining its purpose in dashboard and API identification
  * **hyperdrive_config:** apply description improvements across resource, data source, and list data source schemas
  * **hyperdrive_config:** improve schema descriptions for cache settings to clarify default values
  * **hyperdrive_config:** update port description to clarify defaults for different database types



#### For more information

  * [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
  * [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)
  * [List of stabilized resources ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)



Dec 19, 2025

## [Terraform v5.15.0 now available](https://developers.cloudflare.com/changelog/post/2025-12-19-terraform-v5.15.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a [2-3 week cadence ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774) to ensure its stability and reliability, including the v5.15 release. We have also pivoted from an [issue-to-issue approach to a resource-per-resource approach ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237) \- we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.

Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.

This release includes bug fixes, the stabilization of even more popular resources, and more.

#### Features

  * **ai_search:** Add AI Search endpoints ([6f02adb ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/6f02adb420e872457f71f95b49cb527663388915))
  * **certificate_pack:** Ensure proper Terraform resource ID handling for path parameters in API calls ([081f32a ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/081f32acab4ce9a194a7ff51c8e9fcabd349895a))
  * **worker_version:** Support `startup_time_ms` ([286ab55 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/286ab55bea8d5be0faa5a2b5b8b157e4a2214eba))
  * **zero_trust_dlp_custom_entry:** Support `upload_status` ([7dc0fe3 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c))
  * **zero_trust_dlp_entry:** Support `upload_status` ([7dc0fe3 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c))
  * **zero_trust_dlp_integration_entry:** Support `upload_status` ([7dc0fe3 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c))
  * **zero_trust_dlp_predefined_entry:** Support `upload_status` ([7dc0fe3 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c))
  * **zero_trust_gateway_policy:** Support `forensic_copy` ([5741fd0 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/5741fd0ed9f7270d20731cc47ec45eb0403a628b))
  * **zero_trust_list:** Support additional types (category, location, device) ([5741fd0 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/5741fd0ed9f7270d20731cc47ec45eb0403a628b))



#### Bug fixes

  * **access_rules:** Add validation to prevent state drift. Ideally, we'd use Semantic Equality but since that isn't an option, this will remove a foot-gun. ([4457791 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/44577911b3cbe45de6279aefa657bdee73c0794d))
  * **cloudflare_pages_project:** Addressing drift issues ([6edffcf ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/6edffcfcf187fdc9b10b624b9a9b90aed2fb2b2e)) ([3db318e ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/3db318e747423bf10ce587d9149e90edcd8a77b0))
  * **cloudflare_worker:** Can be cleanly imported ([4859b52 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/4859b52968bb25570b680df9813f8e07fd50728f))
  * **cloudflare_worker:** Ensure clean imports ([5b525bc ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/5b525bc478a4e2c9c0d4fd659b92cc7f7c18016a))
  * **list_items:** Add validation for IP List items to avoid inconsistent state ([b6733dc ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/b6733dc4be909a5ab35895a88e519fc2582ccada))
  * **zero_trust_access_application:** Remove all conditions from sweeper ([3197f1a ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/3197f1aed61be326d507d9e9e3b795b9f1d18fd7))
  * **spectrum_application:** Map missing fields during spectrum resource import ([#6495 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6495)) ([ddb4e72 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/ddb4e722b82c735825a549d651a9da219c142efa))



#### Upgrade to newer version

We suggest waiting to migrate to v5 while we work on stabilization. This helps with avoiding any blocking issues while the Terraform resources are actively being [stabilized ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237). We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.

#### For more information

  * [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
  * [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)



Dec 5, 2025

## [Terraform v5.14.0 now available](https://developers.cloudflare.com/changelog/post/2025-12-05-terraform-v5.14.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a [2-3 week cadence ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774) to ensure its stability and reliability, including the v5.14 release. We have also pivoted from an [issue-to-issue approach to a resource-per-resource approach ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237) \- we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.

Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.

This release includes bug fixes, the stabilization of even more popular resources, and more.

#### Deprecation notice

Resource affected: `api_shield_discovery_operation`

Cloudflare continuously discovers and updates API endpoints and web assets of your web applications. To improve the maintainability of these dynamic resources, we are working on reducing the need to actively engage with discovered operations.

The corresponding public API endpoint of [discovered operations ↗︎](https://developers.cloudflare.com/api/resources/api_gateway/subresources/discovery/subresources/operations/) is not affected and will continue to be supported.

#### Features

  * **pages_project** : Add v4 -> v5 migration tests ([#6506 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/pull/6506))



#### Bug fixes

  * **account_members** : Makes member policies a set ([#6488 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6488))
  * **pages_project** : Ensures non empty refresh plans ([#6515 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6515))
  * **R2** : Improves sweeper ([#6512 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6512))
  * **workers_kv** : Ignores value import state for verify ([#6521 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6521))
  * **workers_script** : No longer treats the migrations attribute as WriteOnly ([#6489 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6489))
  * **workers_script** : Resolves resource drift when worker has unmanaged secret ([#6504 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6504))
  * **zero_trust_device_posture_rule** : Preserves input.version and other fields ([#6500 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6500)) and ([#6503 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6503))
  * **zero_trust_dlp_custom_profile** : Adds sweepers for `dlp_custom_profile`
  * **zone_subscription|account_subscription** : Adds `partners_ent` as valid enum for `rate_plan.id` ([#6505 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6505))
  * **zone** : Ensures datasource model schema parity ([#6487 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6487))
  * **subscription** : Updates import signature to accept account_id/subscription_id to import account subscription ([#6510 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6510))



#### Upgrade to newer version

We suggest waiting to migrate to v5 while we work on stabilization. This helps with avoiding any blocking issues while the Terraform resources are actively being [stabilized ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237). We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.

#### For more information

  * [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
  * [Documentation on using Terraform with Cloudflare ↗︎](https://developers.cloudflare.com/terraform/)



Nov 20, 2025

## [Terraform v5.13.0 now available](https://developers.cloudflare.com/changelog/post/2025-11-20-terraform-v5.13.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a [2-3 week cadence ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774) to ensure its stability and reliability, including the v5.13 release. We have also pivoted from an [issue-to-issue approach to a resource-per-resource approach ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237) \- we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.

Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.

This release includes new features, new resources and data sources, bug fixes, updates to our Developer Documentation, and more.

#### Breaking Change

Please be aware that there are breaking changes for the `cloudflare_api_token` and `cloudflare_account_token` resources. These changes eliminate configuration drift caused by policy ordering differences in the Cloudflare API.

For more specific information about the changes or the actions required, please see the [detailed Repository changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.13.0).

#### Features

  * **New resources and data sources added**
    * cloudflare_connectivity_directory
    * cloudflare_sso_connector
    * cloudflare_universal_ssl_setting
  * **api_token+account_tokens:** state upgrader and schema bump ([#6472 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6472))
  * **docs:** make docs explicit when a resource does not have import support
  * **magic_transit_connector:** support self-serve license key ([#6398 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6398))
  * **worker_version:** add content_base64 support
  * **worker_version:** boolean support for run_worker_first ([#6407 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6407))
  * **workers_script_subdomains:** add import support ([#6375 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6375))
  * **zero_trust_access_application:** add proxy_endpoint for ZT Access Application ([#6453 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6453))
  * **zero_trust_dlp_predefined_profile:** Switch DLP Predefined Profile endpoints, introduce enabled_entries attribute



#### Bug Fixes

  * **account_token:** token policy order and nested resources ([#6440 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6440))
  * allow r2_bucket_event_notification to be applied twice without failing ([#6419 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6419))
  * **cloudflare_worker+cloudflare_worker_version:** import for the resources ([#6357 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6357))
  * **dns_record:** inconsistent apply error ([#6452 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6452))
  * **pages_domain:** resource tests ([#6338 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6338))
  * **pages_project:** unintended resource state drift ([#6377 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6377))
  * **queue_consumer:** id population ([#6181 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6181))
  * **workers_kv:** multipart request ([#6367 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6367))
  * **workers_kv:** updating workers metadata attribute to be read from endpoint ([#6386 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6386))
  * **workers_script_subdomain:** add note to cloudflare_workers_script_subdomain about redundancy with cloudflare_worker ([#6383 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6383))
  * **workers_script:** allow config.run_worker_first to accept list input
  * **zero_trust_device_custom_profile_local_domain_fallback:** drift issues ([#6365 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6365))
  * **zero_trust_device_custom_profile:** resolve drift issues ([#6364 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6364))
  * **zero_trust_dex_test:** correct configurability for 'targeted' attribute to fix drift
  * **zero_trust_tunnel_cloudflared_config:** remove warp_routing from cloudflared_config ([#6471 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6471))



#### Upgrading

We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized. We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.

#### For more info

  * [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
  * [Documentation on using Terraform with Cloudflare ↗︎](https://developers.cloudflare.com/terraform/)



Aug 29, 2025

## [Terraform v5.9 now available](https://developers.cloudflare.com/changelog/post/2025-08-29-terrform-v5.9-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). We are aware of the high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a 2 week cadence to ensure its stability and reliability, including the v5.9 release. We have also pivoted from an issue-to-issue approach to a resource-per-resource approach - we will be focusing on specific resources for every release, stabilizing the release, and closing all associated bugs with that resource before moving onto resolving migration issues.

Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.

This release includes a new resource, `cloudflare_snippet`, which replaces `cloudflare_snippets`. `cloudflare_snippet` is now considered deprecated but can still be used. Please utilize `cloudflare_snippet` as soon as possible.

#### Changes

  * Resources stabilized: 
    * `cloudflare_zone_setting`
    * `cloudflare_worker_script`
    * `cloudflare_worker_route`
    * `tiered_cache`
  * **NEW** resource `cloudflare_snippet` which should be used in place of `cloudflare_snippets`. `cloudflare_snippets` is now deprecated. This enables the management of Cloudflare's snippet functionality through Terraform.
  * DNS Record Improvements: Enhanced handling of DNS record drift detection
  * Load Balancer Fixes: Resolved `created_on` field inconsistencies and improved pool configuration handling
  * Bot Management: Enhanced auto-update model state consistency and fight mode configurations
  * Other bug fixes



For a more detailed look at all of the changes, refer to the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.9.0) in GitHub.

#### Issues Closed

  * [#5921: In cloudflare_ruleset removing an existing rule causes recreation of later rules ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5921)
  * [#5904: cloudflare_zero_trust_access_application is not idempotent ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5904)
  * [#5898: (cloudflare_workers_script) Durable Object migrations not applied ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5898)
  * [#5892: cloudflare_workers_script secret_text environment variable gets replaced on every deploy ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5892)
  * [#5891: cloudflare_zone suddenly started showing drift ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5891)
  * [#5882: cloudflare_zero_trust_list always marked for change due to read only attributes ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5882)
  * [#5879: cloudflare_zero_trust_gateway_certificate unable to manage resource (cant mark as active/inactive) ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5879)
  * [#5858: cloudflare_dns_records is always updated in-place ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5858)
  * [#5839: Recurring change on cloudflare_zero_trust_gateway_policy after upgrade to V5 provider & also setting expiration fails ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5839)
  * [#5811: Reusable policies are imported as inline type for cloudflare_zero_trust_access_application ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5811)
  * [#5795: cloudflare_zone_setting inconsistent value of "editable" upon apply ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5795)
  * [#5789: Pagination issue fetching all policies in "cloudflare_zero_trust_access_policies" data source ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5789)
  * [#5770: cloudflare_zero_trust_access_application type warp diff on every apply ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5770)
  * [#5765: V5 / cloudflare_zone_dnssec fails with HTTP/400 "Malformed request body" ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5765)
  * [#5755: Unable to manage Cloudflare managed WAF rules via Terraform ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5755)
  * [#5738: v4 to v5 upgrade failing Error: no schema available AND Unable to Read Previously Saved State for UpgradeResourceState ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5738)
  * [#5727: cloudflare_ruleset http_request_cache_settings bypass mismatch between dashboard and terraform ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5727)
  * [#5700: cloudflare_account_member invalid type 'string' for field 'roles' ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5700)



If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new issue if one does not already exist for what you are experiencing.

#### Upgrading

We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized.

If you'd like more information on migrating from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition. These do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

  * [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
  * [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)
  * [GitHub Repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare)



Aug 15, 2025

## [Terraform v5.8.4 now available](https://developers.cloudflare.com/changelog/post/2025-08-15-terraform-v5.8.4-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). We are aware of the high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by the Cloudflare Community related to the v5 release. We have committed to releasing improvements on a two week cadence to ensure stability and reliability.

One key change we adopted in recent weeks is a pivot to more comprehensive, test-driven development. We are still evaluating individual issues, but are also investing in much deeper testing to drive our stabilization efforts. We will subsequently be investing in comprehensive migration scripts. As a result, you will see several of the highest traffic APIs have been stabilized in the most recent release, and are supported by comprehensive acceptance tests.

Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.

#### Changes

  * Resources stabilized: 
    * `cloudflare_argo_smart_routing`
    * `cloudflare_bot_management`
    * `cloudflare_list`
    * `cloudflare_list_item`
    * `cloudflare_load_balancer`
    * `cloudflare_load_balancer_monitor`
    * `cloudflare_load_balancer_pool`
    * `cloudflare_spectrum_application`
    * `cloudflare_managed_transforms`
    * `cloudflare_url_normalization_settings`
    * `cloudflare_snippet`
    * `cloudflare_snippet_rules`
    * `cloudflare_zero_trust_access_application`
    * `cloudflare_zero_trust_access_group`
    * `cloudflare_zero_trust_access_identity_provider`
    * `cloudflare_zero_trust_access_mtls_certificate`
    * `cloudflare_zero_trust_access_mtls_hostname_settings`
    * `cloudflare_zero_trust_access_policy`
    * `cloudflare_zone`
  * Multipart handling restored for `cloudflare_snippet`
  * `cloudflare_bot_management` diff issues resolves when running `terraform plan` and `terraform apply`
  * Other bug fixes



For a more detailed look at all of the changes, refer to the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.8.4) in GitHub.

#### Issues Closed

  * [#5017: 'Uncaught Error: No such module' using cloudflare_snippets ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5017)
  * [#5701: cloudflare_workers_script migrations for Durable Objects not recorded in tfstate; cannot be upgraded between versions ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5701)
  * [#5640: cloudflare_argo_smart_routing importing doesn't read the actual value ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5640)



If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new one if one does not already exist for what you are experiencing.

#### Upgrading

We suggest holding off on migration to v5 while we work on stabilization. This will help you avoid any blocking issues while the Terraform resources are actively being stabilized.

If you'd like more information on migrating to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition. These migration scripts do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

  * [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
  * [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)



Aug 1, 2025

## [Terraform v5.8.2 now available](https://developers.cloudflare.com/changelog/post/2025-08-01-terraform-v5.8.2-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). We are aware of the high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a 2 week cadeance to ensure it's stability and reliability. We have also pivoted from an issue-to-issue approach to a resource-per-resource approach - we will be focusing on specific resources for every release, stabilizing the release and closing all associated bugs with that resource before moving onto resolving migration issues.

Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.

#### Changes

  * Resources stabilized: 
    * `cloudflare_custom_pages`
    * `cloudflare_page_rule`
    * `cloudflare_dns_record`
    * `cloudflare_argo_tiered_caching`
  * Addressed chronic drift issues in `cloudflare_logpush_job`, `cloudflare_zero_trust_dns_location`, `cloudflare_ruleset` & `cloudflare_api_token`
  * `cloudflare_zone_subscription` returns expected values `rate_plan.id` from former versions
  * `cloudflare_workers_script` can now successfully be destroyed with bindings & migration for Durable Objects now recorded in tfstate
  * Ability to configure `add_headers` under `cloudflare_zero_trust_gateway_policy`
  * Other bug fixes



For a more detailed look at all of the changes, see the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.8.2) in GitHub.

#### Issues Closed

  * [#5666: cloudflare_ruleset example lists id which is a read-only field ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5666)
  * [#5578: cloudflare_logpush_job plan always suggests changes ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5578)
  * [#5552: 5.4.0: Since provider update, existing cloudflare_list_item would be recreated "created" state ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5552)
  * [#5670: cloudflare_zone_subscription: uses wrong ID field in Read/Update ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5670)
  * [#5548: cloudflare_api_token resource always shows changes (drift) ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5548)
  * [#5634: cloudflare_workers_script with bindings fails to be destroyed ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5634)
  * [#5616: cloudflare_workers_script Unable to deploy worker assets ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5616)
  * [#5331: cloudflare_workers_script 500 internal server error when uploading python ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5331)
  * [#5701: cloudflare_workers_script migrations for Durable Objects not recorded in tfstate; cannot be upgraded between versions ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5701)
  * [#5704: cloudflare_workers_script randomly fails to deploy when changing compatibility_date ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5704)
  * [#5439: cloudflare_workers_script (v5.2.0) ignoring content and bindings properties ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5439)
  * [#5522: cloudflare_workers_script always detects changes after apply ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5522)
  * [#5693: cloudflare_zero_trust_access_identity_provider gives recurring change on OTP pin login ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5693)
  * [#5567: cloudflare_r2_custom_domain doesn't roundtrip jurisdiction properly ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5567)
  * [#5179: Bad request with when creating cloudflare_api_shield_schema resource ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5179)



If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new one if one does not already exist for what you are experiencing.

#### Upgrading

We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized.

If you'd like more information on migrating from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

  * [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
  * [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)



Jul 14, 2025

## [Terraform v5.7.0 now available](https://developers.cloudflare.com/changelog/post/2025-07-11-terraform-v5.7.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). We are aware of the high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by the Cloudflare community related to the v5 release, with 13.5% of resources impacted. We have committed to releasing improvements on a 2 week cadeance to ensure it's stability and relability, including the v5.7 release.

Thank you for continuing to raise issues and please keep an eye on this changelog for more information about upcoming releases.

#### Changes

  * Addressed permanent diff bug on Cloudflare Tunnel config
  * State is now saved correctly for Zero Trust Access applications
  * Exact match is now working as expected within `data.cloudflare_zero_trust_access_applications`
  * `cloudflare_zero_trust_access_policy` now supports OIDC claims & diff issues resolved
  * Self hosted applications with private IPs no longer require a public domain for `cloudflare_zero_trust_access_application`.
  * New resource: 
    * `cloudflare_zero_trust_tunnel_warp_connector`
  * Other bug fixes



For a more detailed look at all of the changes, see the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.7.0) in GitHub.

#### Issues Closed

  * [#5563: cloudflare_logpull_retention is missing import ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5563)
  * [#5608: cloudflare_zero_trust_access_policy in 5.5.0 provider gives error upon apply unexpected new value: .app_count: was cty.NumberIntVal(0), but now cty.NumberIntVal(1) ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5608)
  * [#5612: data.cloudflare_zero_trust_access_applications does not exact match ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5612)
  * [#5532: cloudflare_zero_trust_access_identity_provider detects changes on every plan ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5532)
  * [#5662: cloudflare_zero_trust_access_policy does not support OIDC claims ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5662)
  * [#5565: Running Terraform with the cloudflare_zero_trust_access_policy resource results in updates on every apply, even when no changes are made - breaks idempotency ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5565)
  * [#5529: cloudflare_zero_trust_access_application: self hosted applications with private ips require public domain  ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5529)



If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new one if one does not already exist for what you are experiencing.

#### Upgrading

We suggest holding on migration to v5 while we work on stabilization of the v5 provider. This will ensure Cloudflare can work ahead and avoid any blocking issues.

If you'd like more information on migrating from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

  * [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
  * [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)



Jun 17, 2025

## [Terraform v5.6.0 now available](https://developers.cloudflare.com/changelog/post/2025-06-17-terraform-v5.6.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.6.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.

#### Changes

  * Broad fixes across resources with recurring diffs, including, but not limited to: 
    * `cloudflare_zero_trust_access_identity_provider`
      * `cloudflare_zone`
  * `cloudflare_page_rules` runtime panic when setting `cache_level` to `cache_ttl_by_status`
  * Failure to serialize requests in `cloudflare_zero_trust_tunnel_cloudflared_config`
  * Undocumented field 'priority' on `zone_lockdown` resource
  * Missing importability for `cloudflare_zero_trust_device_default_profile_local_domain_fallback` and `cloudflare_account_subscription`
  * New resources: 
    * `cloudflare_schema_validation_operation_settings`
    * `cloudflare_schema_validation_schemas`
    * `cloudflare_schema_validation_settings`
    * `cloudflare_zero_trust_device_settings`
  * Other bug fixes



For a more detailed look at all of the changes, see the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.6.0) in GitHub.

#### Issues Closed

  * [#5098: 500 Server Error on updating 'zero_trust_tunnel_cloudflared_virtual_network' Terraform resource ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5098)
  * [#5148: cloudflare_user_agent_blocking_rule doesn’t actually support user agents ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5148)
  * [#5472: cloudflare_zone showing changes in plan after following upgrade steps ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5472)
  * [#5508: cloudflare_zero_trust_tunnel_cloudflared_config failed to serialize http request ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5508)
  * [#5509: cloudflare_zone: Problematic Terraform behaviour with paused zones ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5509)
  * [#5520: Resource 'cloudflare_magic_wan_static_route' is not working ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5520)
  * [#5524: Optional fields cause crash in cloudflare_zero_trust_tunnel_cloudflared(s) when left null ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5524)
  * [#5526: Provider v5 migration issue: no import method for cloudflare_zero_trust_device_default_profile_local_domain_fallback ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5526)
  * [#5532: cloudflare_zero_trust_access_identity_provider detects changes on every plan ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5532)
  * [#5561: cloudflare_zero_trust_tunnel_cloudflared: cannot rotate tunnel secret ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5561)
  * [#5569: cloudflare_zero_trust_device_custom_profile_local_domain_fallback not allowing multiple DNS Server entries ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5569)
  * [#5577: Panic modifying page_rule resource ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5577)
  * [#5653: cloudflare_zone_setting resource schema confusion in 5.5.0: value vs enabled ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5653)



If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new one if one does not already exist for what you are experiencing.

#### Upgrading

If you are evaluating a move from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

  * [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
  * [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)



May 19, 2025

## [Terraform v5.5.0 now available](https://developers.cloudflare.com/changelog/post/2025-05-19-terraform-v5.5.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.5.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.

#### Changes

  * Broad fixes across resources with recurring diffs, including, but not limited to: 
    * `cloudflare_zero_trust_gateway_policy`
    * `cloudflare_zero_trust_access_application`
    * `cloudflare_zero_trust_tunnel_cloudflared_route`
    * `cloudflare_zone_setting`
    * `cloudflare_ruleset`
    * `cloudflare_page_rule`
  * Zone settings can be re-applied without client errors
  * Page rules conversion errors are fixed
  * Failure to apply changes to `cloudflare_zero_trust_tunnel_cloudflared_route`
  * Other bug fixes



For a more detailed look at all of the changes, see the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.5.0) in GitHub.

#### Issues Closed

  * [#5304: Importing cloudflare_zero_trust_gateway_policy invalid attribute filter value ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5304)
  * [#5303: cloudflare_page_rule import does not set values for all of the fields in terraform state ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5303)
  * [#5178: cloudflare_page_rule Page rule creation with redirect fails ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5178)
  * [#5336: cloudflare_turnstile_wwidget not able to update ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5336)
  * [#5418: cloudflare_cloud_connector_rules: Provider returned invalid result object after apply ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5418)
  * [#5423: cloudflare_zone_setting: "Invalid value for zone setting always_use_https" ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5423)



If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new one if one does not already exist for what you are experiencing.

#### Upgrading

If you are evaluating a move from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

  * [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
  * [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)



May 6, 2025

## [Terraform v5.4.0 now available](https://developers.cloudflare.com/changelog/post/2025-05-06-terraform-v5.4.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.4.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.

#### Changes

  * Removes the `worker_platforms_script_secret` resource from the provider (see [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade#cloudflare_worker_secret) for alternatives—applicable to both Workers and Workers for Platforms)
  * Removes duplicated fields in `cloudflare_cloud_connector_rules` resource
  * Fixes `cloudflare_workers_route` id issues [#5134 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5134) [#5501 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5501)
  * Fixes issue around refreshing resources that have unsupported response types Affected resources
    * `cloudflare_certificate_pack`
    * `cloudflare_registrar_domain`
    * `cloudflare_stream_download`
    * `cloudflare_stream_webhook`
    * `cloudflare_user`
    * `cloudflare_workers_kv`
    * `cloudflare_workers_script`
  * Fixes `cloudflare_workers_kv` state refresh issues
  * Fixes issues around configurability of nested properties without computed values for the following resources Affected resources
    * `cloudflare_account`
    * `cloudflare_account_dns_settings`
    * `cloudflare_account_token`
    * `cloudflare_api_token`
    * `cloudflare_cloud_connector_rules`
    * `cloudflare_custom_ssl`
    * `cloudflare_d1_database`
    * `cloudflare_dns_record`
    * `email_security_trusted_domains`
    * `cloudflare_hyperdrive_config`
    * `cloudflare_keyless_certificate`
    * `cloudflare_list_item`
    * `cloudflare_load_balancer`
    * `cloudflare_logpush_dataset_job`
    * `cloudflare_magic_network_monitoring_configuration`
    * `cloudflare_magic_transit_site`
    * `cloudflare_magic_transit_site_lan`
    * `cloudflare_magic_transit_site_wan`
    * `cloudflare_magic_wan_static_route`
    * `cloudflare_notification_policy`
    * `cloudflare_pages_project`
    * `cloudflare_queue`
    * `cloudflare_queue_consumer`
    * `cloudflare_r2_bucket_cors`
    * `cloudflare_r2_bucket_event_notification`
    * `cloudflare_r2_bucket_lifecycle`
    * `cloudflare_r2_bucket_lock`
    * `cloudflare_r2_bucket_sippy`
    * `cloudflare_ruleset`
    * `cloudflare_snippet_rules`
    * `cloudflare_snippets`
    * `cloudflare_spectrum_application`
    * `cloudflare_workers_deployment`
    * `cloudflare_zero_trust_access_application`
    * `cloudflare_zero_trust_access_group`
  * Fixed defaults that made `cloudflare_workers_script` fail when using Assets
  * Fixed Workers Logpush setting in `cloudflare_workers_script` mistakenly being readonly
  * Fixed `cloudflare_pages_project` broken when using "source"



The detailed [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.4.0) is available on GitHub.

#### Upgrading

If you are evaluating a move from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues either by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare), or by opening a [support ticket ↗︎](https://www.support.cloudflare.com/s/?language=en_US).

#### For more info

  * [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
  * [Documentation on using Terraform with Cloudflare ↗︎](https://developers.cloudflare.com/terraform/)



Mar 21, 2025

## [Dozens of Cloudflare Terraform Provider resources now have proper drift detection](https://developers.cloudflare.com/changelog/post/2025-03-21-resource-force-replacement-bug/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

In [Cloudflare Terraform Provider ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) versions 5.2.0 and above, dozens of resources now have proper drift detection. Before this fix, these resources would indicate they needed to be updated or replaced — even if there was no real change. Now, you can rely on your `terraform plan` to only show what resources are expected to change.

This issue affected [resources ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) related to these products and features:

  * API Shield
  * Argo Smart Routing
  * Argo Tiered Caching
  * Bot Management
  * BYOIP
  * D1
  * DNS
  * Email Routing
  * Hyperdrive
  * Observatory
  * Pages
  * R2
  * Rules
  * SSL/TLS
  * Waiting Room
  * Workers
  * Zero Trust



Mar 21, 2025

## [Cloudflare Terraform Provider now properly redacts sensitive values](https://developers.cloudflare.com/changelog/post/2025-03-21-sensitive-values-redacted/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

In the [Cloudflare Terraform Provider ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) versions 5.2.0 and above, sensitive properties of resources are redacted in logs. Sensitive properties in [Cloudflare's OpenAPI Schema ↗︎](https://raw.githubusercontent.com/cloudflare/api-schemas/refs/heads/main/openapi.yaml) are now annotated with `x-sensitive: true`. This results in proper auto-generation of the corresponding Terraform resources, and prevents sensitive values from being shown when you run Terraform commands.

This issue affected [resources ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) related to these products and features:

  * Alerts and Audit Logs
  * Device API
  * DLP
  * DNS
  * Magic Visibility
  * Magic WAN
  * TLS Certs and Hostnames
  * Tunnels
  * Turnstile
  * Workers
  * Zaraz



Feb 3, 2025

## [Terraform v5 Provider is now generally available](https://developers.cloudflare.com/changelog/post/2025-02-03-terraform-v5-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

![Screenshot of Terraform defining a Zone](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1330,height=296,format=webp/_astro/2024-02-03-terraform-v5-screenshot.mW8OaFoS.png)

Cloudflare's v5 Terraform Provider is now generally available. With this release, Terraform resources are now automatically generated based on OpenAPI Schemas. This change brings alignment across our SDKs, API documentation, and now Terraform Provider. The new provider boosts coverage by increasing support for API properties to 100%, adding 25% more resources, and more than 200 additional data sources. Going forward, this will also reduce the barriers to bringing more resources into Terraform across the broader Cloudflare API. This is a small, but important step to making more of our platform manageable through GitOps, making it easier for you to manage Cloudflare just like you do your other infrastructure.

The Cloudflare Terraform Provider v5 is a ground-up rewrite of the provider and introduces breaking changes for some resource types. Please refer to the [upgrade guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade) for best practices, or the [blog post on automatically generating Cloudflare's Terraform Provider ↗︎](https://blog.cloudflare.com/automatically-generating-cloudflares-terraform-provider/) for more information about the approach.

For more info

  * [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
  * [Documentation on using Terraform with Cloudflare ↗︎](https://developers.cloudflare.com/terraform/)


