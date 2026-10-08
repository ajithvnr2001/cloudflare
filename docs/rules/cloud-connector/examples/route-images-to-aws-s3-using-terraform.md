---
url: https://developers.cloudflare.com/rules/cloud-connector/examples/route-images-to-aws-s3-using-terraform/
title: Route /images to an S3 Bucket using Terraform \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:45.863486+00:00
---

# Route /images to an S3 Bucket using Terraform · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/cloud-connector/examples/route-images-to-aws-s3-using-terraform/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/)

  4. /[Examples](https://developers.cloudflare.com/rules/cloud-connector/examples/)
  5. /Route /images to an S3 Bucket using Terraform



# Route /images to an S3 Bucket using Terraform

Route requests with a URI path starting with `/images` to a specific AWS S3 bucket with Cloud Connector using Terraform.

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/cloud-connector/examples/route-images-to-aws-s3-using-terraform/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdditional resources

Note

Terraform code snippets below refer to the v4 SDK only.

The following example defines a single Cloud Connector rule for a zone using Terraform. The rule routes requests to `/images` on your domain to an AWS S3 bucket.
    
    
    resource "cloudflare_cloud_connector_rules" "serve_images_in_aws" {
      zone_id = "<ZONE_ID>"
      rules {
        description = "Route images to AWS S3 bucket"
        enabled     = true
        expression  = "http.request.full_uri wildcard \"https://<YOUR_HOSTNAME>/images/*\""
        provider    = "aws_s3"
        parameters {
          host = "<BUCKET_NAME>.s3.amazonaws.com"
        }
      }
    }

## Additional resources

For additional guidance on using Terraform with Cloudflare, refer to the following resources:

  * [Terraform documentation](https://developers.cloudflare.com/terraform/)
  * [Cloudflare Provider for Terraform ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) (reference documentation)



[PreviousRoute /images to an S3 Bucket](https://developers.cloudflare.com/rules/cloud-connector/examples/route-images-to-s3/)[NextSend EU visitors to a Google Cloud Storage bucket](https://developers.cloudflare.com/rules/cloud-connector/examples/send-eu-visitors-to-gcs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/cloud-connector/examples/route-images-to-aws-s3-using-terraform.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
