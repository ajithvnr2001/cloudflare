---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/heartbeat/
title: Heartbeat \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:27.216117+00:00
---

# Heartbeat · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/heartbeat/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/)Configuration[Configure with Connector](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/)

  4. /Maintenance
  5. /Heartbeat



# Heartbeat

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/heartbeat/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Access Cloudflare One Appliance's heartbeat

Cloudflare One Appliance (formerly Magic WAN Connector) communicates periodically with Cloudflare via HTTPS. This is also known as a heartbeat, and lets Cloudflare know that the Cloudflare One Appliance in question is connected to the Internet and reachable.

The heartbeat calls are made to `api.cloudflare.com`. Each Cloudflare One Appliance has a heartbeat frequency of 10 seconds, independently of the number of WAN interfaces you have running on your device.

There are three symbols for the heartbeat signal that allow you to quickly check the status of Cloudflare One Appliance:

  * **Blue`i`**: Cloudflare One Appliance is contacting Cloudflare as expected.
  * **Yellow triangle** : Cloudflare One Appliance has not yet connected to Cloudflare.
  * **Red triangle** : There is a potential problem with Cloudflare One Appliance.



### Access Cloudflare One Appliance's heartbeat

  1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), and go to **Networks**.
  2. Go to **Connectors** > **Appliances** > **Appliances**.
  3. Find your Cloudflare One Appliance, and place your cursor over the icon on the **Status** column to check the timestamp. The timestamp displays the last time Cloudflare One Appliance successfully contacted Cloudflare.



[PreviousDefault password](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/default-password/)[NextInterrupt window](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/heartbeat.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
