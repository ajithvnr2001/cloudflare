---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/
title: Private networks \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:17.861878+00:00
---

# Private networks · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors

  4. /[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)
  5. /Private networks



# Private networks

Last updated Sep 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConnectors

With Cloudflare Zero Trust, you can connect private networks and the services running in those networks to Cloudflare's global network. This involves installing a connector on the private network, and then [setting up routes](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/#2b-connect-a-network) which define the IP addresses available in that environment. Unlike [published applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/), private network routes can expose both HTTP and non-HTTP resources.

To reach private network IPs, end users must connect their device to Cloudflare and enroll in your Zero Trust organization. The most common method is to install the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) on their device, or you can onboard their network traffic to Cloudflare using [Cloudflare Mesh](https://developers.cloudflare.com/mesh/), [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/), or [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/zero-trust/cloudflare-tunnel/).

Administrators can optionally set [Gateway network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) to control access to services based on user identity and device posture.

Note

The restriction described in [Delivering videos with Cloudflare](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/delivering-videos-with-cloudflare/) does not apply to private network routes. You can use these routes for large-file transfers, backups, and high-traffic workloads such as media servers.

## Connectors

Here are the different ways you can connect your private network to Cloudflare:

  * [**Cloudflare Mesh**](https://developers.cloudflare.com/mesh/) creates a private network between mesh nodes, client devices, and the services behind them. Each participant is assigned a [Mesh IP](https://developers.cloudflare.com/cloudflare-one/networks/routes/reserved-ips/#device-ips) for direct connectivity. Mesh nodes install on a Linux server and act as subnet routers for site-to-site, bidirectional, and mesh networking. Client devices install the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) for device-to-device and device-to-network connectivity.
  * [**Cloudflare Tunnel (`cloudflared`)**](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/) installs on a server in your private network and creates a secure, outbound-only tunnel to Cloudflare. `cloudflared` only proxies traffic initiated from a user to a server. Any service or application running behind the tunnel will use the server's default routing table for server-initiated connectivity.
  * [**Cloudflare WAN**](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/) connects entire network locations to Cloudflare using anycast GRE or IPsec tunnels configured on your existing networking equipment.



[PreviousTerraform](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/terraform/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
