---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/coupa-saas/
title: Coupa \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:14.126677+00:00
---

# Coupa · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/coupa-saas/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)[Add web applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)

  4. /[SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/)
  5. /Coupa



# Coupa

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/coupa-saas/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Add a SaaS application to Cloudflare One2\. Download the metadata file3\. Add a SAML SSO provider in Coupa3\. Create a test user and test the integration

This guide covers how to configure [Coupa ↗︎](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-user-authentication/coupa-saml-sso-setup) as a SAML application in Cloudflare One.

## Prerequisites

  * An [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) configured in Cloudflare One
  * Admin access to a Coupa Stage or Production account



## 1\. Add a SaaS application to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.
  2. Select **Create new application** > **SaaS application**.
  3. For **Application** , enter `Coupa` and select the corresponding textbox that appears.
  4. For the authentication protocol, select **SAML**.
  5. Select **Add application**.
  6. Fill in the following fields: 
     * **Entity ID** : `sso-stg1.coupahost.com` for a stage account or `sso-prd1.coupahost.com` for a production account
     * **Assertion Consumer Service URL** : `https://sso-stg1.coupahost.com/sp/ACS.saml2` for a stage account or `https://sso-prd1.coupahost.com/sp/ACS.saml2` for a production account
     * **Name ID format** : _Email_
  7. Copy the **Access Entity ID or Issuer** and **SAML Metadata Endpoint**.
  8. In **Default relay state** , enter `https://<your-subdomain>.coupahost.com/sessions/saml_post`.
  9. Configure [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) for the application.
  10. Save the application.



## 2\. Download the metadata file

  1. Paste the SAML metadata endpoint from application configuration in Cloudflare One in a web browser.
  2. Follow your browser-specific steps to download the URL's contents as an `.xml` file.



## 3\. Add a SAML SSO provider in Coupa

  1. In Coupa, go to **Setup** > **Company Setup** > **Security Controls**.
  2. Under **Sign in using SAML** , turn on **Sign in using SAML**.
  3. In **Upload IdP metadata** , select **Choose File** , and upload the `.xml` file you downloaded in step 2\. Download the metadata file.
  4. Turn on **Advanced Options**.
  5. For **Sign in page URL** and **Timeout URL** , enter `https://sso-stg1.coupahost.com/sp/startSSO.ping?PartnerIdpId=<access-entity-id-or-issuer>&TARGET=https://<your-subdomain>.coupahost.com/sessions/saml_post` using the Access Entity ID or Issuer from application configuration in Cloudflare One.
  6. Select **Save**.



## 3\. Create a test user and test the integration

  1. In Coupa, go to **Setup** > **Company Setup** > **Users**.
  2. Select **Create** , then enter the user details for your test user. For **Login** and **Single Sign-On ID** , enter the user's email address.
  3. Select **Save**.
  4. Open an incognito browser window and go to your Coupa URL. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.
  5. Once the login is successful, you can configure other users for SSO by adding their email to the **Single Sign-On ID** field in **Setup** > **Company Setup** > **Users** > user's name.



Note

You can use the following URL to bypass SSO and login via a username and password: `https://<your-subdomain>.coupahost.com/sessions/support_login`.

[PreviousBraintree](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/braintree-saas/)[NextDigicert](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/digicert-saas/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/http-apps/saas-apps/coupa-saas.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
