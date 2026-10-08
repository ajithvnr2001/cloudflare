---
url: https://developers.cloudflare.com/byoip/service-bindings/
title: IP address service bindings \u00b7 Cloudflare BYOIP docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:40.137294+00:00
---

# IP address service bindings · Cloudflare BYOIP docs

> Source: https://developers.cloudflare.com/byoip/service-bindings/

  1. [Home](https://developers.cloudflare.com/)
  2. /[BYOIP](https://developers.cloudflare.com/byoip/)
  3. /Service bindings



# IP address service bindings

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/byoip/service-bindings/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewScope CDN (Cache) Spectrum Magic Transit CDN egressTutorials

In the context of BYOIP, service bindings map traffic destined for IP addresses to the Cloudflare service it should be routed through - such as Magic Transit, CDN, or Spectrum. A default binding covering the entire prefix is required when you first [onboard](https://developers.cloudflare.com/byoip/get-started/#2-create-service-bindings), and additional bindings can be created at any time to route specific IP addresses or CIDR ranges to a different service.

For example, you could set Magic Transit as the default service for Layer 3 DDoS protection across the entire prefix, while directing specific IPs to the CDN for Layer 7 processing. Refer to Scope for the available combinations.

Note

**API-only** : Service binding operations are currently only available via API. You can find all endpoints and their specifications in the [Cloudflare API documentation](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/). For detailed guidance, refer to the sections and tutorials linked below.

**Time to propagate** : Service bindings take four to six hours to propagate across Cloudflare's global network after being created or deleted. Services for the IP addresses in scope are likely disrupted during this window.

## Scope

Customers using BYOIP with Magic Transit, [CDN services](https://developers.cloudflare.com/cache/), or [Spectrum](https://developers.cloudflare.com/spectrum/) can leverage the [service binding API endpoints](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/) to selectively route traffic through the CDN 1 or Spectrum 2 pipelines on a per-IP address basis. This means:

  * You can upgrade individual IPs within a Magic Transit prefix to either a CDN IP or a Spectrum IP. For example, if you have a Magic Transit prefix `203.0.113.0/24`, you can upgrade `203.0.113.1` to CDN and `203.0.113.2` to Spectrum.
  * You can upgrade individual IPs within a CDN prefix to a Spectrum IP. For example, if you have a CDN prefix `203.0.113.0/24`, you can upgrade `203.0.113.1` to Spectrum.
  * You can upgrade individual IPs within a Spectrum prefix to a CDN IP. For example, if you have a Spectrum prefix `203.0.113.0/24`, you can upgrade `203.0.113.1` to CDN.



Refer to [Magic Transit with CDN](https://developers.cloudflare.com/byoip/service-bindings/magic-transit-with-cdn/) or [CDN and Spectrum](https://developers.cloudflare.com/byoip/service-bindings/cdn-and-spectrum/) for detailed guidance.

Caution

Magic Transit customers must ensure that their contract includes CDN and/or Spectrum according to their needs.

### CDN (Cache)

When a service binding of type `CDN` is applied, once the change has propagated across Cloudflare's global network (four to six hours), any HTTP requests are directed into the CDN pipeline for Layer 7 processing.

### Spectrum

When a service binding of type `Spectrum` is applied, once the change has propagated across Cloudflare's global network (four to six hours), any TCP/HTTP requests are directed into the Spectrum pipeline for Layer 4 or Layer 7 processing.

UDP applications

Spectrum UDP applications are supported with BYOIP, including [CDN and Spectrum service bindings](https://developers.cloudflare.com/byoip/service-bindings/cdn-and-spectrum/). However, they are [not currently supported with Magic Transit service bindings](https://developers.cloudflare.com/spectrum/reference/limitations/#udp).

### Magic Transit

Note

Magic Transit can only be used as default binding, spanning across your entire prefix. You can then add CDN or Spectrum for smaller subnets but not the other way around.

The entire BYOIP prefix is primarily announced for Magic Transit, providing layer 3 DDoS protection and acceleration. Traffic not explicitly bound to CDN will flow through Magic Transit.

Also, traffic egressing to an IP in the prefix will always go to Magic Transit, even if there is an overlapping binding for CDN or Spectrum. This allows customers who want to use the same IP as ingress IP and as origin IP to do so.
    
    
    flowchart LR
            accTitle: Cloudflare as a reverse proxy
            accDescr: Diagram showing Cloudflare's network between clients and the origin server.
            A[Client] --ingress--> B((Cloudflare))--egress--> C[(Origin server)]
    

When adding a service binding for a given IP address, it must be either a CDN service binding or a Spectrum service binding. It is not possible (or necessary) to bind both services.

### CDN egress

[Dedicated CDN Egress IPs](https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/) (formerly known as Aegis) is only available for Enterprise. If you are interested, reach out to your account team. Also note that a single BYOIP prefix can be used for either CDN ingress or CDN egress, but not both.

## Tutorials

  * [Use BYOIP with Magic Transit and CDN](https://developers.cloudflare.com/byoip/service-bindings/magic-transit-with-cdn/)
  * [Use BYOIP with CDN and Spectrum](https://developers.cloudflare.com/byoip/service-bindings/cdn-and-spectrum/)



## Footnotes

  1. Layer 7 HTTP-based ↩

  2. Layer 4 or Layer 7 HTTP with custom ports ↩




[PreviousSetup](https://developers.cloudflare.com/byoip/address-maps/setup/)[NextMagic Transit with CDN](https://developers.cloudflare.com/byoip/service-bindings/magic-transit-with-cdn/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/byoip/service-bindings/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
