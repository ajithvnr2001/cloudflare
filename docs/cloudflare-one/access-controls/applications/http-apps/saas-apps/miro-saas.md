---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/miro-saas/
title: Miro \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:16.630029+00:00
---

# Miro · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/miro-saas/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)[Add web applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)

  4. /[SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/)
  5. /Miro



# Miro

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/miro-saas/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Add a SaaS application to Cloudflare One2\. Add a SAML SSO provider to Miro3\. Test the integration

This guide covers how to configure [Miro ↗︎](https://help.miro.com/hc/articles/360017571414-Single-sign-on-SSO) as a SAML application in Cloudflare One.

## Prerequisites

  * An [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) configured in Cloudflare One
  * Admin access to a Miro Business or Enterprise plan account
  * A [verified domain ↗︎](https://help.miro.com/hc/articles/360034831793-Domain-control) added to your Miro account (Enterprise plan), or be prepared to do so during SSO configuration (Business or Enterprise plan)



## 1\. Add a SaaS application to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.
  2. Select **Create new application** > **SaaS application**.
  3. For **Application** , enter `Miro` and select the corresponding textbox that appears.
  4. For the authentication protocol, select **SAML**.
  5. Select **Add application**.
  6. Fill in the following fields: 
     * **Entity ID** : `https://miro.com/`
     * **Assertion Consumer Service URL** : `https://miro.com/sso/saml`
     * **Name ID format** : _Email_
  7. Copy the **SSO endpoint** and **Public key**.
  8. Configure [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) for the application.
  9. Save the application.



## 2\. Add a SAML SSO provider to Miro

  1. In Miro, select your profile picture > **Settings** > ****Security****.
  2. Turn on **SSO/SAML**.
  3. Fill in the following fields: 
     * **SAML Sign-in URL** : SSO endpoint from application configuration in Cloudflare One
     * **Key x509 Certificate** : Public key from application configuration in Cloudflare One
  4. In **Domain** , enter the domain you want to configure SSO for and select **Enter**.
  5. Enter an email address from that domain and select **send verification**.
  6. Once you receive a verification email, select the link in the email, then select **Save**. When the domain is successfully configured, the **VERIFY EMAIL** label next to the domain in the SSO/SAML configuration page will disappear.
  7. If you have additional domains you want to configure SSO for, repeat steps 4-6 for each domain.



  1. In Miro, select your profile picture > **Settings** > ****Security and Compliance** > **Authentication** > **Single sign-on****.
  2. Turn on **SSO/SAML**.
  3. Fill in the following fields: 
     * **SAML Sign-in URL** : SSO endpoint from application configuration in Cloudflare One
     * **Key x509 Certificate** : Public key from application configuration in Cloudflare One
  4. In **Domain** , enter the domain you want to configure SSO for and select **Enter**.
  5. If you have not previously [verified the domain](https://help.miro.com/hc/articles/360034831793-Domain-control), enter an email address from that domain and select **send verification**.
  6. Once you receive a verification email, select the link in the email, then select **Save**. When the domain is successfully configured, the **VERIFY EMAIL** label next to the domain in the SSO/SAML configuration page will disappear.
  7. If you have additional domains you want to configure SSO for, repeat steps 4-6 for each domain.



## 3\. Test the integration

In the Miro SAML/SSO configuration page, select **Test SSO Configuration**. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider. If the login is successful, you will receive a **SSO configuration test was successful** message.

Note

When testing the integration, you do not have to use an email from a domain you have configured for SSO or a user configured in Miro. The only requirement is that the user is already configured in your identity provider.

[PreviousJamf Pro](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/jamf-pro-saas/)[NextPagerDuty](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/pagerduty-saml-saas/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/http-apps/saas-apps/miro-saas.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
