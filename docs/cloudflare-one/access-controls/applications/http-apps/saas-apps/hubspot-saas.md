---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/hubspot-saas/
title: Hubspot \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:15.933740+00:00
---

# Hubspot · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/hubspot-saas/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)[Add web applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)

  4. /[SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/)
  5. /Hubspot



# Hubspot

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/hubspot-saas/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Configure Hubspot2\. Configure Cloudflare Access3\. Create a x.509 certificate4\. Finalize Hubspot configuration

This guide covers how to configure [Hubspot ↗︎](https://knowledge.hubspot.com/account-security/set-up-single-sign-on-sso) as a SAML application in Cloudflare One.

## Prerequisites

  * An [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) configured in Cloudflare One
  * Admin access to a Hubspot Enterprise plan account



## 1\. Configure Hubspot

  1. Go to **Settings** > **Account** , then go to **Defaults** > **Security**.
  2. Select _Single Sign-on_.
  3. Copy the values for _Audience URI_ and _Sign on URL_.



## 2\. Configure Cloudflare Access

  1. In Cloudflare One, go to **Access controls** > **Applications** , select **Create new application** , and select **SaaS application**.

  2. Set the **Application type** to _Hubspot_.

  3. Use the following Hubspot field mappings:

Hubspot values | Cloudflare values  
---|---  
Audience URI | Entity ID  
Sign On URL | Assertion Consumer Service URL  
  
  4. Set **NameID** to _Email_.

  5. Add any desired [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) to your application.

  6. Copy the **SSO endpoint** and **Access Entity ID**.

  7. Save the application.




## 3\. Create a x.509 certificate

  1. Paste the **Public key** in a text editor.
  2. Wrap the certificate in `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`.



## 4\. Finalize Hubspot configuration

  1. Use the following field mappings:

Cloudflare value | Hubspot value  
---|---  
SSO endpoint | Identity Provider Single Sign-on URL  
Entity ID | Identity Provider Identifier  
Public key | Certificate  
  
  2. Select **Verify** to validate the integration.




Your configuration is now complete. Hubspot SSO can be switched on for specific users or the entire account.

[PreviousGreenhouse Recruiting](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/greenhouse-saas/)[NextIronclad](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/ironclad-saas/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/http-apps/saas-apps/hubspot-saas.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
