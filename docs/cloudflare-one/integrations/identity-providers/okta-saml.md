---
url: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta-saml/
title: Okta (SAML) \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:04.863379+00:00
---

# Okta (SAML) · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta-saml/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)
  5. /Okta (SAML)



# Okta (SAML)

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta-saml/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up Okta as a SAML providerExample API configuration

Cloudflare One can integrate SAML with Okta as an identity provider.

## Set up Okta as a SAML provider

To set up SAML with Okta as your identity provider:

  1. On your Okta admin dashboard, go to **Applications** > **Applications**.

  2. Select **Create App Integration**.

  3. In the pop-up dialog, select **SAML 2.0** and then elect **Next**.

  4. Enter an app name and select **Next**.

![Entering your Cloudflare One callback URL into Okta](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1063,height=515,format=webp/_astro/okta-saml-1.BO9WudzS.png)
  5. In the **Single sign on URL** and the **Audience URI (SP Entity ID)** fields, enter the following URL:
         
         https://<your-team-name>.cloudflareaccess.com/cdn-cgi/access/callback

You can find your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) under **Settings** > **Team name and domain** > **Team name**.

  6. In the **Attribute Statements** section, enter the following information:

     * **Name** : Enter `email`.
     * **Value** : Enter `user.email`.
  7. (Optional) If you are using Okta groups, create a **Group Attribute Statement** with the following information:

     * **Name** : Enter `groups`.
     * **Filter** : Select _Matches regex_ and enter `.*`.

![Configuring attribute statements in Okta](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=737,height=530,format=webp/_astro/okta-saml-2.BkDiypq5.png)

  8. Select **Next**.

  9. Select **I'm an Okta customer adding an internal app** and check **This is an internal app that we have created**.


![Configuring feedback options in Okta](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1354,height=746,format=webp/_astro/okta-saml-3.-GrxFq28.png)

  9. Select **Finish**.

  10. In the **Assignments** tab, select **Assign** and assign individuals or groups you want to grant access to.

  11. Select **Done**. The assigned individuals and groups will display in the **Assignments** tab.


![Assigning individuals and groups to Okta application](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1478,height=522,format=webp/_astro/okta-saml-4.CrMrhldk.png)

  12. To retrieve the SAML provider information, go to the **Sign On** tab and select **View Setup Instructions**. A new page will open showing the **Identity Provider Single Sign-on URL** , **Identity Provider Issuer** , and **X.509 Certificate**. Save this information for configuring your Cloudflare One settings.

![Retrieving SAML provider information in Okta](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1438,height=1262,format=webp/_astro/okta-saml-5.CWJU56SQ.png)

  13. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity provider**.

  14. Under **Your identity providers** , select **Add new identity provider** , and select _SAML_.

  15. Fill in the following information:

     * **Name** : Name your identity provider.
     * **Single Sign On URL** : Enter the Identity Provider Single-Sign-On URL from Okta.
     * **Issuer ID** : Enter the Identity Provider Issuer from Okta, for example `http://www.okta.com/<your-okta-entity-id>`.
     * **Signing Certificate** : Copy-paste the X.509 Certificate from Okta.
  16. (Recommended) Enable **Sign SAML authentication request**.

  17. (Recommended) Under **SAML attributes** , add the `email` and `groups` attributes. The `groups` attribute is required if you want to create policies based on [Okta groups](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/#okta-saml).


![Adding optional SAML attributes in Cloudflare One](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1098,height=756,format=webp/_astro/okta-saml-6.4pq9o6NF.png)

  18. Select **Save**.



To test that your connection is working, go to **Integrations** > **Identity providers** and select **Test** next to Okta. A success response should return the configured SAML attributes.

Caution

SAML attributes are only refreshed during authentications with the Okta identity provider. This means the Okta group membership is not updated unless a user logs in and out of the Cloudflare One Client, or logs in to an Access application.

## Example API configuration
    
    
    {
    	"config": {
    		"issuer_url": "http://www.okta.com/exkbhqj29iGxT7GwT0h7",
    		"sso_target_url": "https://dev-abc123.oktapreview.com/app/myapp/exkbhqj29iGxT7GwT0h7/sso/saml",
    		"attributes": ["email", "group"],
    		"email_attribute_name": "",
    		"sign_request": false,
    		"idp_public_certs": [
    			"MIIDpDCCAoygAwIBAgIGAV2ka+55MA0GCSqGSIb3DQEBCwUAMIGSMQswCQYDVQQGEwJVUzETMBEG\nA1UEC.....GF/Q2/MHadws97cZg\nuTnQyuOqPuHbnN83d/2l1NSYKCbHt24o"
    		]
    	},
    	"type": "saml",
    	"name": "okta saml example"
    }

[PreviousOkta](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta/)[NextOneLogin](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-oidc/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/identity-providers/okta-saml.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
