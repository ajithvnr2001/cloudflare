---
url: https://developers.cloudflare.com/waf/detections/malicious-uploads/terraform-examples/
title: Terraform configuration examples \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:42.452611+00:00
---

# Terraform configuration examples · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/malicious-uploads/terraform-examples/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Traffic detections](https://developers.cloudflare.com/waf/detections/)

  4. /[Malicious uploads](https://developers.cloudflare.com/waf/detections/malicious-uploads/)
  5. /Terraform examples



# Terraform configuration examples

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/malicious-uploads/terraform-examples/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable WAF content scanningConfigure a custom scan expressionAdd a custom rule to block malicious uploadsMore resources

The following Terraform configuration examples address common scenarios for managing, configuring, and using WAF content scanning.

For more information, refer to the [Terraform Cloudflare provider documentation ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs).

If you are using the Cloudflare API, refer to [Common API calls](https://developers.cloudflare.com/waf/detections/malicious-uploads/api-calls/).

## Enable WAF content scanning

Use the `cloudflare_content_scanning` resource to enable content scanning for a zone. For example:
    
    
    resource "cloudflare_content_scanning" "zone_content_scanning_example" {
    	zone_id = var.cloudflare_zone_id
    	enabled = true
    }

## Configure a custom scan expression

Use the `cloudflare_content_scanning_expression` resource to add a custom scan expression. For example:
    
    
    resource "cloudflare_content_scanning_expression" "my_custom_scan_expression" {
      zone_id = var.cloudflare_zone_id
      payload = "lookup_json_string(http.request.body.raw, \"file\")"
    }

For more information, refer to [Custom scan expressions](https://developers.cloudflare.com/waf/detections/malicious-uploads/#custom-scan-expressions).

## Add a custom rule to block malicious uploads

This example adds a [custom rule](https://developers.cloudflare.com/waf/custom-rules/) that blocks requests with one or more content objects considered malicious by using one of the [content scanning fields](https://developers.cloudflare.com/waf/detections/malicious-uploads/#content-scanning-fields) in the rule expression.

To use the [`cf.waf.content_scan.has_malicious_obj`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.has_malicious_obj/) field you must enable content scanning.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`



Configure the [`cloudflare_ruleset` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/ruleset) resource:
    
    
    resource "cloudflare_ruleset" "zone_custom_firewall_malicious_uploads" {
      zone_id     = var.cloudflare_zone_id
      name        = "Phase entry point ruleset for custom rules in my zone"
      description = ""
      kind        = "zone"
      phase       = "http_request_firewall_custom"
    
      rules = [{
        ref         = "block_malicious_uploads"
        description = "Block requests uploading malicious content objects"
        expression  = "(cf.waf.content_scan.has_malicious_obj and http.request.uri.path eq \"/upload.php\")"
        action      = "block"
      }]
    }
    
    
    resource "cloudflare_ruleset" "zone_custom_firewall_malicious_uploads" {
      zone_id     = var.cloudflare_zone_id
      name        = "Phase entry point ruleset for custom rules in my zone"
      description = ""
      kind        = "zone"
      phase       = "http_request_firewall_custom"
    
      rules {
        ref         = "block_malicious_uploads"
        description = "Block requests uploading malicious content objects"
        expression  = "(cf.waf.content_scan.has_malicious_obj and http.request.uri.path eq \"/upload.php\")"
        action      = "block"
      }
    }

## More resources

For additional Terraform configuration examples, refer to [WAF custom rules configuration using Terraform](https://developers.cloudflare.com/terraform/additional-configurations/waf-custom-rules/).

[PreviousCommon API calls](https://developers.cloudflare.com/waf/detections/malicious-uploads/api-calls/)[NextOverview](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/malicious-uploads/terraform-examples.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
