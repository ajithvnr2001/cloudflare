---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/tableau-saml-saas/
title: Tableau Cloud \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:18.459771+00:00
---

# Tableau Cloud · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/tableau-saml-saas/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)[Add web applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)

  4. /[SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/)
  5. /Tableau Cloud



# Tableau Cloud

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/tableau-saml-saas/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Add a SaaS application to Cloudflare One2\. Download the metadata file3\. Add a SAML SSO provider to Tableau Cloud4\. Finish adding a SaaS application to Cloudflare One5\. Test the integration and set default authentication type

This guide covers how to configure [Tableau Cloud ↗︎](https://help.tableau.com/current/online/en-us/saml_config_site.htm) as a SAML application in Cloudflare One.

## Prerequisites

  * An [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) configured in Cloudflare One
  * Admin access to a Tableau Cloud site



## 1\. Add a SaaS application to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.
  2. Select **Create new application** > **SaaS application**.
  3. For **Application** , select _Tableau_.
  4. For the authentication protocol, select **SAML**.
  5. Select **Add application**.
  6. Copy the **SAML Metadata endpoint**.
  7. Keep this window open. You will finish this configuration in step 4\. Finish adding a SaaS application to Cloudflare One.



## 2\. Download the metadata file

  1. Paste the SAML Metadata endpoint from application configuration in Cloudflare One in a web browser.
  2. Follow your browser-specific steps to download the URL's contents as an `.xml` file.



## 3\. Add a SAML SSO provider to Tableau Cloud

  1. In Tableau Cloud, go to **Settings** > **Authentication**.
  2. Turn on **Enable an additional authentication method**. For **select authentication type** , select _SAML_.
  3. Under **1\. Get Tableau Cloud metadata** , copy the **Tableau Cloud entity ID** and **Tableau Cloud ACS URL**.
  4. Under **4\. Upload metadata to Tableau** , select **Choose a file** , and upload the `.xml` file created in step 2\. Download the metadata file
  5. Under **5\. Map attributes** , turn on **Full name**. For **Name (full name)** , enter `name`.
  6. (Optional) Choose whether users who are accessing embedded views will **Authenticate in a separate pop-up window** or **Authenticate using an inline frame**.
  7. Select **Save Changes**.



## 4\. Finish adding a SaaS application to Cloudflare One

  1. In your open Cloudflare One window, fill in the following fields: 
     * **Entity ID** : Tableau Cloud entity ID from Tableau Cloud SAML SSO set-up.
     * **Assertion Consumer Service URL** : Tableau Cloud ACS URL from Tableau Cloud SAML SSO set-up.
     * **Name ID format** : _Email_
  2. Configure [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) for the application.
  3. Save the application.



## 5\. Test the integration and set default authentication type

  1. In Tableau Cloud, go to **Settings** > **Authentication**.
  2. Under **7\. Test Configuration** , select **Test Configuration**.
  3. Sign in. If your sign-in is successful, **You are now signed in as (username)** will appear at the top of the page.
  4. Close the pop-up window.
  5. (Optional) Under **Default Authentication Type for Embedded Views** , turn on **cloudflareaccess.com (SAML)**. You can also configure the default authentication type for individual users under **Users** > **Actions** > **Authentication**.



[PreviousSparkPost](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/sparkpost-saas/)[NextWorkday](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/workday-saas/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/http-apps/saas-apps/tableau-saml-saas.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
