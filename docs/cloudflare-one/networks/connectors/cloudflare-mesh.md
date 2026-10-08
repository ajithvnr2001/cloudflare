---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/
title: Cloudflare Mesh - Private networking \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:08.691689+00:00
---

# Cloudflare Mesh - Private networking · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Networks

  4. /Connectors
  5. /Cloudflare Mesh



# Cloudflare Mesh

Last updated Sep 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse casesGet startedMesh vs. Cloudflare Tunnel

Connect services and devices with post-quantum encrypted private networking through Cloudflare.

Cloudflare Mesh gives every enrolled server, laptop, and phone a private Mesh IP. Participants can communicate by IP over TCP, UDP, or ICMP, including device-to-device connections that do not require customer-managed networking infrastructure.

Mesh nodes run the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) in headless mode on Linux. They can also advertise routes to make private subnets and hostnames reachable from other Mesh participants.

The Mesh participant table lists nodes and enrolled client devices together. You can search for devices, filter by participant type or status, and open a device's Zero Trust details page. If one participant source fails, participants from the other source remain available while you retry the request.

![The Mesh network map in the Cloudflare dashboard showing nodes and devices connected through Cloudflare](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2070,height=875,format=webp/_astro/mesh-network-map.CED6jNHK.gif)

Note

Cloudflare Mesh was previously known as WARP Connector and peer-to-peer connectivity. Existing WARP Connectors are now called Mesh nodes. Existing deployments continue to work without migration.

For details about how Mesh works, protocol requirements, and Mesh IP assignment, refer to [Concepts](https://developers.cloudflare.com/mesh/concepts/).

## Use cases

  * Connect enrolled devices to each other by private IP.
  * Provide bidirectional connectivity between servers, cloud networks, and sites.
  * Route traffic to devices that cannot run the Cloudflare One Client.
  * Preserve long-lived TCP connections for databases, replication, ERP systems, and remote administration.



## Get started

### [Set up Cloudflare Mesh](https://developers.cloudflare.com/mesh/get-started/)

Configure your account and connect your first participant.

### [Understand Mesh](https://developers.cloudflare.com/mesh/concepts/)

Learn how participants, Mesh IPs, routing, and policies work.

### [Explore features](https://developers.cloudflare.com/mesh/features/)

Configure routes and high availability for Mesh nodes.

### [Follow a guide](https://developers.cloudflare.com/mesh/guides/)

Connect client devices or deploy Mesh in containers.

## Mesh vs. Cloudflare Tunnel

Use Mesh when participants need bidirectional private IP connectivity or when a workload requires stable, long-lived connections. Use [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) when you want to publish specific applications, hostnames, or IP routes through an outbound-only connector.

For a detailed comparison, refer to [How Cloudflare Mesh works](https://developers.cloudflare.com/mesh/concepts/#mesh-vs-tunnel).

[PreviousUseful terms](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/local-tunnel-terms/)[NextGet started](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-mesh/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
