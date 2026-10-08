---
url: https://developers.cloudflare.com/turnstile/get-started/widget-management/terraform/
title: Create and manage widgets using Terraform \u00b7 Cloudflare Turnstile docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:07.305412+00:00
---

# Create and manage widgets using Terraform · Cloudflare Turnstile docs

> Source: https://developers.cloudflare.com/turnstile/get-started/widget-management/terraform/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Turnstile](https://developers.cloudflare.com/turnstile/)
  3. /…

[Get started](https://developers.cloudflare.com/turnstile/get-started/)

  4. /Widget management
  5. /Terraform



# Create and manage widgets using Terraform

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/turnstile/get-started/widget-management/terraform/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesSetup 1\. Configure provider 2\. Define widgets 3\. Environment variablesTerraform commands Initialize and plan Manage changesAdvanced Terraform configuration Multiple environments Widget with Enterprise featuresImport existing widgets

Manage Turnstile widgets as code using Terraform for version control and automated deployments.

## Prerequisites

Before you begin, you must have:

  * [Terraform ↗︎](https://terraform.io/) installed
  * A Cloudflare API token with `Account:Turnstile:Edit permissions`
  * (Optional) A `cf-terraforming` tool for importing existing widgets



## Setup

### 1\. Configure provider

Create a `main.tf` file.

Note

Terraform code snippets below refer to the v4 SDK only.
    
    
    terraform {
      required_providers {
        cloudflare = {
          source  = "cloudflare/cloudflare"
          version = "~> 4.0"
        }
      }
    }
    
    provider "cloudflare" {
      api_token = var.cloudflare_api_token
    }
    
    variable "cloudflare_api_token" {
      description = "Cloudflare API Token"
      type        = string
      sensitive   = true
    }
    
    variable "account_id" {
      description = "Cloudflare Account ID"
      type        = string
    }

### 2\. Define widgets
    
    
    resource "cloudflare_turnstile_widget" "login_form" {
      account_id = var.account_id
      name       = "Login Form Widget"
      domains    = ["example.com", "www.example.com"]
      mode       = "managed"
      region     = "world"
    }
    
    resource "cloudflare_turnstile_widget" "api_protection" {
      account_id = var.account_id
      name       = "API Protection"
      domains    = ["api.example.com"]
      mode       = "invisible"
      region     = "world"
    }
    
    # Output the sitekeys for use in your application
    output "login_sitekey" {
      value = cloudflare_turnstile_widget.login_form.sitekey
    }
    
    output "api_sitekey" {
      value = cloudflare_turnstile_widget.api_protection.sitekey
    }

### 3\. Environment variables

Create a `.env` file or set environment variables.
    
    
    export TF_VAR_cloudflare_api_token="your-api-token"
    export TF_VAR_account_id="your-account-id"

* * *

## Terraform commands

### Initialize and plan

Initialize Terraformshell
    
    
    terraform init

Plan changesshell
    
    
    terraform plan

Apply configurationshell
    
    
    terraform apply

### Manage changes

Update widget configurationshell
    
    
    terraform plan

Apply changesshell
    
    
    terraform apply

Destroy widgetsshell
    
    
    terraform destroy

* * *

## Advanced Terraform configuration

### Multiple environments
    
    
    locals {
      environments = {
        dev = {
          domains = ["dev.example.com"]
          mode    = "managed"
        }
        staging = {
          domains = ["staging.example.com"]
          mode    = "non_interactive"
        }
        prod = {
          domains = ["example.com", "www.example.com"]
          mode    = "invisible"
        }
      }
    }
    
    resource "cloudflare_turnstile_widget" "app_widget" {
      for_each = local.environments
      
      account_id = var.account_id
      name       = "App Widget - ${each.key}"
      domains    = each.value.domains
      mode       = each.value.mode
      region     = "world"
    }

### Widget with Enterprise features
    
    
    resource "cloudflare_turnstile_widget" "enterprise_widget" {
      account_id     = var.account_id
      name          = "Enterprise Form"
      domains       = ["enterprise.example.com"]
      mode          = "managed"
      region        = "world"
      offlabel      = true  # Remove Cloudflare branding
      bot_fight_mode = true # Enable bot fight mode
    }

* * *

## Import existing widgets

Use [`cf-terraforming`](https://developers.cloudflare.com/terraform/advanced-topics/import-cloudflare-resources/#cf-terraforming) to import existing widgets.

Install cf-terraformingshell
    
    
    go install github.com/cloudflare/cf-terraforming/cmd/cf-terraforming@latest

Generate Terraform configuration from existing widgetsshell
    
    
    cf-terraforming generate \
      --resource-type cloudflare_turnstile_widget \
      --account $ACCOUNT_ID

Import existing widgetshell
    
    
    terraform import cloudflare_turnstile_widget.existing_widget \
      $ACCOUNT_ID/$WIDGET_SITEKEY

[PreviousAPI](https://developers.cloudflare.com/turnstile/get-started/widget-management/api/)[NextOverview](https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/turnstile/get-started/widget-management/terraform.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
