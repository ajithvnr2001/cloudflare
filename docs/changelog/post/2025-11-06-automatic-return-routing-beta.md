---
url: https://developers.cloudflare.com/changelog/post/2025-11-06-automatic-return-routing-beta/
title: Automatic Return Routing (Beta) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:28.345887+00:00
---

# Automatic Return Routing (Beta) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-06-automatic-return-routing-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 6, 2025

## Automatic Return Routing (Beta)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-06-automatic-return-routing-beta/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Magic WAN now supports Automatic Return Routing (ARR), allowing customers to configure Magic on-ramps (IPsec/GRE/CNI) to learn the return path for traffic flows without requiring static routes.

Key benefits:

  * **Route-less mode** : Static or dynamic routes are optional when using ARR.
  * **Overlapping IP space support** : Traffic originating from customer sites can use overlapping private IP ranges.
  * **Symmetric routing** : Return traffic is guaranteed to use the same connection as the original on-ramp.



This feature is currently in beta and requires the new Unified Routing mode (beta).

For configuration details, refer to [Configure Automatic Return Routing](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-automatic-return-routing).
