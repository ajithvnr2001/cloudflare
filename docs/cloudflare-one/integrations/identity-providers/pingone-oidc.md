---
url: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-oidc/
title: PingOne \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:05.667802+00:00
---

# PingOne · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-oidc/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)
  5. /PingOne



# PingOne

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-oidc/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up PingOne as an OIDC provider 1\. Create an application in PingOne 2\. Add PingOne to Cloudflare OneExample API configuration

The PingOne cloud platform from PingIdentity provides SSO identity management. Cloudflare Access supports PingOne as an OIDC identity provider.

## Set up PingOne as an OIDC provider

### 1\. Create an application in PingOne

  1. In your PingIdentity environment, go to **Connections** > **Applications**.

  2. Select **Add Application**.

  3. Enter an **Application Name**.

  4. Select **OIDC Web App** and then **Save**.

  5. Select **Resource Access** and add the **email** and **profile** scopes.

  6. In the **Configuration** tab, select **General**.

  7. Copy the **Client ID** , **Client Secret** , and **Environment ID** to a safe place. These IDs will be used in a later step to add PingOne to Cloudflare One.

  8. In the **Configuration** tab, select the pencil icon.

  9. In the **Redirect URIs** field, enter the following URL:
         
         https://<your-team-name>.cloudflareaccess.com/cdn-cgi/access/callback

You can find your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) under **Settings** > **Team name and domain** > **Team name**.

  10. Select **Save**.




### 2\. Add PingOne to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.
  2. Under **Your identity providers** , select **Add new identity provider**.
  3. Select **PingOne**.
  4. Input the **Client ID** , **Client Secret** , and **Environment ID** generated previously.
  5. (Optional) Enable [Proof of Key Exchange (PKCE) ↗︎](https://www.oauth.com/oauth2-servers/pkce/). PKCE will be performed on all login attempts.
  6. (Optional) To enable SCIM, refer to [Synchronize users and groups](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-oidc/#synchronize-users-and-groups).
  7. (Optional) Under **Optional configurations** , enter [custom OIDC claims](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims) that you wish to add to your users' identity.
  8. Select **Save**.



You can now [test your connection](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/#test-idps-in-cloudflare-one) and create [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) based on the configured login method.

## Example API configuration
    
    
    {
    	"config": {
    		"client_id": "<your client id>",
    		"client_secret": "<your client secret>",
    		"ping_env_id": "<your ping environment id>"
    	},
    	"type": "ping",
    	"name": "my example idp"
    }

[PreviousPingFederate](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingfederate-saml/)[NextPingOne (SAML)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-saml/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/identity-providers/pingone-oidc.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
