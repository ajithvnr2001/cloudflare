---
url: https://developers.cloudflare.com/changelog/post/2026-04-24-tf-migrate-tool-released/
title: Automate migration from Cloudflare's Terraform v4 to v5 provider \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:39.614483+00:00
---

# Automate migration from Cloudflare's Terraform v4 to v5 provider · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-24-tf-migrate-tool-released/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 24, 2026

## Automate migration from Cloudflare's Terraform v4 to v5 provider

[Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
