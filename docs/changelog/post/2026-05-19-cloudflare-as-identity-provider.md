---
url: https://developers.cloudflare.com/changelog/post/2026-05-19-cloudflare-as-identity-provider/
title: Cloudflare as identity provider and account membership selector \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:53.800553+00:00
---

# Cloudflare as identity provider and account membership selector · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-19-cloudflare-as-identity-provider/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 19, 2026

## Cloudflare as identity provider and account membership selector

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-19-cloudflare-as-identity-provider/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access now supports using Cloudflare itself as an [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/). If you publish an Access application and select Cloudflare as the login method, users can sign in with their existing Cloudflare account — no one-time PINs, no third-party IdP configuration, and no shared email inboxes. Authentication is backed by Cloudflare's own account security (including multi-factor authentication), making it both simpler to set up and more secure than OTP-based login for most use cases.

Cloudflare is now the **default identity provider for all newly created Zero Trust accounts** , replacing One-time PIN.

This also enables two new capabilities:

  * **Cloudflare Account Member selector** — A new [policy selector](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/#selectors) that matches users based on their membership in a Cloudflare account. You can target the current account or specify a different account ID for cross-account access scenarios.
  * **Restrict to account members** — An identity provider configuration option that limits authentication to users who are members of your Cloudflare account.



To get started, add Cloudflare as an [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/) in your Zero Trust settings.
