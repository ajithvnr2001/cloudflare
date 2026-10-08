---
url: https://developers.cloudflare.com/changelog/post/2026-01-30-bgp-over-tunnels/
title: BGP over GRE and IPsec tunnels \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:35.205366+00:00
---

# BGP over GRE and IPsec tunnels · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-30-bgp-over-tunnels/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 30, 2026

## BGP over GRE and IPsec tunnels

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-30-bgp-over-tunnels/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using IPsec and GRE tunnel on-ramps (beta).

Using BGP peering allows customers to:

  * Automate the process of adding or removing networks and subnets.
  * Take advantage of failure detection and session recovery features.



With this functionality, customers can:

  * Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via IPsec and GRE tunnel on-ramps.
  * Secure the session by MD5 authentication to prevent misconfigurations.
  * Exchange routes dynamically between their devices and their Magic routing table.



For configuration details, refer to:

  * [Configure BGP routes for Magic WAN](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes)
  * [Configure BGP routes for Magic Transit](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#configure-bgp-routes)


