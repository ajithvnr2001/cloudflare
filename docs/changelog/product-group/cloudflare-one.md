---
url: https://developers.cloudflare.com/changelog/product-group/cloudflare-one/
title: Cloudflare One Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:26.253584+00:00
---

# Cloudflare One Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product-group/cloudflare-one/

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

Oct 7, 2026

## [Cloudflare One Client for macOS (version 2026.8.2100.0)](https://developers.cloudflare.com/changelog/post/2026-10-07-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release includes the following highlights:

  * Traffic to split tunnel excluded resources is no longer briefly blocked while the client is connecting or reconnecting. The client now keeps its learned split tunnel configuration across reconnects.
  * Support for routing non-RFC 1918 local IPv4 networks through the tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Faster connects and lower memory use. The hosts file is now read once and shared across the client’s DNS resolvers instead of being reloaded by each one.



**Additional changes and improvements**

  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Individual DNS-over-HTTPS queries now time out instead of hanging when the upstream server stops responding.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Added an MDM setting to prefer IPv4 when resolving hostnames in proxy mode. The setting is off by default.
  * Fixed the client reconnecting while Emergency Disconnect was active after switching organizations or re-registering.
  * Fixed the client being unable to connect after an upgrade when its stored registration credentials no longer matched its configuration.
  * Fixed the client service restarting unexpectedly when it was slow to respond, such as after waking from sleep.
  * Fixed Extra Logging failing to capture packets across all interfaces.
  * Fixed an issue that could prevent remote diagnostics from completing.
  * Fixed DNS connectivity checks failing on IPv6-only networks.
  * Fixed the client service exiting when its route-monitoring socket was closed after sleep or wake.
  * Fixed DNS enforcement checks making the client service unresponsive on systems with large routing tables.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report “No network” after a successful manual disconnect.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



Oct 7, 2026

## [Cloudflare One Client for Windows (version 2026.8.2100.0)](https://developers.cloudflare.com/changelog/post/2026-10-07-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release includes the following highlights:

  * Traffic to split tunnel excluded resources is no longer briefly blocked while the client is connecting or reconnecting. The client now keeps its learned split tunnel configuration across tunnel reconnections.
  * Support for routing non-RFC 1918 local IPv4 networks through the tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved connection reliability on devices with very large hosts files. The client now detects a large hosts file, allows more time for its initial DNS check, and shows a banner letting the user know that connecting may take longer.
  * Faster tunnel reconnections and lower memory use. The hosts file is now read once and shared across the client’s DNS resolvers instead of being reloaded by each one.
  * A service recovery mechanism, backed by a Windows scheduled task, now starts the client service on system unlock if it is not already running. This is enabled by default.



**Additional changes and improvements**

  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Individual DNS-over-HTTPS queries now time out instead of hanging when the upstream server stops responding.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Added an MDM setting to prefer IPv4 when resolving hostnames in proxy mode. The setting is off by default.
  * The client no longer requires the Windows WLAN AutoConfig service to be running.
  * Fixed the client reconnecting while Emergency Disconnect was active after switching organizations or re-registering.
  * Fixed the client being unable to connect after an upgrade when its stored registration credentials no longer matched its configuration.
  * Fixed the client service restarting unexpectedly when it was slow to respond, such as after waking from sleep.
  * Fixed the client service failing to restart after an unexpected termination.
  * Fixed the client UI getting stuck in a connecting state after sleep and wake even though the tunnel was connected.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report “No network” after a successful manual disconnect.
  * Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation.
  * Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
  * Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
  * Fixed the client UI crashing at startup when it could not write to the Windows registry.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * A Windows DNS client regression may cause connectivity check failures on systems containing large hosts files. While this release includes a fix to mitigate this issue, users may still experience reduced DNS performance and connectivity check failures.



Oct 7, 2026

## [Cloudflare One Client for Linux (version 2026.8.2100.0)](https://developers.cloudflare.com/changelog/post/2026-10-07-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release includes the following highlights:

  * Traffic to split tunnel excluded resources is no longer briefly blocked while the client is connecting or reconnecting. The client now keeps its learned split tunnel configuration across reconnects.
  * Support for routing non-RFC 1918 local IPv4 networks through the tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Faster tunnel reconnections and lower memory use. The hosts file is now read once and shared across the client’s DNS resolvers instead of being reloaded by each one.
  * Added an MDM setting to prefer IPv4 when resolving hostnames in proxy mode. The setting is off by default.



**Additional changes and improvements**

  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Individual DNS-over-HTTPS queries now time out instead of hanging when the upstream server stops responding.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Fixed the client reconnecting while Emergency Disconnect was active after switching organizations or re-registering.
  * Fixed the client being unable to connect after an upgrade when its stored registration credentials no longer matched its configuration.
  * Fixed the client service restarting unexpectedly when it was slow to respond, such as after waking from sleep.
  * Fixed the client window not appearing on first launch after a fresh install on RHEL 10.
  * Fixed duplicate WARP routing policy rules accumulating on reconnect.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report “No network” after a successful manual disconnect.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * When in DNS Only mode, the client may send DNS queries for names that are configured for Local Domain Fallback to the encrypted DNS server instead of falling back to the system configuration. Local Domain Fallback works as expected in other client modes.



Oct 7, 2026

## [Cloudflare Organizations is generally available](https://developers.cloudflare.com/changelog/post/2026-10-07-organizations-generally-available/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

Cloudflare Organizations is now generally available for Enterprise customers and MSSP/Distributor partners.

Organizations provides a top-level container for centrally managing accounts, members, analytics, and shared policies. Organization Super Administrators receive implicit access to every account in their Organization without requiring separate account memberships.

Enterprise customers can manage accounts in a single-tier Organization. MSSP/Distributor partners can use nested sub-organizations to manage customer accounts.

Organization Roles remains in beta, and current product limitations still apply.

For more information, refer to [Cloudflare Organizations](https://developers.cloudflare.com/fundamentals/organizations/) and [current limitations](https://developers.cloudflare.com/fundamentals/organizations/limitations/).

Oct 5, 2026

## [Detect organization-specific risks with CASB custom finding types](https://developers.cloudflare.com/changelog/post/2026-10-05-casb-custom-findings/)

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

[Cloudflare CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) now supports [**custom finding types**](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/custom-finding-types/), giving security teams full control over the security conditions CASB detects across their SaaS and cloud integrations.

In addition to CASB's library of standard finding types, you can now write your own detection logic using [Rego ↗︎](https://www.openpolicyagent.org/docs/policy-language), the open-source policy language from Open Policy Agent (OPA). Use custom finding types to match your organization's own thresholds and exceptions, such as flagging admin accounts without two-factor authentication, and get higher-confidence findings to act on.

![Create a custom finding type with a name, severity, scope, and Rego detection logic](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1194,height=1194,format=webp/_astro/create-custom-finding-type.CF3GXoPZ.png)

#### Key capabilities

  * **Write your own detection logic** — Define exactly what CASB flags using Rego expressions evaluated against asset data from your connected integrations.
  * **Target any supported provider and asset class** — Scope a custom finding type to a provider (such as Google Workspace or Microsoft 365) and asset class (such as users, files, or groups), and apply it to all integrations for that provider or a selected subset.
  * **Built-in validation** — Select **Validate** to check your expression for syntax errors and schema issues before you create the finding type.
  * **Inspect and duplicate standard finding types** — Open any standard finding type to view its detection logic, then duplicate it as the starting point for a custom finding type.
  * **Works with CASB policies** — Use custom finding types in [CASB remediation policies](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/) to send matching findings to Slack, ServiceNow, or any other webhook destination.



#### Get started

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com), go to **Cloud & SaaS findings** > **Findings library**.
  2. Select **Create finding**.
  3. Enter a name, description, and severity.
  4. Select a provider and asset class, then set the integration scope.
  5. Write your Rego expression and select **Validate**.
  6. Select **Create finding**.



CASB evaluates the custom finding type against assets as they are created or updated within the selected scope. Matching assets appear as posture finding instances under **Posture Findings**.

#### Learn more

  * Learn how to [create and manage custom finding types](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/custom-finding-types/) in Cloudflare One.
  * Learn how to [manage findings](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/) in Cloudflare One.
  * Learn how to [create and manage CASB remediation policies](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/) in Cloudflare One.



CASB custom finding types are now available in Cloudflare One.

Oct 5, 2026

## [BGP over IPsec and GRE tunnels generally available](https://developers.cloudflare.com/changelog/post/2026-10-05-bgp-over-tunnels-ga/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

BGP peering over IPsec and GRE tunnels is generally available for Cloudflare WAN and Magic Transit. You can use it for production workloads.

BGP peering exchanges routes dynamically between your devices and your Cloudflare virtual network routing table. You no longer need to update static routes manually as your network changes.

BGP over IPsec and GRE tunnels is available to all accounts that use [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing). No enablement is required. BGP over CNI remains in closed beta.

For configuration details, refer to:

  * [Configure BGP routes for Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes)
  * [Configure BGP routes for Magic Transit](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#configure-bgp-routes)



Oct 2, 2026

## [New strict service token authentication setting for Access](https://developers.cloudflare.com/changelog/post/2026-10-02-strict-service-token-authentication/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

The strict service token authentication setting applies consistent behavior to requests made with service tokens. When the setting is on for a Zero Trust organization, Access handles requests with service token headers as follows:

  * If authentication or authorization fails, Access always returns `401` or `403` instead of redirecting the client to the login page with `302`.
  * Only Service Auth policies can authorize the request. Access ignores Allow policies and any `CF_Authorization` cookie sent with the request.
  * Access does not return a `CF_Authorization` cookie to the client after successful authentication. Subsequent requests should continue to use service token headers.
  * Failed requests for recognized service tokens appear in [Access authentication logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/#non-identity-authentication).



Zero Trust organizations created on or after October 5, 2026 have strict service token authentication turned on by default and cannot turn it off. Cloudflare recommends that existing organizations turn it on as well.

Organizations created before October 5, 2026 can configure the setting in the dashboard or through the API.

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Access settings**.

[ Go to **Access settings** ↗ ](https://one.dash.cloudflare.com/?to=/:account/access-controls/settings)
  2. Under **Manage service tokens** , turn on **Strict service token authentication**.

  3. In the confirmation dialog, select **Enable**.




To turn off strict service token authentication, turn off the setting and select **Disable**.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/access/organizations" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"strict_service_token_auth": true
    	}'

To turn off strict service token authentication, set `strict_service_token_auth` to `false`.

For behavior and configuration details, refer to [Strict service token authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#strict-service-token-authentication).

Oct 1, 2026

## [Simplified permissions for tagging targets with Access for Infrastructure](https://developers.cloudflare.com/changelog/post/2026-10-01-infrastructure-target-tag-permissions/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

You can now tag [targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#tag-targets) using only the `Zero Trust Write` API token permission. Previously, tagging targets through the API required both `Zero Trust Write` and `Tag Write` permissions on the API token.

This change applies to inline target tagging through the [Infrastructure Access Targets API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/). Tagging resources through the general [Resource Tagging API](https://developers.cloudflare.com/resource-tagging/) still requires the `Tag Admin`, `Tag Write`, or equivalent role.

For more information, refer to [Tag targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#tag-targets).

Sep 30, 2026

## [Cloudflare One Client for Windows (version 2026.8.2033.1)](https://developers.cloudflare.com/changelog/post/2026-09-30-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * The client no longer requires the Windows WLAN AutoConfig service to be running.
  * Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report 'No network' after a successful manual disconnect.
  * Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.
  * Fixed the client UI crashing at startup when it could not write to the Windows registry.
  * Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
  * Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



For Zero Trust documentation, see: <https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/> For Consumer documentation, see: <https://developers.cloudflare.com/warp-client/>

Sep 30, 2026

## [Role-based access control for Browser Isolation policies](https://developers.cloudflare.com/changelog/post/2026-09-30-browser-isolation-rbac/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Isolation policies](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/) support role-based access control (RBAC). Because isolation policies are Gateway HTTP policies with the _Isolate_ action, Gateway's account-level and resource-scoped roles apply to them directly.

Use the `Zero Trust HTTP Policies Admin` account-level role to grant access to all HTTP policies in the account. You can also assign a [resource-scoped role](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/) to let a team member manage a specific isolation policy without exposing other Gateway resources.

[Policy settings](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/#policy-settings) such as copy/paste, file download/upload, keyboard, and printing are part of the policy object and follow the same permissions.

For setup instructions, refer to [Granular permissions for Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/).

Sep 29, 2026

## [Cloudflare One Client for Windows (version 2026.8.2028.1)](https://developers.cloudflare.com/changelog/post/2026-09-29-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * The client no longer requires the Windows WLAN AutoConfig service to be running.
  * Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report 'No network' after a successful manual disconnect.
  * Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.
  * Fixed the client UI crashing at startup when it could not write to the Windows registry.
  * Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
  * Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



Sep 29, 2026

## [Cloudflare One Client for macOS (version 2026.8.2028.1)](https://developers.cloudflare.com/changelog/post/2026-09-29-warp-macos-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the macOS Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Fixed Extra Logging failing to capture packets across all interfaces.
  * Fixed an issue that could prevent remote diagnostics from completing.
  * Fixed DNS connectivity checks failing on IPv6-only networks.
  * Fixed the client service exiting when its route-monitoring socket was closed after sleep or wake.
  * Fixed DNS enforcement checks making the client service unresponsive on systems with large routing tables.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report 'No network' after a successful manual disconnect.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



Sep 29, 2026

## [Identify Mesh, Workers VPC, and Cloudflare Tunnel replicas in network logs](https://developers.cloudflare.com/changelog/post/2026-09-29-mesh-workers-vpc-network-logs/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

You can now tell a person on a laptop apart from a Mesh node or an AI agent running on Workers, without matching on connector email addresses or Mesh IP ranges — and see exactly which Cloudflare Tunnel and `cloudflared` replica received each session.

[Gateway network logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#network-logs) and [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/) now identify two new kinds of traffic:

  * **Mesh** — Traffic sent from or delivered to a [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) node. Previously, Mesh nodes were logged the same way as devices running the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/), because Mesh nodes run the client in headless mode.
  * **Workers VPC** — Traffic sent by a Worker through a [Workers VPC](https://developers.cloudflare.com/workers-vpc/) binding. Previously, Workers VPC sessions were not recorded in Network Session Logs.

![Viewing Mesh and Workers VPC traffic in Gateway network logs](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1439,height=796,format=webp/_astro/2026-09-28-mesh-workers-vpc-network-logs.iGvLKYk7.gif)

#### Gateway network logs

To view these values in the dashboard, go to **Zero Trust** > **Insights & Logs** > **Logs** > **Network logs** , select **Columns** , and turn on **Traffic Source** and **Traffic Destination**. Both values also appear under **Network query details** when you open a log entry.

#### Network Session Logs

The `zero_trust_network_sessions` dataset, available through [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/), includes the following fields:

Field | Description  
---|---  
`OnrampType` | How the session entered Cloudflare One. Values: `CF1_CLIENT`, `MESH`, `WORKERS_VPC`, `MAGIC`, `OTHER`.  
`Offramp` | Where the session was routed. Sessions routed to a Mesh node report `MESH`.  
`SourceName` | Name of the Worker that started the session. Only populated for Workers VPC sessions.  
`SourceID` | Stable identifier of the Worker that started the session. Only populated for Workers VPC sessions.  
`DestinationReplicaID` | The replica that served the session, such as a specific replica of a Mesh node or a `cloudflared` replica of a Cloudflare Tunnel.  
  
For example, `OnrampType = 'WORKERS_VPC' AND Offramp = 'MESH'` returns every session where a Worker reached a service behind a Mesh node, and `SourceName` tells you which Worker it was.

Redeploy your Workers

`SourceName` and `SourceID` are only populated for Workers deployed after 29 September 2026. To include them for an existing Worker, redeploy it — for example, with `npx wrangler deploy`. No code changes are required.

#### See which tunnel and replica received a session

With `DestinationReplicaID`, you can now confirm which [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and which `cloudflared` replica received traffic for a specific session. Combine it with the existing `DestinationTunnelID` field to trace a session to an exact tunnel replica — or Mesh node replica — when you run multiple replicas for high availability. The replica ID matches the **Connector ID** shown in the dashboard, so you can [stream that replica's logs](https://developers.cloudflare.com/tunnel/observability/#remote-log-streaming) with `cloudflared tail --connector-id`.

Sessions logged before this change are not backfilled. For all available fields, refer to [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/).

Sep 25, 2026

## [Managed Rulesets supported in Unified Routing](https://developers.cloudflare.com/changelog/post/2026-09-25-unified-routing-managed-rulesets/)

[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

[Cloudflare Advanced Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) Managed Rulesets are now supported for accounts using [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) mode.

For the full list of feature availability, refer to [Check feature availability before upgrading](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#check-feature-availability-before-upgrading).

Sep 24, 2026

## [MCP server portals are now generally available](https://developers.cloudflare.com/changelog/post/2026-09-24-mcp-portals-ga/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) are now generally available to all Cloudflare customers. A portal gives users one endpoint for approved Model Context Protocol (MCP) servers. Cloudflare Access logs tool, prompt, and resource activity.

Since the open beta, MCP server portals have added:

  * [Gateway routing](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#route-portal-traffic-through-gateway) for HTTP logging and data loss prevention (DLP) scanning
  * [Code Mode policies](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode-policies) that control how portals reduce tool definitions and token use
  * [Static OAuth client credentials](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#configure-manual-oauth-credentials) for providers that do not support Dynamic Client Registration
  * [Session management](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#manage-portal-sessions) for reconnecting servers and changing authorizations from the portal
  * [Service token authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-with-a-service-token) for autonomous agents and machine-to-machine access
  * [Logpush support](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/) for exporting portal activity to external storage or a security information and event management (SIEM) system



To create a portal and connect an MCP client, refer to [MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/).

Sep 23, 2026

## [Traffic Destination selector in Gateway policies](https://developers.cloudflare.com/changelog/post/2026-09-23-traffic-destination-selector/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Gateway [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) policies now include a **Traffic Destination** selector that identifies how traffic exits Cloudflare. This allows administrators to write policies that target specific off-ramp methods - for example, applying different rules to traffic destined for the public Internet compared to traffic routed through Cloudflare Tunnel or Cloudflare WAN.

#### Available traffic destination values

UI name | API value | Description  
---|---|---  
Internet | `internet` | Traffic to the public Internet  
Cloudflare WAN | `cloudflare_wan` | Traffic through a [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/) connection  
Cloudflare Tunnel | `cloudflare_tunnel` | Traffic to a private origin through [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)  
Cloudflare One Client | `device_client` | Traffic to another device running the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)  
Mesh | `mesh` | Traffic through a [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) node  
  
The selector uses the `net.offramp.type` API field in both HTTP and Network policies.

UI name | API example  
---|---  
Traffic Destination | `net.offramp.type == "internet"`  
  
For more information, refer to [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/).

Sep 23, 2026

## [Add Mesh participants with guided onboarding](https://developers.cloudflare.com/changelog/post/2026-09-23-mesh-participant-onboarding/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) now makes it faster to add and manage participants from the dashboard. Select **Add participant** from **Networking** > **Mesh** to deploy a [Mesh node](https://developers.cloudflare.com/mesh/get-started/) or find the information needed to connect a [client device](https://developers.cloudflare.com/mesh/guides/connect-client-devices/).

![Adding a Cloudflare Mesh node through the guided dashboard workflow](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=680,format=webp/_astro/guided-participant-onboarding-clicks.B0r-5ElX.gif)

The updated dashboard includes the following improvements:

  * **More Mesh node deployment options** — Install a node on Linux, Kubernetes, Docker Compose, or Docker CLI. The dashboard provides requirements, commands, configuration, and links for each method. Refer to [Run Mesh in Docker / Kubernetes](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/) for container deployment details.
  * **Client device installation guidance** — Access platform-specific [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) installers, mobile QR codes, and your Cloudflare One organization name. Use the organization name to log in from the client after installation.
  * **Unified participant management** — View [Mesh nodes and enrolled client devices](https://developers.cloudflare.com/mesh/guides/connect-client-devices/#1-enroll-the-cloudflare-one-client) in one table. Search devices, filter participants by type or status, open device details, and load additional results from each participant source. If one source fails, participants from the other source remain available while you retry the request.



You must still install the Cloudflare One Client, log in to your organization, and test the connection.

For complete setup instructions, refer to [Get started with Cloudflare Mesh](https://developers.cloudflare.com/mesh/get-started/).

Sep 22, 2026

## [Automatically manage inactive Access service tokens](https://developers.cloudflare.com/changelog/post/2026-09-22-service-token-inactivity-cleanup/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access administrators can now automatically disable or delete inactive service tokens. Administrators can set an inactivity period from 30 to 365 days and choose what Access does when a token reaches that limit.

To be eligible for cleanup, a token must be older than the configured period, must not have successfully authenticated during that period, and must not be directly referenced by an Access policy rule. Cleanup runs gradually in the background, so eligible tokens may not be disabled or deleted immediately.

For configuration instructions, refer to [Manage inactive service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#manage-inactive-service-tokens).

Sep 22, 2026

## [Private MCP server support for MCP server portals](https://developers.cloudflare.com/changelog/post/2026-09-22-private-mcp-servers/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) can now connect to MCP servers available only on your private network. The portal uses [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) to reach [private hostnames](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) and IP addresses without exposing the MCP server to the public Internet.

Connect the server network to Cloudflare with [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/), [Cloudflare Mesh](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/), or another [Cloudflare One connector](https://developers.cloudflare.com/cloudflare-one/networks/connectors/). Configure a private hostname or CIDR route, then turn on **Route traffic through Cloudflare Gateway** when you add the server. OAuth authorization server endpoints, such as the authorization and token endpoints, must be accessible on the public Internet. If Cloudflare automatically registers the OAuth client through Dynamic Client Registration (DCR), the registration endpoint must also be accessible on the public Internet.

For setup instructions, refer to [Connect a private MCP server](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-a-private-mcp-server).

Sep 21, 2026

## [Cloudflare One Client for macOS (version 2026.8.1755.1)](https://developers.cloudflare.com/changelog/post/2026-09-21-warp-macos-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the macOS Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Fixed Extra Logging failing to capture packets across all interfaces.
  * Fixed an issue that could prevent remote diagnostics from completing.
  * Fixed DNS connectivity checks failing on IPv6-only networks.
  * Fixed the client service exiting when its route-monitoring socket was closed after sleep or wake.
  * Fixed DNS enforcement checks making the client service unresponsive on systems with large routing tables.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report 'No network' after a successful manual disconnect.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



Sep 21, 2026

## [Cloudflare One Client for Windows (version 2026.8.1755.1)](https://developers.cloudflare.com/changelog/post/2026-09-21-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * The client no longer requires the Windows WLAN AutoConfig service to be running.
  * Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report 'No network' after a successful manual disconnect.
  * Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.
  * Fixed the client UI crashing at startup when it could not write to the Windows registry.
  * Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
  * Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



Sep 18, 2026

## [Unified Routing generally available](https://developers.cloudflare.com/changelog/post/2026-09-18-unified-routing-ga/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Unified Routing is generally available for Cloudflare WAN and Magic Transit.

Unified Routing improves the integration between Cloudflare One and the standard connectivity onramps supported by Cloudflare WAN. It is capable of many new features including Automatic Return Routing, BGP and custom client subnets.

We recommend Unified Routing for all new accounts.

For details, refer to [Cloudflare WAN traffic steering](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) and [Magic Transit traffic steering](https://developers.cloudflare.com/magic-transit/reference/traffic-steering/#unified-routing).

Sep 18, 2026

## [cloudflared to deprecate 32-bit Windows and Intel-based macOS builds in 2027](https://developers.cloudflare.com/changelog/post/2026-09-18-cloudflared-architecture-deprecation/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Starting in 2027, Cloudflare will deprecate 32-bit Windows and Intel-based macOS builds of `cloudflared`. After the deprecation takes effect, Cloudflare will no longer publish new `cloudflared` releases for either architecture.

Windows 10, the last Windows release to support 32-bit systems, reached end of support in October 2025. Apple has also deprecated Intel-based Mac computers. macOS 26 Tahoe, released in September 2025, was the final macOS release to support Intel-based Macs. macOS 27, released in September 2026, no longer supports them.

Focusing development on currently supported architectures allows `cloudflared` to align with operating system support and continue receiving updates on supported platforms. For available downloads and supported platforms, refer to the [Cloudflare Tunnel downloads](https://developers.cloudflare.com/tunnel/downloads/) documentation.

Sep 15, 2026

## [Access for Infrastructure now supports tagged targets and tag-based target criteria](https://developers.cloudflare.com/changelog/post/2026-09-15-infrastructure-target-tags/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) now integrates with [Resource Tagging](https://developers.cloudflare.com/resource-tagging/). You can attach key-value tags to [infrastructure targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target) and use them in access policies.

You can manage tags on targets inline when you create or edit a target or through the central [Resource Tagging API](https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/). Cloudflare keeps tags in sync across both methods.

Infrastructure applications also support a target criteria model with `include`, `require`, and `exclude` operators. Each operator can match targets by hostname, tag, or both.

  * **Include** matches targets that have any of the specified values.
  * **Require** matches targets that have all of the specified values.
  * **Exclude** rejects targets that have any of the specified values.

![Infrastructure application builder showing target criteria with an included tag, port 22, and SSH as the selected protocol](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2372,height=1616,format=webp/_astro/tags-in-infra-app.ja2Tp-Gq.png)

For more information, refer to [Add an infrastructure application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/).

Sep 14, 2026

## [Require fresh authentication for SAML identity providers](https://developers.cloudflare.com/changelog/post/2026-09-14-saml-force-authentication/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access can now request fresh authentication from a SAML identity provider for every login. Turn on **Require reauthentication** in the Cloudflare dashboard, or set `force_authn` to `true` through the API. Access will then set `ForceAuthn` to `true` in signed and unsigned SAML authentication requests.

This option is useful when an application requires users to reauthenticate at the identity provider instead of relying on an existing identity provider session. The default value is `false`.

For configuration details, refer to [Require fresh authentication at the identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/#require-fresh-authentication-at-the-identity-provider).

← Prev

1[2](https://developers.cloudflare.com/changelog/product-group/cloudflare-one/2/)…[14](https://developers.cloudflare.com/changelog/product-group/cloudflare-one/14/)

[Next →](https://developers.cloudflare.com/changelog/product-group/cloudflare-one/2/)
