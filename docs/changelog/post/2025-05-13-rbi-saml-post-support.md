---
url: https://developers.cloudflare.com/changelog/post/2025-05-13-rbi-saml-post-support/
title: SAML HTTP-POST bindings support for RBI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:12.319705+00:00
---

# SAML HTTP-POST bindings support for RBI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-13-rbi-saml-post-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 13, 2025

## SAML HTTP-POST bindings support for RBI

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-13-rbi-saml-post-support/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Remote Browser Isolation (RBI) now supports SAML HTTP-POST bindings, enabling seamless authentication for SSO-enabled applications that rely on POST-based SAML responses from Identity Providers (IdPs) within a Remote Browser Isolation session. This update resolves a previous limitation that caused `405` errors during login and improves compatibility with multi-factor authentication (MFA) flows.

With expanded support for major IdPs like Okta and Azure AD, this enhancement delivers a more consistent and user-friendly experience across authentication workflows. Learn how to [set up Remote Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/).
