---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/jamf-pro-saas/
title: Jamf Pro \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:16.495093+00:00
---

# Jamf Pro · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/jamf-pro-saas/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)[Add web applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)

  4. /[SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/)
  5. /Jamf Pro



# Jamf Pro

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/jamf-pro-saas/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Collect Jamf Pro information2\. Add a SaaS application to Cloudflare One3\. Edit Access SAML Metadata4\. Add a SAML SSO provider to Jamf Pro5\. Test the Integration

This guide covers how to configure [Jamf Pro ↗︎](https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/Single_Sign-On.html) as a SAML application in Cloudflare One.

## Prerequisites

  * An [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) configured in Cloudflare One
  * Admin access to a Jamf Pro account



## 1\. Collect Jamf Pro information

  1. In Jamf Pro, go to **Settings** > **Systems** > **Single Sign-On** > **Edit**.
  2. Copy the pre-populated URL in **Entity ID**.
  3. Paste the URL in a web browser to download the Jamf metadata file.
  4. Open the `metadata.xml` file in a text editor, and copy the values for **Entity ID** and **Assertion Consumer Service**.



## 2\. Add a SaaS application to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.
  2. Select **Create new application** > **SaaS application**.
  3. For **Application** , enter `Jamf` or `Jamf Pro` and select the corresponding textbox that appears.
  4. For the authentication protocol, select **SAML**.
  5. Select **Add application**.
  6. Fill in the following fields: 
     * **Entity ID** : Entity ID value from Jamf Pro metadata file.
     * **Assertion Consumer Service URL** : Assertion Consumer Service value from Jamf Pro metadata file.
     * **Name ID format** : _Email_
  7. Copy the **SAML Metadata endpoint**.
  8. Configure [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) for the application.
  9. Save the application.



## 3\. Edit Access SAML Metadata

  1. Paste the **SAML Metadata endpoint** from application configuration in Cloudflare One into a browser.
  2. Copy the file and paste it into a text editor.
  3. Change `WantAuthnRequestsSigned="true"` to `WantAuthnRequestsSigned="false"`.
  4. Set the file extension as `.xml` and save.



## 4\. Add a SAML SSO provider to Jamf Pro

  1. In Jamf Pro, go to **Settings** > **Single Sign-On** > **Edit**.
  2. In Identity Provider menu, select **Other**.
  3. Label **Other provider** as `Cloudflare`.
  4. Fill in the following fields: 
     * **Entity ID** : Entity ID from Jamf Pro metadata file.
     * **Identity Provider Metadata Source** : Select **Metadata File** and upload the `.xml` file from step 2\. Edit Access SAML Metadata.
     * **Identity Provider User Mapping** : _Name ID_
     * **Jamf Pro User Mapping** : _Email_
  5. Turn on **Single Sign On**.



Note

The Failover Login URL located on this page can be used to log in if your SSO does not work.

## 5\. Test the Integration

Log out of Jamf Pro and open an incognito browser window. Go to your Jamf Pro URL. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.

[PreviousIronclad](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/ironclad-saas/)[NextMiro](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/miro-saas/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/http-apps/saas-apps/jamf-pro-saas.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
