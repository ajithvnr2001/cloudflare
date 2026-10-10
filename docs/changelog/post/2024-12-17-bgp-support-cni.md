---
url: https://developers.cloudflare.com/changelog/post/2024-12-17-bgp-support-cni/
title: Establish BGP peering over Direct CNI circuits \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:55.703192+00:00
---

# Establish BGP peering over Direct CNI circuits · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2024-12-17-bgp-support-cni/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 17, 2024

## Establish BGP peering over Direct CNI circuits

[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Network Interconnect](https://developers.cloudflare.com/network-interconnect/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using a Direct CNI on-ramp.

Using BGP peering allows customers to:

  * Automate the process of adding or removing networks and subnets.
  * Take advantage of failure detection and session recovery features.



With this functionality, customers can:

  * Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via CNI.
  * Secure the session by MD5 authentication to prevent misconfigurations.
  * Exchange routes dynamically between their devices and their Magic routing table.



Refer to [Magic WAN BGP peering](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes) or [Magic Transit BGP peering](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#configure-bgp-routes) to learn more about this feature and how to set it up.
