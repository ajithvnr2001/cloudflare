---
url: https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-source-based-breakout/
title: Source-based breakout and prioritization on Cloudflare One Appliance \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:38.651263+00:00
---

# Source-based breakout and prioritization on Cloudflare One Appliance · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-source-based-breakout/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 7, 2026

## Source-based breakout and prioritization on Cloudflare One Appliance

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Breakout and traffic prioritization rules on the Cloudflare One Appliance can now match by **source** in addition to destination application. You can pin breakout or priority behavior to:

  * A source LAN interface — VLANs attached to that LAN are included automatically.
  * A source IP address, range, or CIDR block.



This is the natural way to break out a guest VLAN to the local Internet, or to prioritize traffic from a specific subnet, without enumerating destination applications.

For details, refer to [Breakout traffic](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source).
