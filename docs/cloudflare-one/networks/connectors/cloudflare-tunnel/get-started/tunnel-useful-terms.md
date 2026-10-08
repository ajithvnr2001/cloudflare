---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/tunnel-useful-terms/
title: Useful terms \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:17.177839+00:00
---

# Useful terms · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/tunnel-useful-terms/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

  4. /[Get started](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/)
  5. /Useful terms



# Useful terms

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/tunnel-useful-terms/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTunnelTunnel UUIDTunnel nameConnectorReplicaRemotely-managed tunnelLocally-managed tunnelQuick tunnelsVirtual networks

Review terminology for Cloudflare Tunnels.

## Tunnel

A tunnel is a secure, outbound-only pathway you can establish between your origin and Cloudflare's global network. Each tunnel you create will be assigned a name and a UUID.

## Tunnel UUID

A tunnel UUID is an alphanumeric, unique ID assigned to a tunnel. The tunnel UUID can be used whenever you need to reference a specific tunnel.

## Tunnel name

A tunnel name is a unique, user-friendly identifier that you choose for a tunnel. Since a tunnel can proxy traffic to multiple services, tunnel names do not need to be hostnames. For example, you can assign your tunnel a name that represents your application/network, a particular server, or the cloud environment where it runs.

## Connector

The connector, referred to as `cloudflared`, establishes connectivity from your origin server to the Cloudflare global network. Each `cloudflared` instance creates four long-lived connections to at least two distinct data centers within Cloudflare's global network. This built-in redundancy means that if an individual connection, server, or data center goes down, your origin remains available.

`cloudflared` operates as a secure connector daemon rather than a local reverse proxy. It forwards requests directly to the configured local service without altering request URI paths or performing local load balancing.

## Replica

A replica is an additional instance of `cloudflared` running the same tunnel on a different host. You can create and configure a tunnel once, then run it through multiple replicas for redundancy. DNS records and Cloudflare Load Balancers continue to point to the tunnel (`UUID.cfargotunnel.com`), while Cloudflare distributes traffic across the available replicas. There is no guarantee about which replica will be chosen — Cloudflare routes to the geographically closest one. Replicas are typically deployed to keep a tunnel available if a host running `cloudflared` goes offline.

## Remotely-managed tunnel

A remotely-managed tunnel is a tunnel that was created in the Cloudflare dashboard under **Networking** > **Tunnels**. Tunnel configuration is stored in Cloudflare, which allows you to manage the tunnel from the dashboard or using the [API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/configurations/methods/get/).

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)

## Locally-managed tunnel

A locally-managed tunnel is a tunnel that was created by running `cloudflared tunnel create <NAME>` on the command line. Tunnel configuration is stored in your local cloudflared directory. For terminology specific to locally-managed tunnels, refer to the [Locally-managed tunnel glossary](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/local-tunnel-terms/).

## Quick tunnels

Quick Tunnels generate a random `trycloudflare.com` subdomain that sends traffic to a local service. For more information, refer to [Quick Tunnels](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/).

## Virtual networks

A [virtual network](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/) is a software abstraction that allows you to logically segregate resources on your private network. Virtual networks are especially useful for exposing resources which have overlapping IP routes. To connect to a resource, end users would select a virtual network in their Cloudflare One Client settings before entering the destination IP.

[PreviousCreate a tunnel (API)](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel-api/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/tunnel-useful-terms.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
