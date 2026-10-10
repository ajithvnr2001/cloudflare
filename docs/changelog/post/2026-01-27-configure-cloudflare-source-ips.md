---
url: https://developers.cloudflare.com/changelog/post/2026-01-27-configure-cloudflare-source-ips/
title: Configure Cloudflare source IPs (beta) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:44.609688+00:00
---

# Configure Cloudflare source IPs (beta) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-27-configure-cloudflare-source-ips/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 27, 2026

## Configure Cloudflare source IPs (beta)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare source IPs are the IP addresses used by Cloudflare services (such as Load Balancing, Gateway, and Browser Isolation) when sending traffic to your private networks.

For customers using legacy mode routing, traffic to private networks is sourced from public Cloudflare IPs, which may cause IP conflicts. For customers using Unified Routing mode (beta), traffic to private networks is sourced from dedicated, non-Internet-routable private IPv4 range to ensure:

  * Symmetric routing over private network connections
  * Proper firewall state preservation
  * Private traffic stays on secure paths



Key details:

  * **IPv4** : Sourced from `100.64.0.0/12` by default, configurable to any `/12` CIDR
  * **IPv6** : Sourced from `2606:4700:cf1:5000::/64` (not configurable)
  * **Affected connectors** : GRE, IPsec, CNI, WARP Connector, and WARP Client (Cloudflare Tunnel is not affected)



Configuring Cloudflare source IPs requires Unified Routing (beta) and the `Cloudflare One Networks Write` permission.

For configuration details, refer to [Configure Cloudflare source IPs](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/).
