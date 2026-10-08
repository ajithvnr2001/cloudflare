---
url: https://developers.cloudflare.com/learning-paths/replace-vpn/get-started/create-zero-trust-org/
title: Create a Zero Trust organization \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:54.586705+00:00
---

# Create a Zero Trust organization · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/replace-vpn/get-started/create-zero-trust-org/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Replace Vpn

  4. /[Get started with Zero Trust](https://developers.cloudflare.com/learning-paths/replace-vpn/get-started/)
  5. /Create a Zero Trust organization



# Create a Zero Trust organization

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/replace-vpn/get-started/create-zero-trust-org/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSign up for Zero Trust(Optional) Manage Zero Trust in Terraform

To start using Zero Trust features, create a Zero Trust organization in your Cloudflare account.

## Sign up for Zero Trust

To create a Zero Trust organization:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), select **Zero Trust**.

  2. On the onboarding screen, choose a team name. The team name is a unique, internal identifier for your Zero Trust organization. Users will enter this team name when they enroll their device manually, and it will be the subdomain for your App Launcher (as relevant). Your business name is the typical entry.

You can find your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) by going to **Zero Trust** > **Settings**.

  3. Complete your onboarding by selecting a subscription plan and entering your payment details. If you chose the **Zero Trust Free plan** , this step is still needed but you will not be charged.




When you create your organization, Cloudflare automatically adds the [Cloudflare identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/) as your default login method, so your users can sign in with their Cloudflare account credentials right away. You can add a [one-time PIN](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/) or connect a [third-party identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) at any time.

## (Optional) Manage Zero Trust in Terraform

You can use the [Cloudflare Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest) to manage your Zero Trust organization alongside your other IT infrastructure. To get started with Terraform, refer to our [Terraform tutorial series](https://developers.cloudflare.com/terraform/tutorial/).

To add Zero Trust to your Terraform configuration:

  1. Sign up for Zero Trust on the Cloudflare dashboard.

  2. Add the following permission to your [`cloudflare_api_token` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_token):

     * `Access: Organizations, Identity Providers, and Groups Write`
  3. Add the [`cloudflare_zero_trust_organization` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_organization) resource:
         
         resource "cloudflare_zero_trust_organization" "<your-team-name>" {
         	account_id                         = var.cloudflare_account_id
         	name                               = "Acme Corporation"
         	auth_domain                        = "<your-team-name>.cloudflareaccess.com"
         }

Replace `<your-team-name>` with the Zero Trust organization name selected during onboarding. You can also view your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) under **Zero Trust** > **Settings** > **Team name and domain**.




You can now update Zero Trust organization settings using Terraform.

Tip

If you plan to manage all Zero Trust settings in Terraform, set the dashboard to [API/Terraform read-only mode](https://developers.cloudflare.com/cloudflare-one/api-terraform/#set-dashboard-to-read-only).

[PreviousCreate a Cloudflare account](https://developers.cloudflare.com/learning-paths/replace-vpn/get-started/create-cloudflare-account/)[NextConfigure an identity provider](https://developers.cloudflare.com/learning-paths/replace-vpn/get-started/configure-idp/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/replace-vpn/get-started/create-zero-trust-org.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
