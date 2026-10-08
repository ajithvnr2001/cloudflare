---
url: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-relay/
title: DHCP relay \u00b7 Cloudflare WAN docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:26.710756+00:00
---

# DHCP relay · Cloudflare WAN docs

> Source: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-relay/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)
  3. /…

Configuration[Configure with Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)Network options

  4. /DHCP options
  5. /DHCP relay



# DHCP relay

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-relay/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

DHCP Relay provides a way for DHCP clients to communicate with DHCP servers that are not available on the same local subnet/broadcast domain. When you enable DHCP Relay, Cloudflare One Appliance (formerly Magic WAN Connector) forwards DHCP discover messages to a predefined DHCP server, and routes the responses back to the original device that sent the discover message.
    
    
      	flowchart LR
      	accTitle: DHCP Relay diagram
      	accDescr: The graph shows Cloudflare One Appliance sending DHCP discover messages to a DHCP server offsite.
      			a(Cloudflare One Appliance) <--> b(Cloudflare/Cloudflare WAN) <--> c(DHCP server)
    
      			subgraph Site A
      			d[LAN 1] <--> a
      			e[LAN 2] <--> a
      			end
    
      			subgraph Site B
      			c
      			end
      			classDef orange fill:#f48120,color: black
      			class a,b,c orange
      

_The graph shows Cloudflare One Appliance sending DHCP discover messages to a DHCP server offsite._

Caution

DHCP relay will not work if your DHCP server is behind a [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/). To enable DHCP relay functionality, use either a Cloudflare WAN IPsec/GRE tunnel or a CNI connection.

To configure DHCP relay:

  1. Go to the **Connectors** page.

[ Go to **Connectors** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

  2. Go to the **Appliances** tab > **Profiles**.
  3. Select your Cloudflare One Appliance > **Edit**.
  4. Select **Network Configuration**.
  5. In **LAN configuration** , select the LAN where you need to configure DHCP relay.
  6. Select **Edit**.
  7. Select **This is a DHCP Relay**.
  8. In **Upstream DHCP server addresses** , enter the IP address of your DHCP server.
  9. (Optional) If you need to add more DHCP server addresses, select **Add upstream DHCP server address** as many times as needed, and enter the new values.



Note

You will need your [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) and [API token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/) to use the API.

Create a [`PUT` request](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/lans/methods/update/) to update the LAN where you want to enable DHCP relay:

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
    						"dhcp_relay": {
    								"server_addresses": [
    										"192.0.2.1"
    								]
    						}
    				}
    		}
    	}'

[PreviousConfigure link aggregation groups](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/link-aggregation/)[NextDHCP server](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-relay.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
