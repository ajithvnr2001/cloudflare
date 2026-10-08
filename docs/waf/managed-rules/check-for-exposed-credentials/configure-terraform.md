---
url: https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/configure-terraform/
title: Configure exposed credentials checks using Terraform \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:43.956838+00:00
---

# Configure exposed credentials checks using Terraform · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/configure-terraform/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Managed rules](https://developers.cloudflare.com/waf/managed-rules/)

  4. /[Check for exposed credentials](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/)
  5. /Configure using Terraform



# Configure exposed credentials checks using Terraform

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/configure-terraform/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdd a custom rule to check for exposed credentialsMore resources

Deprecation notice

Exposed credentials check has been deprecated.

Switch from exposed credentials check to [leaked credentials detection](https://developers.cloudflare.com/waf/detections/leaked-credentials/) for improved security. To upgrade your current configuration, refer to the [upgrade guide](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/).

The following Terraform configuration example addresses a common use case of exposed credentials checks.

For more information, refer to the [Terraform Cloudflare provider documentation ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs).

If you are using the Cloudflare API, refer to [Configure exposed credentials checks via API](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/configure-api/).

## Add a custom rule to check for exposed credentials

The following configuration creates a custom ruleset with a single rule that [checks for exposed credentials](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/configure-api/#create-a-custom-rule-checking-for-exposed-credentials).

You can only add exposed credential checks to rules in a custom ruleset (that is, a ruleset with `kind = "custom"`).

Note

Terraform code snippets below refer to the v4 SDK only.
    
    
    resource "cloudflare_ruleset" "account_firewall_custom_ruleset_exposed_creds" {
      account_id  = "<ACCOUNT_ID>"
      name        = "Custom ruleset checking for exposed credentials"
      description = ""
      kind        = "custom"
      phase       = "http_request_firewall_custom"
    
      rules {
        ref         = "check_for_exposed_creds_add_header"
        description = "Add header when there is a rule match and exposed credentials are detected"
        expression  = "http.request.method == \"POST\" && http.request.uri == \"/login.php\""
        action      = "rewrite"
        action_parameters {
          headers {
            name      = "Exposed-Credential-Check"
            operation = "set"
            value     = "1"
          }
        }
        exposed_credential_check {
          username_expression = "url_decode(http.request.body.form[\"username\"][0])"
          password_expression = "url_decode(http.request.body.form[\"password\"][0])"
        }
      }
    }

To create another rule, add a new `rules` object to the same `cloudflare_ruleset` resource.

The following configuration deploys the custom ruleset. It defines a dependency on the `account_firewall_custom_ruleset_exposed_creds` resource and obtains the ID of the created custom ruleset:

Note

Terraform code snippets below refer to the v4 SDK only.
    
    
    resource "cloudflare_ruleset" "account_firewall_custom_entrypoint" {
      account_id  = "<ACCOUNT_ID>"
      name        = "Account-level entry point ruleset for the http_request_firewall_custom phase deploying a custom ruleset checking for exposed credentials"
      description = ""
      kind        = "root"
      phase       = "http_request_firewall_custom"
    
      depends_on = [cloudflare_ruleset.account_firewall_custom_ruleset_exposed_creds]
    
      rules {
        ref         = "deploy_custom_ruleset_example_com"
        description = "Deploy custom ruleset for example.com"
        expression  = "(cf.zone.name eq \"example.com\")"
        action      = "execute"
        action_parameters {
          id = cloudflare_ruleset.account_firewall_custom_ruleset_exposed_creds.id
        }
      }
    }

## More resources

For additional Terraform configuration examples, refer to [WAF custom rules configuration using Terraform](https://developers.cloudflare.com/terraform/additional-configurations/waf-custom-rules/).

[PreviousConfigure via API](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/configure-api/)[NextTest your configuration](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/test-configuration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/managed-rules/check-for-exposed-credentials/configure-terraform.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
