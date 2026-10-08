---
url: https://developers.cloudflare.com/changelog/product/cloudflare-wan/
title: Cloudflare WAN Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:43.375031+00:00
---

# Cloudflare WAN Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/cloudflare-wan/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Oct 5, 2026

## [BGP over IPsec and GRE tunnels generally available](https://developers.cloudflare.com/changelog/post/2026-10-05-bgp-over-tunnels-ga/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

BGP peering over IPsec and GRE tunnels is generally available for Cloudflare WAN and Magic Transit. You can use it for production workloads.

BGP peering exchanges routes dynamically between your devices and your Cloudflare virtual network routing table. You no longer need to update static routes manually as your network changes.

BGP over IPsec and GRE tunnels is available to all accounts that use [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing). No enablement is required. BGP over CNI remains in closed beta.

For configuration details, refer to:

  * [Configure BGP routes for Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes)
  * [Configure BGP routes for Magic Transit](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#configure-bgp-routes)



Sep 25, 2026

## [Managed Rulesets supported in Unified Routing](https://developers.cloudflare.com/changelog/post/2026-09-25-unified-routing-managed-rulesets/)

[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

[Cloudflare Advanced Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) Managed Rulesets are now supported for accounts using [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) mode.

For the full list of feature availability, refer to [Check feature availability before upgrading](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#check-feature-availability-before-upgrading).

Sep 18, 2026

## [Unified Routing generally available](https://developers.cloudflare.com/changelog/post/2026-09-18-unified-routing-ga/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Unified Routing is generally available for Cloudflare WAN and Magic Transit.

Unified Routing improves the integration between Cloudflare One and the standard connectivity onramps supported by Cloudflare WAN. It is capable of many new features including Automatic Return Routing, BGP and custom client subnets.

We recommend Unified Routing for all new accounts.

For details, refer to [Cloudflare WAN traffic steering](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) and [Magic Transit traffic steering](https://developers.cloudflare.com/magic-transit/reference/traffic-steering/#unified-routing).

Sep 2, 2026

## [Define custom applications for breakout and prioritized traffic from the Cloudflare One Appliance dashboard](https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-custom-application-traffic-steering/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

You can now define [custom applications](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#create-edit-or-delete-a-custom-application) for [breakout](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/) and [prioritized](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/) traffic on the [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) directly from the dashboard, without calling the API.

![Adding a custom application by hostname, IP subnet, and source subnet from the Traffic Steering tab of an appliance profile](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1034,format=webp/_astro/2026-09-01-appliance-custom-application-traffic-steering.D25Ga9-d.gif)

  * In **Traffic Steering** > **Breakout traffic** or **Prioritized traffic** , select **Assign application traffic** > **Add** to create a custom application matched by **Hostnames** , **IP subnets** , and/or the new **Source subnets** field, alongside Cloudflare-managed applications.
  * Edit or delete an existing custom application from the same panel, no API round-trip required.
  * **Source subnets** lets you match traffic by its source IP range, complementing the existing [source LAN interface breakout criteria](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source).



This complements the existing API and Terraform workflow for managing applications.

For details, refer to [Breakout traffic](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/) and [Prioritized traffic](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/).

Sep 2, 2026

## [Configure DHCP options from the dashboard on Cloudflare One Appliance](https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-dhcp-options-ui/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

You can now configure [custom DHCP options](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/) directly from the dashboard when the [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) is acting as the DHCP server for a LAN.

![Adding a custom DHCP option to a LAN's DHCP server from the Network Configuration tab of an appliance profile](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1034,format=webp/_astro/2026-09-01-appliance-dhcp-options-ui.B5OEZmib.gif)

  * In **LAN configuration** , under **DHCP server options** , select **Add DHCP option** to choose from common options for PXE / iPXE boot, VoIP phone provisioning, and vendor-specific configuration, or select **Add custom option** to enter your own option code, type, and value.
  * This complements the existing [API and Terraform workflow](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/#configure-dhcp-options) for configuring DHCP options.



For details, refer to [DHCP server options](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/).

Sep 2, 2026

## [Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once](https://developers.cloudflare.com/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

You can now create multiple [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) routes from the Routes page in a single action, instead of submitting one route at a time.

![Creating multiple Cloudflare Tunnel and Cloudflare Mesh routes at once from the Routes page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1034,format=webp/_astro/2026-09-01-tunnel-mesh-bulk.zu4fOWN3.gif)

When creating a route, you can now:

  * **Add multiple destinations at once** — Enter a comma-separated list of CIDR ranges or hostnames to create several routes of the same type and connector together.
  * **Queue up multiple routes** — Select **Add another** to stage additional routes, including different types or connectors, before creating them all in one action.
  * **Retry only what failed** — If some routes in a batch fail (for example, an invalid CIDR), the routes that were created successfully are removed from the form automatically, so you only need to fix and resubmit the ones that failed.



The same Routes UI already supports bulk creation for [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) static routes, so you can add multiple WAN destinations or queue up several WAN routes before creating them together as well.

[ Go to **Routes** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/routes)

For setup steps, refer to [Add routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/).

Aug 24, 2026

## [Download the Cloudflare One Virtual Appliance for your hypervisor from the dashboard](https://developers.cloudflare.com/changelog/post/2026-08-24-virtual-appliance-self-serve-download/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

When you register a [Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/), you can now select your hypervisor and download the appliance directly from the dashboard — no need to look up asset URLs.

![Selecting a hypervisor and downloading the Cloudflare One Virtual Appliance from the Connectors page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2813,height=1241,format=webp/_astro/2026-08-24-virtual-appliance-self-serve-download.Ca2YGpCA.png)

  * On the **Connectors** page, select **Add an appliance** , choose **Virtual appliance** , then select your hypervisor: **VMware ESXi** , **Proxmox** , or **libvirt/KVM**.
  * Download the OVA image (VMware ESXi) or the install script (Proxmox and libvirt/KVM) for the selected hypervisor.
  * Use **View setup guide** to open deployment instructions for your platform.



This complements the existing self-serve [registration and license key generation](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key) in the dashboard.

For details, refer to [Configure a Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#configure-a-virtual-machine).

Aug 19, 2026

## [Threat Intel Lists supported in Unified Routing](https://developers.cloudflare.com/changelog/post/2026-08-19-unified-routing-threat-lists/)

[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

[Cloudflare Advanced Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) Threat Intel Lists are now supported for accounts using [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) mode. This feature requires a Cloudflare Advanced Network Firewall subscription.

Support for additional features - Rate Limiting and Managed Rulesets - is planned.

For the full list of current beta limitations, refer to [Traffic steering beta limitations](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#check-feature-availability-before-upgrading).

Jul 17, 2026

## [Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard](https://developers.cloudflare.com/changelog/post/2026-07-17-appliance-restart-reboot-shutdown/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

You can now restart, reboot, or shut down a [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) directly from the dashboard or via API.

![Restarting a Cloudflare One Appliance from the Operations section of the Edit Appliance page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/2026-07-17-appliance-restart-reboot-shutdown.DKqTLOh6.gif)

  * **Restart** — Restart managed services. Purges temporary and (optionally) persistent state.
  * **Reboot** — Power cycle the appliance. Optionally, purge persistent state. Re-applies configuration starting from scratch.
  * **Shutdown** — Power off the appliance. Optionally, purge persistent state. The machine will be offline until manually powered on again.



In the dashboard, go to **Networking** > **Connectors** > **Appliances** , select an appliance, then **Edit** > **Operations** to send an operation. Via API, `POST` to the `/accounts/{account_id}/magic/connectors/{connector_id}/interrupts` endpoint.

For details, refer to [Appliance operations](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/).

Jul 8, 2026

## [IPsec downgrade protection (beta)](https://developers.cloudflare.com/changelog/post/2026-07-08-ipsec-downgrade-protection/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Cloudflare IPsec now supports the [`IKE_SA_INIT_FULL_TRANSCRIPT_AUTH` ↗︎](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-downgrade-prevention/) IKEv2 extension to protect against downgrade attacks on IPsec tunnels.

IKEv2's original authentication design has each endpoint sign only its own outbound messages, not the full handshake transcript. A quantum-capable [on-path attacker ↗︎](https://www.cloudflare.com/learning/security/threats/on-path-attack/) can exploit this to bypass post-quantum key exchange by downgrading the connection to classical cryptography. The `IKE_SA_INIT_FULL_TRANSCRIPT_AUTH` extension addresses this by having both peers sign the entire handshake transcript during the authentication exchange, preventing an attacker from manipulating the negotiation without detection.

Key details:

  * Available in beta for Cloudflare WAN and Magic Transit IPsec tunnels.
  * Cloudflare sends the `IKE_SA_INIT_FULL_TRANSCRIPT_AUTH` notification unconditionally as a responder when the feature flag is enabled.
  * Both the initiator (your device) and responder (Cloudflare) must support the extension for downgrade protection to be effective.
  * This feature is currently gated by a per-account feature flag. Contact your account team to turn it on.



Refer to [Downgrade protection](https://developers.cloudflare.com/cloudflare-wan/reference/gre-ipsec-tunnels/#improved-downgrade-protection-beta) for more details.

Jul 8, 2026

## [IP lists, IDS, and SIP rules supported in Unified Routing](https://developers.cloudflare.com/changelog/post/2026-07-08-unified-routing-iplist-ids-sip/)

[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

[Cloudflare Advanced Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) IP lists, IDS, and SIP rules are now supported for accounts using [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) mode. These features require a Cloudflare Advanced Network Firewall subscription.

Support for additional features - Threat Intel Lists, Rate Limiting, and Managed Rulesets - is planned.

For the full list of current beta limitations, refer to [Traffic steering beta limitations](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#check-feature-availability-before-upgrading).

Jul 6, 2026

## [Self-serve registration of Cloudflare One Virtual Appliance in the dashboard](https://developers.cloudflare.com/changelog/post/2026-07-06-virtual-appliance-self-serve-ui/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

You can now register a [Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) and generate its license key directly from the dashboard, without contacting your account team.

![Registering a Cloudflare One Virtual Appliance and generating its authentication key from the Connectors page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=988,format=webp/_astro/2026-07-06-virtual-appliance-self-serve-ui.Dn2NC_ql.gif)

  * On the **Connectors** page, select **Add an appliance** and choose **Virtual appliance** to register a virtual appliance and generate its authentication key.
  * Use **Regenerate authentication key** from a virtual appliance connector's menu to rotate its key. The previous key is immediately and irrevocably revoked.
  * The authentication key is shown only once — copy and store it securely.



This complements the existing [API and Terraform self-serve workflow](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key) for provisioning virtual appliances. Hardware appliances continue to use the existing account-team fulfillment workflow.

For details, refer to [Configure a Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/).

Jun 19, 2026

## [Manage all your routes from one page in the dashboard](https://developers.cloudflare.com/changelog/post/2026-06-19-unified-routes-page/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

The **Routes** page in the Cloudflare dashboard now shows the routes across all of your connectors — [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) and [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) routes alongside [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) and [Magic Transit](https://developers.cloudflare.com/magic-transit/) static routes — in a single table, instead of a separate routes view per product.

![The unified Routes page in the Cloudflare dashboard, showing routes across connectors in a single table](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/2026-06-19-unified-routes.B3igBY20.gif)

From the unified Routes page you can:

  * **Visualize your network with an interactive map** that shows how your destinations flow through to your connectors — including equal-cost multi-path (ECMP) routes where the same prefix is served by several connectors. Select a node to filter the table down to the routes behind it.
  * **See every route in one table** , with its destination, type, connector, priority, and source, and filter or sort to find what you need.
  * **Create, edit, and delete routes** of any supported type without leaving the page. When adding a Cloudflare WAN or Magic Transit static route, you now pick the next hop by **connector name** instead of typing its IP.
  * **Manage[virtual networks](https://developers.cloudflare.com/cloudflare-one/networks/virtual-networks/)** from a dedicated tab.
  * **Test a route** to see which connector and next hop a destination resolves to before you commit a change.



To find it, go to **Networking** > **Routes** in the dashboard sidebar.

[ Go to **Routes** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/routes)

Your existing routes, APIs, and configurations are unchanged — this is a dashboard experience that brings them together in one place. Learn how to [add routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/) and [manage virtual networks](https://developers.cloudflare.com/cloudflare-one/networks/virtual-networks/).

Jun 2, 2026

## [Cisco IOS XE](https://developers.cloudflare.com/changelog/post/2026-06-02-cisco-ios-xe/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

The Cisco IOS XE third-party integration guide for Cloudflare WAN has been updated to include:

  * Post Quantum Cryptography (PQC)
  * Policy-Based Routing (PBR)
  * IP Service Level Agreement (IP SLA)



This link will take you directly to the updated [Cisco IOS XE](https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/cisco-ios-xe/) guide.

May 18, 2026

## [Network Analytics support for Unified Routing](https://developers.cloudflare.com/changelog/post/2026-05-18-unified-routing-network-analytics/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)

[Network Analytics](https://developers.cloudflare.com/analytics/network-analytics/) is now fully supported for accounts using [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) mode. Traffic that traverses Unified Routing onramps and offramps is now visible in Network Analytics with the same dimensions and filters as traffic on the standard data plane.

This closes a parity gap for customers who had moved tunnels onto Unified Routing and lost visibility into their dataplane traffic in the Network Analytics dashboard. No configuration change is required — analytics data is collected automatically for all accounts with Unified Routing enabled.

For the remaining beta limitations, refer to [Traffic steering beta limitations](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#check-feature-availability-before-upgrading).

May 12, 2026

## [New accounts assigned a single IPv4 anycast address](https://developers.cloudflare.com/changelog/post/2026-05-12-single-anycast-ip-default/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

New Magic Transit and Cloudflare WAN accounts are now assigned a single IPv4 anycast address by default.

Cloudflare handles failures on its network automatically by advertising your endpoint IP from multiple nodes across many globally distributed data centers. To handle failures on your network, configure two tunnels from separate routers.

To request additional anycast IP addresses for your account, contact your account team.

For tunnel configuration guidance, refer to [Configure tunnel endpoints](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/) for Cloudflare WAN or [Configure tunnel endpoints](https://developers.cloudflare.com/magic-transit/how-to/configure-tunnel-endpoints/) for Magic Transit.

May 11, 2026

## [NAT-T support for IKE on UDP port 500](https://developers.cloudflare.com/changelog/post/2026-05-11-nat-t-port-500/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)

Cloudflare IPsec now supports the standard NAT traversal (NAT-T) flow, where IKE begins on UDP port `500` and switches to UDP port `4500` after NAT is detected.

Previously, devices behind NAT had to be configured to initiate IKE on UDP port `4500` directly. Devices that started on UDP port `500` could not complete the IKE handshake when NAT was in the path. This required custom configuration on devices such as VeloCloud SD-WAN edges, Cisco IOS-XE routers, and Juniper SRX firewalls, and was not possible on every platform.

What changed:

  * Devices behind NAT can now initiate IKE on either UDP port `500` or UDP port `4500`.
  * Devices that start IKE on UDP port `500` and switch to UDP port `4500` after NAT detection now complete the handshake successfully.
  * No configuration change is required on Cloudflare. The change is available for all IPsec tunnels on Cloudflare WAN and Magic Transit.



This change does not affect existing tunnels:

  * Tunnels using UDP port `500` with no NAT detected continue to operate as before.
  * Tunnels configured to start IKE on UDP port `4500` continue to operate as before.
  * NAT detection logic is unchanged.



For configuration details, refer to [GRE and IPsec tunnels](https://developers.cloudflare.com/cloudflare-wan/reference/gre-ipsec-tunnels/).

May 7, 2026

## [Custom DHCP options on Cloudflare One Appliance](https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-dhcp-options/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

When the Cloudflare One Appliance is acting as the DHCP server for a LAN, you can now configure custom DHCP options on the leases it issues. This unlocks workflows such as PXE / iPXE boot, VoIP phone provisioning, and vendor-specific client configuration.

Each option is defined by `option_number`, `value`, and one of four value types: `text`, `integer`, `hex`, or `ip`. Configurations are validated on the appliance before being applied — invalid configurations are rejected and the underlying error is returned to the API caller, so a bad option will not disrupt the live DHCP service.

For details, refer to [DHCP server options](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/).

May 7, 2026

## [Source-based breakout and prioritization on Cloudflare One Appliance](https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-source-based-breakout/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Breakout and traffic prioritization rules on the Cloudflare One Appliance can now match by **source** in addition to destination application. You can pin breakout or priority behavior to:

  * A source LAN interface — VLANs attached to that LAN are included automatically.
  * A source IP address, range, or CIDR block.



This is the natural way to break out a guest VLAN to the local Internet, or to prioritize traffic from a specific subnet, without enumerating destination applications.

For details, refer to [Breakout traffic](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source).

May 7, 2026

## [Self-serve provisioning of Cloudflare One Virtual Appliance via API](https://developers.cloudflare.com/changelog/post/2026-05-07-virtual-appliance-self-serve-api/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

You can now create, rotate, and delete Cloudflare One Virtual Appliance instances and their license keys directly via the API and Terraform.

  * Create a virtual appliance and receive a license key: `POST /accounts/{account_id}/magic/connectors` with `device.provision_license: true`.
  * Rotate the license key for an existing virtual appliance: `PATCH /accounts/{account_id}/magic/connectors/{connector_id}` with `provision_license: true`. The previous key is immediately and irrevocably revoked.
  * Delete a virtual appliance to release the associated licensed device.



The license key is returned in the response only once, at create or rotate time. Copy and store it securely.

For details, refer to [Configure a Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/).

Apr 30, 2026

## [Post-quantum IPsec interoperability with third-party devices](https://developers.cloudflare.com/changelog/post/2026-04-30-ipsec-post-quantum-third-party/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Cloudflare IPsec now supports post-quantum key agreement with compatible third-party devices. [Cisco ↗︎](https://www.cisco.com/) and [Fortinet ↗︎](https://www.fortinet.com/) are the first third-party vendors validated to interoperate with Cloudflare IPsec using ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).

Post-quantum IPsec uses [RFC 9370 ↗︎](https://datatracker.ietf.org/doc/rfc9370/) and [draft-ietf-ipsecme-ikev2-mlkem ↗︎](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/) to negotiate hybrid key agreement during the IKEv2 `IKE_INTERMEDIATE` phase. This combines classical Diffie-Hellman (Group 20) with ML-KEM-768 or ML-KEM-1024 to protect against [harvest-now, decrypt-later ↗︎](https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later) attacks.

Key details:

  * Compatible with Cisco 8000 Series Secure Routers with IOS XR Release 26.1.1 and Fortinet FortiOS 7.6.6 and later.
  * Uses ML-KEM-768 or ML-KEM-1024 as an additional Key Exchange to DH Group 20.
  * Follows RFC 9370 and draft-ietf-ipsecme-ikev2-mlkem standards.
  * No additional licensing required.



Post-quantum IPsec with third-party devices is now generally available with confirmed interoperability for the platforms listed above. Cloudflare intends to support interoperability with more vendors as they build out support for draft-ietf-ipsecme-ikev2-mlkem. Contact your account team to discuss support for additional vendors.

For supported key exchange methods and the list of validated platforms, refer to [GRE and IPsec tunnels](https://developers.cloudflare.com/cloudflare-wan/reference/gre-ipsec-tunnels/#tested-third-party-vendor-interoperability).

Apr 21, 2026

## [Country rules supported in Unified Routing](https://developers.cloudflare.com/changelog/post/2026-04-21-unified-routing-geoip-country-rules/)

[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

[Cloudflare Advanced Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) Country rules are now supported for accounts using [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) mode. This feature requires a Cloudflare Advanced Network Firewall subscription.

You can create firewall rules that match traffic based on source or destination country to enforce geographic access policies across your network.

This is the first of the Cloudflare Advanced Network Firewall features to become available in Unified Routing. Support for additional features - IP Lists, ASN Lists, Threat Intel Lists, IDS, Rate Limiting, SIP, and Managed Rulesets - is planned.

For the full list of current beta limitations, refer to [Traffic steering beta limitations](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#check-feature-availability-before-upgrading).

Apr 7, 2026

## [Link aggregation (LACP) support for Cloudflare One Appliance](https://developers.cloudflare.com/changelog/post/2026-04-07-link-aggregation-lacp-appliance/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Cloudflare One Appliance now supports Link Aggregation Control Protocol (LACP), allowing you to bundle up to six physical LAN ports into a single logical interface. Link aggregation increases available bandwidth and eliminates single points of failure on the LAN side of the appliance.

This feature is available in beta on physical appliance hardware with the latest OS. No entitlement is required.

To configure a Link Aggregation Group, refer to [Configure link aggregation groups](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/link-aggregation/).

Feb 17, 2026

## [Cloudflare One Product Name Updates](https://developers.cloudflare.com/changelog/post/2026-02-17-product-name-updates/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)[Network Flow](https://developers.cloudflare.com/network-flow/)

We are updating naming related to some of our Networking products to better clarify their place in the Zero Trust and Secure Access Service Edge (SASE) journey.

We are retiring some older brand names in favor of names that describe exactly what the products do within your network. We are doing this to help customers build better, clearer mental models for comprehensive SASE architecture delivered on Cloudflare.

#### What's changing

  * **Magic WAN** → **Cloudflare WAN**
  * **Magic WAN IPsec** → **Cloudflare IPsec**
  * **Magic WAN GRE** → **Cloudflare GRE**
  * **Magic WAN Connector** → **Cloudflare One Appliance**
  * **Magic Firewall** → **Cloudflare Network Firewall**
  * **Magic Network Monitoring** → **Network Flow**
  * **Magic Cloud Networking** → **Cloudflare One Multi-cloud Networking**



**No action is required by you** — all functionality, existing configurations, and billing will remain exactly the same.

For more information, visit the [Cloudflare One documentation](https://developers.cloudflare.com/cloudflare-one/).

Feb 12, 2026

## [Anycast IPs displayed on the dashboard](https://developers.cloudflare.com/changelog/post/2026-02-12-anycast-ips-on-dashboard/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Cloudflare WAN now displays your Anycast IP addresses directly in the dashboard when you configure IPsec or GRE tunnels.

Previously, customers received their Anycast IPs during onboarding or had to retrieve them with an API call. The dashboard now pre-loads these addresses, reducing setup friction and preventing configuration errors.

No action is required. All Cloudflare WAN customers can see their Anycast IPs in the tunnel configuration form automatically.

For more information, refer to [Configure tunnel endpoints](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/).

← Prev

1[2](https://developers.cloudflare.com/changelog/product/cloudflare-wan/2/)

[Next →](https://developers.cloudflare.com/changelog/product/cloudflare-wan/2/)
