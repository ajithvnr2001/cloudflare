---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/google-cloud-saas/
title: Google Cloud \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:15.386275+00:00
---

# Google Cloud · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/google-cloud-saas/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)[Add web applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)

  4. /[SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/)
  5. /Google Cloud



# Google Cloud

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/google-cloud-saas/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Add a SaaS application to Cloudflare One2\. Create a x.509 certificate3\. Create an SSO provider in Google Cloud4\. Test the integrationTroubleshooting

This guide covers how to configure [Google Cloud ↗︎](https://support.google.com/cloudidentity/topic/7558767) as a SAML application in Cloudflare One.

Caution

When configuring Google Cloud with Access, the following limitations apply:

  * Users will not be able to log in using [Google](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/google/) or [Google Workspace](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/google-workspace/) as an identity provider after Google Cloud is configured with Access.

  * The integration of Access as a single sign-on provider for your Google Cloud account does not work for Google super admins. It will work for other users.




## Prerequisites

  * An [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) configured in Cloudflare One
  * Admin access to a Google Workspace account
  * [Cloud Identity Free or Premium ↗︎](https://support.google.com/cloudidentity/answer/7389973) set up in your organization's Google Cloud account



## 1\. Add a SaaS application to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.
  2. Select **Create new application** > **SaaS application**.
  3. For **Application** , select _Google Cloud_.
  4. For the authentication protocol, select **SAML**.
  5. Select **Add application**.
  6. Fill in the following fields: 
     * **Entity ID** : `google.com`
     * **Assertion Consumer Service URL** : `https://www.google.com/a/<your_domain.com>/acs`
     * **Name ID format** : _Email_
  7. Copy the **SSO endpoint** , **Access Entity ID or Issuer** , and **Public key**.
  8. Configure [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) for the application.
  9. Save the application.



## 2\. Create a x.509 certificate

  1. Paste the Public key from application configuration in Cloudflare One into a text editor.
  2. Wrap the certificate in `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`.
  3. Set the file extension as `.crt` and save.



## 3\. Create an SSO provider in Google Cloud

  1. In your [Google Admin console ↗︎](https://admin.google.com/), go to **Security** > **Authentication** > **SSO with third party IdP**.
  2. Select **Third-party SSO profile for your organization** > **Add SSO Profile**.
  3. Turn on **Set up SSO with third-party identity provider**.
  4. Fill in the following information: 
     * **Sign-in page URL** : SSO endpoint from application configuration in Cloudflare One.
     * **Sign-out page URL** : `https://<team-name>.cloudflareaccess.com/cdn-cgi/access/logout`, where `<team-name>` is your Cloudflare One team name.
     * **Verification certificate** : Upload the `.crt` certificate file from step 2\. Create a x.509 certificate.
  5. (Optional) Turn on **Use a domain specific issuer**. If you select this option, Google will send an issuer specific to your Google Cloud domain (`google.com/a/<your_domain.com>` instead of the standard `google.com`).



## 4\. Test the integration

Open an incognito browser window and go to your Google Cloud URL (`https://console.cloud.google.com/a/<your_domain.com>`). Sign in using credentials that do not belong to a super admin account.

## Troubleshooting

`Error: "G Suite - This account cannot be accessed because the login credentials could not be verified."`

If you see this error, it is likely that the public key and private key do not match. Confirm that your certificate file includes the correct public key.

[PreviousGitHub Enterprise Cloud](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/github-saas/)[NextGoogle Workspace](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/google-workspace-saas/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/http-apps/saas-apps/google-cloud-saas.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
