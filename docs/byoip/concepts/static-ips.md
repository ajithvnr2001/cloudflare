---
url: https://developers.cloudflare.com/byoip/concepts/static-ips/
title: Static IPs \u00b7 Cloudflare BYOIP docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:39.995978+00:00
---

# Static IPs · Cloudflare BYOIP docs

> Source: https://developers.cloudflare.com/byoip/concepts/static-ips/

  1. [Home](https://developers.cloudflare.com/)
  2. /[BYOIP](https://developers.cloudflare.com/byoip/)
  3. /Concepts
  4. /Static IPs



# Static IPs

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/byoip/concepts/static-ips/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityCheck Static IPs

When you use Cloudflare as a [reverse proxy](https://developers.cloudflare.com/fundamentals/concepts/how-cloudflare-works/), Cloudflare assigns shared [anycast IP addresses](https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/) to proxied DNS records by default. These IPs can change at any time. Static IPs give you a set of specifically assigned Cloudflare IP addresses — Cloudflare will not change them without notifying you, and will typically only do so at your request.

Static IPs are useful when you need to allowlist your IPs or communicate them to third parties in advance.

Note

Although BYOIP and static IPs are different offerings, both can be managed using [Address Maps](https://developers.cloudflare.com/byoip/address-maps/).

Static IPs are allocated at the account level but can be assigned to a single zone, meaning multiple zones can share the same static IPs. You can specify which zones are mapped to your static IPs and control when the IPs for your zones change.

## Availability

Static IPs are available as an add-on purchase for Enterprise plans.

## Check Static IPs

You can find your leased Static IPs for CDN Ingress on the dashboard under [**Address space** > **Leased IPs** ↗︎](https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space).

[PreviousPrefix delegations](https://developers.cloudflare.com/byoip/concepts/prefix-delegations/)[NextAbout](https://developers.cloudflare.com/byoip/address-maps/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/byoip/concepts/static-ips.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
