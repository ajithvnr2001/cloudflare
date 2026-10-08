---
url: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/network-segmentation/
title: Network segmentation \u00b7 Cloudflare WAN docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:26.943303+00:00
---

# Network segmentation · Cloudflare WAN docs

> Source: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/network-segmentation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)
  3. /…

Configuration[Configure with Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)

  4. /Network options
  5. /Network segmentation



# Network segmentation

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/network-segmentation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a policyEdit a policyDelete a policy

You can define policies in your Cloudflare One Appliance (formerly Magic WAN Connector) to either allow traffic to flow between your LANs without it leaving your local premises or to forward it via the Cloudflare network where you can add additional security features. The default behavior is to drop all LAN-to-LAN traffic. These policies can be created for specific subnets, and link two LANs.
    
    
      	flowchart LR
      	accTitle: LAN-to-LAN traffic flow
      	accDescr: In this example, the red path shows traffic that stays in the customer's premises (allowing direct communication between LAN 3 and LAN 4), and the orange path shows traffic that goes to Cloudflare before returning to the customer's premises (processing traffic between LAN 1 and LAN 2 in Cloudflare).
      			a(Cloudflare One Appliance) <---> b(Internet) <---> c(Cloudflare)
    
      			subgraph Customer site
      			d[LAN 1] <---> a
      			e[LAN 2] <---> a
      			g[LAN 3] <---> a
      			h[LAN 4] <---> a
      			end
      			classDef orange fill:#f48120,color: black
      			class a,c orange
    
      			linkStyle 0,1,2,3 stroke:#f48120,stroke-width:3px
      			linkStyle 4,5 stroke:red,stroke-width:3px
      

_In this example, the red path shows traffic that stays in the customer's premises (allowing direct communication between LAN 3 and LAN 4), and the orange path shows traffic that goes to Cloudflare before returning to the customer's premises (processing traffic between LAN 1 and LAN 2 in Cloudflare)._

  


As a best practice for security, we recommend sending all traffic through Cloudflare's network for Zero Trust security filtering. Use these policies with care and only for scenarios where you have a hard requirement for LAN-to-LAN traffic flows.

If you enable LAN to LAN traffic flows, communications can only be initiated from origin to destination — for example, LAN 1 to LAN 2 — and not the other way around. This is by design and prevents potential exfiltration of information. This does not mean bidirectional communication on TCP is not possible. It only means that the origin is the only one authorized to initiate communications.

Unidirectional communication can be enabled for UDP and ICMP, but it is not available for TCP, as it would break that protocol.

The following guide assumes you have already created a site and configured your Cloudflare One Appliance. For instructions to create a site and configure your Cloudflare One Appliance, refer to [Configure hardware Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-hardware-appliance/) or [Configure Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/), depending on the type of Cloudflare One Appliance you have on your premises.

## Create a policy

Follow these steps to create a new LAN policy to segment your network. Only the fields marked **required** are mandatory.

  1. Go to the **Connectors** page.

[ Go to **Connectors** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

  2. Go to the **Appliances** tab > **Profiles**.

  3. Select the Cloudflare One Appliance you want to configure > **Edit**.

  4. Go to **Network Configuration** > **LAN configuration**.

  5. Select **LAN policies** > **Create**.

  6. In **Policy name** , enter a descriptive name for the policy you are creating.

  7. From the drop-down menu **Origin (required)** , select your origin LAN.

  8. Specify a subnet for your first LAN in **Subnets**.

  9. In **Ports** specify the TCP/UDP ports you want to use. Valid ports range from `1` to `65535`. Zero (`0`) is not a valid port number. Add a comma to separate each of the ports or add a port range. For example, `2,5,6,9-14`.

  10. In **Destination (required)** , select the destination LAN and repeat the above process to configure it.

  11. In **Protocols** , select the type of traffic you want to allow. You can choose **TCP** , **UDP** , and **ICMP**. You can also select **Any** to choose all types of traffic.

  12. In **Traffic direction** you can choose between bidirectional traffic (the default) and unidirectional traffic. What you can choose depends on the protocol that you chose for the policy:

     * **Any** : If **Any** is selected and you choose **Unidirectional** , the system will alert you that this will break TCP traffic.
     * **TCP** : You can only select **Bidirectional**.
     * **UDP** : The system defaults to **Bidirectional** but you can choose **Unidirectional**.
     * **ICMP** : The system defaults to **Bidirectional** but you can choose **Unidirectional**.
  13. In **Traffic path** , select **Forwarded via Cloudflare** if you want traffic to be forwarded to Cloudflare to be processed. If you do not select this option, traffic will flow locally in your premises, without passing through Cloudflare.

  14. Select **Save**.




Note

You will need your [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) and [API token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/) to use the API.

Create a `POST` request [using the API](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/acls/methods/create/) to create a network policy.

Example:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Magic WAN Write`
  * `Magic Transit Write`

Create a new Site ACLbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/sites/$SITE_ID/acls" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"description": "<POLICY_DESCRIPTION>",
    		"forward_locally": true,
    		"lan_1": {
    				"lan_id": "<LAN_ID>",
    				"lan_name": "<LAN_NAME>",
    				"ports": [
    						1
    				],
    				"subnets": [
    						"192.0.2.1"
    				]
    		},
    		"lan_2": {
    				"lan_id": "<LAN_ID>",
    				"lan_name": "<LAN_NAME",
    				"ports": [
    						1
    				],
    				"subnets": [
    						"192.0.2.1"
    				]
    		},
    		"name": "<POLICY_NAME>",
    		"protocols": [
    				"tcp"
    		]
    	}'
    
    
    {
      "errors": [
        {
          "code": 1000,
          "message": "message"
        }
      ],
      "messages": [
        {
          "code": 1000,
          "message": "message"
        }
      ],
      "result": {
        "id": "023e105f4ecef8ad9ca31a8372d0c353",
        "description": "Allows local traffic between PIN pads and cash register.",
        "forward_locally": true,
        "lan_1": {
          "lan_id": "lan_id",
          "lan_name": "lan_name",
          "port_ranges": [
            "8080-9000"
          ],
          "ports": [
            1
          ],
          "subnets": [
            "192.0.2.1"
          ]
        },
        "lan_2": {
          "lan_id": "lan_id",
          "lan_name": "lan_name",
          "port_ranges": [
            "8080-9000"
          ],
          "ports": [
            1
          ],
          "subnets": [
            "192.0.2.1"
          ]
        },
        "name": "PIN Pad - Cash Register",
        "protocols": [
          "tcp"
        ],
        "unidirectional": true
      },
      "success": true
    }

Take note of the `id` parameter, as you will need it to edit or delete network policies.

The new policy will ensure that traffic between the specified LANs flows locally, bypassing Cloudflare.

## Edit a policy

  1. Go to the **Connectors** page.

[ Go to **Connectors** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

  2. Go to the **Appliances** tab > **Profiles**.

  3. Select the Cloudflare One Appliance you want to configure > **Edit**.

  4. Go to **Network Configuration** > **LAN configuration**.

  5. Select **LAN policies**.

  6. Select the policy you need to edit > **Edit**.

  7. Make your changes, and select **Update policy**.




Note

You will need your [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) and [API token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/) to use the API.

Create a `PUT` request [using the API](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/acls/methods/update/) to edit a network policy.

Example:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Magic WAN Write`
  * `Magic Transit Write`

Update Site ACLbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/sites/$SITE_ID/acls/$ACL_ID" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"description": "<POLICY_DESCRIPTION>",
    		"forward_locally": true,
    		"lan_1": {
    				"lan_id": "<LAN_ID>",
    				"lan_name": "<LAN_NAME>",
    				"ports": [
    						1
    				],
    				"subnets": [
    						"192.0.2.1"
    				]
    		},
    		"lan_2": {
    				"lan_id": "<LAN_ID>",
    				"lan_name": "<LAN_NAME>",
    				"ports": [
    						1
    				],
    				"subnets": [
    						"192.0.2.1"
    				]
    		},
    		"name": "<POLICY_NAME>",
    		"protocols": [
    				"tcp"
    		]
    	}'
    
    
    {
      "errors": [
        {
          "code": 1000,
          "message": "message"
        }
      ],
      "messages": [
        {
          "code": 1000,
          "message": "message"
        }
      ],
      "result": {
        "id": "023e105f4ecef8ad9ca31a8372d0c353",
        "connector_id": "ac60d3d0435248289d446cedd870bcf4",
        "description": "description",
        "ha_mode": true,
        "location": {
          "lat": "37.6192",
          "lon": "122.3816"
        },
        "name": "site_1",
        "secondary_connector_id": "8d67040d3835dbcf46ce29da440dc482"
      },
      "success": true
    }

## Delete a policy

  1. Go to the **Connectors** page.

[ Go to **Connectors** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

  2. Go to the **Appliances** tab > **Profiles**.

  3. Select the Cloudflare One Appliance you want to configure > **Edit**.

  4. Go to **Network Configuration** > **LAN configuration**.

  5. Select **LAN policies**.

  6. Select the policy you need to edit > **Edit**.

  7. Select **Delete**.

  8. Select **I understand that deleting a policy is permanent** in the dialog box > **Delete**.




Note

You will need your [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) and [API token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/) to use the API.

Create a `DELETE` request [using the API](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/acls/methods/delete/) to delete a network policy.

Example:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Magic WAN Write`
  * `Magic Transit Write`

Delete Site ACLbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/sites/$SITE_ID/acls/$ACL_ID" \
    	--request DELETE \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

[PreviousEnable NAT for a subnet](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/nat-subnet/)[NextRouted subnets](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/routed-subnets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-wan/configuration/appliance/network-options/network-segmentation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
