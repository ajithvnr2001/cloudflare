---
url: https://developers.cloudflare.com/changelog/post/2026-02-17-clientless-access-for-private-apps/
title: Streamlined clientless browser isolation for private applications \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.563056+00:00
---

# Streamlined clientless browser isolation for private applications · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-17-clientless-access-for-private-apps/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 17, 2026

## Streamlined clientless browser isolation for private applications

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new **Allow clientless access** setting makes it easier to connect users without a device client to internal applications, without using public DNS.

![Allow clientless access setting in the Cloudflare One dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1117,height=206,format=webp/_astro/allow-clientless-access.BHKwQuVt.png)

Previously, to provide clientless access to a private hostname or IP without a [published application](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/#add-a-published-application-route), you had to create a separate [bookmark application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/bookmarks/) pointing to a prefixed [Clientless Web Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/) URL (for example, `https://<your-teamname>.cloudflareaccess.com/browser/https://10.0.0.1/`). This bookmark was visible to all users in the App Launcher, regardless of whether they had access to the underlying application.

Now, you can manage clientless access directly within your [private self-hosted application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/). When **Allow clientless access** is turned on, users who pass your Access application policies will see a tile in their App Launcher pointing to the prefixed URL. Users must have [remote browser permissions](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/) to open the link.
