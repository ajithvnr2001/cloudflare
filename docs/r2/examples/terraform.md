---
url: https://developers.cloudflare.com/r2/examples/terraform/
title: Terraform \u00b7 Cloudflare R2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:46.475326+00:00
---

# Terraform · Cloudflare R2 docs

> Source: https://developers.cloudflare.com/r2/examples/terraform/

  1. [Home](https://developers.cloudflare.com/)
  2. /[R2](https://developers.cloudflare.com/r2/)
  3. /[Examples](https://developers.cloudflare.com/r2/examples/)
  4. /Terraform



# Terraform

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/r2/examples/terraform/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You must [generate an Access Key](https://developers.cloudflare.com/r2/api/tokens/) before getting started. All examples will utilize `access_key_id` and `access_key_secret` variables which represent the **Access Key ID** and **Secret Access Key** values you generated.

  


This example shows how to configure R2 with Terraform using the [Cloudflare provider ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

Note for using AWS provider

When using the Cloudflare Terraform provider, you can only manage buckets. To configure items such as CORS and object lifecycles, you will need to use the [AWS Provider](https://developers.cloudflare.com/r2/examples/terraform-aws/).

With [`terraform` ↗︎](https://developer.hashicorp.com/terraform/downloads) installed, create `main.tf` and copy the content below replacing with your API Token.
    
    
    terraform {
      required_providers {
        cloudflare = {
          source = "cloudflare/cloudflare"
          version = "~> 4"
        }
      }
    }
    
    provider "cloudflare" {
      api_token = "<YOUR_API_TOKEN>"
    }
    
    resource "cloudflare_r2_bucket" "cloudflare-bucket" {
      account_id = "<YOUR_ACCOUNT_ID>"
      name       = "my-tf-test-bucket"
      location   = "WEUR"
    }

You can then use `terraform plan` to view the changes and `terraform apply` to apply changes.

[Previouss3mini](https://developers.cloudflare.com/r2/examples/aws/s3mini/)[NextTerraform (AWS)](https://developers.cloudflare.com/r2/examples/terraform-aws/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/r2/examples/terraform.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
