---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/application-based-policies/
title: Application-aware policies \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:28.501050+00:00
---

# Application-aware policies · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/application-based-policies/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/)Configuration[Configure with Connector](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/)

  4. /Network options
  5. /Application-aware policies



# Application-aware policies

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/application-based-policies/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Standard traffic policies match on network-layer attributes like IP addresses and port ranges. Application-aware policies go further — they identify traffic by the application generating it, so you can make routing and security decisions based on what the traffic is, not just where it is going.

Cloudflare One Appliance (formerly Magic WAN Connector) classifies traffic using the same application categories used across Cloudflare's [Secure Web Gateway](https://developers.cloudflare.com/cloudflare-one/policies/gateway/). This means routing decisions on the Appliance and security policies in Gateway use the same application definitions.

For the full list of recognized applications and categories, refer to [Applications and app types](https://developers.cloudflare.com/cloudflare-one/policies/gateway/application-app-types/).

With application-aware policies, you can:

  * **Break out traffic directly to the Internet** — route specific applications directly to the Internet from the Appliance, bypassing Cloudflare's security filtering.
  * **Prioritize traffic** — assign higher priority to specific applications so the Appliance processes them first when the network is congested.



For details, refer to the following pages:

  * [Breakout traffic](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/)
  * [Prioritized traffic](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/)



[PreviousConfigure Virtual Appliance](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/configure-virtual-appliance/)[NextBreakout traffic](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/application-based-policies/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
