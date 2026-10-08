---
url: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-static-address-reservation/
title: DHCP static address reservation \u00b7 Cloudflare WAN docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:26.875272+00:00
---

# DHCP static address reservation · Cloudflare WAN docs

> Source: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-static-address-reservation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)
  3. /…

Configuration[Configure with Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)Network options

  4. /DHCP options
  5. /DHCP static address reservation



# DHCP static address reservation

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-static-address-reservation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

If you configure your Cloudflare One Appliance (formerly Magic WAN Connector) to be a DHCP server, you can also assign IP addresses to specific devices on your network. To reserve IP addresses:

  1. Configure your Cloudflare One Appliance to be a [DHCP server](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/).
  2. Select **Add DHCP Reservation**.
  3. In **Hardware Address** enter the [MAC address ↗︎](https://en.wikipedia.org/wiki/MAC_address) for the device you want a specific IP address for.
  4. In **IP Address** , enter the IP address for that device.
  5. (Optional) If you need to reserve more IP addresses, select **Add DHCP Reservation** as many times as needed, and enter the new values.



Note

You will need your [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) and [API token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/) to use the API.

Create a [`PUT` request](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/lans/methods/update/) to update the LAN where you want to reserve addresses:

Example:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Magic WAN Write`
  * `Magic Transit Write`

Update Site LANbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/sites/$SITE_ID/lans/$LAN_ID" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"lan": {
    				"static_addressing": {
    						"dhcp_server": {
    								"reservations": {
    										"<HARDWARE_MAC_ADDRESS>": "<IP_ADDRESS>",
    										"<HARDWARE_MAC_ADDRESS_2>": "<IP_ADDRESS>"
    								}
    						}
    				}
    		}
    	}'

[PreviousDHCP server options](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/)[NextEnable NAT for a subnet](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/nat-subnet/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-static-address-reservation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
