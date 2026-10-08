---
url: https://developers.cloudflare.com/rules/url-forwarding/single-redirects/terraform-example/
title: Create a redirect rule using Terraform \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:00.676530+00:00
---

# Create a redirect rule using Terraform · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/single-redirects/terraform-example/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)

  4. /[Single Redirects](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/)
  5. /Create rule using Terraform



# Create a redirect rule using Terraform

Last updated Aug 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/terraform-example/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdditional resources

Note

Terraform code snippets below refer to the v4 SDK only.

The following example defines a single redirect rule for a zone using Terraform. The rule creates a static URL redirect for visitors requesting the contacts page using an old URL.
    
    
    # Single Redirects resource
    resource "cloudflare_ruleset" "single_redirects_example" {
      zone_id     = "<ZONE_ID>"
      name        = "redirects"
      description = "Redirects ruleset"
      kind        = "zone"
      phase       = "http_request_dynamic_redirect"
    
      rules {
        ref         = "redirect_old_url"
        description = "Redirect visitors still using old URL"
        expression  = "(http.request.uri.path matches \"^/contact-us/\")"
        action      = "redirect"
        action_parameters {
          from_value {
            status_code = 301
            target_url {
              value = "/contacts/"
            }
            preserve_query_string = false
          }
        }
      }
    }

Use the `ref` field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to [Troubleshooting](https://developers.cloudflare.com/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications) in the Terraform documentation.

## Additional resources

For additional guidance on using Terraform with Cloudflare, refer to the following resources:

  * [Terraform documentation](https://developers.cloudflare.com/terraform/)
  * [Cloudflare Provider for Terraform ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) (reference documentation)



[PreviousCreate rule via API](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/create-api/)[NextAvailable settings](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/settings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/single-redirects/terraform-example.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
