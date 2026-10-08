---
url: https://developers.cloudflare.com/changelog/post/2026-04-14-oauth-consent-and-revoke/
title: Improved OAuth experience for consent and management \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:46.633702+00:00
---

# Improved OAuth experience for consent and management · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-14-oauth-consent-and-revoke/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 14, 2026

## Improved OAuth experience for consent and management

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-14-oauth-consent-and-revoke/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OAuth allows third-party applications to access your Cloudflare account on your behalf — like when Wrangler deploys Workers or when monitoring tools read your analytics. You now have **granular control** over which accounts these applications can access, plus the ability to revoke access anytime.

#### What's new

#### Choose which accounts to authorize

When authorizing an OAuth application, you can now **select specific accounts** instead of granting access to all your accounts:

  * **Account-by-account selection** — Choose exactly which accounts the application can access
  * **"All accounts" option** — Still available for trusted tools like Wrangler This gives you precise control who can access your data.



#### Clear consent screens

The OAuth consent screen now shows:

  * **What the application can access** — Explicit list of permissions being requested
  * **Who created the application** — Application owner and contact information
  * **Which accounts you're authorizing** — Checkboxes for account selection



#### Revoke access anytime

Manage authorized OAuth applications from your profile:

  * **See all connected apps** — View every OAuth application with access to your accounts
  * **Review permissions and scope** — Check what each application can do and which accounts it can access
  * **Revoke instantly** — Remove access with one click when you no longer need it To manage your OAuth applications, navigate to **Profile** > **Access Management** > **[Connected Applications ↗︎](https://dash.cloudflare.com/profile/access-management/authorization)**.



#### Why this matters

These updates give you:

  * **Granular control** — Authorize apps per-account instead of all-or-nothing
  * **Transparency** — Know exactly what you're authorizing before you consent
  * **Security** — Limit blast radius by restricting access to only necessary accounts
  * **Easy cleanup** — Revoke access when applications are no longer needed



#### Learn more

Read more about these improvements in our blog post: [Improving the OAuth consent experience ↗︎](https://blog.cloudflare.com/improved-developer-security/#improving-the-oauth-consent-experience).
