---
url: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/yandex/
title: Yandex \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:06.303399+00:00
---

# Yandex · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/yandex/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)
  5. /Yandex



# Yandex

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/yandex/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up YandexExample API Config

Yandex is a web search engine that also offers identity provider (IdP) services.

## Set up Yandex

To set up Yandex for Cloudflare Access:

  1. Log in to your Yandex account.

  2. Select **Open a new OAuth Application**.

  3. Select **New client**.

  4. Complete the required fields.

  5. Choose **Yandex.Passport API** to set the basic scopes.

  6. Select the **Access to email address** , **Access to user avatar,** and **Access to username, first name and surname, gender** options.

  7. Select **Platform** and select **Web Services.**

  8. In the **Callback URL #1** field, enter the following URL:
         
         https://<your-team-name>.cloudflareaccess.com/cdn-cgi/access/callback

You can find your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) under **Settings** > **Team name and domain** > **Team name**.

![Yandex Platform interface with Web services checked and callback URI in open form field](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1414,height=694,format=webp/_astro/yandex-3.DteBNxdB.png)
  9. Select **Add**.

  10. Scroll to the **Platforms** card, and select **Submit**.

**Yandex OAuth** card titled **Cloudflare Access App** displays.

  11. Copy the **ID** and **Password**.

  12. In Cloudflare One, go to **Integrations** > **Identity providers**.

  13. Under **Your identity providers** , select **Add new identity provider**.

  14. Select Yandex.

  15. Paste the ID and password in the appropriate fields.

  16. Select **Save**.




## Example API Config
    
    
    {
    	"config": {
    		"client_id": "<your client id>",
    		"client_secret": "<your client secret>"
    	},
    	"type": "yandex",
    	"name": "my example idp"
    }

[PreviousSigned AuthN requests (SAML)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/signed_authn/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/identity-providers/yandex.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
