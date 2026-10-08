---
url: https://developers.cloudflare.com/waf/detections/leaked-credentials/terraform-examples/
title: Terraform configuration examples \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:42.239672+00:00
---

# Terraform configuration examples · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/leaked-credentials/terraform-examples/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Traffic detections](https://developers.cloudflare.com/waf/detections/)

  4. /[Leaked credentials](https://developers.cloudflare.com/waf/detections/leaked-credentials/)
  5. /Terraform examples



# Terraform configuration examples

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/leaked-credentials/terraform-examples/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable leaked credentials detectionConfigure a custom detection locationAdd a custom rule to challenge requests with leaked credentialsMore resources

The following Terraform configuration examples address common scenarios for managing, configuring, and using leaked credentials detection.

For more information, refer to the [Terraform Cloudflare provider documentation ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs).

If you are using the Cloudflare API, refer to [Common API calls](https://developers.cloudflare.com/waf/detections/leaked-credentials/api-calls/).

## Enable leaked credentials detection

Use the `cloudflare_leaked_credential_check` resource to enable leaked credentials detection for a zone. For example:
    
    
    resource "cloudflare_leaked_credential_check" "zone_lcc_example" {
    	zone_id = var.cloudflare_zone_id
    	enabled = true
    }

## Configure a custom detection location

Use the `cloudflare_leaked_credential_check_rule` resource to add a custom detection location. For example:
    
    
    resource "cloudflare_leaked_credential_check_rule" "custom_location_example" {
    	zone_id = var.cloudflare_zone_id
    	username = "lookup_json_string(http.request.body.raw, \"user\")"
    	password = "lookup_json_string(http.request.body.raw, \"secret\")"
    }

You only need to provide an expression for the username in custom detection locations.

## Add a custom rule to challenge requests with leaked credentials

This example adds a [custom rule](https://developers.cloudflare.com/waf/custom-rules/) that challenges requests with leaked credentials by using one of the [leaked credentials fields](https://developers.cloudflare.com/waf/detections/leaked-credentials/#leaked-credentials-fields) in the rule expression.

To use the [`cf.waf.credential_check.username_and_password_leaked`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.credential_check.username_and_password_leaked/) field you must enable leaked credentials detection.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`



Configure the [`cloudflare_ruleset` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/ruleset) resource:
    
    
    resource "cloudflare_ruleset" "zone_custom_firewall_leaked_creds" {
      zone_id     = var.cloudflare_zone_id
      name        = "Phase entry point ruleset for custom rules in my zone"
      description = ""
      kind        = "zone"
      phase       = "http_request_firewall_custom"
    
      rules = [{
        ref         = "challenge_leaked_username_password"
        description = "Challenge requests with a leaked username and password"
        expression  = "(cf.waf.credential_check.username_and_password_leaked)"
        action      = "managed_challenge"
      }]
    }
    
    
    resource "cloudflare_ruleset" "zone_custom_firewall_leaked_creds" {
      zone_id     = var.cloudflare_zone_id
      name        = "Phase entry point ruleset for custom rules in my zone"
      description = ""
      kind        = "zone"
      phase       = "http_request_firewall_custom"
    
      rules {
        ref         = "challenge_leaked_username_password"
        description = "Challenge requests with a leaked username and password"
        expression  = "(cf.waf.credential_check.username_and_password_leaked)"
        action      = "managed_challenge"
      }
    }

## More resources

For additional Terraform configuration examples, refer to [WAF custom rules configuration using Terraform](https://developers.cloudflare.com/terraform/additional-configurations/waf-custom-rules/).

[PreviousCommon API calls](https://developers.cloudflare.com/waf/detections/leaked-credentials/api-calls/)[NextExample mitigation rules](https://developers.cloudflare.com/waf/detections/leaked-credentials/examples/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/leaked-credentials/terraform-examples.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
