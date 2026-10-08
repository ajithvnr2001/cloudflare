---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/pingboard-saas/
title: Pingboard \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:17.346730+00:00
---

# Pingboard · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/pingboard-saas/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)[Add web applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)

  4. /[SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/)
  5. /Pingboard



# Pingboard

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/pingboard-saas/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Add a SaaS application to Cloudflare One2\. Add a SAML SSO provider to Pingboard3\. Test the integration

This guide covers how to configure [Pingboard ↗︎](https://support.pingboard.com/hc/en-us/articles/360046585994-Set-Up-a-Custom-SSO-Solution) as a SAML application in Cloudflare One.

## Prerequisites

  * An [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) configured in Cloudflare One
  * Admin access to a Pingboard account



## 1\. Add a SaaS application to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.
  2. Select **Create new application** > **SaaS application**.
  3. For **Application** , enter `Pingboard` and select the corresponding textbox that appears.
  4. For the authentication protocol, select **SAML**.
  5. Select **Add application**.
  6. Fill in the following fields: 
     * **Entity ID** : `http://app.pingboard.com/sp`
     * **Assertion Consumer Service URL** : `https://sso-demo.pingboard.com/auth/saml/consume`
     * **Name ID format** : _Email_
  7. Copy the **SAML Metadata endpoint**.
  8. Configure [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) for the application.
  9. Save the application.



## 2\. Add a SAML SSO provider to Pingboard

  1. In Pingboard, go to **Account** > **Add-Ons**.
  2. Under **Third-Party Integrations** , select **Custom SSO**.
  3. In a web browser, paste the SAML Metadata endpoint you copied from the application configuration in Cloudflare One. Next, copy the contents of the displayed page.
  4. In Pingboard, under **IdP Metadata** , paste the contents from the SAML Metadata endpoint.
  5. (Optional) Under **Sign in with** , enter a name (for example, `Cloudflare Access`). Your users will select this name when signing in.



## 3\. Test the integration

Open an incognito browser window and go to your Pingboard URL. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.

[PreviousPagerDuty](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/pagerduty-saml-saas/)[NextSalesforce (OIDC)](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-oidc/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/http-apps/saas-apps/pingboard-saas.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
