---
url: https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/
title: Introducing self-managed OAuth clients \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:37.294528+00:00
---

# Introducing self-managed OAuth clients · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 3, 2026

## Introducing self-managed OAuth clients

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Today we are launching self-managed OAuth, enabling developers to build third-party applications that integrate with Cloudflare via OAuth. This provides a more secure, user-friendly, and manageable alternative to API tokens.

OAuth lets third-party applications act on behalf of a user to access their Cloudflare account. For example, after a user grants consent, Wrangler can deploy Workers into that account.

#### What is new

Cloudflare Developers can now create and manage their own OAuth applications to integrate with Cloudflare.

#### Create an application

To create an application, go to **Manage account** > **OAuth clients** in your account on the Cloudflare dashboard.

[ Go to **OAuth clients** ↗ ](https://dash.cloudflare.com/?to=/:account/oauth-clients)

#### Select limited scopes

If you have used an API token to call Cloudflare APIs, OAuth client scopes will look familiar. Select only the scopes your application needs during application creation, and include that scope list when sending users to Cloudflare for consent.

Users can review the requested scopes before they consent.

#### Apps for both private and public use

Applications start with `private` visibility. Private applications can only be used by members of the account where the application was created.

To make an application available to any Cloudflare user, complete the prerequisites for `public` visibility.

For more information, refer to [client visibility](https://developers.cloudflare.com/fundamentals/oauth/create-an-oauth-client/#private-and-public-clients).

#### Client domain verification

Before an application can be made public, you must verify the client domain. Domain verification helps users confirm that the application owner controls the domain shown on the consent page.

After verification, users see a verified badge on the consent page.

For more information, refer to [domain verification](https://developers.cloudflare.com/fundamentals/oauth/create-an-oauth-client/#client-url-domain-ownership-verification).

#### Learn more

For more information, refer to [OAuth clients](https://developers.cloudflare.com/fundamentals/oauth/).
