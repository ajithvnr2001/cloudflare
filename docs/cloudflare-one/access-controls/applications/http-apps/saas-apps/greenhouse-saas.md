---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/greenhouse-saas/
title: Greenhouse Recruiting \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:16.073891+00:00
---

# Greenhouse Recruiting · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/greenhouse-saas/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)[Add web applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)

  4. /[SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/)
  5. /Greenhouse Recruiting



# Greenhouse Recruiting

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/greenhouse-saas/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Add a SaaS application to Cloudflare One2\. Download the metadata file3\. Add a SAML SSO provider to Greenhouse4\. Finish adding a SaaS application to Cloudflare One5\. Test the integration and finalize configuration

This guide covers how to configure [Greenhouse Recruiting ↗︎](https://support.greenhouse.io/hc/en-us/articles/360040753811-Configure-single-sign-on-SSO-for-Greenhouse-Recruiting) as a SAML application in Cloudflare One.

## Prerequisites

  * An [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) configured in Cloudflare One
  * Admin access to an Advanced or Expert Greenhouse Recruiting site



## 1\. Add a SaaS application to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.
  2. Select **Create new application** > **SaaS application**.
  3. For **Application** , enter `Greenhouse` and select the corresponding textbox that appears.
  4. For the authentication protocol, select **SAML**.
  5. Select **Add application**.
  6. Copy the **SAML Metadata endpoint**.
  7. Keep this window open. You will finish this configuration in step 4\. Finish adding a SaaS application to Cloudflare One.



## 2\. Download the metadata file

  1. Paste the SAML Metadata endpoint from application configuration in Cloudflare One in a web browser.
  2. Follow your browser-specific steps to download the URL's contents as an `.xml` file.



## 3\. Add a SAML SSO provider to Greenhouse

  1. In Greenhouse Recruiting, go to the **Configure** icon > **Dev Center** > **Single sign-on**.
  2. Copy the **SSO Assertion Consumer URL**.
  3. Under **Upload XML file** , select **Choose a file** , and upload the `.xml` file created in step 2\. Download the metadata file.
  4. Change the **Entity ID** to `greenhouse.io`.
  5. Keep this window open without selecting **Begin testing**. You will finish this configuration in step 5\. Test the integration and finalize configuration.



## 4\. Finish adding a SaaS application to Cloudflare One

  1. In your open Cloudflare One window, fill in the following fields: 
     * **Entity ID** : `greenhouse.io`
     * **Assertion Consumer Service URL** : SSO Assertion Consumer URL from SSO configuration in Greenhouse Recruiting.
     * **Name ID format** : _Email_
  2. Configure [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) for the application.
  3. Save the application.



## 5\. Test the integration and finalize configuration

  1. In your open Greenhouse Recruiting window, select **Begin Testing** > **Proceed**.
  2. Open an incognito browser window and go to your Greenhouse Recruiting URL. Choose the SSO login option. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.
  3. Once SSO sign in is successful, go to the **Configure** icon > **Dev Center** > **Single sign-on**.
  4. Select **Finalize Configuration**.
  5. In the text field, enter `CONFIGURE`.
  6. Select **Finalize**. Now, users will only be able to sign in with SSO.



[PreviousGrafana Cloud](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/grafana-cloud-saas-oidc/)[NextHubspot](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/hubspot-saas/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/http-apps/saas-apps/greenhouse-saas.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
