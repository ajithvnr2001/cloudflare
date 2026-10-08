---
url: https://developers.cloudflare.com/network-interconnect/changelog/
title: Changelog \u00b7 Cloudflare Network Interconnect docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:24.388012+00:00
---

# Changelog · Cloudflare Network Interconnect docs

> Source: https://developers.cloudflare.com/network-interconnect/changelog/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Network Interconnect](https://developers.cloudflare.com/network-interconnect/)
  3. /Changelog



# Changelog

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/network-interconnect/changelog/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview2024-10-012024-09-02

[Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/network-interconnect.xml)

## 2026-03-24

  
**Interconnects moved to Connectors**  


The top-level **Interconnects** page in the Cloudflare dashboard has been removed. Interconnects are now located under **Connectors** > **Interconnects**.

Your existing configurations and functionality remain the same.

## 2025-06-20

  
**CNI maintenance alerts**  


Customers using Cloudflare Network Interconnect with the v1 dataplane can now subscribe to maintenance alert emails. These alerts notify you of planned maintenance windows that may affect your CNI circuits.

For more information, refer to [Monitoring and alerts](https://developers.cloudflare.com/network-interconnect/monitoring-and-alerts/).

## 2024-12-17

  
**Establish BGP peering over Direct CNI circuits**  


Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using a Direct CNI on-ramp.

Using BGP peering allows customers to:

  * Automate the process of adding or removing networks and subnets.
  * Take advantage of failure detection and session recovery features.



With this functionality, customers can:

  * Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via CNI.
  * Secure the session by MD5 authentication to prevent misconfigurations.
  * Exchange routes dynamically between their devices and their Magic routing table.



Refer to [Magic WAN BGP peering](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes) or [Magic Transit BGP peering](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#configure-bgp-routes) to learn more about this feature and how to set it up.

## 2024-10-01

**Early access testing for BGP on Direct CNI circuits**

Customers can exchange routes dynamically with their Magic virtual network overlay via Direct CNI or Cloud CNI based connectivity.

## 2024-09-02

**Interconnect portal displays all available locations in a list**

Customers can now see all available Direct CNI locations when searching for a Cloudflare site in the Interconnects interface.

[PreviousOperational guidance](https://developers.cloudflare.com/network-interconnect/operational-guidance/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/network-interconnect/changelog.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
