---
url: https://developers.cloudflare.com/terraform/tutorial/initialize-terraform/
title: Introduction to Terraform init \u00b7 Cloudflare Terraform docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:01.584331+00:00
---

# Introduction to Terraform init · Cloudflare Terraform docs

> Source: https://developers.cloudflare.com/terraform/tutorial/initialize-terraform/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Terraform](https://developers.cloudflare.com/terraform/)
  3. /[Tutorials](https://developers.cloudflare.com/terraform/tutorial/)
  4. /1 – Initialize Terraform



# 1 – Initialize Terraform

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/terraform/tutorial/initialize-terraform/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview2\. Initialize and plan3\. Apply and verify

This tutorial shows you how to get started with Terraform. You just signed up your domain (`example.com`) on Cloudflare to manage everything in Terraform and now you will create a DNS record pointing `www.example.com` to a web server at `203.0.113.10`.

Before you begin, ensure you have:

  * [Installed Terraform](https://developers.cloudflare.com/terraform/installing/)
  * [Created an API Token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with permissions to edit resources for this tutorial



Note

Terraform code snippets below refer to the v5 SDK only.

## 1\. Create your configuration

Create a file named `main.tf`, filling in your own values for the [API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/), [zone ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/), [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/), and [domain](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/):
    
    
    terraform {
      required_providers {
        cloudflare = {
          source  = "cloudflare/cloudflare"
          version = "~> 5"
        }
      }
    }
    
    provider "cloudflare" {
      api_token = "<YOUR_API_TOKEN>"
    }
    
    variable "zone_id" {
      default = "<YOUR_ZONE_ID>"
    }
    
    variable "account_id" {
      default = "<YOUR_ACCOUNT_ID>"
    }
    
    variable "domain" {
      default = "<YOUR_DOMAIN>"
    }
    
    resource "cloudflare_dns_record" "www" {
      zone_id = "<YOUR_ZONE_ID>"
      name    = "www"
      content = "203.0.113.10"
      type    = "A"
      ttl     = 1
      proxied = true
      comment = "Domain verification record"
    }

Caution

To prevent accidentally exposing your Cloudflare credentials, do not save this file in your version control system. The [next tutorial](https://developers.cloudflare.com/terraform/tutorial/track-history/) will cover best practices for passing in your API token.

## 2\. Initialize and plan

Initialize Terraform to download the Cloudflare provider:
    
    
    terraform init

Review what will be created:
    
    
    terraform plan
    
    
    Terraform used the selected providers to generate the following execution plan. Resource actions are
    indicated with the following symbols:
      + create
    
    Terraform will perform the following actions:
    
      # cloudflare_dns_record.www will be created
      + resource "cloudflare_dns_record" "www" {
          + comment             = "Domain verification record"
          + comment_modified_on = (known after apply)
          + content             = "203.0.113.10"
          + created_on          = (known after apply)
          + id                  = (known after apply)
          + meta                = (known after apply)
          + modified_on         = (known after apply)
          + name                = "www"
          + proxiable           = (known after apply)
          + proxied             = true
          + settings            = (known after apply)
          + tags                = (known after apply)
          + tags_modified_on    = (known after apply)
          + ttl                 = 1
          + type                = "A"
          + zone_id             = "<YOUR_ZONE_ID>"
        }
    
    Plan: 1 to add, 0 to change, 0 to destroy.

## 3\. Apply and verify

Apply your configuration:
    
    
    terraform apply

Type `yes` when prompted.
    
    
    Terraform used the selected providers to generate the following execution plan. Resource actions are
    indicated with the following symbols:
      + create
    
    Terraform will perform the following actions:
    
      # cloudflare_dns_record.www will be created
      + resource "cloudflare_dns_record" "www" {
          + comment             = "Domain verification record"
          + comment_modified_on = (known after apply)
          + content             = "203.0.113.10"
          + created_on          = (known after apply)
          + id                  = (known after apply)
          + meta                = (known after apply)
          + modified_on         = (known after apply)
          + name                = "www"
          + proxiable           = (known after apply)
          + proxied             = true
          + settings            = (known after apply)
          + tags                = (known after apply)
          + tags_modified_on    = (known after apply)
          + ttl                 = 1
          + type                = "A"
          + zone_id             = "<YOUR_ZONE_ID>"
        }
    
    Plan: 1 to add, 0 to change, 0 to destroy.
    
    Do you want to perform these actions?
      Terraform will perform the actions described above.
      Only 'yes' will be accepted to approve.
    
      Enter a value: yes
    
    cloudflare_dns_record.www: Creating...
    cloudflare_dns_record.www: Creation complete after 0s
    
    Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

After creation, verify the DNS record:
    
    
    dig www.example.com

Test the web server response:
    
    
    curl https://www.example.com
    
    
    Hello, this is 203.0.113.10!

To see the full results returned from the API call:
    
    
    terraform show

You can also check the Cloudflare dashboard and go to the **DNS** > **Records** page.

[ Go to **Account home** ↗ ](https://dash.cloudflare.com/?to=/:account/home)

[PreviousOverview](https://developers.cloudflare.com/terraform/tutorial/)[Next2 – Track your history](https://developers.cloudflare.com/terraform/tutorial/track-history/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/terraform/tutorial/initialize-terraform.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
