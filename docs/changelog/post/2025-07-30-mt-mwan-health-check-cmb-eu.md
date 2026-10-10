---
url: https://developers.cloudflare.com/changelog/post/2025-07-30-mt-mwan-health-check-cmb-eu/
title: Magic Transit and Magic WAN health check data is fully compatible with the CMB EU setting. \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:50.535655+00:00
---

# Magic Transit and Magic WAN health check data is fully compatible with the CMB EU setting. · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-30-mt-mwan-health-check-cmb-eu/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 30, 2025

## Magic Transit and Magic WAN health check data is fully compatible with the CMB EU setting.

[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Today, we are excited to announce that all Magic Transit and Magic WAN customers with CMB EU ([Customer Metadata Boundary - Europe](https://developers.cloudflare.com/data-localization/metadata-boundary/)) enabled in their account will be able to access GRE, IPsec, and CNI health check and traffic volume data in the Cloudflare dashboard and via API.

This ensures that all Magic Transit and Magic WAN customers with CMB EU enabled will be able to access all Magic Transit and Magic WAN features.

Specifically, these two GraphQL endpoints are now compatible with CMB EU:

  * `magicTransitTunnelHealthChecksAdaptiveGroups`
  * `magicTransitTunnelTrafficAdaptiveGroups`


