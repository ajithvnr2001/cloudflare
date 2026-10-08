---
url: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/remove-appliances/
title: Remove appliances \u00b7 Cloudflare WAN docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:26.028246+00:00
---

# Remove appliances · Cloudflare WAN docs

> Source: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/remove-appliances/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)
  3. /…

Configuration[Configure with Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)

  4. /Maintenance
  5. /Remove appliances



# Remove appliances

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/remove-appliances/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRemove a profileRemove a physical device

When adding or removing Cloudflare One Appliances (formerly Magic WAN Connectors), you need to be aware of the difference between the physical device and its profile.

  * The physical device is the hardware at your site.
  * The profile contains the configuration that allows the device to connect to Cloudflare, including your WANs, LANs, traffic steering, and LAN policies.



You can have more than one Cloudflare One Appliance in one profile if you initially enabled high availability during the configuration of the profile. If you did not enable high availability, you need to delete the profile associated with a site before adding a new Cloudflare One Appliance.

## Remove a profile

  1. Go to the **Connectors** page.

[ Go to **Connectors** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

  2. Go to **Appliances** > **Profiles**.
  3. Find the profile that you want to edit > select the three dots next to it > **Delete**.



## Remove a physical device

To remove a Cloudflare One Appliance from your account:

  1. Go to the **Connectors** page.

[ Go to **Connectors** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

  2. Go to the **Appliances** tab > **Appliances**.
  3. Find the Cloudflare One Appliance that you want to delete > select the three dots next to it > **Delete**.



[PreviousRegister Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/register-appliance/)[NextDevice metrics](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/device-metrics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-wan/configuration/appliance/maintenance/remove-appliances.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
