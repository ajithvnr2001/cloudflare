---
url: https://developers.cloudflare.com/changelog/post/2026-06-25-api-token-search/
title: Search API tokens by name \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:36.008792+00:00
---

# Search API tokens by name · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-25-api-token-search/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 25, 2026

## Search API tokens by name

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now search API tokens by name, making it easier to find specific tokens across large token lists without manually paginating.

#### What's new

  * **Dashboard search** : Both [account API tokens ↗︎](https://dash.cloudflare.com/?to=/:account/account-api-tokens) and [user API tokens ↗︎](https://dash.cloudflare.com/profile/api-tokens) pages now include a search bar. Type a name to filter results.
  * **API search support** : The [`/user/tokens`](https://developers.cloudflare.com/api/resources/user/subresources/tokens/methods/list/) and [`/accounts/{account_id}/tokens`](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/methods/list/) endpoints now accept a `name` query parameter to filter tokens by name.



For more information, refer to [Create an API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) and [Account API tokens](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/).
