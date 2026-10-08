---
url: https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflare-mesh/
title: Connect with Cloudflare Mesh \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:54.146644+00:00
---

# Connect with Cloudflare Mesh · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflare-mesh/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Replace Vpn

  4. /[Connect your private network](https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/)
  5. /Connect with Cloudflare Mesh



# Connect with Cloudflare Mesh

Last updated Sep 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflare-mesh/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up Cloudflare MeshWhen to use MeshBest practices

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) (formerly WARP Connector) connects your private networks to Cloudflare using the Cloudflare One Client (`warp-cli`) running in headless mode on a Linux server. Every enrolled device and node receives a private Mesh IP and can communicate with any other participant over TCP, UDP, or ICMP.

Mesh supports bidirectional traffic — devices can reach servers, servers can reach devices, and networks can reach other networks. This makes it the recommended approach for replacing a VPN, as it covers both user-to-network and network-to-network connectivity.

## Set up Cloudflare Mesh

To connect your private network using Cloudflare Mesh, refer to [Get started with Cloudflare Mesh](https://developers.cloudflare.com/mesh/get-started/).

The setup wizard in the dashboard configures enrollment, device profiles, and connectivity settings automatically. Once a node is online, add [CIDR routes](https://developers.cloudflare.com/mesh/features/routes/) to make the subnet behind it reachable from any enrolled device.

## When to use Mesh

  * Replacing a VPN for remote access to private networks
  * Bidirectional connectivity (VoIP, SIP, Active Directory, SCCM, DevOps pipelines)
  * Long-lived TCP connections sensitive to interruptions (SAP, database replication, ERP systems, RDP sessions)
  * Site-to-site networking between offices, data centers, or cloud VPCs
  * Client-to-client connectivity (two laptops reaching each other by private IP)
  * Any L3/L4 workload where source IP preservation matters



## Best practices

  * Enable [high availability](https://developers.cloudflare.com/mesh/features/high-availability/) for production nodes with CIDR routes.
  * Use [Gateway network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) to control which users and devices can reach specific resources.
  * Refer to [Tips and best practices](https://developers.cloudflare.com/mesh/best-practices/) for cloud VPC configuration and running alongside Cloudflare Tunnel.



[PreviousChoose a connection method](https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/connection-methods/)[NextConnect with Cloudflare Tunnel](https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflared/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/replace-vpn/connect-private-network/cloudflare-mesh.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
