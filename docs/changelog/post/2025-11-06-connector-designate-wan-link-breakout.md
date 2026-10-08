---
url: https://developers.cloudflare.com/changelog/post/2025-11-06-connector-designate-wan-link-breakout/
title: Designate WAN link for breakout traffic \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:28.366290+00:00
---

# Designate WAN link for breakout traffic · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-06-connector-designate-wan-link-breakout/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 6, 2025

## Designate WAN link for breakout traffic

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-06-connector-designate-wan-link-breakout/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Magic WAN Connector now allows you to designate a specific WAN port for breakout traffic, giving you deterministic control over the egress path for latency-sensitive applications.

With this feature, you can:

  * Pin breakout traffic for specific applications to a preferred WAN port.
  * Ensure critical traffic (such as Zoom or Teams) always uses your fastest or most reliable connection.
  * Benefit from automatic failover to standard WAN port priority if the preferred port goes down.



This is useful for organizations with multiple ISP uplinks who need predictable egress behavior for performance-sensitive traffic.

For configuration details, refer to [Designate WAN ports for breakout apps](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#designate-wan-ports-for-breakout-apps).
