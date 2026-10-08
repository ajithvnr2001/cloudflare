---
url: https://developers.cloudflare.com/basin-pipelines/reference/terraform/
title: Terraform \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:25.356916+00:00
---

# Terraform · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/reference/terraform/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /Reference
  4. /Terraform



# Terraform

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/reference/terraform/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesTerraform resourcesEnd-to-end example 1\. Define variables and provider 2\. Create the pipeline resources 3\. Define outputs 4\. DeployClean up

This example shows how to configure [Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/) and [Basin Catalog](https://developers.cloudflare.com/basin-catalog/) with Terraform using the [Cloudflare provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) (v5.19.0+).

Legacy product names

Terraform resource and API permission group names for Basin Catalog still use legacy R2 Data Catalog identifiers, such as `cloudflare_r2_data_catalog` and `Workers R2 Data Catalog Write`. These names will be updated in the coming weeks. Until then, use the identifiers shown in this guide.

The configuration creates a complete data pipeline: an R2 bucket with the data catalog enabled, a scoped API token for the sink, and the stream, sink, and pipeline resources that ingest JSON data into an [Apache Iceberg ↗︎](https://iceberg.apache.org/) table.

## Prerequisites

  * [Terraform CLI ↗︎](https://developer.hashicorp.com/terraform/downloads) `>= 1.0`
  * A Cloudflare account with R2 and Basin Pipelines enabled
  * An API token scoped to your account with the following permissions: 
    * **Basin Pipelines** \- Edit
    * **Workers R2 Storage** \- Edit
    * **Basin Catalog** \- Edit
    * **Account API Tokens** \- Edit



For general information on using Terraform with Cloudflare, refer to [the Terraform documentation](https://developers.cloudflare.com/terraform/).

## Terraform resources

This example uses the following Cloudflare Terraform resources:

Resource | Description  
---|---  
[`cloudflare_r2_bucket` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/r2_bucket) | Creates an R2 bucket to store pipeline data  
[`cloudflare_r2_data_catalog` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/r2_data_catalog) | Enables the Basin Catalog on a bucket  
[`cloudflare_pipeline_stream` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline_stream) | Creates a stream that receives events via HTTP or Worker bindings  
[`cloudflare_pipeline_sink` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline_sink) | Creates a sink that writes data to Basin Catalog or R2  
[`cloudflare_pipeline` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline) | Creates a pipeline with SQL that connects a stream to a sink  
[`cloudflare_account_token` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/account_token) | Creates a scoped API token for sink authentication  
  
## End-to-end example

With [`terraform` ↗︎](https://developer.hashicorp.com/terraform/downloads) installed, create a directory and the following files.

### 1\. Define variables and provider

Create `variables.tf`:
    
    
    terraform {
      required_providers {
        cloudflare = {
          source  = "cloudflare/cloudflare"
          version = "~> 5.19"
        }
      }
    }
    
    provider "cloudflare" {
      api_token = var.cloudflare_api_token
    }
    
    variable "cloudflare_api_token" {
      type      = string
      sensitive = true
    }
    
    variable "cloudflare_account_id" {
      type = string
    }

### 2\. Create the pipeline resources

Create `main.tf`:
    
    
    # --- R2 bucket and Data Catalog ---
    
    resource "cloudflare_r2_bucket" "pipeline_bucket" {
      account_id = var.cloudflare_account_id
      name       = "my-pipeline-bucket"
    }
    
    resource "cloudflare_r2_data_catalog" "pipeline_catalog" {
      account_id  = var.cloudflare_account_id
      bucket_name = cloudflare_r2_bucket.pipeline_bucket.name
    }
    
    # --- Scoped API token for the sink ---
    
    data "cloudflare_account_api_token_permission_groups_list" "r2_bucket_item_write" {
      account_id = var.cloudflare_account_id
      name       = "Workers R2 Storage Bucket Item Write"
    }
    
    data "cloudflare_account_api_token_permission_groups_list" "r2_data_catalog_write" {
      account_id = var.cloudflare_account_id
      name       = "Workers R2 Data Catalog Write"
    }
    
    resource "cloudflare_account_token" "sink_token" {
      name       = "pipeline-sink-token"
      account_id = var.cloudflare_account_id
    
      policies = [{
        effect = "allow"
        permission_groups = [
          { id = data.cloudflare_account_api_token_permission_groups_list.r2_bucket_item_write.result[0].id },
          { id = data.cloudflare_account_api_token_permission_groups_list.r2_data_catalog_write.result[0].id },
        ]
        resources = jsonencode({
          "com.cloudflare.api.account.${var.cloudflare_account_id}" = "*"
        })
      }]
    }
    
    # --- Stream ---
    
    resource "cloudflare_pipeline_stream" "my_stream" {
      account_id = var.cloudflare_account_id
      name       = "my_stream"
      format = {
        type = "json"
      }
      schema = {
        fields = [{
          name     = "value"
          type     = "json"
          required = true
        }]
      }
      http = {
        enabled        = true
        authentication = false
        cors           = {}
      }
      worker_binding = {
        enabled = false
      }
    }
    
    # --- Sink (Basin Catalog) ---
    
    resource "cloudflare_pipeline_sink" "my_sink" {
      account_id = var.cloudflare_account_id
      name       = "my_sink"
      type       = "r2_data_catalog"
      format = {
        type = "parquet"
      }
      schema = {
        fields = []
      }
      config = {
        account_id = var.cloudflare_account_id
        bucket     = cloudflare_r2_bucket.pipeline_bucket.name
        table_name = cloudflare_r2_data_catalog.pipeline_catalog.name
        token      = cloudflare_account_token.sink_token.value
      }
    }
    
    # --- Pipeline ---
    
    resource "cloudflare_pipeline" "my_pipeline" {
      account_id = var.cloudflare_account_id
      name       = "my_pipeline"
      sql        = "INSERT INTO ${cloudflare_pipeline_sink.my_sink.name} SELECT * FROM ${cloudflare_pipeline_stream.my_stream.name}"
    }

Use an R2 sink instead of Basin Catalog

To write raw Parquet or JSON files to R2 instead of Iceberg tables, replace the sink resource with an R2 sink. This requires R2 S3-compatible credentials instead of a catalog token.

Add variables for S3 credentials to `variables.tf`:
    
    
    variable "r2_access_key_id" {
      type      = string
      sensitive = true
    }
    
    variable "r2_access_key_secret" {
      type      = string
      sensitive = true
    }

Replace the sink resource in `main.tf`:
    
    
    resource "cloudflare_pipeline_sink" "my_sink" {
      account_id = var.cloudflare_account_id
      name       = "my_sink"
      type       = "r2"
      format = {
        type = "json"
      }
      schema = {
        fields = []
      }
      config = {
        account_id = var.cloudflare_account_id
        bucket     = cloudflare_r2_bucket.pipeline_bucket.name
        credentials = {
          access_key_id     = var.r2_access_key_id
          secret_access_key = var.r2_access_key_secret
        }
      }
    }

When using an R2 sink, you can remove the `cloudflare_r2_data_catalog`, `cloudflare_account_token`, and the two `cloudflare_account_api_token_permission_groups_list` data sources from your configuration.

### 3\. Define outputs

Create `outputs.tf`:
    
    
    output "pipeline_id" {
      value = cloudflare_pipeline.my_pipeline.id
    }
    
    output "pipeline_status" {
      value = cloudflare_pipeline.my_pipeline.status
    }
    
    output "stream_endpoint" {
      value = cloudflare_pipeline_stream.my_stream.endpoint
    }
    
    output "sink_id" {
      value = cloudflare_pipeline_sink.my_sink.id
    }

### 4\. Deploy

Set your environment variables:
    
    
    export TF_VAR_cloudflare_api_token="<YOUR_API_TOKEN>"
    export TF_VAR_cloudflare_account_id="<YOUR_ACCOUNT_ID>"

You can then use `terraform plan` to view the changes and `terraform apply` to apply them:
    
    
    terraform init
    terraform plan
    terraform apply

After the apply completes, Terraform outputs the stream endpoint URL. Use it to send data to your pipeline:
    
    
    curl -X POST https://<STREAM_ENDPOINT> \
      -H "Content-Type: application/json" \
      -d '[{"value": {"event": "page_view", "user_id": "user_123"}}]'

## Clean up

To remove all resources created by this configuration:
    
    
    terraform destroy

[PreviousLegacy pipelines](https://developers.cloudflare.com/basin-pipelines/reference/legacy-pipelines/)[NextWrangler commands](https://developers.cloudflare.com/basin-pipelines/reference/wrangler-commands/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/reference/terraform.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
