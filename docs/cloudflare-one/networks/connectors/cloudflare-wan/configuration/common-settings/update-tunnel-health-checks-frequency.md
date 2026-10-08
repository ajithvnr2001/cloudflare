---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/update-tunnel-health-checks-frequency/
title: Update tunnel health checks frequency \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:31.143583+00:00
---

# Update tunnel health checks frequency · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/update-tunnel-health-checks-frequency/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/)Configuration

  4. /[Common settings](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/)
  5. /Update tunnel health checks frequency



# Update tunnel health checks frequency

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/update-tunnel-health-checks-frequency/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewManual configurationConfigure Connector

By default, Cloudflare servers send [health checks](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/reference/tunnel-health-checks/) to each GRE, Cloudflare Network Interconnect (CNI), or IPsec tunnel endpoint you configure to receive traffic from Cloudflare WAN.

For Cloudflare One Appliance (formerly Magic WAN Connector), Cloudflare sends health checks to IPsec tunnel endpoints.

You can configure the health check frequency through the dashboard or [the API](https://developers.cloudflare.com/api/resources/magic_transit/subresources/gre_tunnels/methods/update/) to suit your use case. For example, if you are connecting a lower-traffic site that does not need immediate failover and you prefer a lower volume of health check traffic, set the frequency to `low`. On the other hand, if you are connecting a site that is extremely sensitive to any issues and you want proactive failover at the earliest sign of a potential problem, set this to `high`.

Available options are `low`, `mid`, and `high`.

To configure health checks frequency in Cloudflare One Appliance, refer to Configure Connector

## Manual configuration

  1. To create or edit your tunnel, refer to [Add tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels).
  2. Change the **Health check rate** to your desired rate. For example, _Low_.
  3. Save your changes.



You can adjust the health check frequency by updating your [GRE](https://developers.cloudflare.com/api/resources/magic_transit/subresources/gre_tunnels/methods/update/), [IPsec](https://developers.cloudflare.com/api/resources/magic_transit/subresources/ipsec_tunnels/methods/update/), or [CNI](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf_interconnects/methods/update/) tunnels.

The following example adjusts tunnel health check frequency to `low`. Note that this command applies to GRE, IPsec and CNI tunnels:
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/magic/ipsec_tunnels/%7Bipsec_tunnel_id%7D" \
    	--request PUT \
    	--json '{
    		"health_check": {
    				"rate": "low"
    		}
    	}'

## Configure Connector

  1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/) > **Networks**.

  2. Go to **Connectors** > **Appliances**.

  3. In **Profiles** , find the Connector profile you want to edit > select the three dots > **Edit**.

  4. In **Network Configuration** > **WAN configuration** > select your WAN > **Edit**.

  5. Change the **Health check rate** to your desired rate.

  6. Select **Save**.




Note

Cloudflare WAN customers with [Customer Metadata Boundary](https://developers.cloudflare.com/data-localization/metadata-boundary/) enabled for the European Union can access GRE, IPsec, and CNI (Cloudflare Network Interconnect) health check and traffic volume data in the Cloudflare dashboard and through the API. This ensures that customers who need to be General Data Protection Regulation (GDPR) compliant can access all Cloudflare WAN features.

[PreviousCheck tunnel health in the dashboard](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/)[NextConfigure tunnel health alerts](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/configure-tunnel-health-alerts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/update-tunnel-health-checks-frequency.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
