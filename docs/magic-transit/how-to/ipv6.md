---
url: https://developers.cloudflare.com/magic-transit/how-to/ipv6/
title: Configure IPv6 (beta) \u00b7 Cloudflare Magic Transit docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:18.413728+00:00
---

# Configure IPv6 (beta) · Cloudflare Magic Transit docs

> Source: https://developers.cloudflare.com/magic-transit/how-to/ipv6/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Magic Transit](https://developers.cloudflare.com/magic-transit/)
  3. /How to
  4. /Configure IPv6 (beta)



# Configure IPv6 (beta)

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/magic-transit/how-to/ipv6/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCloudflare support for IPv6 in Magic TransitCurrent known limitationsHow to configure IPv6 Example MSS clamping recommendations

IPv6 (beta) for Magic Transit allows customers with existing IPv4 tunnels to enable and test IPv6 functionality with minimal configuration changes. This beta provides an opportunity to evaluate IPv6 addressing, routing, and security within Magic Transit while maintaining the existing IPv4 setup.

As this is a beta release, we encourage customers to contact their account team to enable the feature and provide feedback to help refine the IPv6 functionality before general availability.

## Cloudflare support for IPv6 in Magic Transit

Cloudflare transports IPv6 traffic over an IPv6-over-IPv4 GRE tunnel. Here is how it works:

  1. The IPv6 packet is encapsulated into an IPv4 GRE packet, with the IP protocol field set to `47` (indicating it is a GRE packet) along with a GRE header.
  2. The IPv4 packet header and GRE header are the additional headers (or encapsulation overhead) that ensure the correct routing of the IPv6 traffic.
  3. On most routers that support this tunneling method, the tunnel mode is set to `gre`.

![The IPv4 packet header and GRE header are the additional headers \(or encapsulation overhead\) that ensure the correct routing of the IPv6 traffic.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=572,height=124,format=webp/_astro/ipv6.CBQeelu5.png)

## Current known limitations

  * The IPv6 beta is not available for accounts with CNI (Cloudflare Network Interconnect) links configured.
  * MTU (Maximum Transmission Unit) is 1,420 bytes for egress traffic (does not impact Direct Server Return).
  * Cloudflare Network Firewall supports two matching fields for IPv6 traffic: source IP address and destination IP address.
  * Cloudflare supports the advertisement of IPv6 prefixes ranging from `/48` to `/32`.
  * Limited to IPv4-based [tunnel health checks](https://developers.cloudflare.com/magic-transit/reference/tunnel-health-checks/) only.
  * Supports only IPv4-based endpoint health checks.



## How to configure IPv6

Since IPv6 works over an existing IPv4 tunnel, you need to select either an existing IPv4 GRE tunnel or create a new one to test IPv6. All settings that apply to the IPv4 GRE tunnel apply to the IPv6 tunnel as well, except for any MSS clamping you might need to configure — refer to MSS clamping recommendations in the following section for more information.

To test and set up IPv6 in the Cloudflare dashboard, complete one new field when creating a new IPv4 GRE tunnel or editing an existing one: **IPv6 Interface address**. Enter the Cloudflare-assigned IPv6 address for the Cloudflare side of the tunnel. Each tunnel is assigned a `/127` subnet from your allocated `/96` range. You configure one address on the Cloudflare side and the other address on your router.

Caution

Cloudflare allocates a `/96` IPv6 prefix for each account. The first two addresses in this range are reserved for Cloudflare. The remaining addresses are available for customer GRE tunnels, starting from `:2`, with two IPv6 addresses assigned per tunnel.

To configure IPv6:

  1. Follow the instructions on how to [add a GRE tunnel](https://developers.cloudflare.com/magic-transit/how-to/configure-tunnel-endpoints/#add-tunnels).
  2. In **IPv6 Interface address** , enter the IPv6 address assigned to you for the Cloudflare side of the tunnel. This address is one of the two addresses in the `/127` subnet allocated from your `/96` allocation.
  3. Configure your router with the paired IPv6 address from the same `/127` subnet.



### Example

Your account has been assigned the prefix `2001:db8:abcd:1234::/96`.

In this example, the first two addresses in the range (`::0` and `::1`) are reserved for Cloudflare. You can use any of the remaining addresses in the `/96` block to create `/127` subnets for your tunnels.

If you decide to use the first available `/127` after the reserved addresses (`2001:db8:abcd:1234::2/127`), your configuration would be:

  * **Cloudflare IPv6 Interface address** : `2001:db8:abcd:1234::2`
  * **Router IPv6 address** : `2001:db8:abcd:1234::3`



Continuing with the example, the next `/127` for the second tunnel would be `2001:db8:abcd:1234::4/127`. Thus, your configuration would be:

  * **Cloudflare IPv6 Interface address** : `2001:db8:abcd:1234::4`
  * **Router IPv6 address** : `2001:db8:abcd:1234::5`



After the first two reserved addresses, you can continue allocating `/127` subnets sequentially (or in any order you prefer) for as many tunnels as needed until you reach the end of your `/96` range. Each `/127` contains exactly two IPv6 addresses — one for Cloudflare, one for your router.

### MSS clamping recommendations

If you use Magic Transit ingress-only traffic (DSR), apply a TCP MSS (Maximum Segment Size) clamp with a maximum of 1,416 bytes to your edge router's transit ports to account for the larger IPv6 header.

[PreviousConfigure routes](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/)[NextAdvertise prefixes](https://developers.cloudflare.com/magic-transit/how-to/advertise-prefixes/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/magic-transit/how-to/ipv6.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
