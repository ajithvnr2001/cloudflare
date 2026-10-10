---
url: https://developers.cloudflare.com/changelog/product/cloudflare-one-appliance/
title: Cloudflare One Appliance Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:10.039162+00:00
---

# Cloudflare One Appliance Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/cloudflare-one-appliance/

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

Apr 7, 2026

## [Link aggregation (LACP) support for Cloudflare One Appliance](https://developers.cloudflare.com/changelog/post/2026-04-07-link-aggregation-lacp-appliance/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Cloudflare One Appliance now supports Link Aggregation Control Protocol (LACP), allowing you to bundle up to six physical LAN ports into a single logical interface. Link aggregation increases available bandwidth and eliminates single points of failure on the LAN side of the appliance.

This feature is available in beta on physical appliance hardware with the latest OS. No entitlement is required.

To configure a Link Aggregation Group, refer to [Configure link aggregation groups](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/link-aggregation/).

Feb 11, 2026

## [Post-quantum encryption support for Cloudflare One Appliance](https://developers.cloudflare.com/changelog/post/2026-02-11-appliance-post-quantum-encryption/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Cloudflare One Appliance version 2026.2.0 adds [post-quantum encryption](https://developers.cloudflare.com/ssl/post-quantum-cryptography/) support using hybrid ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).

The appliance now uses TLS 1.3 with hybrid ML-KEM for its connection to the Cloudflare edge. During the TLS handshake, the appliance and the edge share a symmetric secret over the TLS connection and inject it into the ESP layer of IPsec. This protects IPsec data plane traffic against harvest-now, decrypt-later attacks.

This upgrade deploys automatically to all appliances during their configured interrupt windows with no manual action required.

For more information, refer to [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/).

Dec 31, 2025

## [Breakout traffic visibility via NetFlow](https://developers.cloudflare.com/changelog/post/2025-12-31-connector-breakout-traffic-netflow/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Magic WAN Connector now exports NetFlow data for breakout traffic to Magic Network Monitoring (MNM), providing visibility into traffic that bypasses Cloudflare's security filtering.

This feature allows you to:

  * Monitor breakout traffic statistics in the Cloudflare dashboard.
  * View traffic patterns for applications configured to bypass Cloudflare.
  * Maintain visibility across all traffic passing through your Magic WAN Connector.



For more information, refer to [NetFlow statistics](https://developers.cloudflare.com/cloudflare-wan/analytics/netflow-analytics/).

Nov 6, 2025

## [Designate WAN link for breakout traffic](https://developers.cloudflare.com/changelog/post/2025-11-06-connector-designate-wan-link-breakout/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Magic WAN Connector now allows you to designate a specific WAN port for breakout traffic, giving you deterministic control over the egress path for latency-sensitive applications.

With this feature, you can:

  * Pin breakout traffic for specific applications to a preferred WAN port.
  * Ensure critical traffic (such as Zoom or Teams) always uses your fastest or most reliable connection.
  * Benefit from automatic failover to standard WAN port priority if the preferred port goes down.



This is useful for organizations with multiple ISP uplinks who need predictable egress behavior for performance-sensitive traffic.

For configuration details, refer to [Designate WAN ports for breakout apps](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#designate-wan-ports-for-breakout-apps).

Jul 21, 2025

## [Virtual Cloudflare One Appliance with KVM support (open beta)](https://developers.cloudflare.com/changelog/post/2025-07-21-virtual-appliance-kvm-proxmox/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

The KVM-based virtual Cloudflare One Appliance is now in open beta with official support for Proxmox VE.

Customers can deploy the virtual appliance on KVM hypervisors to connect branch or data center networks to Cloudflare WAN without dedicated hardware.

For setup instructions, refer to [Configure a virtual Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/).

Apr 30, 2025

## [Cloudflare One Appliance supports multiple DNS server IPs](https://developers.cloudflare.com/changelog/post/2025-04-30-appliance-multiple-dns-servers/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Cloudflare One Appliance DHCP server settings now support specifying multiple DNS server IP addresses in the DHCP pool.

Previously, customers could only configure a single DNS server per DHCP pool. With this update, you can specify multiple DNS servers to provide redundancy for clients at branch locations.

For configuration details, refer to [DHCP server](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/).

Feb 14, 2025

## [Configure your Magic WAN Connector to connect via static IP assignment](https://developers.cloudflare.com/changelog/post/2025-02-14-local-console-access/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

You can now locally configure your [Magic WAN Connector](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) to work in a static IP configuration.

This local method does not require having access to a DHCP Internet connection. However, it does require being comfortable with using tools to access the serial port on Magic WAN Connector as well as using a serial terminal client to access the Connector's environment.

For more details, refer to [WAN with a static IP address](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#bootstrap-via-serial-console).
