---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/analytics/site-analytics/
title: Cloudflare WAN network visibility \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:24.204257+00:00
---

# Cloudflare WAN network visibility · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/analytics/site-analytics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/)

  4. /[Analytics](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/analytics/)
  5. /Network visibility



# Network visibility

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/analytics/site-analytics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Network map and traffic overview Traffic overview Set thresholds for site health

After adding your sites, the Network visibility section of the dashboard provides a summary of the connectivity status and traffic analytics for all your sites. This is a great place to start if you receive a Cloudflare WAN alert, need to begin the troubleshooting process, or are performing routine monitoring. Refer to [Set up a site](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/sites/) for more information on how to set up a site.

Network visibility has the following data types available:

Geographic map summary

  * Aggregate Cloudflare WAN site health
  * Cloudflare WAN availability status for sites
  * Cloudflare WAN site geographic location



Cloudflare WAN site data table

  * Site Name
  * Site Health
  * Site Tunnel Names
  * Site Tunnel Statuses
  * Site Traffic Sent
  * Site Traffic Received



Cloudflare WAN site data

  * Traffic Sent by Tunnel
  * Traffic Received by Tunnel



To start using network overview:

  1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/).
  2. Go to **Insights** > **Network visibility**.



You will have access to an overview map with all your active sites, and any alerts for sites that are unhealthy or have no status available to them.

Review the following topics to learn more about the options available to you.

### Network map and traffic overview

The network map section shows all the sites configured with Cloudflare WAN. At a glance, you can check:

  * How many active sites you have
  * Location for sites in a map (if you set up their geographic location)
  * Sites that are healthy or unhealthy
  * Sites that have no status available
  * Sites that have no location set



The Traffic overview section displays a more granular list of your sites and their status.

#### Site health

Sites can be healthy or unhealthy, and Cloudflare WAN uses this information to route traffic. Refer to Set thresholds for site health to learn more about this topic.

#### No status available

The status of a site refers to its health. If your sites show a **No status available** message, this means you did not configure your alert settings when creating your site. For instructions, refer to [Configure Tunnel health alerts](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/configure-tunnel-health-alerts/).

#### No location set

The dashboard displays the number of sites with no location set, meaning sites for which you did not set up a geographic location. To add a location to a site, find the site you want to add location to, and select **no location set** to edit its location settings. Refer to [Set geographic coordinates](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/sites/#set-geographic-coordinates) for more information.

### Traffic overview

Traffic overview aggregates all Cloudflare WAN sites configured in your account. Here, you can check summary information about each site like:

  * Site status
  * Traffic sent and received



Select one of your sites to have access to a more detailed view of its traffic, including traffic by tunnel.

### Set thresholds for site health

When you set up an alert for your site, you will be notified when there is an issue with one or more on-ramps. These alerts are sent when the percentage of successful health checks for a Cloudflare WAN on-ramp drops below the selected service-level objective (SLO). Setting health alerts will also display unhealthy tunnels in the Network map and in the Traffic overview sections.

To set up health alerts:

  1. Configure [Tunnel health alerts](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/configure-tunnel-health-alerts/) across all of the tunnels associated with each Cloudflare WAN site.
  2. After configuring Tunnel health alerts, any Cloudflare WAN site with a tunnel (on-ramp) that is outside of its SLO threshold will be labeled unhealthy in Network map and Traffic overview.



[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/analytics/)[NextNetwork analytics](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/analytics/network-analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-wan/analytics/site-analytics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
