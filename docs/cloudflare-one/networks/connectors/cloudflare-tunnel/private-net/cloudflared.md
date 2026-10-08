---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/
title: Connect with cloudflared \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:18.016883+00:00
---

# Connect with cloudflared · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

  4. /[Private networks](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/)
  5. /Connect with cloudflared



# Connect with cloudflared

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`cloudflared` is a daemon that runs on a host machine in your private network and proxies traffic from Cloudflare to local services. The tunnel created by `cloudflared` is outbound-only, meaning it only handles requests initiated from a user to your private network. Server-initiated requests (from applications behind the tunnel) use the server's default routing table and do not pass through the tunnel.

On the client side, end users connect to Cloudflare's global network using the Cloudflare One Client. The Cloudflare One Client can be rolled out to your entire organization in just a few minutes using your in-house MDM tooling. When users connect to an IP address or hostname made available through Cloudflare Tunnel, WARP sends their connection through Cloudflare's network and down the corresponding tunnel to the internal service. Traffic to services behind the tunnel will carry the local source IP address of the host machine running the `cloudflared` daemon.

![Diagram displaying connections between a device, Cloudflare, and a private network.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2530,height=1144,format=webp/_astro/private-ips-diagram.BXgaklt9.png)

To enable remote access to your private network, refer to the following guides:

  * [**Connect a private hostname**](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/): Route network traffic to an internal application using its hostname.
  * [**Connect an IP/CIDR**](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/): Route traffic to an internal IP address or CIDR range.



[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/)[NextConnect a private hostname](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
