---
url: https://developers.cloudflare.com/magic-transit/on-demand/
title: Magic Transit on-demand \u00b7 Cloudflare Magic Transit docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:19.475801+00:00
---

# Magic Transit on-demand · Cloudflare Magic Transit docs

> Source: https://developers.cloudflare.com/magic-transit/on-demand/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Magic Transit](https://developers.cloudflare.com/magic-transit/)
  3. /Magic Transit on-demand



# Magic Transit on-demand

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/magic-transit/on-demand/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

If you have access to the Magic Transit on-demand option, you can [configure prefix advertisement](https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/#configure-dynamic-advertisement) from the **IP Prefixes** page in your Cloudflare account home or through the [Cloudflare API](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/advertisement_status/methods/edit/).

A common workflow is to enable prefix advertisement during an attack so that you can take advantage of Cloudflare protection and then disable advertisement once the incident is resolved. Dynamic advertisement (through the dashboard or API) does not support prefixes using BGP-controlled advertisements. Specify your preferred on-demand advertisement method during prefix onboarding.

To ensure smooth operation and simplify the advertisement process during an attack scenario, refer to [Dynamic advertisement: Best practices](https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/).

Note

You cannot use Magic Transit on-demand with Cloudflare leased IPs.

[PreviousCloudflare IPs](https://developers.cloudflare.com/magic-transit/cloudflare-ips/)[NextNetwork Interconnect (CNI)](https://developers.cloudflare.com/magic-transit/network-interconnect/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/magic-transit/on-demand.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
