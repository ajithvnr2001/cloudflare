---
url: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/keycloak/
title: Keycloak (SAML) \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:04.403543+00:00
---

# Keycloak (SAML) · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/keycloak/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)
  5. /Keycloak (SAML)



# Keycloak (SAML)

Last updated Aug 4, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/keycloak/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up Keycloak (SAML)

Keycloak is an open source identity and access management solution built by JBoss.

## Set up Keycloak (SAML)

To set up Keycloak (SAML) as your identity provider:

  1. In Keycloak, select the realm that you want Cloudflare Access to use.

  2. Go to **Clients** > **Create client**.

  3. For **Client type** , select **SAML**.

  4. Under **Client ID** , enter your Cloudflare Access callback URL:
         
         https://<your-team-name>.cloudflareaccess.com/cdn-cgi/access/callback

You can find your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) under **Settings** > **Team name and domain** > **Team name**.

  5. Select **Next**.

  6. Change **Name ID format** to **email**.

  7. In **Valid redirect URIs** , enter your Cloudflare Access callback URL:
         
         https://<your-team-name>.cloudflareaccess.com/cdn-cgi/access/callback

  8. In **Master SAML Processing URL** , enter the SAML endpoint for your Keycloak realm:
         
         https://<keycloak_domain>/realms/<realm_name>/protocol/saml

Keycloak v17 and later use `/realms/<realm_name>/protocol/saml` by default. Keycloak v16 and earlier may use `/auth/realms/<realm_name>/protocol/saml` instead.

  9. If you wish to enable client signatures, enable **Client Signature Required** and select **Save**.

     1. You will need to [follow the steps here to get the certificate and enable it in the Cloudflare dashboard](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/signed_authn/).

     2. Import the Access certificate you downloaded into the **Keys** tab. Use **Certificate PEM** as the format.

  10. Configure a protocol mapper for the user's email address.

     1. Go to **Clients** > your Cloudflare Access SAML client > **Client scopes**.
     2. Select the dedicated client scope for the client.
     3. Go to **Mappers** > **Add mapper** > **By configuration**.
     4. Select **User Property**.
     5. Set **Property** to `email` and **SAML Attribute Name** to `email`.

Next, you will need to integrate with Cloudflare Access.

  11. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.

  12. Under **Your identity providers** , select **Add new identity provider**.

  13. Choose **SAML** on the next page.

You will need to input the Keycloak details manually. The examples below should be replaced with the specific domains in use with Keycloak and Cloudflare Access.

Field | Example  
---|---  
Single Sign-On URL | `https://<keycloak_domain>/realms/<realm_name>/protocol/saml`  
IdP Entity ID or Issuer URL | `https://<unique_id>.cloudflareaccess.com/cdn-cgi/access/callback`  
Signing certificate | Use the X509 certificate from the Keycloak realm keys  
  
  14. Select **Save**.




To test that your connection is working, go to **Integrations** > **Identity providers** and select **Test** next to the login method you want to test.

[PreviousJumpCloud (SAML)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/jumpcloud-saml/)[NextLinkedIn](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/linkedin/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/identity-providers/keycloak.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
