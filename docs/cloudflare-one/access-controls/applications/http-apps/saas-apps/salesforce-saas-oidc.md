---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-oidc/
title: Salesforce (OIDC) \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:16.816248+00:00
---

# Salesforce (OIDC) · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-oidc/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)[Add web applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)

  4. /[SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/)
  5. /Salesforce (OIDC)



# Salesforce (OIDC)

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-oidc/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Add a SaaS application to Cloudflare One2\. Add a SSO provider to Salesforce3\. Enable Single Sign-On in Salesforce

This guide covers how to configure [Salesforce ↗︎](https://help.salesforce.com/s/articleView?id=sf.sso_provider_openid_connect.htm&type=5) as an OpenID Connect (OIDC) application in Cloudflare One.

## Prerequisites

  * An [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) configured in Cloudflare One
  * Admin access to a Salesforce account



## 1\. Add a SaaS application to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.
  2. Select **Create new application** > **SaaS application**.
  3. For **Application** , select _Salesforce_.
  4. For the authentication protocol, select **OIDC**.
  5. Select **Add application**.
  6. In **Scopes** , select the attributes that you want Access to send in the ID token.
  7. In **Redirect URLs** , enter the callback URL obtained from Salesforce (`https://<your-domain>.my.salesforce.com/services/authcallback/<URL Suffix>`). Refer to Add a SSO provider to Salesforce for instructions on obtaining this value.
  8. (Optional) Enable [Proof of Key Exchange (PKCE) ↗︎](https://www.oauth.com/oauth2-servers/pkce/) if the protocol is supported by your IdP. PKCE will be performed on all login attempts.
  9. Copy the following values: 
     * **Client ID**
     * **Client Secret**
     * **Authorization endpoint**
     * **Token endpoint**
     * **User info endpoint**
  10. Configure [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) for the application.
  11. (Optional) In **Experience settings** , configure [App Launcher settings](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/app-launcher/) by turning on **Enable App in App Launcher** and, in **App Launcher URL** , entering `https://<your-domain>.my.salesforce.com`.
  12. Save the application.



## 2\. Add a SSO provider to Salesforce

  1. In Salesforce, go to **Setup**.
  2. In the **Quick Find** box, enter `auth` and select **Auth providers**.
  3. Select **New**.
  4. For the provider type, select **OpenID Connect**.
  5. Enter a name for the SSO provider (for example, `Cloudflare Access`).
  6. Fill in the following fields with values obtained from Cloudflare Access: 
     * **Consumer Key** : Client ID
     * **Consumer Secret** : Client Secret
     * **Authorize Endpoint URL** : Authorization endpoint
     * **Token endpoint URL** : Token endpoint
     * **User Info Endpoint URL** : User info endpoint
     * **Token Issuer** : Issuer
  7. (Optional) Enable **Use Proof Key for Code Exchange** if you enabled it in Access.
  8. In **Default Scopes** , enter a space-separated list of the scopes you configured in Access (for example, `openid email profile groups`).
  9. Select **Save**.
  10. Copy the **Callback URL** : 
         
         https://<your-domain>.my.salesforce.com/services/authcallback/<URL Suffix>

  11. In Cloudflare One, paste the Callback URL into the **Redirect URL** field.



To test the integration, open an incognito browser window and go to the **Test-Only Initialization URL** ( `https://<your-domain>.my.salesforce.com/services/auth/test/<URL Suffix>`)

## 3\. Enable Single Sign-On in Salesforce

  1. Enable Cloudflare Access as an identity provider on your Salesforce domain:

     1. In the **Quick Find** box, enter `domain` and select **My Domain**.
     2. In **Authentication Configuration** , select **Edit**.
     3. In **Authentication Service** , turn on the Cloudflare Access provider.
  2. (Optional) To require users to login with Cloudflare Access: 
     1. In the **Quick Find** box, enter `single sign-on` and select **Single Sign-On Settings**.
     2. Turn on **Disable login with Salesforce credentials**.



To test, open an incognito browser window and go to your Salesforce domain (`https://<your-domain>.my.salesforce.com`).

[PreviousPingboard](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/pingboard-saas/)[NextSalesforce (SAML)](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-saml/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-oidc.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
