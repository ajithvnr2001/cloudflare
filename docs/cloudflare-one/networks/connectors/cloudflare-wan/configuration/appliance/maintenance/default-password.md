---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/default-password/
title: Default password \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:26.391664+00:00
---

# Default password · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/default-password/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/)Configuration[Configure with Connector](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/)

  4. /Maintenance
  5. /Default password



# Default password

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/default-password/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDefault password to access hardware Cloudflare One ApplianceDefault password to access Virtual Appliance

Cloudflare One Appliance (formerly Magic WAN Connector) ships to you with a default password that enables you to access the hardware box or the virtual machine. Cloudflare recommends that you change this password after the first boot.

## Default password to access hardware Cloudflare One Appliance

The default password for Cloudflare One Appliance is the serial number (also known as a Service Tag for Dell devices), all uppercase followed by an `!` (exclamation mark). For example, `A1B2C3D!`

## Default password to access Virtual Appliance

The default password for Virtual Appliance is the last seven characters of your license key, all uppercase, plus an `!` (exclamation mark).

For example, if your license key is `mconn-abcdefghijklmnopqrstuvwxyz`, your default password will be `TUVWXYZ!`.

[PreviousDeactivate Connector](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/deactivate-appliance/)[NextHeartbeat](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/heartbeat/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/default-password.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
