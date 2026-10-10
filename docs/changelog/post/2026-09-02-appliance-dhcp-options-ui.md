---
url: https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-dhcp-options-ui/
title: Configure DHCP options from the dashboard on Cloudflare One Appliance \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.789453+00:00
---

# Configure DHCP options from the dashboard on Cloudflare One Appliance · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-dhcp-options-ui/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 2, 2026

## Configure DHCP options from the dashboard on Cloudflare One Appliance

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure [custom DHCP options](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/) directly from the dashboard when the [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) is acting as the DHCP server for a LAN.

![Adding a custom DHCP option to a LAN's DHCP server from the Network Configuration tab of an appliance profile](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1034,format=webp/_astro/2026-09-01-appliance-dhcp-options-ui.B5OEZmib.gif)

  * In **LAN configuration** , under **DHCP server options** , select **Add DHCP option** to choose from common options for PXE / iPXE boot, VoIP phone provisioning, and vendor-specific configuration, or select **Add custom option** to enter your own option code, type, and value.
  * This complements the existing [API and Terraform workflow](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/#configure-dhcp-options) for configuring DHCP options.



For details, refer to [DHCP server options](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/).
