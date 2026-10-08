---
url: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-saml/
title: OneLogin (SAML) \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:05.340928+00:00
---

# OneLogin (SAML) · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-saml/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)
  5. /OneLogin (SAML)



# OneLogin (SAML)

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-saml/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up OneLogin as a SAML provider1\. Create an application in OneLogin 2\. Add OneLogin to Cloudflare OneDownload SP metadata (optional)Example API configuration

OneLogin provides SSO identity management. Cloudflare Access supports OneLogin as an SAML identity provider.

## Set up OneLogin as a SAML provider

## 1\. Create an application in OneLogin

  1. Log in to your OneLogin admin portal.

  2. Select **Apps** > **Add Apps**.

  3. Under **Find Applications** , search for **Cloudflare Access**.

  4. Select the result sponsored by **Cloudflare, Inc**. You can customize the name or logo.

  5. Select **Save**. You can change this information at any time.

  6. Select the **Configuration** tab.

  7. In the **Cloudflare Access Authorization Domain** field, paste your team domain:
         
         https://<your-team-name>.cloudflareaccess.com

You can find your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) under **Settings** > **Team name and domain** > **Team name**.

  8. Select the **Parameters** tab, select **Add Parameter** and enter your values for **Cloudflare Access Field**.

  9. Select the **Access** tab

  10. In Roles, use the mapping to programmatically and automatically assign users that can access the application.

![OneLogin SAML Application Access interface with available Roles listed](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1999,height=932,format=webp/_astro/onelogin-saml-6.72q8OCR8.png)
  11. Select the **SSO** tab.

  12. Copy the OneLogin **SAML 2.0 Endpoint (HTTP)** to the Cloudflare Single Sign On URL.

  13. Copy the OneLogin **Issuer URL** to the Cloudflare **IdP Entity ID**.

  14. Copy the **X.509 Certificate** to the Cloudflare **Signing Certificate**.

![OneLogin SAML Application SSO interface with SAML2.0 sign on method, Issuer URL, and X.509 Certificate](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1999,height=1075,format=webp/_astro/onelogin-saml-7.DF0eCD1C.png)



### 2\. Add OneLogin to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.

  2. Under **Your identity providers** , select **Add new identity provider**.

  3. Select **SAML**.

  4. Input the details from your OneLogin account in the fields.

  5. (Optional) To enable SCIM, refer to [Synchronize users and groups](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/#synchronize-users-and-groups).

  6. (Optional) Under **Optional configurations** , configure [additional SAML options](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/#optional-configurations). If you added other SAML headers and attribute names to OneLogin, be sure to add them to Cloudflare.

  7. Select **Save**.




To test that your connection is working, go to **Integrations** > **Identity providers** and select **Test** next to the login method you want to test.

## Download SP metadata (optional)

OneLogin SAML allows administrators to upload metadata files from the service provider.

To add a metadata file to your OneLogin SAML configuration:

  1. Download your unique SAML metadata file at the following URL:
         
         https://<your-team-name>.cloudflareaccess.com/cdn-cgi/access/saml-metadata

  2. Save the file as an XML document.

  3. Upload the XML document to **OneLogin**.




## Example API configuration
    
    
    {
    	"config": {
    		"issuer_url": "https://app.onelogin.com/saml/metadata/1b84ee45-d4fa-4373-8853-abz438942123",
    		"sso_target_url": "https://sandbox.onelogin.com/trust/saml2/http-post/sso/123456",
    		"attributes": ["email"],
    		"email_attribute_name": "",
    		"sign_request": false,
    		"idp_public_cert": "MIIDpDCCAoygAwIBAgIGAV2ka+55MA0GCSqGSIb3DQEBCwUAMIGSMQswCQYDVQQGEwJVUzETMBEG\nA1UEC.....GF/Q2/MHadws97cZg\nuTnQyuOqPuHbnN83d/2l1NSYKCbHt24o"
    	},
    	"type": "saml",
    	"name": "onelogin saml example"
    }

[PreviousOneLogin](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-oidc/)[NextPingFederate](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingfederate-saml/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/identity-providers/onelogin-saml.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
