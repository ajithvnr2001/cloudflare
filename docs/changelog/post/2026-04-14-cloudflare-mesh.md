---
url: https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-mesh/
title: Introducing Cloudflare Mesh \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:40.627170+00:00
---

# Introducing Cloudflare Mesh · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-mesh/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 14, 2026

## Introducing Cloudflare Mesh

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) is now available ([blog post ↗︎](https://blog.cloudflare.com/mesh/)). Mesh connects your services and devices with post-quantum encrypted networking, allowing you to route traffic privately between servers, laptops, and phones over TCP, UDP, and ICMP.

![Cloudflare Mesh network map showing nodes and devices connected through Cloudflare](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2070,height=875,format=webp/_astro/mesh-network-map.CED6jNHK.gif)

#### What Cloudflare Mesh does

  * Assigns a private [Mesh IP](https://developers.cloudflare.com/mesh/concepts/#mesh-ips) to every enrolled device and node.
  * Enables any participant to reach any other participant by IP — including client-to-client, without deploying any infrastructure.
  * Supports [CIDR routes](https://developers.cloudflare.com/mesh/features/routes/) for subnet routing through Mesh nodes.
  * Supports [high availability](https://developers.cloudflare.com/mesh/features/high-availability/) with active-passive replicas for nodes with routes.
  * All traffic flows through Cloudflare, so [Gateway network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/), [device posture checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/), and access rules apply to every connection.



#### What changed

  * **WARP Connector** is now **Cloudflare Mesh**. Existing WARP Connectors are now called mesh nodes. All existing deployments continue to work — no migration required.
  * **Peer-to-peer connectivity** is now called **Mesh connectivity** and is part of the Cloudflare Mesh documentation.
  * **Mesh node limit** increased from 10 to **50 per account**.
  * New [dashboard experience ↗︎](https://dash.cloudflare.com/?to=/:account/mesh) at **Networking** > **Mesh** with an interactive network map, node management, route configuration, diagnostics, and a setup wizard.



#### Get started

Refer to the [Cloudflare Mesh documentation](https://developers.cloudflare.com/mesh/) to set up your first Mesh network.
