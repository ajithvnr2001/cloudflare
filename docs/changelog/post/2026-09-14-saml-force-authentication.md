---
url: https://developers.cloudflare.com/changelog/post/2026-09-14-saml-force-authentication/
title: Require fresh authentication for SAML identity providers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.310233+00:00
---

# Require fresh authentication for SAML identity providers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-14-saml-force-authentication/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 14, 2026

## Require fresh authentication for SAML identity providers

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access can now request fresh authentication from a SAML identity provider for every login. Turn on **Require reauthentication** in the Cloudflare dashboard, or set `force_authn` to `true` through the API. Access will then set `ForceAuthn` to `true` in signed and unsigned SAML authentication requests.

This option is useful when an application requires users to reauthenticate at the identity provider instead of relying on an existing identity provider session. The default value is `false`.

For configuration details, refer to [Require fresh authentication at the identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/#require-fresh-authentication-at-the-identity-provider).
