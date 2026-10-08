---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/github-saas/
title: GitHub Enterprise Cloud \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:15.267070+00:00
---

# GitHub Enterprise Cloud · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/github-saas/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)[Add web applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)

  4. /[SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/)
  5. /GitHub Enterprise Cloud



# GitHub Enterprise Cloud

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/github-saas/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Add a SaaS application to Cloudflare One2\. Create an X.509 certificate3\. Configure an identity provider and SAML SSO in GitHub Enterprise Cloud4\. Test the integration

This guide covers how to configure [GitHub Enterprise Cloud ↗︎](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise) as a SAML application in Cloudflare One.

## Prerequisites

  * An [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) configured in Cloudflare One
  * A GitHub Enterprise Cloud subscription
  * Access to a GitHub account as an organization owner



## 1\. Add a SaaS application to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.
  2. Select **Create new application** > **SaaS application**.
  3. For **Application** , select _GitHub_.
  4. For the authentication protocol, select **SAML**.
  5. Select **Add application**.
  6. Fill in the following fields: 
     * **Entity ID** : `https://github.com/orgs/<your-organization>`
     * **Assertion Consumer Service URL** : `https://github.com/orgs/<your-organization>/saml/consume`
     * **Name ID format** : _Email_
  7. Copy the **SSO endpoint** , **Access Entity ID or Issuer** , and **Public key**.
  8. Configure [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) for the application.
  9. Save the application.



## 2\. Create an X.509 certificate

  1. Paste the **Public key** in a text editor.
  2. Wrap the certificate in `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`.



## 3\. Configure an identity provider and SAML SSO in GitHub Enterprise Cloud

  1. In your GitHub organization page, go to **Settings** > **Authentication security**.
  2. Under **SAML single sign-on** , turn on **Enable SAML authentication**.
  3. Fill in the following fields: 
     * **Sign on URL** : SSO endpoint from application configuration in Cloudflare One.
     * **Issuer** : Access Entity ID or Issuer from application configuration in Cloudflare One.
     * **Public certificate** : Paste the entire x.509 certificate from step 2\. Create a x.509 certificate.



## 4\. Test the integration

Select **Test SAML configuration**. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider. When this is successful, select **Save**.

You can also turn on **Require SAML SSO authentication for all members of your organization** if you want to enforce SSO login with Cloudflare Access.

[PreviousDropbox](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/dropbox-saas/)[NextGoogle Cloud](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/google-cloud-saas/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/http-apps/saas-apps/github-saas.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
