---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/private-dns/
title: Private DNS \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:18.720588+00:00
---

# Private DNS · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/private-dns/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)[Private networks](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/)

  4. /[Connect with cloudflared](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/)
  5. /Private DNS



# Private DNS

Last updated Jun 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/private-dns/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure private DNSTest the setupTroubleshooting

By default, all DNS requests on the user device are resolved by Cloudflare's [public DNS resolver](https://developers.cloudflare.com/1.1.1.1/) except for common top level domains used for local resolution (such as `localhost`). You can connect an internal DNS resolver to Cloudflare and use it to resolve non-publicly routed domains.

## Configure private DNS

To resolve private DNS queries:

  1. [Connect your private network](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/) with Cloudflare Tunnel.

  2. Under **Networking** > **Routes** , verify that the IP address of your internal DNS resolver is included in the tunnel.

[ Go to **Routes** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/routes)

Note

Ensure that **Split Tunnels** are configured to [include traffic to private IPs and hostnames](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/#3-route-private-network-ips-through-the-cloudflare-one-client).

  3. Route specific DNS queries to your internal DNS resolver using one of the following options:

     * [Create a Local Domain Fallback entry](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/) that points to the internal DNS resolver. For example, you can instruct the Cloudflare One Client to resolve all requests for `myorg.privatecorp` through an internal resolver at `10.0.0.25` rather than attempting to resolve this publicly.
     * Alternatively, [create a resolver policy](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/#create-a-resolver-policy) that points to the internal DNS resolver. 

[Resolver policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/) provide similar functionality to Local Domain Fallback but occur in Cloudflare Gateway rather than on the local device. This option is recommended if you want more granular control over private DNS resolution. For example, you can ensure that all users in a specific geography use the private DNS server closest to them, ensure that specific conditions are met before resolving private DNS traffic, and apply [Gateway DNS policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/) to private DNS traffic.

  4. [Enable the Gateway proxy](https://developers.cloudflare.com/cloudflare-one/traffic-policies/proxy/#turn-on-the-gateway-proxy) for TCP and UDP.

  5. Finally, ensure that your tunnel uses QUIC as the default [transport protocol](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#protocol). This will enable `cloudflared` to proxy UDP-based traffic which is required in most cases to resolve DNS queries.




The Cloudflare One Client will now send DNS queries to your internal DNS resolver for resolution. To learn more, refer to [How the Cloudflare One Client handles DNS requests](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/#how-the-warp-client-handles-dns-requests).

## Test the setup

For testing, run a `dig` command for the internal DNS service:
    
    
    dig AAAA www.myorg.privatecorp

The `dig` command will work because `myorg.privatecorp` was configured above as a fallback domain. If you skip that step, you can still force `dig` to use your private DNS resolver:
    
    
    dig @10.0.0.25 AAAA www.myorg.privatecorp

Both `dig` commands will fail if the Cloudflare One Client is disabled on your end user's device.

## Troubleshooting

Use the following troubleshooting strategies if you are running into issues while configuring private DNS with Cloudflare Tunnel.

  * Ensure that `cloudflared` is connected to Cloudflare by visiting **Networking** > **Tunnels** in the Cloudflare dashboard.

  * Ensure that `cloudflared` is running with the `quic` protocol (search for `Initial protocol quic` in its logs).

  * Ensure that the machine where `cloudflared` is running is allowed to egress via UDP to port 7844 to talk out to Cloudflare.

  * Ensure that end-user devices are enrolled into the Cloudflare One Client by visiting <https://help.teams.cloudflare.com>[ ↗︎](https://help.teams.cloudflare.com).

  * Double-check the [order of precedence](https://developers.cloudflare.com/cloudflare-one/traffic-policies/order-of-enforcement/#order-of-precedence) for your [Gateway network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/). Ensure that a more global Block or Allow policy will not supersede application-specific policies.

  * Check your [Gateway network logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#network-logs) to see whether your UDP DNS resolutions are being allowed or blocked.

  * Ensure that your internal DNS resolver is available over a routable private IP address. You can check that by trying the `dig` command on your machine running `cloudflared`.

  * Check your set up by using `dig ... +tcp` to force the DNS resolution to use TCP instead of UDP.




[PreviousConnect an IP/CIDR](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/)[NextVirtual networks](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/private-dns.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
