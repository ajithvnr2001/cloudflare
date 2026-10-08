---
url: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingfederate-saml/
title: PingFederate \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:05.502633+00:00
---

# PingFederate · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingfederate-saml/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)
  5. /PingFederate



# PingFederate

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingfederate-saml/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up PingFederate as an identity providerExample API configuration

The PingFederate offering from PingIdentity provides SSO identity management. Cloudflare Access supports PingFederate as a SAML identity provider.

## Set up PingFederate as an identity provider

  1. Log in to your **Ping** dashboard and go to **Applications**.

  2. Select **Add Application**.

  3. Select **New SAML Application**.

  4. Complete the fields for name, description, and category.




These can be any value. A prompt displays to select a signing certificate to use.

  5. In the **SAML attribute configuration** dialog select **Email attribute** > **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

  6. Go to **SP Connections** > **SP Connection** > **Credentials**.

  7. Add the matching certificate that you upload into the Cloudflare SAML configuration for Ping. Select **Include the certificate in the signature`<KEYINFO>` element**.




Note

There is an additional setting for PingFederate prior to 9.0.

  8. In the **Signature Policy** tab, disable the option to **Always Sign Assertion**.

  9. Leave the option enabled for **Sign Response As Required**.




This ensures that SAML destination headers are sent during the integration.

In versions 9.0 above, you can leave both of these options enabled.

  10. A prompt displays to download the SAML metadata from Ping.



This file shares several fields with Cloudflare Access so you do not have to input this data.

  11. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.

  12. Under **Your identity providers** , select **Add new identity provider**.

  13. Select SAML.

  14. In the **IdP Entity ID** field, enter the following URL:



    
    
    https://<your-team-name>.cloudflareaccess.com/cdn-cgi/access/callback

You can find your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) under **Settings** > **Team name and domain** > **Team name**.

  15. Fill the other fields with values from your Ping dashboard.

  16. Select **Save**.




To test that your connection is working, go to **Authentication** > **Login methods** and select **Test** next to the login method you want to test.

## Example API configuration
    
    
    {
    	"config": {
    		"issuer_url": "https://example.cloudflareaccess.com/cdn-cgi/access/callback",
    		"sso_target_url": "https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=aebe6668-32fe-4a87-8c2b-avcd3599a123",
    		"attributes": ["PingOne.AuthenticatingAuthority", "PingOne.idpid"],
    		"email_attribute_name": "",
    		"sign_request": false,
    		"idp_public_cert": "MIIDpDCCAoygAwIBAgIGAV2ka+55MA0GCSqGSIb3DQEBCwUAMIGSMQswCQYDVQQGEwJVUzETMBEG\nA1UEC.....GF/Q2/MHadws97cZg\nuTnQyuOqPuHbnN83d/2l1NSYKCbHt24o"
    	},
    	"type": "saml",
    	"name": "ping saml example"
    }

[PreviousOneLogin (SAML)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-saml/)[NextPingOne](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-oidc/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/identity-providers/pingfederate-saml.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
