---
url: https://developers.cloudflare.com/changelog/post/2025-10-09-assets-terraform/
title: You can now deploy full-stack apps on Workers using Terraform \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:25.843301+00:00
---

# You can now deploy full-stack apps on Workers using Terraform · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-09-assets-terraform/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 9, 2025

## You can now deploy full-stack apps on Workers using Terraform

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-09-assets-terraform/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now upload Workers with [static assets](https://developers.cloudflare.com/workers/static-assets/) (like HTML, CSS, JavaScript, images) with the [Cloudflare Terraform provider v5.11.0 ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs), making it even easier to deploy and manage full-stack apps with IaC.

**Previously** , you couldn't use Terraform to upload static assets without writing custom scripts to handle generating an [asset manifest](https://developers.cloudflare.com/workers/static-assets/direct-upload/#upload-manifest), calling the [Cloudflare API to upload assets in chunks](https://developers.cloudflare.com/workers/static-assets/direct-upload/#upload-static-assets), and handling change detection.

**Now** , you simply define the directory where your assets are built, and we handle the rest. Check out the [examples](https://developers.cloudflare.com/changelog/#examples) for what this looks like in Terraform configuration.

You can get started today with [the Cloudflare Terraform provider (v5.11.0) ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs), using either the existing [`cloudflare_workers_script` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script), or the beta [`cloudflare_worker_version` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version).

#### Examples

#### With `cloudflare_workers_script`

Here's how you can use the existing [`cloudflare_workers_script` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_script) resource to upload your Worker code and assets in one shot.
    
    
    resource "cloudflare_workers_script" "my_app" {
      account_id  = var.account_id
      script_name = "my-app"
    
      content_file   = "./dist/worker/index.js"
      content_sha256 = filesha256("./dist/worker/index.js")
      main_module    = "index.js"
    
      # Just point to your assets directory - that's it!
      assets = {
        directory = "./dist/static"
      }
    }

#### With `cloudflare_worker`, `cloudflare_worker_version`, and `cloudflare_workers_deployment`

And here's an example using the beta [`cloudflare_worker_version` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/worker_version) resource, alongside the [`cloudflare_worker` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker) and [`cloudflare_workers_deployment` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_deployment) resources:
    
    
    # This tracks the existence of your Worker, so that you
    # can upload code and assets separately from tracking Worker state.
    
    resource "cloudflare_worker" "my_app" {
      account_id = var.account_id
      name       = "my-app"
    }
    
    resource "cloudflare_worker_version" "my_app_version" {
      account_id = var.account_id
      worker_id  = cloudflare_worker.my_app.id
    
      # Just point to your assets directory - that's it!
      assets = {
        directory = "./dist/static"
      }
    
      modules = [{
        name         = "index.js"
        content_file = "./dist/worker/index.js"
        content_type = "application/javascript+module"
      }]
    }
    
    resource "cloudflare_workers_deployment" "my_app_deployment" {
      account_id  = var.account_id
      script_name = cloudflare_worker.my_app.name
    
      strategy = "percentage"
      versions = [{
        version_id = cloudflare_worker_version.my_app_version.id
        percentage = 100
      }]
    }

#### What's changed

Under the hood, the Cloudflare Terraform provider now handles the same logic that Wrangler uses for static asset uploads. This includes scanning your assets directory, computing hashes for each file, generating a manifest with file metadata, and calling the Cloudflare API to upload any missing files in chunks. We support large directories with parallel uploads and chunking, and when the asset manifest hash changes, we detect what's changed and trigger an upload for _only_ those changed files.

#### Try it out

  * Get started with [the Cloudflare Terraform provider (v5.11.0) ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs)
  * You can use either the existing [`cloudflare_workers_script` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script) to upload your Worker code and assets in one resource.
  * Or you can use the new beta [`cloudflare_worker_version` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version) (along with the [`cloudflare_worker` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker) and [`cloudflare_workers_deployment` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_deployment)) resources to more granularly control the lifecycle of each Worker resource.


