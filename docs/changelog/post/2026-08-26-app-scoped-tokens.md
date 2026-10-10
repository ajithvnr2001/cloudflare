---
url: https://developers.cloudflare.com/changelog/post/2026-08-26-app-scoped-tokens/
title: Create app-scoped API tokens for Flagship \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.172375+00:00
---

# Create app-scoped API tokens for Flagship · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-26-app-scoped-tokens/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 26, 2026

## Create app-scoped API tokens for Flagship

[Flagship](https://developers.cloudflare.com/flagship/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create **app-scoped API tokens** for [Flagship](https://developers.cloudflare.com/flagship/). These tokens grant access only to the Flagship apps you select, instead of every app in the account.

When you create a custom token, open the resource dropdown (it defaults to **Entire Account**) and select **Specified Flagship apps**. Then choose the app and a **Flagship App** permission: Evaluate, Read, or Write. Account-wide Flagship Evaluate, Read, and Write permissions still exist when you need access to every app.

Use app-scoped tokens in trusted server-side environments, such as Wrangler, CI, or a backend service that should only touch one app.

To create a token, refer to [API tokens](https://developers.cloudflare.com/flagship/api-tokens/) or [open the app-scoped token form ↗︎](https://dash.cloudflare.com/?to=/:account/api-tokens&permissionGroupKeys=%5B%7B%22key%22:%22flagship_app%22,%22type%22:%22evaluate%22%7D%5D&scope=specified_flagship_app) in the dashboard.
