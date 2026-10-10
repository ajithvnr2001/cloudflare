---
url: https://developers.cloudflare.com/changelog/post/2025-10-09-workflows-terraform/
title: You can now deploy and manage Workflows in Terraform \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:47.884346+00:00
---

# You can now deploy and manage Workflows in Terraform · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-09-workflows-terraform/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 9, 2025

## You can now deploy and manage Workflows in Terraform

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create and manage [Workflows](https://developers.cloudflare.com/workflows/) using Terraform, now supported in the [Cloudflare Terraform provider v5.11.0 ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workflow). Workflows allow you to build durable, multi-step applications -- without needing to worry about retrying failed tasks or managing infrastructure.

Now, you can deploy and manage Workflows through Terraform using the new [`cloudflare_workflow` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workflow):
    
    
    resource "cloudflare_workflow" "my_workflow" {
      account_id    = var.account_id
      workflow_name = "my-workflow"
      class_name    = "MyWorkflow"
      script_name   = "my-worker"
    }

#### Examples

Here are full examples of how to configure `cloudflare_workflow` in Terraform, using the existing [`cloudflare_workers_script` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script), and the beta [`cloudflare_worker_version` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version).

#### With `cloudflare_workflow` and `cloudflare_workers_script`
    
    
    resource "cloudflare_workers_script" "workflow_worker" {
      account_id  = var.cloudflare_account_id
      script_name = "my-workflow-worker"
    
      content_file   = "${path.module}/../dist/worker/index.js"
      content_sha256 = filesha256("${path.module}/../dist/worker/index.js")
      main_module    = "index.js"
    }
    
    resource "cloudflare_workflow" "workflow" {
      account_id    = var.cloudflare_account_id
      workflow_name = "my-workflow"
      class_name    = "MyWorkflow"
      script_name   = cloudflare_workers_script.workflow_worker.script_name
    }

#### With `cloudflare_workflow`, and the new beta resources

You can more granularly control the lifecycle of each Worker resource using the beta [`cloudflare_worker_version` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/worker_version) resource, alongside the [`cloudflare_worker` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker) and [`cloudflare_workers_deployment` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_deployment) resources.
    
    
    resource "cloudflare_worker" "workflow_worker" {
      account_id = var.cloudflare_account_id
      name       = "my-workflow-worker"
    }
    
    resource "cloudflare_worker_version" "workflow_worker_version" {
      account_id = var.cloudflare_account_id
      worker_id  = cloudflare_worker.workflow_worker.id
    
      main_module         = "index.js"
    
      modules = [{
        name         = "index.js"
        content_file = "${path.module}/../dist/worker/index.js"
        content_type = "application/javascript+module"
      }]
    }
    
    resource "cloudflare_workers_deployment" "workflow_deployment" {
      account_id  = var.cloudflare_account_id
      script_name = cloudflare_worker.workflow_worker.name
    
      strategy = "percentage"
      versions = [{
        version_id = cloudflare_worker_version.workflow_worker_version.id
        percentage = 100
      }]
    }
    
    resource "cloudflare_workflow" "my_workflow" {
      account_id    = var.cloudflare_account_id
      workflow_name = "my-workflow"
      class_name    = "MyWorkflow"
      script_name   = cloudflare_worker.workflow_worker.name
    }

#### Try it out

  * Get started with [the Cloudflare Terraform provider (v5.11.0) ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs) and the new [`cloudflare_workflow` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workflow).


