---
url: https://developers.cloudflare.com/changelog/post/2025-06-30-graceful-byoip-withdrawal/
title: Graceful withdrawal of BYOIP prefixes \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:51.307129+00:00
---

# Graceful withdrawal of BYOIP prefixes · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-30-graceful-byoip-withdrawal/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 30, 2025

## Graceful withdrawal of BYOIP prefixes

[Magic Transit](https://developers.cloudflare.com/magic-transit/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Magic Transit customers can now configure AS prepending on their BYOIP prefixes advertised at the Cloudflare edge. This allows for smoother traffic migration and minimizes packet loss when changing providers.

AS prepending makes the Cloudflare route less preferred by increasing the AS path length. You can use this to gradually shift traffic away from Cloudflare before withdrawing a prefix, avoiding abrupt routing changes.

Prepending can be configured via the API or through BGP community values when peering with the Magic Transit routing table. For more information, refer to [Advertise prefixes](https://developers.cloudflare.com/magic-transit/how-to/advertise-prefixes/).
