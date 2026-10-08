---
url: https://developers.cloudflare.com/changelog/post/2026-06-23-regionalized-ip-bindings/
title: Regionalized IP Bindings for Regional Services \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:59.136584+00:00
---

# Regionalized IP Bindings for Regional Services · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-23-regionalized-ip-bindings/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 23, 2026

## Regionalized IP Bindings for Regional Services

[Data Localization Suite](https://developers.cloudflare.com/data-localization/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-23-regionalized-ip-bindings/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Regional Services now supports **Regionalized IP Bindings** , letting you regionalize traffic at the IP layer for prefixes you bring to Cloudflare through [Bring Your Own IP (BYOIP)](https://developers.cloudflare.com/byoip/).

Where [Regional Hostnames](https://developers.cloudflare.com/data-localization/regional-services/regional-hostnames/) regionalize traffic by hostname, Regionalized IP Bindings let you bind a CIDR from one of your prefixes to a region — ideal for address-map deployments and any service you address by IP rather than hostname. Cloudflare then terminates TLS and processes traffic to those addresses only within the data centers in that region.

Regionalized IP Bindings requires the Regional Services and Regional Services for BYOIP entitlements. Contact your account team to enable them.

To get started, refer to [Regionalized IP Bindings](https://developers.cloudflare.com/data-localization/regional-services/ip-bindings/).
