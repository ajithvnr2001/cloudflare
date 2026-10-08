---
url: https://developers.cloudflare.com/fundamentals/api/get-started/keys/
title: Get Global API key (legacy) \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:20.517602+00:00
---

# Get Global API key (legacy) · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/api/get-started/keys/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /…

Cloudflare's API

  4. /Get started
  5. /Get Global API key (legacy)



# Get Global API key (legacy)

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/api/get-started/keys/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLimitationsView your Global API keyChange your Global API key

Global API key is the previous authorization scheme for interacting with the Cloudflare API. When possible, use [API tokens](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) instead of Global API key.

New and rolled Global API Keys use the `cfk_` prefixed [scannable format](https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/), which allows credential scanning tools to detect leaked keys.

Note

Global API key is only available after the [account email address is verified](https://developers.cloudflare.com/fundamentals/user-profiles/verify-email-address/).

## Limitations

Global API key has multiple limitations when compared to API tokens:

  * **Access to all Cloudflare resources** \- Global API key has access to all of a user's resources. This makes it impossible to safely use Global API key to access non-production resources when a user also has access to production resources.

  * **Full permissions** \- Similarly, Global API key has the exact same permissions as the user, which means if the user can delete zones or change DNS records, so can the Global API key.

  * **Limited to one per user** \- Only one Global API key can be provisioned per user. This complicates using Cloudflare's API in production systems where maintaining two secrets for accessing the API is important in the case one needs to be rolled.

  * **Lack of advanced limits on usage** \- API tokens can be limited to specific time windows and expire or be limited to use from specific IP ranges.




For these reasons, Global API key is not recommended for new customers. Current customers using Global API key are encouraged to migrate and use API tokens instead.

## View your Global API key

To retrieve your Global API key:

  1. In the Cloudflare dashboard and select **User Profile** > **API Tokens**.

[ Go to **Account API tokens** ↗ ](https://dash.cloudflare.com/?to=/:account/api-tokens)
  2. In the **API Keys** section, click `View` button of **Global API Key**.




## Change your Global API key

If your API key might be compromised, change your API key:

  1. Log in to the Cloudflare dashboard.

[ Go to **Account home** ↗ ](https://dash.cloudflare.com/?to=/:account/home)
  2. Go to **My Profile** > **API Tokens**.

  3. In the **API Keys** section, find your key.

  4. Select **Change**.




[PreviousCreate API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/)[NextGet Origin CA keys](https://developers.cloudflare.com/fundamentals/api/get-started/ca-keys/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/api/get-started/keys.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
