---
url: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/
title: DHCP server \u00b7 Cloudflare WAN docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:26.825407+00:00
---

# DHCP server · Cloudflare WAN docs

> Source: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)
  3. /…

Configuration[Configure with Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)Network options

  4. /DHCP options
  5. /DHCP server



# DHCP server

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When you use a static IP address, Cloudflare One Appliance (formerly Magic WAN Connector) can also act as a DHCP server in your network. To enable this feature:

  1. Go to the **Connectors** page.

[ Go to **Connectors** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

  2. Go to the **Appliances** tab > **Profiles**.
  3. Select the Cloudflare One Appliance you want to configure > **Edit**.
  4. Select **Network Configuration** > **LAN configuration**.
  5. In **LAN configuration** , select the LAN where you want to enable DHCP server.
  6. Select **Edit**.
  7. Under **Static addressing** , select **This is a DHCP Server**. You also have to specify: 
     * The DNS server address. You can have more than one IP address. Select **Add DNS Server** for each server you want to add.
     * The DHCP pool start
     * The DHCP pool end



Note

You will need your [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) and [API token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/) to use the API.

Create a [`PUT` request](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/lans/methods/update/) to update the LAN where you want to enable DHCP server:

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
    								"dhcp_pool_end": "<IP_ADDRESS>",
    								"dhcp_pool_start": "<IP_ADDRESS>",
    								"dns_server": "<IP_ADDRESS>"
    						}
    				}
    		}
    	}'

[PreviousDHCP relay](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-relay/)[NextDHCP server options](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
