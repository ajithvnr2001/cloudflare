---
url: https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-idp-default/
title: Cloudflare identity provider is now the default for new accounts \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:58.632551+00:00
---

# Cloudflare identity provider is now the default for new accounts · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-idp-default/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 18, 2026

## Cloudflare identity provider is now the default for new accounts

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-idp-default/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When you create a new Zero Trust organization, Cloudflare now adds the [Cloudflare identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/) as your default login method. Previously, new organizations started with [one-time PIN (OTP)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/).

With the Cloudflare identity provider, your users authenticate using their existing Cloudflare account credentials, and authentication is restricted to members of your account. You can still add OTP or connect any [third-party identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) whenever you need to.

This change only applies to newly created accounts. Existing organizations keep the login methods they already have configured. If you would like to use the Cloudflare Identity Provider in an existing account, you must enable it.
