---
url: https://developers.cloudflare.com/load-balancing/private-network/public-to-tunnel/
title: Set up Private Network Load Balancing for Public traffic to Tunnel \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:06.012866+00:00
---

# Set up Private Network Load Balancing for Public traffic to Tunnel · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/private-network/public-to-tunnel/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /[Private Network Load Balancing](https://developers.cloudflare.com/load-balancing/private-network/)
  4. /Set up Private Network Load Balancing for Public traffic to Tunnel



# Set up Private Network Load Balancing for Public traffic to Tunnel

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/private-network/public-to-tunnel/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Configure a Cloudflare tunnel with an assigned virtual network2\. Configure Cloudflare Load Balancing

Consider the following steps to learn how to configure Private Network Load Balancing solution, using [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) as the off-ramp to securely connect to your private or internal services.

## 1\. Configure a Cloudflare tunnel with an assigned virtual network

The specific configuration steps can vary depending on your infrastructure and services you are looking to connect. If you are not familiar with Cloudflare Tunnel, the pages linked on each step provide more guidance.

  1. [Create a tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/#1-create-a-tunnel) to connect your data center to Cloudflare.
  2. Create a [virtual network](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/) and assign it to the tunnel you configured in the previous step.



To create a virtual network:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Settings** > **WARP Client** and find the **Virtual networks** setting.
  2. Select **Add new** or **Manage** > **Create virtual network** to create virtual networks.
  3. Define your virtual network name and select **Save**.



To assign the virtual network to the tunnel:

  1. Go to **Networks** > **Tunnels**.
  2. Select the tunnel you created in the previous steps and select **Configure**.
  3. Under **Private Network** , select **Add a private network**.
  4. Specify an IP range under **CIDR** and select the virtual network under **Additional settings**.
  5. Select **Save private network**.



To create a virtual network:
    
    
    cloudflared tunnel vnet add <VNET_NAME>

To assign the virtual network to the tunnel:
    
    
    cloudflared tunnel route ip add --vnet <VNET_NAME> <IP_RANGE> <TUNNEL_NAME>

## 2\. Configure Cloudflare Load Balancing

Once you have Cloudflare tunnels with associated virtual networks (VNets) configured, the VNets can be specified for each endpoint when you [create or edit a pool](https://developers.cloudflare.com/load-balancing/pools/create-pool/#create-a-pool). This will enable Cloudflare load balancers to use the correct tunnel and securely reach the private IP endpoints.

The specific configuration will vary depending on your use case. Refer to the following steps to understand the workflow.

  1. [Create the Load Balancing monitor](https://developers.cloudflare.com/load-balancing/monitors/create-monitor/) according to your needs.
  2. [Create the pool](https://developers.cloudflare.com/load-balancing/pools/create-pool/) specifying your private IP addresses and corresponding virtual networks.



Note

  * Currently, Cloudflare does not support entering the same endpoint IP addresses more than once, even when using different virtual networks.
  * All endpoints with private IPs must have `virtual_network_id` specified.



  3. [Create the load balancer](https://developers.cloudflare.com/load-balancing/load-balancers/create-load-balancer/), specifying the pool and monitor you created in the previous steps, as well as the desired [global traffic steering policies](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/) and [custom rules](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/).



Spectrum limitations

If you will use the load balancer with [Spectrum](https://developers.cloudflare.com/spectrum/), consider the applicable [limitations](https://developers.cloudflare.com/load-balancing/additional-options/spectrum/#limitations) on load balancing and monitoring options.

[PreviousOverview](https://developers.cloudflare.com/load-balancing/private-network/)[NextSet up Private Network Load Balancing with Cloudflare WAN](https://developers.cloudflare.com/load-balancing/private-network/cloudflare-wan/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/private-network/public-to-tunnel.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
