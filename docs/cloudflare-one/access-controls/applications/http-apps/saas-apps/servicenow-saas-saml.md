---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-saml/
title: ServiceNow (SAML) \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:17.806148+00:00
---

# ServiceNow (SAML) · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-saml/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)[Add web applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)

  4. /[SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/)
  5. /ServiceNow (SAML)



# ServiceNow (SAML)

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-saml/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Add a SaaS application to Cloudflare One2\. Add the Multiple Provider Single Sign-On Installer Plugin to ServiceNow3\. Add and Test a SAML SSO provider in ServiceNow

This guide covers how to configure [ServiceNow ↗︎](https://docs.servicenow.com/bundle/washingtondc-platform-security/page/integrate/single-sign-on/task/t_CreateASAML2Upd1SSOConfigMultiSSO.html) as a SAML application in Cloudflare One.

## Prerequisites

  * An [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) configured in Cloudflare One
  * Admin access to a ServiceNow account



## 1\. Add a SaaS application to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.
  2. Select **Create new application** > **SaaS application**.
  3. For **Application** , enter `ServiceNow` and select the corresponding textbox that appears.
  4. For the authentication protocol, select **SAML**.
  5. Select **Add application**.
  6. Fill in the following fields: 
     * **Entity ID** : `https://<INSTANCE-NAME>.service-now.com`
     * **Assertion Consumer Service URL** : `https://<INSTANCE-NAME>.service-now.com/navpage.do`
     * **Name ID format** : _Email_
  7. Copy the **SAML Metadata endpoint**.
  8. Configure [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) for the application.
  9. Save the application.



## 2\. Add the Multiple Provider Single Sign-On Installer Plugin to ServiceNow

  1. In ServiceNow, select **All**.
  2. In the search bar, enter `System Applications`, and under **All Available Applications** , select **All**.
  3. In the search bar, enter `Integration - Multiple Provider Single Sign-On Installer`.
  4. Select **Install**.
  5. Ensure that **Install now** is selected, and select **Install**.



## 3\. Add and Test a SAML SSO provider in ServiceNow

  1. Select **All**.
  2. In the search bar enter `Multi-Provider SSO`, and select **Identity Providers**.
  3. Select **New** > **SAML**.
  4. In the pop-up, ensure that **URL** is selected.
  5. Paste the **SAML Metadata endpoint** from application configuration in Cloudflare One in the empty field.
  6. Select **Import**.
  7. (Optional) Change the **Name** field to a more recognizable name.
  8. Turn off **Sign AuthnRequest**.
  9. Select **Update**.
  10. In the pop-up, select **Cancel** and then **>**.
  11. Select the **Name** of the configuration you just completed.
  12. Select **Test Connection**.
  13. If the test succeeds, select **Activate**.



[PreviousServiceNow (OIDC)](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-oidc/)[NextSlack](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/slack-saas/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-saml.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
