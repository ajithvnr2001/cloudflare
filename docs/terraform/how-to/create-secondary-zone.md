---
url: https://developers.cloudflare.com/terraform/how-to/create-secondary-zone/
title: Create a subdomain zone using Terraform \u00b7 Cloudflare Terraform docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:01.486683+00:00
---

# Create a subdomain zone using Terraform · Cloudflare Terraform docs

> Source: https://developers.cloudflare.com/terraform/how-to/create-secondary-zone/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Terraform](https://developers.cloudflare.com/terraform/)
  3. /How-to guides
  4. /Create a subdomain zone



# Create a subdomain zone using Terraform

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/terraform/how-to/create-secondary-zone/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesCreate the zoneRelated resources

A [subdomain zone](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/) lets you manage a subdomain in a separate Cloudflare zone from the parent domain. This is useful for access control and team management. This guide shows how to automate the setup using the [Cloudflare Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs). It is only available for Enterprise accounts

> NOTE: subdomain setup is only available for Enterprise accounts

## Prerequisites

  * Terraform installed. Refer to [Get started](https://developers.cloudflare.com/terraform/installing/).
  * Your Cloudflare account ID and a configured provider block. Refer to [Initialize Terraform](https://developers.cloudflare.com/terraform/tutorial/initialize-terraform/).



## Create the zone

Create a `cloudflare_zone` resource for the subdomain zone. The following example creates a zone for `subdomain.example.com`:
    
    
    resource "cloudflare_zone" "subdomain_example_com" {
      account = {
        id = var.cloudflare_account_id
      }
      name = "subdomain.example.com"
      type = "full"
    }

Terraform creates the zone in a **Pending** state. You must add NS delegation records to the parent zone before Cloudflare activates it.

Note

Refer to the [cloudflare_zone docs ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zone) in the Terraform provider documentation when you need to reference other zone properties.

## Related resources

  * [Subdomain setup](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/)
  * [`cloudflare_zone` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zone)
  * [`cloudflare_dns_record` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/dns_record)



[PreviousCreate a partial zone](https://developers.cloudflare.com/terraform/how-to/create-partial-zone/)[NextBest practices](https://developers.cloudflare.com/terraform/advanced-topics/best-practices/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/terraform/how-to/create-secondary-zone.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
