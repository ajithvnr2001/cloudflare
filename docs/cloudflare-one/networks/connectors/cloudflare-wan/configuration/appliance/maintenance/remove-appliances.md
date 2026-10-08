---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/remove-appliances/
title: Remove connectors \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:27.498722+00:00
---

# Remove connectors · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/remove-appliances/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/)Configuration[Configure with Connector](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/)

  4. /Maintenance
  5. /Remove connectors



# Remove connectors

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/remove-appliances/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRemove a profileRemove a physical device

When adding or removing Cloudflare One Appliances (formerly Magic WAN Connectors), you need to be aware of the difference between the physical device and its profile.

  * The physical device is the hardware at your site.
  * The profile contains the configuration that allows the device to connect to Cloudflare, including your WANs, LANs, traffic steering, and LAN policies.



You can have more than one Cloudflare One Appliance in one profile if you initially enabled high availability during the configuration of the profile. If you did not enable high availability, you need to delete the profile associated with a site before adding a new Cloudflare One Appliance.

## Remove a profile

  1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), and go to **Networks**.
  2. Go to **Connectors** > **Appliances** > **Profiles**.
  3. Find the profile that you want to edit > select the three dots next to it > **Delete**.



## Remove a physical device

To remove a Cloudflare One Appliance from your account:

  1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), and go to **Networks**.
  2. Go to **Connectors** > **Appliances** > **Appliances**.
  3. Find the Cloudflare One Appliance that you want to delete > select the three dots next to it > **Delete**.



[PreviousEdit basic information](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/edit-basic-info/)[NextEdit network settings](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/edit-network-settings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/remove-appliances.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
