---
url: https://developers.cloudflare.com/rules/cloud-connector/create-terraform/
title: Configure Cloud Connector rules using Terraform \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:45.736772+00:00
---

# Configure Cloud Connector rules using Terraform · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/cloud-connector/create-terraform/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/)
  4. /Configure rules using Terraform



# Configure Cloud Connector rules using Terraform

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/cloud-connector/create-terraform/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRequired permissionsExample configurationMore resources

You can create Cloud Connector rules using the [Terraform Cloudflare provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest).

To get started with Terraform for Cloudflare configuration, refer to [Get started](https://developers.cloudflare.com/terraform/installing/).

## Required permissions

The [API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) used by Terraform must have at least the following permission:

  * _Zone_ > _Cloud Connector_ > _Write_



## Example configuration

Note

Terraform code snippets below refer to the v4 SDK only.

The following example Terraform configuration creates Cloud Connector rules for various [supported providers](https://developers.cloudflare.com/rules/cloud-connector/providers/) to route traffic between them based on URI paths:
    
    
    resource "cloudflare_cloud_connector_rules" "cloud_connector_rules" {
      zone_id = "<ZONE_ID>"
    
      rules {
        description = "Route /data to GCP bucket"
        enabled     = true
        expression  = "(http.request.uri.path wildcard \"*/data/*\")"
        provider    = "gcp_storage"
        parameters {
          host = "mystorage.storage.googleapis.com"
        }
      }
    
      rules {
        description = "Route /resources to AWS bucket"
        enabled     = true
        expression  = "(http.request.uri.path wildcard \"*/resources/*\")"
        provider    = "aws_s3"
        parameters {
          host = "mystorage.s3.ams.amazonaws.com"
        }
      }
    
      rules {
        description = "Route /files to Azure bucket"
        enabled     = true
        expression  = "(http.request.uri.path wildcard \"*/files/*\")"
        provider    = "azure_storage"
        parameters {
          host = "mystorage.blob.core.windows.net"
        }
      }
    
      rules {
        description = "Route /images to R2 bucket"
        enabled     = true
        expression  = "(http.request.uri.path wildcard \"*/images/*\")"
        provider    = "cloudflare_r2"
        parameters {
          host = "mybucketcustomdomain.example.com"
        }
      }
    }

## More resources

Refer to the [Terraform Cloudflare provider documentation ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) for more information on the `cloudflare_cloud_connector_rules` resource.

[PreviousConfigure a rule via API](https://developers.cloudflare.com/rules/cloud-connector/create-api/)[NextSupported cloud providers](https://developers.cloudflare.com/rules/cloud-connector/providers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/cloud-connector/create-terraform.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
