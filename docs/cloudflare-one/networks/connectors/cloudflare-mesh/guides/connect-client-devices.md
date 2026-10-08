---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/guides/connect-client-devices/
title: Connect client devices to Cloudflare Mesh \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:10.081485+00:00
---

# Connect client devices to Cloudflare Mesh · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/guides/connect-client-devices/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare Mesh](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/)

  4. /Guides
  5. /Connect client devices



# Connect client devices

Last updated Sep 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/guides/connect-client-devices/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Enroll the Cloudflare One Client Headless Windows, macOS, and Linux devices2\. Verify connectivityWhat devices can reachSplit Tunnel configuration Exclude mode (default) Include modeFirewall considerations

Client devices — laptops, phones, and desktops — join your Mesh network by installing the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) and enrolling. Each device receives a [Mesh IP](https://developers.cloudflare.com/mesh/concepts/#mesh-ips) and can immediately communicate with every other enrolled device and Mesh node.

## 1\. Enroll the Cloudflare One Client

Use the Mesh dashboard to find the Cloudflare One Client installer and organization name for your device:

  1. In the Cloudflare dashboard, go to **Networking** > **Mesh**.

[ Go to **Mesh** ↗ ](https://dash.cloudflare.com/?to=/:account/mesh)
  2. Select **Add participant** > **Add device**.

  3. Select Windows, macOS, Linux, iOS, or Android.

  4. Use the provided link or QR code to install the Cloudflare One Client.

  5. Open the client and select **Cloudflare Zero Trust** when prompted for a connection type.

  6. Enter the organization name displayed in the Mesh dashboard and complete authentication.




The Add device workflow does not enroll the device or verify connectivity. For manual installation and enrollment instructions, refer to [Download the Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/) and [Enroll a device](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/).

### Headless Windows, macOS, and Linux devices

Do not use interactive CLI enrollment on a device without a browser. Instead, [create a Service Auth enrollment policy](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/#check-for-service-token). Configure the [`organization`](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization), [`auth_client_id`](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#auth_client_id), and [`auth_client_secret`](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#auth_client_secret) managed deployment parameters.

For platform-specific installation methods and configuration file locations, refer to [Managed deployment](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/). For a complete Linux example, refer to [Deploy the Cloudflare One Client on headless Linux machines](https://developers.cloudflare.com/cloudflare-one/tutorials/deploy-client-headless-linux/).

This method works on [supported Windows, macOS, and Linux systems](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/). Service-token devices use the shared identity `non_identity@<team-name>.cloudflareaccess.com`. Policies based on identity provider users or groups do not apply to these devices. To assign device profiles, use the expression `identity.service_token_uuid == "<SERVICE_TOKEN_ID>"`, where `<SERVICE_TOKEN_ID>` is the service token resource UUID (`id`), not its `auth_client_id`. Place this [Service Token selector](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/#service-token) before broader OS or email profiles. Use the shared non-identity email only when all Service Auth devices should match the profile.

After enrollment, the device receives a Mesh IP and connects to your Mesh network.

The device then appears with Mesh nodes in the participant table under **Networking** > **Mesh**. Use the table to search for devices, filter participants by type or status, and open a device's Zero Trust details page. If more results are available, select **Load more participants** , **Load more nodes** , or **Load more devices**. New results append without replacing the participants already shown.

## 2\. Verify connectivity

From a Windows, macOS, or Linux device, test TCP connectivity to a Mesh node or another client device. For example, test SSH:
    
    
    nc -vz <MESH-IP> 22
    
    
    Test-NetConnection <MESH-IP> -Port 22

Replace `<MESH-IP>` with the Mesh IP of a node (visible on the [Mesh overview page ↗︎](https://dash.cloudflare.com/?to=/:account/mesh)) or another enrolled device. Replace port `22` with the port used by your service. You can test HTTP services from a mobile browser. If you turned on the ICMP Gateway proxy, you can also run `ping <MESH-IP>` as a diagnostic check.

If the device profile routes `www.cloudflare.com` through WARP, verify the data path:
    
    
    curl --silent https://www.cloudflare.com/cdn-cgi/trace | grep '^warp=on$'
    
    
    if (-not (curl.exe --silent https://www.cloudflare.com/cdn-cgi/trace | Select-String '^warp=on$')) { exit 1 }

In Include mode, expect `warp=off` for destinations that are not in the include list. Use the successful connection to an included Mesh IP as the data-path check. Do not rely only on the success message from `warp-cli`: Mesh connectivity requires Traffic and DNS mode. In DNS-only mode, use `warp-cli registration show` only to verify enrollment. DNS-only mode cannot carry Mesh traffic.

## What devices can reach

Once connected, a client device can:

  * **Other client devices** — Reach any enrolled device by its Mesh IP. No Mesh nodes involved.
  * **Mesh nodes** — Reach any online node by its Mesh IP. SSH, database connections, API calls all work.
  * **Subnets behind nodes** — Access hosts on private networks that a node advertises via [CIDR routes](https://developers.cloudflare.com/mesh/features/routes/) (for example, printers, databases, or servers that cannot run the client).



All traffic is subject to your [Gateway network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/), so you can control which users and devices can reach specific resources.

## Split Tunnel configuration

For client devices to reach Mesh IPs, the Mesh IP range must route through Cloudflare. How you configure this depends on your [Split Tunnel mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/).

### Exclude mode (default)

The Mesh setup wizard updates the default device profile to route the Mesh IP range through Cloudflare. If you did not use the wizard, or if another profile applies to the device, verify that `100.96.0.0/12` (or your custom device IP range) is not in the exclude list or contained by a broader exclusion.

Depending on your Cloudflare networking configuration, you may need to remove additional IPs from your exclude list. For a list of IPs to check, refer to [Reserved IP addresses](https://developers.cloudflare.com/cloudflare-one/networks/routes/reserved-ips/).

### Include mode

In Include mode, add the following to your include list:

  * `100.96.0.0/12` — Mesh IPs (device IPs)
  * Any CIDR routes you have [configured for your Mesh nodes](https://developers.cloudflare.com/mesh/features/routes/)



The IPv4 range used for [hostname routing](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes) (`172.64.128.0/20`; requires MASQUE) and all Cloudflare One IPv6 ranges are [automatically routed through Cloudflare](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#automatically-managed-ranges) and do not need to be added manually.

## Firewall considerations

Some operating systems block inbound traffic from the Mesh IP range by default:

  * **Windows** — Windows Firewall blocks inbound traffic from `100.96.0.0/12`. Add a firewall rule that allows incoming requests from `100.96.0.0/12` for your desired protocols and ports.
  * **macOS / Linux** — Most configurations allow this traffic by default. If you have custom firewall rules, ensure `100.96.0.0/12` is permitted.



[PreviousHigh availability](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/features/high-availability/)[NextRun Mesh in Docker / Kubernetes](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/guides/run-mesh-in-containers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-mesh/guides/connect-client-devices.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
