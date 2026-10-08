---
url: https://developers.cloudflare.com/learning-paths/replace-vpn/configure-device-agent/enable-proxy/
title: Proxy traffic through Gateway \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:53.567739+00:00
---

# Proxy traffic through Gateway · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/replace-vpn/configure-device-agent/enable-proxy/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Replace Vpn

  4. /[Configure the device agent](https://developers.cloudflare.com/learning-paths/replace-vpn/configure-device-agent/)
  5. /Proxy traffic through Gateway



# Proxy traffic through Gateway

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/replace-vpn/configure-device-agent/enable-proxy/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable the proxy

With Cloudflare Gateway, you can log and filter DNS, network, and HTTP traffic from devices running the Cloudflare One Client. This includes traffic to the public Internet and traffic directed to your private network. DNS filtering is enabled by default since the Cloudflare One Client sends DNS queries to Cloudflare's public DNS resolver, [1.1.1.1](https://developers.cloudflare.com/1.1.1.1/). To enable network and HTTP filtering, you will need to allow Cloudflare Gateway to proxy that traffic.

## Enable the proxy

  1. Go to **Traffic policies** > **Traffic settings**.
  2. In **Proxy and inspection** , turn on **Allow Secure Web Gateway to proxy traffic**.
  3. Select **TCP**.
  4. Select **UDP** (required to proxy traffic to internal DNS resolvers).
  5. (Recommended) To proxy traffic for diagnostic tools such as `ping` and `traceroute`, select **ICMP**. You may also need to [update your system](https://developers.cloudflare.com/cloudflare-one/traffic-policies/proxy/#icmp) to allow ICMP traffic through `cloudflared`.



  1. Add the following permission to your [`cloudflare_api_token` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_token):

     * `Zero Trust Write`
  2. Turn on the TCP and/or UDP proxy using the [`cloudflare_zero_trust_device_settings` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_device_settings) resource:
         
         resource "cloudflare_zero_trust_device_settings "global_warp_settings" {
         	account_id            = var.cloudflare_account_id
           gateway_proxy_enabled = true
         	gateway_udp_proxy_enabled = true
         }




Cloudflare will now proxy traffic from enrolled devices, except for the traffic excluded in your [split tunnel settings](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/#3-route-private-network-ips-through-the-cloudflare-one-client). For more information on how Gateway forwards traffic, refer to [Gateway proxy](https://developers.cloudflare.com/cloudflare-one/traffic-policies/proxy/).

[PreviousCustomize device profiles](https://developers.cloudflare.com/learning-paths/replace-vpn/configure-device-agent/device-profiles/)[NextEnable TLS decryption (optional)](https://developers.cloudflare.com/learning-paths/replace-vpn/configure-device-agent/enable-tls-decryption/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/replace-vpn/configure-device-agent/enable-proxy.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
