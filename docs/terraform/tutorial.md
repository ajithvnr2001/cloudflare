---
url: https://developers.cloudflare.com/terraform/tutorial/
title: Tutorials \u00b7 Cloudflare Terraform docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:01.361769+00:00
---

# Tutorials · Cloudflare Terraform docs

> Source: https://developers.cloudflare.com/terraform/tutorial/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Terraform](https://developers.cloudflare.com/terraform/)
  3. /Tutorials



# Tutorials

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/terraform/tutorial/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1 – Initialize Terraform2 – Track your history3 – Configure HTTPS settings4 – Improve performance and reliability5 – Add exceptions with page rules6 – Revert configuration

Before you begin, [install Terraform](https://developers.cloudflare.com/terraform/installing/). Each tutorial builds on the previous, so you should complete the tutorials in the order shown below.

Note

If you are upgrading from v4, review the [migration guide ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/blob/main/docs/guides/version-5-upgrade.md) for breaking changes.

## [1 – Initialize Terraform](https://developers.cloudflare.com/terraform/tutorial/initialize-terraform/)

  * Brief introduction.
  * Introduction of `terraform init`, `plan`, `apply`, and `show`.
  * Resource covered: [`cloudflare_dns_record` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/dns_record) (DNS record).



## [2 – Track your history](https://developers.cloudflare.com/terraform/tutorial/track-history/)

  * Store Cloudflare configuration in source control.



## [3 – Configure HTTPS settings](https://developers.cloudflare.com/terraform/tutorial/configure-https-settings/)

  * Modify zone settings.
  * Resource covered: [`cloudflare_zone_setting` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zone_setting).



## [4 – Improve performance and reliability](https://developers.cloudflare.com/terraform/tutorial/use-load-balancing/)

  * Add load balancing rules.
  * Resources covered: 
    * [`cloudflare_load_balancer` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/load_balancer)
    * [`cloudflare_load_balancer_pool` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/load_balancer_pool)
    * [`cloudflare_load_balancer_monitor` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/load_balancer_monitor)



## [5 – Add exceptions with page rules](https://developers.cloudflare.com/terraform/tutorial/add-page-rules/)

  * Add page rule.
  * Resource covered: [`cloudflare_page_rule` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/page_rule).
  * Increase security level for a specific URL: `/expensive-db-call`.
  * Add a redirect (URL forward) with a `301` status code from `/old-location.php` to `/expensive-db-call`.



## [6 – Revert configuration](https://developers.cloudflare.com/terraform/tutorial/revert-configuration/)

  * Review change history.
  * Roll back changes.



[PreviousGet started](https://developers.cloudflare.com/terraform/installing/)[Next1 – Initialize Terraform](https://developers.cloudflare.com/terraform/tutorial/initialize-terraform/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/terraform/tutorial/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
