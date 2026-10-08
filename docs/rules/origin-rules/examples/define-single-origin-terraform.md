---
url: https://developers.cloudflare.com/rules/origin-rules/examples/define-single-origin-terraform/
title: Define a single origin rule using Terraform \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:49.661258+00:00
---

# Define a single origin rule using Terraform · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/origin-rules/examples/define-single-origin-terraform/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Origin Rules](https://developers.cloudflare.com/rules/origin-rules/)

  4. /[Examples](https://developers.cloudflare.com/rules/origin-rules/examples/)
  5. /Define a single origin rule using Terraform



# Define a single origin rule using Terraform

Create an origin rule using Terraform to override the `Host` header, the resolved hostname, and the destination port of API requests.

Last updated Aug 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/origin-rules/examples/define-single-origin-terraform/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdditional resources

Note

Terraform code snippets below refer to the v4 SDK only.

The following example defines a single origin rule for a zone using Terraform. The rule overrides the `Host` header, the resolved hostname, and the destination port of API requests.
    
    
    # Change origin for API requests
    resource "cloudflare_ruleset" "http_origin_example" {
      zone_id     = "<ZONE_ID>"
      name        = "Change origin"
      description = ""
      kind        = "zone"
      phase       = "http_request_origin"
    
      rules {
    	  ref         = "change_api_origin"
        description = "Change origin of API requests"
        expression  = "(http.request.uri.path matches \"^/api/\")"
        action      = "route"
        action_parameters {
          host_header = "example.net"
          origin {
            host = "example.net"
            port = 8000
          }
        }
      }
    }

Use the `ref` field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to [Troubleshooting](https://developers.cloudflare.com/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications) in the Terraform documentation.

## Additional resources

For additional guidance on using Terraform with Cloudflare, refer to the following resources:

  * [Terraform documentation](https://developers.cloudflare.com/terraform/)
  * [Cloudflare Provider for Terraform ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) (reference documentation)



[PreviousChange the HTTP Host header and DNS record](https://developers.cloudflare.com/rules/origin-rules/examples/change-http-host-header/)[NextOverview](https://developers.cloudflare.com/rules/origin-rules/tutorials/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/origin-rules/examples/define-single-origin-terraform.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
