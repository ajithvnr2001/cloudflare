---
url: https://developers.cloudflare.com/changelog/post/2026-05-18-unified-routing-network-analytics/
title: Network Analytics support for Unified Routing \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:38.409605+00:00
---

# Network Analytics support for Unified Routing · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-18-unified-routing-network-analytics/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 18, 2026

## Network Analytics support for Unified Routing

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Network Analytics](https://developers.cloudflare.com/analytics/network-analytics/) is now fully supported for accounts using [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) mode. Traffic that traverses Unified Routing onramps and offramps is now visible in Network Analytics with the same dimensions and filters as traffic on the standard data plane.

This closes a parity gap for customers who had moved tunnels onto Unified Routing and lost visibility into their dataplane traffic in the Network Analytics dashboard. No configuration change is required — analytics data is collected automatically for all accounts with Unified Routing enabled.

For the remaining beta limitations, refer to [Traffic steering beta limitations](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#check-feature-availability-before-upgrading).
