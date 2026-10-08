---
url: https://developers.cloudflare.com/byoip/
title: Bringing Your Own IPs to Cloudflare \u00b7 Cloudflare BYOIP docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:39.315989+00:00
---

# Bringing Your Own IPs to Cloudflare · Cloudflare BYOIP docs

> Source: https://developers.cloudflare.com/byoip/

  1. [Home](https://developers.cloudflare.com/)
  2. /BYOIP



# Cloudflare BYOIP

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/byoip/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFeaturesMore resources

Get Cloudflare's security and performance while using your own IPs.

Enterprise-only

When you use Cloudflare as a [reverse proxy](https://developers.cloudflare.com/fundamentals/concepts/how-cloudflare-works/), Cloudflare responds to DNS queries for proxied records with Cloudflare-owned IP addresses1. For some organizations, it is important to keep their website or application associated with IP addresses they already own rather than using Cloudflare's.

With Bring Your Own IP (BYOIP), Cloudflare announces your IP prefixes in all our locations. Use your IPs with [Magic Transit](https://developers.cloudflare.com/magic-transit/), [Spectrum](https://developers.cloudflare.com/spectrum/), [CDN services](https://developers.cloudflare.com/cache/), or Gateway [DNS locations](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/) and [dedicated egress IPs](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/).

Learn how to [get started](https://developers.cloudflare.com/byoip/get-started/).

* * *

## Features

[Service bindings](https://developers.cloudflare.com/byoip/service-bindings/)

Control whether traffic destined for a given IP address is routed to Magic Transit, CDN, or Spectrum.

Use Service bindings

[Address maps](https://developers.cloudflare.com/byoip/address-maps/)

Specify which IP addresses should be mapped to DNS records when they are proxied through Cloudflare.

Use Address maps

* * *

## More resources

### [RPKI blog post](https://blog.cloudflare.com/rpki/)

An overview of BGP, RPKI, and other important aspects of Internet routing.

### [Reference Architectures](https://developers.cloudflare.com/reference-architecture/)

Explore how you can leverage Cloudflare's platform to create solutions based on your business needs.

## Footnotes

  1. Without BYOIP, when your domain's records are `proxied`, Cloudflare responds with a Cloudflare-owned [anycast IP address](https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/). ↩




[NextGet started](https://developers.cloudflare.com/byoip/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/byoip/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
