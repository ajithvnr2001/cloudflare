---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/adobe-sign-saas/
title: Adobe Acrobat Sign \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:13.226456+00:00
---

# Adobe Acrobat Sign · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/adobe-sign-saas/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)[Add web applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)

  4. /[SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/)
  5. /Adobe Acrobat Sign



# Adobe Acrobat Sign

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/adobe-sign-saas/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Add a SaaS application to Cloudflare One2\. Add a SAML SSO provider to Adobe Sign3\. Finish adding a SaaS application to Cloudflare One4\. Test the integration and finalize configuration

This guide covers how to configure [Adobe Acrobat Sign ↗︎](https://helpx.adobe.com/sign/using/enable-saml-single-sign-on.html) as a SAML application in Cloudflare One.

## Prerequisites

  * An [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) configured in Cloudflare One
  * Admin access to a Adobe Acrobat Sign account
  * A [claimed domain ↗︎](https://helpx.adobe.com/sign/using/claim-domain-names.html) in Adobe Acrobat Sign



## 1\. Add a SaaS application to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.
  2. Select **Create new application** > **SaaS application**.
  3. For **Application** , enter `Adobe Sign` and select the corresponding textbox that appears.
  4. For the authentication protocol, select **SAML**.
  5. Select **Add application**.
  6. Copy the **Access Entity ID or Issuer** , **Public key** , and **SSO endpoint**.
  7. Keep this window open without selecting **Select configuration**. You will finish this configuration in step 3\. Finish adding a SaaS application to Cloudflare One.



## 2\. Add a SAML SSO provider to Adobe Sign

  1. In Adobe Acrobat Sign, select your profile picture > your name > **Account Settings** > **SAML Settings**.
  2. Turn **SAML Allowed** on.
  3. Enter a hostname (for example, `yourcompanyname`). Users can use this URL or `https://secure.adobesign.com/public/login` to sign in via SSO.
  4. (Optional) For **Single Sign On Login Message** , enter a custom message (for example, `Log in via SSO`). The default message is **Sign in using your corporate credentials**.
  5. Fill in the following fields: 
     * **Entity ID/Issuer URL** : Access Entity ID or Issuer from application configuration in Cloudflare One.
     * **Login URL/SSO Endpoint** : SSO endpoint from application configuration in Cloudflare One.
     * **IdP Certificate** : Public key from application configuration in Cloudflare One. Wrap the certificate in `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`.
  6. Copy the **Entity ID/SAML Audience** and **Assertion Consumer URL**.
  7. Select **Save**.



## 3\. Finish adding a SaaS application to Cloudflare One

  1. In your open Cloudflare One window, fill in the following fields: 
     * **Entity ID** : Entity ID/SAML Audience from Adobe Acrobat Sign SAML SSO configuration.
     * **Assertion Consumer Service URL** : Assertion Consumer URL from Adobe Acrobat Sign SAML SSO configuration.
     * **Name ID format** : _Email_
  2. Configure [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) for the application.
  3. Save the application.



## 4\. Test the integration and finalize configuration

  1. Open an incognito browser window and go to your Adobe Sign hostname URL or `https://secure.adobesign.com/public/login`. Select the option to sign in via SSO (**Sign in using your corporate credentials** if you have not configured a custom message). You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.



Note

If you receive an error while testing SSO integration, go to your profile picture > your name > **Account Settings** > **SAML Errors** for more information.

  2. Once this is successful, you can make sign in via SSO mandatory. Select your profile picture > your name > **Account Settings** > **SAML Settings** , and then turn on **SAML Mandatory**. Keeping **Allow Acrobat Sign Account Administrators to log in using their Acrobat Sign Credentials** turned on will allow administrators to log in even if your account experiences SSO issues.



[PreviousGeneric SAML application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/generic-saml-saas/)[NextArea 1](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/area-1/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/http-apps/saas-apps/adobe-sign-saas.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
