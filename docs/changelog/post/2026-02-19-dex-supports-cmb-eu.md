---
url: https://developers.cloudflare.com/changelog/post/2026-02-19-dex-supports-cmb-eu/
title: DEX Supports EU Customer Metadata Boundary \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:37.855767+00:00
---

# DEX Supports EU Customer Metadata Boundary · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-19-dex-supports-cmb-eu/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 19, 2026

## DEX Supports EU Customer Metadata Boundary

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-19-dex-supports-cmb-eu/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) provides visibility into [WARP](https://developers.cloudflare.com/warp-client/) device connectivity and performance to any internal or external application.

Now, all DEX logs are fully compatible with Cloudflare's [Customer Metadata Boundary](https://developers.cloudflare.com/data-localization/metadata-boundary/) (CMB) setting for the 'EU' (European Union), which ensures that DEX logs will not be stored outside the 'EU' when the option is configured.

If a Cloudflare One customer using DEX enables CMB 'EU', they will not see any DEX data in the Cloudflare One dashboard. Customers can ingest DEX data via [LogPush](https://developers.cloudflare.com/logs/logpush/), and build their own analytics and dashboards.

If a customer enables CMB in their account, they will see the following message in the Digital Experience dashboard: "DEX data is unavailable because Customer Metadata Boundary configuration is on. Use Cloudflare LogPush to export DEX datasets."

![Digital Experience Monitoring message when Customer Metadata Boundary for the EU is enabled](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2143,height=1221,format=webp/_astro/dex_supports_cmb.6YOLXjHN.png)
