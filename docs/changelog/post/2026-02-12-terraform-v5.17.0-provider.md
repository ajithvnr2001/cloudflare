---
url: https://developers.cloudflare.com/changelog/post/2026-02-12-terraform-v5.17.0-provider/
title: Terraform v5.17.0 now available \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.933494+00:00
---

# Terraform v5.17.0 now available · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-12-terraform-v5.17.0-provider/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 12, 2026

## Terraform v5.17.0 now available

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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


