---
url: https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/
title: Configure Cloudflare source IPs \u00b7 Cloudflare WAN docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:27.621728+00:00
---

# Configure Cloudflare source IPs · Cloudflare WAN docs

> Source: https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)
  3. /…

Configuration

  4. /How to
  5. /Configure Cloudflare source IPs



# Configure Cloudflare source IPs

Last updated Sep 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesAffected connectors and services Connectors Services that originate or proxy connectionsConfigure source IPs

You can configure the source IP address range used by Cloudflare whenever a Cloudflare service, such as Cloudflare Load Balancing, sends traffic to a Cloudflare One private network. This address range is referred to as the Cloudflare Source IP Prefix (or `cloudflare_source` subnet type in the API).

  * IPv4 traffic is sourced from `100.64.0.0/12`. This range is configurable.
  * IPv6 traffic is sourced from `2606:4700:cf1:5000::/64`. This range is not configurable.



When Cloudflare services send traffic to your private network, the source IP address determines how return traffic is routed. It also determines whether on-premises security devices can properly inspect the traffic. In legacy routing mode, traffic to private networks is sourced from public Cloudflare IPs, which can cause routing and security issues.

For customers using [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing), traffic to private networks is sourced from a dedicated, non-internet-routable private IPv4 range by default. This ensures:

  * **Symmetric routing** — Return traffic stays on your private network connection instead of taking an asymmetric path over the public Internet.
  * **Firewall state preservation** — On-premises stateful firewalls can track connections end-to-end because they see both request and response traffic.
  * **Security and compliance** — Private traffic stays on secure private paths.



Customers may wish to change the default allocated range to avoid IP conflicts or fit with an existing IP Address Management plan.

You must configure routes in your network so that response traffic for these source ranges is sent back to Cloudflare over your Cloudflare One connections.

## Prerequisites

Before you begin, ensure that:

  * You have Cloudflare One [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing). If your account uses Legacy Routing, follow [How to upgrade to Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#how-to-upgrade-to-unified-routing).
  * You have [Cloudflare One Networks Write](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) permission.
  * Your desired new network range meets the following requirements: 
    * Your network must be defined as a single CIDR with a prefix length of `/12`.
    * Cloudflare One subnets in the same account cannot overlap. Default allocations include: 
      * Cloudflare Source IPs (`100.64.0.0/12`)
      * Hostname Route Token IPs (`172.64.128.0/20` by default; configurable)
      * Cloudflare One Clients (`100.96.0.0/12`)
      * Private Load Balancers (`100.112.0.0/16`)
    * The source subnet cannot match or contain any existing route in your Cloudflare One routing table. The source subnet can be within a supernet route.



## Affected connectors and services

### Connectors

Cloudflare One supports multiple [connectivity options](https://developers.cloudflare.com/cloudflare-wan/zero-trust/connectivity-options/). The following connectors will receive traffic from the `cloudflare_source` subnet when a Cloudflare service initiates a request to the connected network or endpoint as an offramp:

  * **Anycast tunnels:** GRE, IPsec, and CNI
  * **Software connectors:** Cloudflare One Client and Cloudflare Mesh



Networks or endpoints connected via Cloudflare Tunnel will not receive traffic from the Cloudflare source IP subnet. Instead, the source IP address will be that of the host running the `cloudflared` software.

### Services that originate or proxy connections

All Cloudflare services that originate or proxy connections will send traffic from a Cloudflare source IP.

This includes traffic that is proxied from a private network or endpoint onramp.

For example, traffic onramped from a Cloudflare One Client through Cloudflare Load Balancer or Gateway DNS Resolver will present a Cloudflare source IP to the destination offramp.

## Configure source IPs

Note

You need Unified Routing to configure source IPs. If your account uses Legacy Routing, follow [How to upgrade to Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#how-to-upgrade-to-unified-routing).

  1. Go to the **Address space** page.

[ Go to **Address space** ↗ ](https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space)
  2. Select the **Custom IPs** tab.

  3. Find the prefix you want to update. This is your new `/12` range.

  4. Select the three dots to the right of the prefix > **Edit**.

  5. Enter a new prefix in the **IP address** field.

  6. Select **Save**.




To set up your source IPs, send a `PATCH` request to the [Update Cloudflare Source Subnet endpoint](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/subresources/cloudflare_source/) with your desired network range. The payload must include the network (your new `/12` range), and may include a name and comment.

Example:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Cloudflare One Networks Write`

Update Cloudflare Source Subnetbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/zerotrust/subnets/cloudflare_source/$ADDRESS_FAMILY" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"comment": "example_comment",
    		"name": "IPv4 Cloudflare Source IPs",
    		"network": "100.64.0.0/12"
    	}'

[PreviousConfigure routes](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/)[NextRun traceroute](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/traceroute/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
