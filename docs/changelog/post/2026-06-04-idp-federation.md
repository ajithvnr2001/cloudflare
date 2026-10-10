---
url: https://developers.cloudflare.com/changelog/post/2026-06-04-idp-federation/
title: Share identity providers across accounts with IdP federation \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:37.210129+00:00
---

# Share identity providers across accounts with IdP federation · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-04-idp-federation/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 4, 2026

## Share identity providers across accounts with IdP federation

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access now supports [IdP federation](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/idp-federation/), which allows organizations to share a single identity provider across multiple Cloudflare accounts.

Instead of configuring the same IdP (for example, Okta or Entra ID) separately in every account, you configure it once in a source account and share it with the other accounts in your organization. Each recipient account gets a read-only IdP connection that routes authentication back to the source account through a bridge — a hidden application in the source account that brokers the cross-account login. End users sign in with their existing IdP credentials, and each account's Access policies evaluate the resulting identity just like any other IdP login.

Key capabilities:

  * **One IdP, many accounts** — Configure your IdP once and share it with all accounts in your organization.
  * **Lifecycle management** — As accounts join or leave your Cloudflare organization, their IdP connections are provisioned and removed automatically — no manual cleanup required.
  * **Immutable recipient connections** — IdP connections in recipient accounts cannot be accidentally modified or deleted.



To get started, refer to [IdP federation](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/idp-federation/).
