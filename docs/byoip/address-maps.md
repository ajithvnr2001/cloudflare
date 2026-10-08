---
url: https://developers.cloudflare.com/byoip/address-maps/
title: About address maps \u00b7 Cloudflare BYOIP docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:39.546324+00:00
---

# About address maps · Cloudflare BYOIP docs

> Source: https://developers.cloudflare.com/byoip/address-maps/

  1. [Home](https://developers.cloudflare.com/)
  2. /[BYOIP](https://developers.cloudflare.com/byoip/)
  3. /Address maps



# About address maps

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/byoip/address-maps/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow Address Maps works Static IPs or BYOIPImmutable address mapsSpectrum compatibility

Address map is a data structure enabling customers with BYOIP prefixes or account-level static IPs to specify which IP addresses should be mapped to DNS records when they are proxied through Cloudflare.

By default, Cloudflare responds to DNS queries for proxied hostnames with Cloudflare-owned [anycast IP addresses](https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/). Address maps allow you to override this behavior — when a zone or account is associated with an address map, Cloudflare responds with the IP addresses you specify instead.

To use address maps, you must first have [BYOIP](https://developers.cloudflare.com/byoip/) prefixes or [static IPs](https://developers.cloudflare.com/byoip/concepts/static-ips/) configured on your account. You can [customize the IPs Cloudflare uses](https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/#customize-cloudflare-ip-addresses) through either approach. If you are interested in address maps but do not yet have BYOIP or static IPs, contact your account manager.

Note

Both IPv4 and IPv6 addresses are supported.

* * *

## How Address Maps works

For zones using [Cloudflare's authoritative DNS](https://developers.cloudflare.com/dns/), Cloudflare typically responds to DNS queries for proxied hostnames with [anycast IPs](https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/). However, if you [customize the IPs Cloudflare uses](https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/#customize-cloudflare-ip-addresses) and use Address Maps, Cloudflare will respond with the IP address(es) on the address map.

Address maps do not change [how Cloudflare reaches the configured origin](https://developers.cloudflare.com/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-reverse-proxy). The IP addresses defined on your zone's [DNS Records ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/dns/records) continue to instruct Cloudflare how to reach the origin.

Caution

Depending on whether you use static IPs or BYOIP, the process to [create an address map](https://developers.cloudflare.com/byoip/address-maps/setup/) is different.

### Static IPs or BYOIP

Leased static IPs allow you to use a set of specifically assigned Cloudflare IPs to ensure they do not change. Cloudflare creates an address map with your static IPs that you may edit. You cannot create another map using your static IPs.

With BYOIP, you use your IPs by bringing an address space that you lease or own and creating an address map.

* * *

## Immutable address maps

Some customers may only proxy zones through BYOIP addresses, and are prohibited from using Cloudflare IP addresses for proxied DNS names. In this case, Cloudflare will create an immutable, account-wide address map to ensure all zones in your account receive BYOIP addresses as a fallback. These address maps cannot be deleted.

It is still possible to create more specific zone-level address maps with specific BYOIPs, but DNS will fall back to the account-wide address map without one.

To specify different addresses for certain zones, [create a new address map](https://developers.cloudflare.com/byoip/address-maps/setup/).

* * *

## Spectrum compatibility

You can use address maps to set up [non-SNI support](https://developers.cloudflare.com/byoip/address-maps/setup/#spectrum-https-applications) for Spectrum HTTPS applications.

However, to control what IP address Cloudflare will use when responding to requests for your Spectrum applications, you should first refer to their respective configuration and set the `edge_ips` field as `static`, e.g.:
    
    
    "edge_ips": {
      "type": "static",
      "ips": ["1.2.3.4"]
    }

For details, refer to the [Spectrum API](https://developers.cloudflare.com/api/resources/spectrum#%28resource%29%20spectrum%20%3E%20%28model%29%20edge_ips%20%3E%20%28schema%29%20%3E%20%28variant%29%201).

[PreviousStatic IPs](https://developers.cloudflare.com/byoip/concepts/static-ips/)[NextSetup](https://developers.cloudflare.com/byoip/address-maps/setup/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/byoip/address-maps/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
