---
url: https://developers.cloudflare.com/cloudflare-one/networks/routes/configure-initial-resolved-ips/
title: Configure initial resolved IPs \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:44.115366+00:00
---

# Configure initial resolved IPs · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/routes/configure-initial-resolved-ips/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Networks

  4. /Routes
  5. /Configure initial resolved IPs



# Configure initial resolved IPs

Last updated Aug 18, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/routes/configure-initial-resolved-ips/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesCheck your current rangeUpdate your range

Initial resolved IPs (also called token IPs) are ephemeral addresses that Gateway assigns to DNS queries so it can associate hostname-based traffic with the correct policy or tunnel at the network layer, where hostname information is not usually available. Refer to [Gateway initial resolved IPs](https://developers.cloudflare.com/cloudflare-one/networks/routes/reserved-ips/#gateway-initial-resolved-ips) for a list of features that depend on this range.

By default, initial resolved IPs are assigned from:

  * **IPv4** : `172.64.128.0/20`
  * **IPv6** : `2606:4700:0cf1:4000::/64`



This is the default range. You can [configure a custom initial resolved IP range](https://developers.cloudflare.com/cloudflare-one/networks/routes/configure-initial-resolved-ips/) for IPv4 if it conflicts with your existing network.

The IPv6 range is not configurable.

Caution

If you configure a custom IPv4 range within Carrier-Grade NAT (CGNAT) address space, this can lead to [Google Chrome's Local Network Access restrictions](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/#google-chrome-restricts-access-to-private-hostnames), which the public default range avoids.

## Prerequisites

  * You have the [Cloudflare One Networks Write](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) permission (for API access), or dashboard access to **Networking** > **IP addresses** > **Address space** > **Custom IPs**.
  * Your new range does not conflict with existing routes or other reserved [Cloudflare One subnets](https://developers.cloudflare.com/cloudflare-one/networks/routes/reserved-ips/) in your account.



## Check your current range

  1. Go to **Networking** > **IP addresses** > **Address space** > **Custom IPs**.

[ Go to **Custom IPs** ↗ ](https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space/custom-ips)
  2. Find the row where **Assign to** is **Initial Resolved IP** to see your account's current IPv4 range in the **Prefix** column.




Send a `GET` request to the [Get Initial Resolved IP Subnet](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/subresources/initial_resolved_ip/methods/get/) endpoint for the address family you want to check:
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/zerotrust/subnets/initial_resolved_ip/$ADDRESS_FAMILY" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

## Update your range

  1. Go to **Networking** > **IP addresses** > **Address space** > **Custom IPs**.

[ Go to **Custom IPs** ↗ ](https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space/custom-ips)
  2. Find the row where **Assign to** is **Initial Resolved IP** , select the three dots menu, and select **Edit**.

  3. Enter your new IPv4 range in **IP address**.

  4. Select **Save**.




Send a `PUT` request to the [Update Initial Resolved IP Subnet](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/subresources/initial_resolved_ip/methods/update/) endpoint with your desired network range:
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/zerotrust/subnets/initial_resolved_ip/$ADDRESS_FAMILY" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"comment": "example comment",
    		"name": "IPv4 Gateway initial resolved IPs",
    		"network": "172.64.128.0/20"
    	}'

The new CIDR must not conflict with existing private routes or other reserved subnets in your account. If it does, the request fails and the response describes the conflicting route or subnet.

Note

Only the IPv4 range is configurable. The IPv6 initial resolved IP range (`2606:4700:0cf1:4000::/64`) is fixed and does not need to be changed to resolve Chromium's Local Network Access restrictions, which do not affect IPv6.

The default IPv4 range is [automatically routed through the Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#automatically-managed-ranges) and does not require any Split Tunnel configuration. If you configure a custom range, update your [Split Tunnel configuration](https://developers.cloudflare.com/cloudflare-one/networks/routes/reserved-ips/#split-tunnel-configuration) so that traffic to the new range routes through the Cloudflare One Client, and remove the old range if it is no longer used by any other reserved IP purpose.

Initial resolved IPs have a TTL of approximately 10 minutes. DNS queries resolved before you change your range continue to use the previous range until that TTL expires. After that, new DNS queries receive an initial resolved IP from the new range.

[PreviousReserved IP addresses](https://developers.cloudflare.com/cloudflare-one/networks/routes/reserved-ips/)[NextAdd locations](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/routes/configure-initial-resolved-ips.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
