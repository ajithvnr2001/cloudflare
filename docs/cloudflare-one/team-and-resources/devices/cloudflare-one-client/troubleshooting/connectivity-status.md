---
url: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/
title: Connectivity status \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:03.426544+00:00
---

# Connectivity status · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Team and resources[Devices](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/)[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

  4. /[Troubleshoot](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/)
  5. /Connectivity status



# Connectivity status

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Cloudflare One Client (formerly WARP) GUI displays the following status messages when transitioning from a **Disconnected** to **Connected** state. These messages indicate the connectivity stage of the Cloudflare One Client daemon as it establishes a connection from the device to Cloudflare. The [client mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/) determines which messages are displayed during the connection process. If the Cloudflare One Client encounters an error while connecting, the status message will change to an [error code](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/client-errors/).

To print status messages to the console, run the `warp-cli -l status` command before connecting the client.

Status message | Description  
---|---  
Verifying connection settings | Initializes connection components based on your [device client settings](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/).  
Validating network | Validates Ethernet and/or Wi-Fi network connectivity.  
Initializing IP connection | Checks for IPv4 and IPv6 connectivity to Cloudflare using the [Happy Eyeballs algorithm ↗︎](https://datatracker.ietf.org/doc/html/rfc6555).  
Establishing a connection | Connects to the endpoint discovered by Happy Eyeballs.  
Building a Tunnel | Creates a [virtual network interface](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#virtual-interface) on the operating system for the WARP tunnel.  
Configuring the firewall | Configures the system firewall to allow WARP tunnel traffic.  
Setting up your routing table | Updates the [system routing table](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#routing-table) based on your [Split Tunnel rules](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/).  
Configuring your firewall rules | Configures the [system firewall](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#system-firewall) based on your Split Tunnel rules.  
Checking connectivity to DNS | Checks connectivity to the DNS endpoint (`<account-id>.cloudflare-gateway.com`).  
Setting local endpoint communication | Configures local DNS proxy sockets.  
Configuring local DNS proxy | Creates a [local DNS proxy](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#dns-traffic) for DNS resolution.  
Applying DNS settings | Sets the local DNS proxy as the default DNS server on the device.  
Configuring forward proxy | (Only in [Local proxy mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode)) Configures the SOCKS proxy.  
Confirming Tunnel connection | Checks connectivity to [destinations](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/#connectivity-checks) inside and outside of the WARP tunnel.  
Validating DNS configuration | Verifies that DNS requests are answered by WARP's local DNS proxy.  
Verifying SOCKS proxy configuration | (Only in [Local proxy mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode)) Verifies the SOCKS proxy configuration.  
Ensuring MTLS identity | (Only in [Posture only mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only/)) Installs a client certificate for mTLS authentication.  
  
[PreviousKnown limitations](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/known-limitations/)[NextBusiness Continuity Guide](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/business-continuity/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
