---
url: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/facebook-login/
title: Facebook \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:03.169682+00:00
---

# Facebook · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/facebook-login/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)
  5. /Facebook



# Facebook

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/facebook-login/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExample API Configuration

Use these steps to set up Facebook as your identity provider.

  1. Go to [developers.facebook.com ↗︎](https://developers.facebook.com/). Create a Developer account if you do not have one.

  2. Select **Create App** at the top-right. The **Create an app** card displays.

  3. Enter the **App name** and **App contact email**. Then, select **Next**.

  4. In the **Add use cases** page, select **Authenticate and request data from users with Facebook Login**. Select **Next**.

  5. Fill in the necessary information and select **Next** until you reach **Overview**. Then, select **Create app**.

  6. In the **My Apps** page, go to **App settings** > **Basic**.

  7. Copy the **App ID** and **App Secret**.

  8. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com), go to **Zero Trust** > **Integrations** > **Identity providers**.

  9. Under **Your identity providers** , select **Add an identity provider**.

  10. Fill in the **App ID** and **App Secret** obtained from Facebook.

  11. (Optional) Enable [Proof of Key Exchange (PKCE) ↗︎](https://www.oauth.com/oauth2-servers/pkce/). PKCE will be performed on all login attempts.

  12. Select **Save**.

  13. Go back to **My Apps** in [developers.facebook.com ↗︎](https://developers.facebook.com/), and select your app.

  14. Under **App customization and requirements** , select **Customize the Authenticate and request data from users with Facebook Login use case**.

  15. Select **Settings** , and ensure that **Use Strict Mode for redirect URIs** slider is set to **Yes**.

  16. In the **Valid OAuth Redirect URIs** field, enter the following URL:
         
         https://<your-team-name>.cloudflareaccess.com/cdn-cgi/access/callback

You can find your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) under **Settings** > **Team name and domain** > **Team name**.

  17. Select **Save Changes**.




To test that your connection is working, follow the steps on [SSO Integration](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/#test-idps-in-cloudflare-one).

## Example API Configuration
    
    
    {
    	"config": {
    		"client_id": "<your client id>",
    		"client_secret": "<your client secret>"
    	},
    	"type": "facebook",
    	"name": "my example idp"
    }

[PreviousCitrix ADC (SAML)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/citrixadc-saml/)[NextGitHub](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/github/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/identity-providers/facebook-login.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
