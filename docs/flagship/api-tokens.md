---
url: https://developers.cloudflare.com/flagship/api-tokens/
title: API tokens \u00b7 Cloudflare Flagship docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:17.795120+00:00
---

# API tokens · Cloudflare Flagship docs

> Source: https://developers.cloudflare.com/flagship/api-tokens/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Flagship](https://developers.cloudflare.com/flagship/)
  3. /API tokens



# API tokens

Last updated Aug 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/flagship/api-tokens/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate an account-wide tokenCreate an app-scoped tokenUse the tokenNext steps

Flagship supports two kinds of API tokens. Both use the same [Create API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) flow. The difference is the resource the permission policy applies to.

Token type | Resource | What it can access  
---|---|---  
Account-wide | **Entire Account** | Every Flagship app in the account  
App-scoped | **Specified Flagship apps** | Only the Flagship apps you select  
  
Use an account-wide token when a trusted server-side workflow needs access to every Flagship app. Use an app-scoped token when that workflow should only touch the apps you select — for example, CI or a backend service for one product.

Both token types support **Read** , **Write** , and **Evaluate**. The names change with the resource:

Access | Account-wide | App-scoped  
---|---|---  
Evaluate flags | **Flagship Evaluate** | **Flagship App Evaluate**  
Read flag configuration | **Flagship Read** | **Flagship App Read**  
Manage flags | **Flagship Write** | **Flagship App Write**  
  
You must [create a Flagship app](https://developers.cloudflare.com/flagship/get-started/#create-an-app-and-a-flag) before you can create an app-scoped token. The dashboard can only list apps that already exist.

## Create an account-wide token

[Create an account-wide Flagship token ↗︎](https://dash.cloudflare.com/?to=/:account/api-tokens) to open the Account API tokens page. Then create a custom token and leave the resource set to **Entire Account**.

To create the token yourself:

  1. In the Cloudflare dashboard, go to the **Account API tokens** page.

[ Go to **Account API tokens** ↗ ](https://dash.cloudflare.com/?to=/:account/api-tokens)

You can also create a user token from [My Profile ↗︎](https://dash.cloudflare.com/profile/api-tokens) > **API Tokens**.

  2. Select **Create Token**.

  3. Select **Create Custom Token** > **Get started**.

  4. Enter a token name.

  5. Under **Permission policies** , leave the resource dropdown set to **Entire Account**.

  6. Search for Flagship and select **Flagship Evaluate** , **Flagship Read** , or **Flagship Write**.

  7. (Optional) Restrict the token with [IP address filtering or a TTL](https://developers.cloudflare.com/fundamentals/api/how-to/restrict-tokens/).

  8. Select **Review token** > **Create Token**.

  9. Copy the token secret and store it securely.




Warning

The token secret is **only shown once**. Do not store the secret in plaintext where others can access it. Anyone with this token can perform the authorized actions against the resources that the token has access to.

## Create an app-scoped token

[Create an app-scoped Flagship token ↗︎](https://dash.cloudflare.com/?to=/:account/api-tokens&permissionGroupKeys=%5B%7B%22key%22:%22flagship_app%22,%22type%22:%22evaluate%22%7D%5D&scope=specified_flagship_app) to open the token form with **Specified Flagship apps** and **Flagship App Evaluate** already selected. Then choose the app and create the token.

To create the token yourself:

  1. In the Cloudflare dashboard, go to the **Account API tokens** page.

[ Go to **Account API tokens** ↗ ](https://dash.cloudflare.com/?to=/:account/api-tokens)

You can also create a user token from [My Profile ↗︎](https://dash.cloudflare.com/profile/api-tokens) > **API Tokens**.

  2. Select **Create Token**.

  3. Select **Create Custom Token** > **Get started**.

  4. Enter a token name that describes where you will use it, such as `checkout-service-ci`.

  5. Under **Permission policies** , open the resource dropdown (it defaults to **Entire Account**) and select **Specified Flagship apps**.

  6. In **Select Flagship apps** , choose the app or apps this token should access.

  7. Under **Developer Platform** , select a **Flagship App** permission:

Use case | Permission  
---|---  
Evaluate flags in the selected apps | **Flagship App Evaluate**  
Read flag configuration for the selected apps | **Flagship App Read**  
Manage flags in the selected apps | **Flagship App Write**  
  
  8. (Optional) Restrict the token with [IP address filtering or a TTL](https://developers.cloudflare.com/fundamentals/api/how-to/restrict-tokens/).

  9. Select **Review token** > **Create Token**.

  10. Copy the token secret and store it securely.




Warning

The token secret is **only shown once**. Do not store the secret in plaintext where others can access it. Anyone with this token can perform the authorized actions against the resources that the token has access to.

## Use the token

Pass the token to an OpenFeature SDK as `authToken` (TypeScript) or the equivalent option in [Python](https://developers.cloudflare.com/flagship/sdk/python/) and [Go](https://developers.cloudflare.com/flagship/sdk/go/).
    
    
    import { OpenFeature } from "@openfeature/server-sdk";
    import { FlagshipServerProvider } from "@cloudflare/flagship/server";
    
    await OpenFeature.setProviderAndWait(
    	new FlagshipServerProvider({
    		appId: "<APP_ID>",
    		accountId: "<ACCOUNT_ID>",
    		authToken: "<APP_SCOPED_API_TOKEN>",
    	}),
    );

Replace `<APP_ID>` and `<ACCOUNT_ID>` with the app and account the token is scoped to. An app-scoped token is rejected if you evaluate a different app.

Inside a Cloudflare Worker, prefer the [binding](https://developers.cloudflare.com/flagship/binding/). The binding authenticates automatically and does not need an API token.

## Next steps

  * Set up the [TypeScript Server SDK](https://developers.cloudflare.com/flagship/sdk/server-provider/) outside of Workers.
  * Restrict token use with [IP filtering or a TTL](https://developers.cloudflare.com/fundamentals/api/how-to/restrict-tokens/).



[PreviousConcepts](https://developers.cloudflare.com/flagship/concepts/)[NextConfiguration](https://developers.cloudflare.com/flagship/configuration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/flagship/api-tokens.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
