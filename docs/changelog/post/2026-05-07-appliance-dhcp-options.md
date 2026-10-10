---
url: https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-dhcp-options/
title: Custom DHCP options on Cloudflare One Appliance \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:38.722340+00:00
---

# Custom DHCP options on Cloudflare One Appliance · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-dhcp-options/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 7, 2026

## Custom DHCP options on Cloudflare One Appliance

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When the Cloudflare One Appliance is acting as the DHCP server for a LAN, you can now configure custom DHCP options on the leases it issues. This unlocks workflows such as PXE / iPXE boot, VoIP phone provisioning, and vendor-specific client configuration.

Each option is defined by `option_number`, `value`, and one of four value types: `text`, `integer`, `hex`, or `ip`. Configurations are validated on the appliance before being applied — invalid configurations are rejected and the underlying error is returned to the API caller, so a bad option will not disrupt the live DHCP service.

For details, refer to [DHCP server options](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/).
