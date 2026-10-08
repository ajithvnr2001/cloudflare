---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/sparkpost-saas/
title: SparkPost \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:18.222105+00:00
---

# SparkPost · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/sparkpost-saas/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)[Add web applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)

  4. /[SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/)
  5. /SparkPost



# SparkPost

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/sparkpost-saas/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Add a SaaS application to Cloudflare One2\. Download the metadata file3\. Add a SAML SSO provider to SparkPost4\. Add a test user and test the integration

This guide covers how to configure [SparkPost or SparkPost EU ↗︎](https://support.sparkpost.com/docs/my-account-and-profile/sso) as a SAML application in Cloudflare Zero Trust.

## Prerequisites

  * An [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) configured in Cloudflare One
  * Admin access to a SparkPost or SparkPost EU account



## 1\. Add a SaaS application to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.
  2. Select **Create new application** > **SaaS application**.
  3. For **Application** , enter `SparkPost` and select the corresponding textbox that appears.
  4. For the authentication protocol, select **SAML**.
  5. Select **Add application**.
  6. Fill in the following fields: 
     * **Entity ID** : 
       * `https://api.sparkpost.com` for SparkPost accounts
       * `https://api.eu.sparkpost.com` for SparkPost EU accounts
       * `https://<api-host>` for SparkPost accounts with dedicated tenants
     * **Assertion Consumer Service URL** : 
       * `https://api.sparkpost.com/api/v1/users/saml/consume` for SparkPost accounts
       * `https://api.eu.sparkpost.com/api/v1/users/saml/consume` for SparkPost EU accounts
       * `https://<api-host>/api/v1/users/saml/consume` for SparkPost accounts with dedicated tenants
     * **Name ID format** : _Email_
  7. Copy the **SAML Metadata endpoint**.
  8. Configure [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) for the application.
  9. Save the application.



## 2\. Download the metadata file

  1. Paste the SAML metadata endpoint from application configuration in Cloudflare One in a web browser.
  2. Follow your browser-specific steps to download the URL's contents as an `.xml` file.



## 3\. Add a SAML SSO provider to SparkPost

  1. In SparkPost, select your profile picture > **Account Settings**.
  2. Under **Single Sign-On** , select **Provision SSO**.
  3. Under **Upload your Security Assertion Markup Language (SAML)** , select **select a file** and upload the `.xml` file you created in step 2\. Download the metadata file.
  4. Select **Provision SSO**.
  5. Select **Enable SSO**.



## 4\. Add a test user and test the integration

  1. In SparkPost, current users must be deleted and re-invited to use SSO. To create a test user, select your profile picture > **Users** > name of the user > **Delete User**. Then, select **Invite User** and fill in the necessary information. Alternatively, invite a new user. An invitation email will be sent.
  2. Go to the link sent in the invitation email. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.
  3. Once SSO is successful, you can turn on SSO for the rest of your current users by deleting and then re-inviting them.



Note

The SparkPost SSO login link is `https://app.sparkpost.com/auth/sso`. Alternatively, you can go to the usual sign in page and select **Log in with Single Sign-On**.

[PreviousSmartsheet](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/smartsheet-saas/)[NextTableau Cloud](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/tableau-saml-saas/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/http-apps/saas-apps/sparkpost-saas.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
