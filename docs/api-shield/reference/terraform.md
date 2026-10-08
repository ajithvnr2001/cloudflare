---
url: https://developers.cloudflare.com/api-shield/reference/terraform/
title: Terraform \u00b7 Cloudflare API Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:18.444686+00:00
---

# Terraform · Cloudflare API Shield docs

> Source: https://developers.cloudflare.com/api-shield/reference/terraform/

  1. [Home](https://developers.cloudflare.com/)
  2. /[API Shield](https://developers.cloudflare.com/api-shield/)
  3. /Reference
  4. /Terraform



# Terraform

Last updated Aug 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/api-shield/reference/terraform/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewManage API Shield session identifiersManage Web Assets operationsManage Schema validationValidate JWTs

Get started with API Shield using Terraform from the examples below. For more information on how to use Terraform with Cloudflare, refer to the [Terraform documentation](https://developers.cloudflare.com/terraform/).

The following resources are available to configure through Terraform:

**Session identifiers**

  * [`api_shield` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_shield) for configuring session identifiers in API Shield.



**Web Assets operations**

  * [`api_shield_operation` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_shield_operation) for configuring operations.



**Schema validation**

  * [`cloudflare_schema_validation_schemas` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/schema_validation_schemas) for configuring a schema in [Schema validation](https://developers.cloudflare.com/api-shield/security/schema-validation/). ~~[`api_shield_schema` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_shield_schema)~~ has been deprecated and will be removed in a future version of the terraform provider.



**JWT Validation**

  * [`cloudflare_token_validation_config` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/token_validation_config) for setting up JWT validation with specific keying material and token locations.
  * [`cloudflare_token_validation_rules` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/token_validation_rules) for setting up rules to action on the validation result.



## Manage API Shield session identifiers

Refer to the example configuration below to set up [session identifiers](https://developers.cloudflare.com/api-shield/get-started/#to-set-up-session-identifiers) on your zone.

Example configurationtf
    
    
    resource "cloudflare_api_shield" "session_identifiers" {
      zone_id = var.zone_id
      auth_id_characteristics = [{
        name = "authorization"
        type = "header"
      }]
    }

## Manage Web Assets operations

Manage operations by method, hostname, and path. Operations appear in the Web Assets inventory.

Example configurationtf
    
    
    resource "cloudflare_api_shield_operation" "get_image" {
      zone_id  = var.zone_id
      method   = "GET"
      host     = "example.com"
      endpoint = "/api/images/{var1}"
    }
    
    resource "cloudflare_api_shield_operation" "post_image" {
      zone_id  = var.zone_id
      method   = "POST"
      host     = "example.com"
      endpoint = "/api/images/{var1}"
    }

## Manage Schema validation

Note

Configure Web Assets operations before activating uploaded schema evaluation with Terraform.

The schema resource uploads an OpenAPI schema. Setting `validation_enabled` to `true` makes uploaded profile evaluation available.

Example configurationtf
    
    
    # Upload an OpenAPI schema for Schema Validation
    resource "cloudflare_schema_validation_schemas" "example_schema" {
      zone_id            = var.zone_id
      kind               = "openapi_v3"
      name               = "example-schema.yaml"
      # In this example, we assume that the `example-schema.yaml` includes `get_image` and `post_image` operations from above
      source             = file("./schemas/example-schema.yaml")
      validation_enabled = true
    }

Activation does not configure mitigation. Use `cf.schema_validation.uploaded.violated` in [WAF Custom Rules](https://developers.cloudflare.com/waf/detections/application-profiles/enforce-profiles-with-custom-rules/).

## Validate JWTs

Refer to the example configuration below to perform [JWT Validation](https://developers.cloudflare.com/api-shield/security/jwt-validation/) on your zone.

Example configurationtf
    
    
    # Setting up JWT validation with specific keying material and location of the token
    resource "cloudflare_token_validation_config" "example_es256_config" {
      zone_id       = var.zone_id
      token_type    = "JWT"
      title         = "ES256 Example"
      description   = "An example configuration that validates ES256 JWTs with `b0078548-c9bc-46e5-a678-06fb72443427` key ID in the authorization header"
      token_sources = ["http.request.headers[\"authorization\"][0]"]
      credentials   = {
        keys = [
          {
            alg = "ES256"
            kid = "b0078548-c9bc-46e5-a678-06fb72443427"
            kty = "EC"
            crv = "P-256"
            x   = "yl_BZSxUG5II7kJCMxDfWImiU6zkcJcBYaTgzV3Jgnk"
            y   = "0qAzLQe_YGEdotb54qWq00k74QdiTOiWnuw_YzuIqr0"
          }
        ]
      }
    }
    
    # Setting up JWT rules for all configured endpoints on `example.com` except for `get_image`
    resource "cloudflare_token_validation_rules" "example_com" {
     zone_id      = var.zone_id
     title        = "Validate JWTs on example.com"
     description  = "This actions JWT validation results for requests to example.com except for the get_image endpoint"
     action       = "block"
     enabled      = true
     # Require that the JWT described through the example_es256_config is valid.
     # Reference the ID of the generated token config, this constructs: is_jwt_valid("<id>")
     # If the expression is >not true<, Cloudflare will perform the configured action on the request
     expression   = format("(is_jwt_valid(%q))", cloudflare_token_validation_config.example_es256_config.id)
     selector     = {
        # all current and future operations matching this include selector will perform the described action when the expression fails to match
        include = [
          {
            host          = ["example.com"]
          }
        ]
        exclude = [
          {
            # reference the ID of the get_image operation to exclude it
            operation_ids = ["${cloudflare_api_shield_operation.get_image.id}"]
          }
        ]
     }
    }
    
    # With JWT validation, we can also refine session identifiers to use claims from the JWT
    resource "cloudflare_api_shield" "session_identifiers" {
      zone_id = var.zone_id
      auth_id_characteristics = [{
        # select the JWT's `sub` claim as an extremely stable session identifier
        # this is "<token_config_id:json_path>" format
        name = "${cloudflare_token_validation_config.example_es256_config.id}:$.sub"
        type = "jwt"
      }]
    }

[PreviousClassic Schema validation](https://developers.cloudflare.com/api-shield/reference/classic-schema-validation/)[NextAPI Gateway](https://developers.cloudflare.com/api-shield/api-gateway/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/api-shield/reference/terraform.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
