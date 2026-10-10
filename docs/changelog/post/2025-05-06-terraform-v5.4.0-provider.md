---
url: https://developers.cloudflare.com/changelog/post/2025-05-06-terraform-v5.4.0-provider/
title: Terraform v5.4.0 now available \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:52.512660+00:00
---

# Terraform v5.4.0 now available · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-06-terraform-v5.4.0-provider/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 6, 2025

## Terraform v5.4.0 now available

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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


