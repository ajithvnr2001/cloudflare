---
url: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/
title: Interrupt window \u00b7 Cloudflare WAN docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:26.195011+00:00
---

# Interrupt window · Cloudflare WAN docs

> Source: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)
  3. /…

Configuration[Configure with Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)

  4. /Maintenance
  5. /Interrupt window



# Interrupt window

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Interrupt window defines when Cloudflare One Appliance (formerly Magic WAN Connector) can update its systems. When Cloudflare One Appliance is updating, this may result in an interruption to existing connections. Set up a time window that minimizes disruption to your sites.

  1. Go to the **Connectors** page.

[ Go to **Connectors** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

  2. Go to the **Appliances** tab > **Appliances**.
  3. Find the Cloudflare One Appliance you want to set up the update window for > **Edit**.
  4. In **Interrupt window** , select the most appropriate time for the Cloudflare One Appliance to update its systems: 
     * **Timezone** : Select the time zone for the Cloudflare One Appliance to update.
     * **Start time** : Choose an hour for the Cloudflare One Appliance to start updating. Cloudflare recommends you choose an hour when there is minimal activity in your network, to avoid potential disruptions.
     * **Duration** : Duration indicates the time window during which the Cloudflare One Appliance is scheduled to update. For example, if you configure your Cloudflare One Appliance to update at `22:00` and specify a **Duration** of `4 hours`, the Cloudflare One Appliance will attempt to update within the four-hour period following `22:00`.



[PreviousHeartbeat](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/heartbeat/)[NextRegister Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/register-appliance/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
