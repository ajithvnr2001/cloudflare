---
url: https://developers.cloudflare.com/fundamentals/api/how-to/roll-token/
title: Roll tokens \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:21.108987+00:00
---

# Roll tokens · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/api/how-to/roll-token/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /…

Cloudflare's API

  4. /How to
  5. /Roll tokens



# Roll tokens

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/api/how-to/roll-token/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

If your token is lost or compromised, you can either create a new token or roll your token to generate a new secret. Rolling your API token into a new one will invalidate the previous token, but the access and permissions will be the same as the previous API token. The new token uses the [scannable format](https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/), which allows credential scanning tools to detect leaked tokens.

To roll your API token:

  1. Go to **My Profile** > **API Tokens**.

[ Go to **API Tokens** ↗ ](https://dash.cloudflare.com/profile/api-tokens)
  2. Next to the API token you want to roll, select the **three dot icon** > **Roll**.

  3. Select **Confirm** to generate a new API token.




[PreviousRestrict tokens](https://developers.cloudflare.com/fundamentals/api/how-to/restrict-tokens/)[NextAPI token template URLs](https://developers.cloudflare.com/fundamentals/api/how-to/account-owned-token-template/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/api/how-to/roll-token.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
