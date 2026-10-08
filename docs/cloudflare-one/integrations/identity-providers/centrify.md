---
url: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/centrify/
title: Centrify \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:02.333170+00:00
---

# Centrify · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/centrify/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)
  5. /Centrify



# Centrify

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/centrify/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up Centrify as an OIDC provider 1\. Create an application in Centrify 2\. Add Centrify to Cloudflare OneExample API Config

Centrify secures access to infrastructure, DevOps, cloud, and other modern enterprise so you can prevent the number one cause of breaches: privileged access abuse.

## Set up Centrify as an OIDC provider

### 1\. Create an application in Centrify

  1. Log in to the Centrify administrator panel.

  2. Select **Apps**.

  3. Select **Add Web Apps**.

  4. Select the **Custom** tab, then select **Add OpenID Connect**.

  5. On the **Add Web App** screen, select **Yes** to create an OpenID Connect application.

  6. Enter an **Application ID**.

![Centrify Settings with Application ID added](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1999,height=1136,format=webp/_astro/centrify-4.C0i78_vc.png)
  7. Select **Save**.

  8. Select **Trust** in the **Settings** menu.

  9. Enter a strong application secret on the **Trust** section.

  10. Under **Service Provider Configuration** enter your application's authentication domain as the resource application URL.

  11. Under **Authorized Redirect URIs** , select **Add**.

  12. Under **Authorized Redirect URIs** , enter the following URL:
         
         https://<your-team-name>.cloudflareaccess.com/cdn-cgi/access/callback

You can find your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) under **Settings** > **Team name and domain** > **Team name**.

![Centrify Trust Identity Provider Configuration with team domain and callback](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1999,height=1343,format=webp/_astro/centrify-6.ChCQ_t69.png)
  13. Select **Save**.

  14. Copy the following values:



  * **Client ID**
  * **Client Secret**
  * **OpenID Connect Issuer URL**
  * **Application ID** from the **Settings** tab


  15. Go to the **User Access** tab.

  16. Select the roles to grant access to your application.




### 2\. Add Centrify to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.

  2. Under **Your identity providers** , select **Add new identity provider**.

  3. Paste in the **Client ID** , **Client Secret** , **Centrify account URL** and **Application ID**.

  4. (Optional) To enable SCIM, refer to [Synchronize users and groups](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-oidc/#synchronize-users-and-groups).

  5. (Optional) Under **Optional configurations** , enter [custom OIDC claims](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims) that you wish to add to your users' identity.

  6. Select **Save**.




To test that your connection is working, go to **Integrations** > **Identity providers** and select **Test** next to the identity provider you want to test.

## Example API Config
    
    
    {
    	"config": {
    		"client_id": "<your client id>",
    		"client_secret": "<your client secret>",
    		"centrify_account": "https://abc123.my.centrify.com/",
    		"centrify_app_id": "exampleapp"
    	},
    	"type": "centrify",
    	"name": "my example idp"
    }

[PreviousAWS IAM (SAML)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/aws-saml/)[NextCentrify (SAML)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/centrify-saml/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/identity-providers/centrify.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
