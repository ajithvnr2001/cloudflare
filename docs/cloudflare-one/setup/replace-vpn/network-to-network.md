---
url: https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/network-to-network/
title: Network to network \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:52.124447+00:00
---

# Network to network · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/network-to-network/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Get started](https://developers.cloudflare.com/cloudflare-one/setup/)

  4. /[Replace your VPN](https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/)
  5. /Network to network



# Network to network

Last updated Sep 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/network-to-network/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksPrerequisitesStep 1: Create your first mesh nodeStep 2: Add a route for the first networkStep 3: Create your second mesh nodeStep 4: Add a route for the second networkStep 5: Forward device trafficStep 6: Verify your connectionRecommended next stepsTroubleshoot

Connect two separate private networks so devices on each network can send and receive traffic in both directions through Cloudflare. This is useful when you need to link office locations, data centers, or cloud environments. For example, employees in one office could access a file server, printer, or internal application in another office.

To explore other connection scenarios, refer to [Replace your VPN](https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/).

## How it works

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) (formerly WARP Connector) lets you deploy mesh nodes — lightweight network connectors that you install on a single Linux device in each network. That device handles traffic for the entire network: it sends outbound traffic to Cloudflare and receives inbound traffic back, then passes it to the right device on the network. Because of this, other devices on the network do not need to install any software.

## Prerequisites

  * A [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up).
  * A Linux device or virtual machine on your first private network. This is where you install your first mesh node.
  * A second Linux device or virtual machine on a separate private network. This is where you install your second mesh node.



Note

Mesh nodes are currently Linux-only. For more details on requirements, refer to [Cloudflare Mesh](https://developers.cloudflare.com/mesh/).

## Step 1: Create your first mesh node

  1. In the Cloudflare dashboard, go to **Networking** > **Mesh**.

[ Go to **Mesh** ↗ ](https://dash.cloudflare.com/?to=/:account/mesh)
  2. Select **Add participant** > **Add node**.

  3. Enter a name for the node (for example, `office-a`).

  4. Follow the wizard to configure enrollment and device profile settings.

  5. Copy the install commands from the wizard and run them on your Linux device.

  6. After the node connects, the dashboard confirms it is online.




## Step 2: Add a route for the first network

  1. Go to the node detail page for your first node.
  2. Select the **Routes** tab.
  3. Select **Add a route**.
  4. Enter the IP range of your first network (for example, `10.0.0.0/24`).
  5. Select **Create**.



## Step 3: Create your second mesh node

Repeat Step 1 on a Linux device in your second network. Give it a distinct name (for example, `office-b`).

## Step 4: Add a route for the second network

Repeat Step 2 for your second node, entering the IP range of your second network (for example, `192.168.1.0/24`). The IP range must not overlap with your first network.

## Step 5: Forward device traffic

If the mesh node is installed on your network's router (the device that serves as the default gateway), other devices on the network automatically send traffic through it. No additional configuration is needed, and you can skip this step.

If the mesh node is installed on a different device, other devices on the network need a static route so they know to send cross-network traffic to the mesh node. Without this route, devices do not know where to send traffic destined for the other network.

For details on routing options, refer to [Routes](https://developers.cloudflare.com/mesh/features/routes/).

## Step 6: Verify your connection

Devices on both networks can now communicate through Cloudflare. To verify connectivity, try reaching a device on the opposite network (for example, `ping 192.168.1.100` from a device on your first network).

## Recommended next steps

After verifying your connection, consider securing your connected networks with policies and access controls:

  * **Set up Gateway policies** : By default, all traffic between your network segments flows through Cloudflare without restriction. Gateway policies let you scan, filter, and log traffic between your networks. For more information, refer to [DNS policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/), [Network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/), and [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/).
  * **Create an Access application** : Restrict access to specific services or hosts on your connected networks with identity-based rules. For more information, refer to [Secure a private IP or hostname](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/).
  * **Enable high availability** : Deploy multiple replicas of each mesh node for automatic failover. For more information, refer to [High availability](https://developers.cloudflare.com/mesh/features/high-availability/).



For in-depth guidance on policy design and device posture checks, refer to the [Replace your VPN learning path](https://developers.cloudflare.com/learning-paths/replace-vpn/concepts/).

## Troubleshoot

If you have issues connecting, refer to these resources:

  * [Tips and best practices](https://developers.cloudflare.com/mesh/best-practices/): review common Cloudflare Mesh configuration tips and troubleshooting strategies.
  * [Troubleshoot tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/): diagnose tunnel connectivity and routing problems.



[PreviousDevice to device](https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/device-to-device/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/setup/secure-private-apps/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/setup/replace-vpn/network-to-network.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
