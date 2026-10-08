---
url: https://developers.cloudflare.com/magic-transit/cloudflare-ips/
title: Cloudflare IPs \u00b7 Cloudflare Magic Transit docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:17.992269+00:00
---

# Cloudflare IPs · Cloudflare Magic Transit docs

> Source: https://developers.cloudflare.com/magic-transit/cloudflare-ips/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Magic Transit](https://developers.cloudflare.com/magic-transit/)
  3. /Cloudflare IPs



# Cloudflare IPs

Last updated Oct 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/magic-transit/cloudflare-ips/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCheck your Cloudflare IPs

To use Magic Transit, you need to own a publicly routable IP address block with a minimum size of `/24`. If you do not own a `/24` address block, you can use Magic Transit with a Cloudflare-owned IP address. This option is helpful if you do not meet the `/24` prefix length requirements or want to protect a smaller network.

To protect your network with a Cloudflare IP address, contact your account manager. After you receive your IP address:

  * [Create a tunnel](https://developers.cloudflare.com/magic-transit/how-to/configure-tunnel-endpoints/).
  * [Set up static routes](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#configure-static-routes) or [BGP peering](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#configure-bgp-routes).
  * [Configure health checks](https://developers.cloudflare.com/magic-transit/network-health/run-endpoint-health-checks/).
  * Confirm you properly configured [tunnel](https://developers.cloudflare.com/magic-transit/network-health/update-tunnel-health-checks-frequency/) and endpoint health checks.
  * Update your infrastructure at your own pace to use the allocated Cloudflare IPs.



When you use a Cloudflare-owned IP space, you do not need a Letter of Agency (LOA). When using Cloudflare-leased IPs, Cloudflare automatically enables [Magic Transit Egress](https://developers.cloudflare.com/magic-transit/reference/egress/), which routes your egress traffic to Cloudflare instead of the Internet. Set up policy-based routing on your end to ensure return traffic routes properly.

## Check your Cloudflare IPs

You can find your leased Anycast IPs for Magic Transit on the dashboard under [**Address space** > **Leased IPs** ↗︎](https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space).

[PreviousNetwork Flow](https://developers.cloudflare.com/magic-transit/network-flow/)[NextMagic Transit on-demand](https://developers.cloudflare.com/magic-transit/on-demand/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/magic-transit/cloudflare-ips.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
