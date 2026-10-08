---
url: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/
title: Cloudflare as Primary \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:04.611334+00:00
---

# Cloudflare as Primary · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS setups](https://developers.cloudflare.com/dns/zone-setups/)

  4. /[DNS Zone transfers](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/)
  5. /Cloudflare as Primary



# Cloudflare as Primary

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow toAvailabilityNotes

With outgoing zone transfers, you can use Cloudflare as your primary DNS provider and configure one or more peer DNS servers as secondary DNS providers.

When you [make edits](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) to Cloudflare DNS, those DNS records will be transferred from Cloudflare to your secondary provider via zone transfer using [AXFR ↗︎](https://datatracker.ietf.org/doc/html/rfc5936) or [IXFR ↗︎](https://datatracker.ietf.org/doc/html/rfc1995)

![With Cloudflare as your primary provider in a multi-provider setup, Cloudflare periodically transfers records to your secondary DNS provider.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1618,height=830,format=webp/_astro/cloudflare-as-primary.CS_-J48n.png)

## How to

  * [Set up outgoing zone transfers](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/setup/)



## Availability

Outgoing zone transfers are available to Enterprise customers who are currently using Cloudflare as their [authoritative DNS provider](https://developers.cloudflare.com/dns/zone-setups/full-setup/). For more details on activation and pricing, contact your account team.

## Notes

If you use [Cloudflare Load Balancing](https://developers.cloudflare.com/load-balancing/), only proxied Load Balancer DNS records will be transferred.

[PreviousOverview](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/)[NextSetup](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/setup/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/zone-setups/zone-transfers/cloudflare-as-primary/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
