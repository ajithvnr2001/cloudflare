---
url: https://developers.cloudflare.com/changelog/post/2026-08-03-eager-redirect-cookie-setting/
title: Control authorization cookies for multi-domain Access applications \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:33.964656+00:00
---

# Control authorization cookies for multi-domain Access applications · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-03-eager-redirect-cookie-setting/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 3, 2026

## Control authorization cookies for multi-domain Access applications

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access administrators can now control whether a self-hosted application preemptively sets authorization cookies across its public hostnames.

Previously, Access automatically used eager redirects for applications with five or fewer hostnames. Applications with more than five hostnames received cookies as users visited each hostname. Administrators can now choose either behavior, regardless of the number of hostnames.

The new **Eager redirect cookie** setting is turned on by default for new applications. After a user signs in, Access redirects the browser through each hostname and sets a `CF_Authorization` cookie. This supports applications that need to make requests across hostnames before the user visits each one.

For applications with many hostnames, the redirect chain can cause sign-in loops in some browsers. Turn off the setting to issue the cookie only when a user visits each hostname.

To configure the setting, refer to [Authorization cookie](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#eager-redirect-cookie).
