---
url: https://developers.cloudflare.com/rules/configuration-rules/examples/define-single-configuration-terraform/
title: Define a single configuration rule using Terraform \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:48.254145+00:00
---

# Define a single configuration rule using Terraform · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/configuration-rules/examples/define-single-configuration-terraform/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/)

  4. /[Examples](https://developers.cloudflare.com/rules/configuration-rules/examples/)
  5. /Define a single configuration rule using Terraform



# Define a single configuration rule using Terraform

Create a configuration rule using Terraform to turn off Email Obfuscation and Browser Integrity Check for API requests in a given zone.

Last updated Aug 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/configuration-rules/examples/define-single-configuration-terraform/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdditional resources

Note

Terraform code snippets below refer to the v4 SDK only.

The following example defines a single configuration rule for a zone using Terraform. The rule disables Email Obfuscation and Browser Integrity Check for API requests.
    
    
    # Disable a couple of Cloudflare settings for API requests
    resource "cloudflare_ruleset" "http_config_rules_example" {
      zone_id     = "<ZONE_ID>"
      name        = "Config rules ruleset"
      description = "Set configuration rules for incoming requests"
      kind        = "zone"
      phase       = "http_config_settings"
    
      rules {
        ref         = "disable_obfuscation_bic"
        description = "Disable email obfuscation and BIC for API requests"
        expression  = "(http.request.uri.path matches \"^/api/\")"
        action      = "set_config"
        action_parameters {
          email_obfuscation = false
          bic               = false
        }
      }
    }

Use the `ref` field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to [Troubleshooting](https://developers.cloudflare.com/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications) in the Terraform documentation.

## Additional resources

For additional guidance on using Terraform with Cloudflare, refer to the following resources:

  * [Terraform documentation](https://developers.cloudflare.com/terraform/)
  * [Cloudflare Provider for Terraform ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) (reference documentation)



[PreviousOverview](https://developers.cloudflare.com/rules/configuration-rules/examples/)[NextOverview](https://developers.cloudflare.com/rules/snippets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/configuration-rules/examples/define-single-configuration-terraform.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
