---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-saml/
title: Salesforce (SAML) \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:17.169870+00:00
---

# Salesforce (SAML) · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-saml/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)[Add web applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)

  4. /[SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/)
  5. /Salesforce (SAML)



# Salesforce (SAML)

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-saml/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Add a SaaS application to Cloudflare One2\. Create a certificate file3\. Add a SAML SSO provider to Salesforce4\. Enable Single Sign-On in Salesforce

This guide covers how to configure [Salesforce ↗︎](https://help.salesforce.com/s/articleView?id=sf.sso_saml.htm&type=5) as a SAML application in Cloudflare One.

## Prerequisites

  * An [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) configured in Cloudflare One
  * Admin access to a Salesforce account



## 1\. Add a SaaS application to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.
  2. Select **Create new application** > **SaaS application**.
  3. For **Application** , select _Salesforce_.
  4. For the authentication protocol, select **SAML**.
  5. Select **Add application**.
  6. Fill in the following fields: 
     * **Entity ID** : `https://<your-domain>.my.salesforce.com` or `https://<your-domain>.my.salesforce.com?so=<your-salesforce-org-id>`, if your account was created before summer 2019 or does not have a My Domain subdomain.
     * **Assertion Consumer Service URL** : `https://<your-domain>.my.salesforce.com` or `https://<your-domain>.my.salesforce.com?so=<your-salesforce-org-id>`, if your account was created before summer 2019 or does not have a My Domain subdomain.
     * **Name ID format** : _Email_



Note

If you are unsure of which URL to use in the **Entity ID** and **Assertion Consumer Service URL** fields, you can check your Salesforce account's metadata. In Salesforce, go to the **Single Sign-On Settings** page and select **Download Metadata**. In this file, you will find the correct URLs to use.

  7. Copy the **SSO endpoint** , **Public key** , and **Access Entity ID or Issuer**.
  8. Configure [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) for the application.
  9. Save the application.



## 2\. Create a certificate file

  1. Paste the **Public key** in a text editor.
  2. Wrap the certificate in `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`.
  3. Set the file extension as `.crt` and save.



## 3\. Add a SAML SSO provider to Salesforce

  1. In Salesforce, go to **Setup**.

  2. In the **Quick Find** box, enter `single sign-on` and select **Single Sign-On Settings**.

  3. In **SAML Single Sign-On Settings** , select **New**.

  4. Fill in the following fields:

     * **Name:** Name of the SSO provider (for example, `Cloudflare Access`). Users will select this name when signing in to Salesforce.
     * **API name:** (this will pre-populate)
     * **Issuer:** Paste the Access Entity ID or Issuer from application configuration in Cloudflare One.
     * **Identity Provider Certificate** : Upload the `.crt` certificate file from 2\. Create a certificate file.
     * **Entity ID** : `https://<your-domain>.my.salesforce.com`
     * **SAML Identity type:** If the user's Salesforce username is their email address, select _Assertion contains the User's Salesforce username_. Otherwise, select _Assertion contains the Federation ID from the User object_ and make sure the user's Federation ID matches their email address.

Configure Federation IDs

     1. In the **Quick Find** box, enter `users` and select **Users**. 2. Select the user. 3. Verify that the user's **Federation ID** matches the email address used to authenticate to Cloudflare Access.
     * **Identity Provider Login URL** : SSO endpoint provided in Cloudflare One for this application.
  5. Select **Save**.




## 4\. Enable Single Sign-On in Salesforce

  1. Configure Single Sign-On settings: 
     1. In the **Quick Find** box, enter `single sign-on` and select **Single Sign-On Settings**.
     2. (Optional) To require users to login with Cloudflare Access, turn on **Disable login with Salesforce credentials**.
     3. Turn on **SAML Enabled**.
     4. Turn on **Make federation ID case-insensitive**.
  2. Enable Cloudflare Access as an identity provider on your Salesforce domain:

     1. In the **Quick Find** box, enter `domain` and select **My Domain**.
     2. In **Authentication Configuration** , select **Edit**.
     3. In **Authentication Service** , turn on the Cloudflare Access provider.



To test, open an incognito browser window and go to your Salesforce domain (`https://<your-domain>.my.salesforce.com`).

[PreviousSalesforce (OIDC)](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-oidc/)[NextServiceNow (OIDC)](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-oidc/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-saml.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
