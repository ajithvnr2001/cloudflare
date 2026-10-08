---
url: https://developers.cloudflare.com/changelog/post/2026-07-07-authorization-proxy-endpoint-support/
title: Browser Isolation support for authorization proxy endpoints \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:01.442596+00:00
---

# Browser Isolation support for authorization proxy endpoints · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-07-authorization-proxy-endpoint-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 7, 2026

## Browser Isolation support for authorization proxy endpoints

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-07-authorization-proxy-endpoint-support/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) now supports Gateway [authorization proxy endpoints](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint). You can apply [HTTP Isolate policies](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/) to traffic routed through authorization proxy endpoints, the same way you can for traffic from the Cloudflare One Client.

Previously, only [source IP proxy endpoints](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint) supported Browser Isolation, and only with non-identity policies. Because authorization proxy endpoints authenticate users through an identity provider, you can now apply identity-based Isolate policies to PAC file-proxied traffic without requiring the Cloudflare One Client.

To get started, [create an authorization proxy endpoint](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint) and [build an Isolate policy](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/).
