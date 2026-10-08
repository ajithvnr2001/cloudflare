---
url: https://developers.cloudflare.com/learning-paths/clientless-access/initial-setup/configure-idp/
title: Configure an identity provider (recommended) \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:45.034080+00:00
---

# Configure an identity provider (recommended) · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/clientless-access/initial-setup/configure-idp/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Clientless Access

  4. /[Initial setup](https://developers.cloudflare.com/learning-paths/clientless-access/initial-setup/)
  5. /Configure an identity provider (recommended)



# Configure an identity provider (recommended)

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/clientless-access/initial-setup/configure-idp/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

An [identity provider (IdP)](https://www.cloudflare.com/learning/access-management/what-is-an-identity-provider/) stores and manages users' digital identities. You can integrate your existing identity provider with Cloudflare Zero Trust in order to manage user access to your private network. This requires configuration both in Cloudflare and with the identity provider itself.

Note

Some admins choose to test by authenticating with a [one-time PIN (OTP)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/) instead of an IdP. OTP can also be used as an alternative login method for contractors or other guests that are not part of your IdP.

To add an identity provider:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.

  2. In the **Your identity providers** card, select **Add new identity provider**.

  3. Select the identity provider you want to add.

If you do not see your identity provider listed, these providers can typically still be enabled. If they support OIDC or OAuth, select the [generic OIDC](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-oidc/) option. If they support SAML, select the [generic SAML](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/) option. Cloudflare supports all SAML and OIDC providers and can integrate with the majority of OAuth providers. If your provider supports both SAML and OIDC, we recommend OIDC for ease of configuration.

  4. Fill in the necessary fields to set up your identity provider.

Each identity provider will have different required fields for you to fill in. Step-by-step instructions are shown in the dashboard side panel. Alternatively, refer to the [IdP-specific documentation](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/).

  5. Once you have filled in the necessary fields, select **Save**.




  1. Add the following permission to your [`cloudflare_api_token` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_token):

     * `Access: Organizations, Identity Providers, and Groups Write`
  2. Add an identity provider to Cloudflare One using the [`cloudflare_zero_trust_access_identity_provider` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_access_identity_provider) resource. For example, to add a Microsoft Entra ID integration:
         
         resource "cloudflare_zero_trust_access_identity_provider" "microsoft_entra_id" {
         	account_id = var.cloudflare_account_id
         	name       = "Entra ID example"
         	type       = "azureAD"
         	config 		 = {
         		client_id                  = var.entra_id_client_id
         		client_secret              = var.entra_id_client_secret
         		directory_id               = var.entra_id_directory_id
         		support_groups             = true
         		}
         }

Each identity provider integration has different required attributes. You will need to obtain these attribute values from your identity provider. For more information, refer to the [IdP-specific documentation](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/).

If you do not see your identity provider listed, these providers can typically still be enabled. If they support OIDC or OAuth, use the [generic OIDC](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-oidc/) option. If they support SAML, use the [generic SAML](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/) option. Cloudflare supports all SAML and OIDC providers and can integrate with the majority of OAuth providers. If your provider supports both SAML and OIDC, we recommend OIDC for ease of configuration.




Users will now be able to select this IdP when they are prompted to authenticate.

[PreviousCreate a Zero Trust organization](https://developers.cloudflare.com/learning-paths/clientless-access/initial-setup/create-zero-trust-org/)[NextOverview](https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/clientless-access/initial-setup/configure-idp.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
