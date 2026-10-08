---
url: https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/device-to-device/
title: Device to device \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:51.862569+00:00
---

# Device to device · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/device-to-device/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Get started](https://developers.cloudflare.com/cloudflare-one/setup/)

  4. /[Replace your VPN](https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/)
  5. /Device to device



# Device to device

Last updated Sep 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/device-to-device/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksPrerequisitesStep 1: Enroll your first deviceStep 2: Enroll your second deviceStep 3: Verify your connectionRecommended next stepsTroubleshoot

Create a secure connection between two devices so they can communicate directly through Cloudflare's network, without needing to be on the same physical network. This is useful when you need to remotely access a specific device, for example connecting to a home computer from a laptop at a coffee shop.

To explore other connection scenarios, refer to [Replace your VPN](https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/).

## How it works

The [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) is an app that you install on each device you want to connect. When you enroll a device in your Cloudflare account, it is assigned a [Mesh IP](https://developers.cloudflare.com/cloudflare-one/networks/routes/reserved-ips/#device-ips).

Devices use their Mesh IPs to communicate with each other through Cloudflare's network. This works for most common types of network traffic, including web requests, remote desktop, file sharing, and ping.

Only devices enrolled in your Cloudflare account can reach these addresses, so they are not accessible to anyone outside your organization. No tunnel infrastructure or network configuration is required, and the connection does not disrupt existing traffic on your network.

For more details, refer to [Connect client devices](https://developers.cloudflare.com/mesh/guides/connect-client-devices/).

## Prerequisites

  * A [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up)
  * Two Linux, Windows, macOS, Android, or iOS devices you want to connect together.



## Step 1: Enroll your first device

The Mesh dashboard provides the Cloudflare One Client installer and organization name.

  1. In the Cloudflare dashboard, go to **Networking** > **Mesh**.

[ Go to **Mesh** ↗ ](https://dash.cloudflare.com/?to=/:account/mesh)
  2. Select **Add participant** > **Add device**.

  3. Select your platform and use the provided link or QR code to install the Cloudflare One Client.

  4. Open the client and select **Cloudflare Zero Trust** when prompted for a connection type.

  5. Enter the organization name displayed in the Mesh dashboard and sign in.




## Step 2: Enroll your second device

Both devices must be enrolled in your Cloudflare account for the connection to work.

  1. Download the Cloudflare One Client on your second device.
  2. Open the client, enter the same team name, and sign in.
  3. The client should show as **Connected** on both devices.



## Step 3: Verify your connection

Both devices are now connected through Cloudflare's network using their assigned Mesh IPs.

To view your device's assigned Mesh IP:

  1. In the Cloudflare dashboard, go to **Networking** > **Mesh**.

[ Go to **Mesh** ↗ ](https://dash.cloudflare.com/?to=/:account/mesh)
  2. Your connected devices appear with their Mesh IPs.




To test connectivity, `ping` the Mesh IP of one device from the other.

## Recommended next steps

After verifying your connection, consider securing your connected devices with policies and access controls:

  * **Set up Gateway policies** : By default, all enrolled devices can reach each other over the Mesh IP space. Gateway policies let you scan, filter, and log traffic between your devices. For more information, refer to [DNS policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/), [Network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/), and [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/).
  * **Create an Access application** : Restrict access to specific destinations on enrolled devices with identity-based rules. For more information, refer to [Secure a private IP or hostname](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/).



For in-depth guidance on policy design and device posture checks, refer to the [Replace your VPN learning path](https://developers.cloudflare.com/learning-paths/replace-vpn/concepts/).

## Troubleshoot

If you have issues connecting, try these steps:

  * **Windows users** : Windows Firewall blocks device-to-device traffic by default. You may need to add a firewall rule that allows incoming traffic from `100.96.0.0/12`. For details, refer to [Connect client devices](https://developers.cloudflare.com/mesh/guides/connect-client-devices/).
  * [Troubleshoot the Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/): resolve connection and enrollment issues.



[PreviousDevice to network](https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/device-to-network/)[NextNetwork to network](https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/network-to-network/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/setup/replace-vpn/device-to-device.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
