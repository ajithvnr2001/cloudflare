---
url: https://developers.cloudflare.com/changelog/product/gateway/
title: Gateway Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:07.515821+00:00
---

# Gateway Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/gateway/

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

## [Cloudflare Organizations is generally available](https://developers.cloudflare.com/changelog/post/2026-10-07-organizations-generally-available/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

Cloudflare Organizations is now generally available for Enterprise customers and MSSP/Distributor partners.

Organizations provides a top-level container for centrally managing accounts, members, analytics, and shared policies. Organization Super Administrators receive implicit access to every account in their Organization without requiring separate account memberships.

Enterprise customers can manage accounts in a single-tier Organization. MSSP/Distributor partners can use nested sub-organizations to manage customer accounts.

Organization Roles remains in beta, and current product limitations still apply.

For more information, refer to [Cloudflare Organizations](https://developers.cloudflare.com/fundamentals/organizations/) and [current limitations](https://developers.cloudflare.com/fundamentals/organizations/limitations/).

Sep 30, 2026

## [Role-based access control for Browser Isolation policies](https://developers.cloudflare.com/changelog/post/2026-09-30-browser-isolation-rbac/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Isolation policies](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/) support role-based access control (RBAC). Because isolation policies are Gateway HTTP policies with the _Isolate_ action, Gateway's account-level and resource-scoped roles apply to them directly.

Use the `Zero Trust HTTP Policies Admin` account-level role to grant access to all HTTP policies in the account. You can also assign a [resource-scoped role](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/) to let a team member manage a specific isolation policy without exposing other Gateway resources.

[Policy settings](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/#policy-settings) such as copy/paste, file download/upload, keyboard, and printing are part of the policy object and follow the same permissions.

For setup instructions, refer to [Granular permissions for Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/).

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

Aug 13, 2026

## [Detect and control software package downloads with package registry security](https://developers.cloudflare.com/changelog/post/2026-08-13-package-protection/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Cloudflare Gateway can now detect software package downloads and give you policy control over supply chain traffic. When a developer or CI/CD pipeline downloads a package through Gateway, the proxy identifies the registry protocol from the request URL and extracts the package ecosystem, name, version, and namespace. You can then write [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) using `pkg.*` selectors to allow or block package downloads.

#### Supported ecosystems

Gateway detects package downloads for the following ecosystems:

Ecosystem | Namespace  
---|---  
npm | Scope (for example, `@babel`)  
PyPI | \--  
RubyGems | \--  
Cargo | \--  
Go | Module path  
Maven | Group ID  
NuGet | \--  
  
#### Selectors

In the dashboard, select **Package Ecosystem** to access the package registry selectors. After selecting a single ecosystem, nested fields for package name, version, and namespace become available. Five `pkg.*` selectors are available for HTTP policies with the Allow and Block actions:

Selector | Description  
---|---  
`pkg.ecosystem` | The package ecosystem detected from the request URL.  
`pkg.name` | The package name extracted from the download URL.  
`pkg.version` | The package version, with support for ecosystem-aware comparison operators.  
`pkg.namespace` | The package namespace, when the ecosystem supports one.  
`pkg.purl` | The [Package URL (PURL) ↗︎](https://github.com/package-url/purl-spec) derived from the detected coordinates. Available in the API only.  
  
Detection is based on the registry protocol rather than the hostname, so it works the same way whether traffic goes to a public registry, a corporate proxy such as Artifactory or Nexus, or a self-hosted mirror.

Package registry security requires [TLS decryption](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tls-decryption/) to be turned on.

For more information, refer to [Package registry security](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/package-registry-security/).

Aug 12, 2026

## [MCP protocol detection and AI Security dashboard](https://developers.cloudflare.com/changelog/post/2026-08-12-mcp-detection-and-dashboard/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Cloudflare Gateway now automatically detects [Model Context Protocol (MCP) ↗︎](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/) traffic flowing through your network. MCP is the standard protocol used by AI agents to connect to external tools and data sources. Gateway identifies MCP requests by inspecting protocol-specific headers and payload characteristics.

#### MCP policy selector

A new **Is MCP** selector (`experimental.is_mcp`) is available in [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#is-mcp). Use this selector to build Gateway rules that allow, block, or isolate MCP traffic.

This selector is currently in beta and may change before general availability.

For example, the following policy blocks MCP traffic that does not arrive through an approved [MCP portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/):

Selector | Operator | Value | Logic | Action  
---|---|---|---|---  
Is MCP | is | _True_ | And | Block  
Traffic Source | is not | _MCP portal_ |  |   
  
![Example Gateway policy that blocks MCP traffic not arriving through an MCP portal](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1104,height=664,format=webp/_astro/gateway-block-unknown-mcp.B2Ainj8x.png)

#### AI security report

A new **AI security report** dashboard under **Insights & Logs > Dashboards** provides visibility into MCP usage across your organization. The dashboard includes:

  * Total MCP request volume, unique users, and unique MCP servers
  * A timeseries chart of unique MCP servers observed over time
  * A summary of Gateway policies that target MCP traffic

![AI security report dashboard showing MCP detection data including total MCP requests, users, servers, and Gateway policies for MCP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2406,height=928,format=webp/_astro/gateway-mcp-dashboard.C9jPahkp.png)

For more information, refer to [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/).

Aug 12, 2026

## [Traffic Source selector in Gateway policies](https://developers.cloudflare.com/changelog/post/2026-08-12-traffic-source-selector/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Gateway [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) policies now include a **Traffic Source** selector that identifies how traffic reaches Cloudflare. This allows administrators to write policies that target specific on-ramp methods - for example, applying different rules to traffic arriving via the Cloudflare One Client compared to traffic routed through an MCP portal or a proxy endpoint.

#### Available traffic source values

UI name | API value | Description  
---|---|---  
Device client | `device_client` | Traffic from the [Cloudflare One Client (WARP)](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)  
Mesh | `mesh` | Traffic from a [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) connector  
Cloudflare WAN | `cloudflare_wan` | Traffic from [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/zero-trust/cloudflare-gateway/) (Magic WAN)  
Clientless RDP | `clientless_rdp` | Traffic from a clientless RDP session  
Proxy endpoint | `proxy_endpoint` | Traffic from a [proxy endpoint](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/) (PAC file)  
Clientless Browser Isolation | `agentless_biso` | Traffic from [clientless Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)  
MCP portal | `mcp_portal` | Traffic from an [MCP portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/)  
  
The selector uses the `net.onramp.type` API field in both HTTP and Network policies.

UI name | API example  
---|---  
Traffic Source | `net.onramp.type == "device_client"`  
  
#### Browser Isolation selector

A **Browser Isolation** selector is also available in Network and HTTP policies. This selector identifies whether the current session is running inside [Remote Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/), allowing administrators to apply different policy behavior to isolated traffic.

UI name | API example  
---|---  
Browser Isolation | `net.is_isolated == true`  
  
For more information, refer to [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/).

Aug 11, 2026

## [Hostname routing is now generally available, with a new public IP range for initial resolved IPs](https://developers.cloudflare.com/changelog/post/2026-08-11-hostname-routing-ga-public-initial-resolved-ips/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Hostname routing ↗︎](https://blog.cloudflare.com/tunnel-hostname-routing/) is now generally available. Instead of managing static IP lists and routes, you can route traffic by hostname across multiple Cloudflare One connectors:

  * **Cloudflare Tunnel** : route a [private hostname](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) (for example, `wiki.internal.local`) to a private application behind your tunnel, or a [public hostname](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/) (for example, `bank.example.com`) to egress through a specific tunnel and anchor traffic to a dedicated exit node.
  * **Cloudflare Mesh** : attract a [private or public hostname's traffic](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes) to a Mesh node.



Alongside GA, the default IPv4 range used for initial resolved IPs (also called token IPs) is changing from a Carrier-Grade NAT (CGNAT) range to a public Cloudflare-owned range:

  * **IPv4** : `172.64.128.0/20`
  * **IPv6** : `2606:4700:0cf1:4000::/64`



This is the default range. You can [configure a custom initial resolved IP range](https://developers.cloudflare.com/cloudflare-one/networks/routes/configure-initial-resolved-ips/) for IPv4 if it conflicts with your existing network.

**Why this is changing:** Starting with [Chrome 142 ↗︎](https://developer.chrome.com/release-notes/142), Local Network Access (LNA) restrictions block background requests to CGNAT addresses (`100.64.0.0/10`), which included the previous initial resolved IP default (`100.80.0.0/16`). LNA is implemented at the Chromium engine level, so it affects all Chromium-based browsers (for example, Microsoft Edge, Brave, and Opera), not only Google Chrome. This could silently break hostname-based Gateway features for users of these browsers, and required Chrome Enterprise policy workarounds. The new default range is public Cloudflare address space, so it is not affected by this restriction.

**What is affected:** Initial resolved IPs are used by several features that associate a DNS query with the network connection that follows it:

  * [Private](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) and [public](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/) hostname routing for Cloudflare Tunnel
  * [Hostname routes](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes) for Cloudflare Mesh
  * [Access private applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/) on non-HTTPS ports
  * [Egress policy host selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/host-selectors/) (Domain, Host, Application, and Content Categories)



You can check your account's current range, or configure a custom range, at any time from **Networking** > **IP addresses** > **Address space** > **Custom IPs** , or using the [Initial Resolved IP Subnet API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/#\(resource\)%20zero_trust.networks.subnets.initial_resolved_ip).

[ Go to **Custom IPs** ↗ ](https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space/custom-ips)

For full instructions, refer to [Configure initial resolved IPs](https://developers.cloudflare.com/cloudflare-one/networks/routes/configure-initial-resolved-ips/). The IPv6 range (`2606:4700:0cf1:4000::/64`) is unchanged and is not affected by this restriction.

The default IPv4 range, and all Cloudflare One IPv6 ranges, are automatically routed through the Cloudflare One Client and do not require any Split Tunnel configuration. Refer to [Automatically managed ranges](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#automatically-managed-ranges) for details.

If you were relying on a Chrome Enterprise policy workaround (such as `LocalNetworkAccessRestrictionsTemporaryOptOut`) while your account was still on the legacy CGNAT-based range, refer to [Google Chrome restricts access to private hostnames](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/#google-chrome-restricts-access-to-private-hostnames) for next steps.

Jul 28, 2026

## [Control Cloudflare Gateway DNS caching with a maximum TTL setting](https://developers.cloudflare.com/changelog/post/2026-07-28-gateway-maximum-dns-ttl/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

You can now set a maximum time-to-live (TTL) for DNS responses returned by Gateway. When an upstream DNS record has a TTL that exceeds the configured maximum, Gateway caps it to your specified value. This ensures that DNS policy changes - such as blocking a newly identified malicious domain - take effect faster across all clients.

![The maximum DNS TTL setting in Traffic policies > Traffic settings, showing a numeric input field that accepts values between 60 and 36,000 seconds](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2170,height=294,format=webp/_astro/gateway-max-ttl-traffic-settings.BRF3NUMp.png)

The setting is available at two levels:

  * **Account level** \- In **Traffic Policies** > **Traffic Settings** , under **Proxy and inspection**. This sets the default cap for all DNS locations.
  * **Per-location** \- Each [DNS location](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-proxies/) can inherit the account setting, disable the cap, or override it with a custom value.



Two new fields are also available in DNS logs: `upstream_record_ttls` (the original TTL from the upstream response) and `applied_max_ttl` (the cap Gateway applied). These appear in the DNS logs column picker and in Logpush datasets.

For more information, refer to [Maximum DNS TTL](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/).

Jul 17, 2026

## [New header control options for Gateway HTTP policies](https://developers.cloudflare.com/changelog/post/2026-07-17-http-request-header-manipulation/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Cloudflare Gateway now supports advanced header control on [Allow policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#allow). Administrators can add, overwrite, or delete headers on matching requests using static values or dynamic variables.

#### Header operations

Gateway HTTP policies using the Allow action support three operations in `rule_settings`:

Operation | API field | Behavior  
---|---|---  
Add | `add_headers` | Appends a value to the header. Existing values are preserved.  
Overwrite | `set_headers` | Replaces the header value. Creates the header if it does not exist.  
Delete | `delete_headers` | Removes the header from the request.  
  
Gateway applies operations in order: delete, then overwrite, then add.

#### Dynamic variables

Header values can include dynamic variables using the `@{...}` syntax. Gateway resolves variables at request time from identity, device, and network context.

Variable | Description  
---|---  
`@{identity.email}` | User email from the identity provider  
`@{identity.name}` | User display name from the identity provider  
`@{identity.id}` | Cloudflare identity UUID  
`@{identity.groups}` | Identity provider group memberships  
`@{identity.SAML}` | SAML attributes (if configured)  
`@{identity.OIDC}` | OIDC claims (if configured)  
`@{source.ip}` | Source IP of the connection  
`@{destination.ip}` | Destination IP of the request  
`@{device.id}` | Cloudflare One Client device UUID  
`@{device.posture}` | Device posture check results (JSON string)  
  
You can mix static text and dynamic variables in a single header value. For example, `user-@{identity.email}` resolves to `user-jdoe@example.com`.

For more information, refer to [Custom headers](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tenant-control/).

Jul 15, 2026

## [Internal DNS is now generally available](https://developers.cloudflare.com/changelog/post/2026-07-15-internal-dns-ga/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[DNS](https://developers.cloudflare.com/dns/)

[Internal DNS](https://developers.cloudflare.com/dns/internal-dns/) is now generally available. Internal DNS provides authoritative and recursive DNS for private networks on the same global network and control plane you already use for public DNS, Zero Trust, and application services.

#### Why it matters

  * **Consolidate DNS operations.** Public and private DNS run on one platform, with one API, one audit trail, and one place to set policy.
  * **Simplify split-horizon DNS.** Internal and external resolution are defined as separate [views](https://developers.cloudflare.com/dns/internal-dns/dns-views/) over shared zones, managed from a single control plane — so there is no drift to chase down.
  * **Extend Zero Trust to DNS.** Resolver policies decide which users and devices resolve against which view, enforced by the same [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) that already governs the rest of your traffic.



Setting up Internal DNS takes three steps: create a zone, create a view, and define a resolver policy.
    
    
    POST /zones
    {
      "account": {
        "id": "<ACCOUNT_ID>"
      },
      "name": "corp.internal",
      "type": "internal"
    }

Internal DNS is included with [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) for Enterprise customers. To get started, refer to the [Internal DNS documentation](https://developers.cloudflare.com/dns/internal-dns/).

Jun 30, 2026

## [New permissions and roles for Gateway policies and lists](https://developers.cloudflare.com/changelog/post/2026-06-30-gateway-granular-permissions/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

You can now assign granular, resource-scoped roles for [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) firewall policies and [Zero Trust lists](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/). Administrators can delegate access to specific policy types or list management without granting account-wide or product-wide control.

#### What is new

When you [add a member](https://developers.cloudflare.com/fundamentals/manage-members/manage/) or create a [permission policy](https://developers.cloudflare.com/fundamentals/manage-members/policies/), the following resource-scoped roles are now available:

Role | Description  
---|---  
Zero Trust Gateway Firewall Policies Admin | Can view and edit all Gateway firewall policies, including DNS, HTTP, and Network policies.  
Zero Trust Gateway DNS Policies Admin | Can view and edit Gateway DNS policies.  
Zero Trust Gateway HTTP Policies Admin | Can view and edit Gateway HTTP policies.  
Zero Trust Gateway Network Policies Admin | Can view and edit Gateway Network policies.  
Zero Trust Gateway Egress Policies Admin | Can view and edit Gateway Egress policies.  
Zero Trust Gateway Resolver Policies Admin | Can view and edit Gateway Resolver policies.  
Zero Trust Gateway Policies Admin | Can view and edit all Gateway policies.  
Zero Trust Gateway Policies Read | Can view all Gateway policies.  
Zero Trust Gateway Read Only | Can view all Gateway resources.  
Zero Trust DNS Locations Admin | Can view and edit DNS locations.  
Zero Trust Proxy Endpoints Admin | Can view and edit Gateway Proxy Endpoints.  
Zero Trust Account Lists Admin | Can view and edit all Gateway and Access lists.  
Zero Trust Account Lists Read | Can view all Gateway and Access lists.  
  
These roles allow you to:

  * Grant a network engineer write access to Network policies only, without exposing DNS or HTTP policy configuration.
  * Allow a security analyst to view all Gateway policies in read-only mode for auditing purposes.
  * Delegate list management to a team that maintains block and allow lists without giving them access to policy configuration.



You can also now assign _Resource-scoped roles_. These roles are complementary to existing account-level roles, and allow you to grant access to a specific resource, like an individual Gateway policy or Cloudflare One list. **Existing account-level roles continue to work.** A member with the `Cloudflare Gateway` or `Cloudflare Zero Trust` role retains full access to all Gateway resources. This ensures backward compatibility for existing automation and API tokens.

#### Get started

  * Refer to [Granular permissions for Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/) for setup instructions and supported resources.
  * Learn how to [create permission policies](https://developers.cloudflare.com/fundamentals/manage-members/policies/) that use these roles.



Jun 5, 2026

## [Filter Workers' public Internet traffic using Gateway policies](https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Workers using a [VPC Network](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) binding with `network_id: "cf1:network"` now egress to public Internet destinations through [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/). This means your existing Zero Trust traffic policies — DNS, HTTP, Network, and egress — extend to traffic that originates from your Workers, the same way they do for WARP users today.

  1. [Worker](https://developers.cloudflare.com/workers/)

Calls `env.EGRESS.fetch()`

  2. [VPC binding](https://developers.cloudflare.com/workers-vpc/)↓
  3. [Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

Bind via [`cf1:network`](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/)

  4. ↓
  5. [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Policies applied:

[DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/)[HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/)[Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/)

  6. ↓
  7. ↗Public Internet

Any public hostname or IP


[Gateway logsDNSHTTPNetwork](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/)

What you get by default:

  * **Visibility.** Worker egress shows up in Gateway [DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/), [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/), and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) logs alongside your other traffic, so you can audit what your Workers are calling and when.
  * **Enforcement.** Any existing Gateway policy whose selectors match a Worker request will apply — including allow / block lists, DNS category filtering, and HTTP destination rules. If you have already blocked a category for your workforce, your Workers inherit that block.


    
    
    {
    	"vpc_networks": [
    		{
    			"binding": "EGRESS",
    			"network_id": "cf1:network",
    			"remote": true,
    		},
    	],
    }
    
    
    [[vpc_networks]]
    binding = "EGRESS"
    network_id = "cf1:network"
    remote = true
    
    
    // Egress to a public destination — subject to your Gateway policies and logged
    const response = await env.EGRESS.fetch("https://api.example.com/data");
    
    
    // Egress to a public destination — subject to your Gateway policies and logged
    const response = await env.EGRESS.fetch("https://api.example.com/data");

For configuration options, refer to [VPC Networks](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/). For policy authoring, refer to [Cloudflare Gateway traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/).

May 27, 2026

## [Write regex using natural language in Cloudflare One](https://developers.cloudflare.com/changelog/post/2026-05-27-cloudy-regex-assistance/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

[Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) policy selectors which support regular expressions can now be authored in the dashboard using natural language. When building a [policy](https://developers.cloudflare.com/cloudflare-one/traffic-policies/expression-syntax/) with a regex-based selector (like `matches regex`), you can describe what you want to match in plain English and the Cloudflare Agent will generate and validate a corresponding regular expression.

![Write policy regex using natural language](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1000,height=638,format=webp/_astro/gateway-regex-ai-generation.CtJ0S6FS.png)

To get started, select a regex-compatible selector in the [Gateway policy builder](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) and select the icon. You'll see an input field for natural language, such as "any URL starting with /api/v1" or ".com, .net, and .app hosts which contain `gooogle` in the host."

You can also use the tool to explain existing regular expressions. If a policy already contains a regex pattern, you can instantly generate a plain-language description.

A built-in feedback mechanism allows you to rate each interaction to help improve output quality over time.

For more information, refer to [Cloudflare One firewall policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) and expect to see the same functionality supported soon in [Data loss prevention profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/).

May 12, 2026

## [Create Gateway firewall policies with natural language](https://developers.cloudflare.com/changelog/post/2026-05-12-natural-language-policy-creation/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Cloudflare Gateway now supports natural language policy creation for [DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/), [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/), and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) firewall policies. Administrators can describe the outcome they want in plain language, and Cloudflare will generate a complete policy rule that populates the policy builder form.

![Create with AI button on the Gateway firewall policies page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2360,height=1088,format=webp/_astro/gateway-create-with-ai.BYG07coh.png)

To create a policy with natural language, select **Create with AI** on any Gateway firewall policy tab. Choose a policy type, describe what the policy should do, and a fully configured rule will appear in the policy builder for review. You can edit any field before saving, or re-generate with a different prompt.

The generated policy incorporates your account context - including lists, DLP profiles, applications, and device posture checks - so that references to your existing resources resolve automatically.

A built-in feedback mechanism allows you to rate each generated policy and provide optional comments, which Cloudflare uses to improve output quality over time.

For more information, refer to [Gateway firewall policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/).

Apr 29, 2026

## [Gateway Authorization Proxy and hosted PAC files are now generally available](https://developers.cloudflare.com/changelog/post/2026-04-29-gateway-authorization-proxy-pac-files-ga/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

The [Gateway Authorization Proxy](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint) and [hosted PAC files](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file) are now generally available for all plan types.

Authorization proxy endpoints add an identity-aware option alongside the existing [source IP proxy endpoints](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint), using [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) authentication to verify who a user is before applying Gateway filtering — without installing the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/). Cloudflare-hosted PAC files let you create and distribute PAC files directly from Cloudflare One on Cloudflare's global network.

These features are ideal for environments where deploying a device client is not an option, such as virtual desktops (VDI) or compliance-restricted endpoints.

To get started, refer to the [proxy endpoints documentation](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/).

Apr 24, 2026

## [Network Session Logs now available for all on-ramps](https://developers.cloudflare.com/changelog/post/2026-04-24-nsl-all-onramps/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/) are now generated for all traffic proxied through Cloudflare Gateway, regardless of on-ramp type. This includes traffic from [proxy endpoints (PAC files)](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/) and [Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) egress — on-ramps that previously did not generate session logs.

Customers who already consume the `zero_trust_network_sessions` dataset via [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/) or [Log Explorer](https://developers.cloudflare.com/log-explorer/) may see increased log volume if they use these on-ramps.

For field definitions, refer to [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/). For traffic analysis, refer to [Network session analytics](https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/).

Apr 20, 2026

## [Network session analytics dashboard](https://developers.cloudflare.com/changelog/post/2026-04-20-network-session-analytics/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

The new [Network session analytics](https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/) dashboard is now available in Cloudflare One. This dashboard provides visibility into your network traffic patterns, helping you understand how traffic flows through your Cloudflare One infrastructure.

![Cloudflare One Network Session Analytics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2926,height=1574,format=webp/_astro/cf1-network-session-analytics.Gl90hEcp.png)

#### What you can do with Network session analytics

  * **Analyze geographic distribution** : View a world map showing where your network traffic originates, with a list of top locations by session count.
  * **Monitor key metrics** : Track session count, total bytes transferred, and unique users.
  * **Identify connection issues** : Analyze connection close reasons to troubleshoot network problems.
  * **Review protocol usage** : See which network protocols (TCP, UDP, ICMP) are most used.



#### Dashboard features

  * **Summary metrics** : Session count, bytes total, and unique users
  * **Traffic by location** : World map visualization and location list with top traffic sources
  * **Top protocols** : Breakdown of TCP, UDP, ICMP, and ICMPv6 traffic
  * **Connection close reasons** : Insights into why sessions terminated (client closed, origin closed, timeouts, errors)



#### How to access

  1. Log in to [Cloudflare One ↗︎](https://dash.cloudflare.com).
  2. Go to **Zero Trust** > **Insights** > **Dashboards**.
  3. Select **Network session analytics**.



For more information, refer to the [Network session analytics documentation](https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/).

Apr 14, 2026

## [Configure how sensitive data appears in DLP payload logs](https://developers.cloudflare.com/changelog/post/2026-04-14-configurable-payload-log-masking/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You can now configure how sensitive data matches are displayed in your DLP payload match logs — giving your incident response team the context they need to validate alerts without compromising your security posture.

To get started, go to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), select **Zero Trust** > **Data loss prevention** > **DLP settings** and find the **Payload log masking** card.

Previously, all DLP payload logs used a single masking mode that obscured matched data entirely and hid the original character count, making it difficult to distinguish true positives from false positives. This update introduces three options:

  * **Full Mask (default):** Masks the match while preserving character count and visual formatting (for example, `***-**-****` for a Social Security Number). This is an improvement over the previous default, which did not preserve character count.
  * **Partial Mask:** Reveals 25% of the matched content while masking the remainder (for example, `***-**-6789`).
  * **Clear Text:** Stores the full, unmasked violation for deep investigation (for example, `123-45-6789`).



**Important:** The masking level you select is applied at detection time, before the payload is encrypted. This means the chosen format is what your team will see after decrypting the log with your private key — the existing encryption workflow is unchanged.

**Applies to all enabled detections:** When a masking level other than Full Mask is selected, it applies to all sensitive data matches found within a payload window — not just the match that triggered the policy. Any data matched by your enabled DLP detection entries will be masked at the selected level.

For more information, refer to [DLP logging options](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-the-payload-of-matched-rules).

Apr 6, 2026

## [Organizations is now in public beta for enterprises](https://developers.cloudflare.com/changelog/post/2026-04-06-organizations-public-beta/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

We're announcing the public beta of **Organizations** for enterprise customers, a new top-level Cloudflare container that lets Cloudflare customers manage multiple accounts, members, analytics, and shared policies from one centralized location.

**What's New**

**Organizations [BETA]** : [Organizations](https://developers.cloudflare.com/fundamentals/organizations/) are a new top-level container for centrally managing multiple accounts. Each Organization supports up to 500 accounts and 5000 zones, giving larger teams a single place to administer resources at scale.

**Self-serve onboarding** : Enterprise customers can [create an Organization](https://developers.cloudflare.com/fundamentals/organizations/setup/) in the dashboard and assign accounts where they are already Super Administrators.

**Centralized Account Management** : At launch, every Organization member has the Organization Super Admin role. Organization Super Admins can invite other users and manage any child account under the Organization implicitly. **Shared policies** : Share [WAF](https://developers.cloudflare.com/waf/custom-rules/) or [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/organizations/) policies across multiple accounts within your Organization to simplify centralized policy management. **Implicit access** : Members of an Organization automatically receive Super Administrator permissions across child accounts, removing the need for explicit membership on each account. Additional Org-level roles will be available over the course of the year.

**Unified analytics** : View, filter, and download aggregate HTTP analytics across all Organization child accounts from a single dashboard for centralized visibility into traffic patterns and security events.

**Terraform provider support** : Manage Organizations with infrastructure as code from day one. Provision organizations, assign accounts, and configure settings programmatically with the [Cloudflare Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/organization).

**Shared policies** : Share [WAF](https://developers.cloudflare.com/waf/custom-rules/) or [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) policies across multiple accounts within your Organization to simplify centralized policy management.

Note

Organizations is in Public Beta. You must have an Enterprise account to create an organization, but once created, you can add accounts of any plan type where you are a Super Administrator.

For more info:

  * [Get started with Organizations](https://developers.cloudflare.com/fundamentals/organizations/)
  * [Set up your Organization](https://developers.cloudflare.com/fundamentals/organizations/setup/)
  * [Review limitations](https://developers.cloudflare.com/fundamentals/organizations/limitations/)



Apr 1, 2026

## [Logs UI refresh](https://developers.cloudflare.com/changelog/post/2026-04-01-logs-ui-refresh/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Access authentication logs and Gateway activity logs (DNS, Network, and HTTP) now feature a refreshed user interface that gives you more flexibility when viewing and analyzing your logs.

![Screenshot of the new logs UI showing DNS query logs with customizable columns and filtering options](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2984,height=842,format=webp/_astro/cf1-new-logs-ui.DxF4x0l-.png)

The updated UI includes:

  * **Filter by field** \- Select any field value to add it as a filter and narrow down your results.
  * **Customizable fields** \- Choose which fields to display in the log table. Querying for fewer fields improves log loading performance.
  * **View details** \- Select a timestamp to view the full details of a log entry.
  * **Switch to classic view** \- Return to the previous log viewer interface if needed.



For more information, refer to [Access authentication logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/) and [Gateway activity logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/).

Mar 24, 2026

## [OIDC Claims filtering now available in Gateway Firewall, Resolver, and Egress policies](https://developers.cloudflare.com/changelog/post/2026-03-24-oidc-claims-filtering-gateway-policies/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Cloudflare Gateway now supports [OIDC Claims](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/#oidc-claims) as a selector in Firewall, Resolver, and Egress policies. Administrators can use custom OIDC claims from their identity provider to build fine-grained, identity-based traffic policies across all Gateway policy types.

With this update, you can:

  * Filter traffic in [DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/), [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/), and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) firewall policies based on OIDC claim values.
  * Apply custom [resolver policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/) to route DNS queries to specific resolvers depending on a user's OIDC claims.
  * Control [egress policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/) to assign dedicated egress IPs based on OIDC claim attributes.



For example, you can create a policy that routes traffic differently for users with `department=engineering` in their OIDC claims, or restrict access to certain destinations based on a user's role claim.

To get started, configure [custom OIDC claims](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims) on your identity provider and use the **OIDC Claims** selector in the Gateway policy builder.

For more information, refer to [Identity-based policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/).

Mar 4, 2026

## [Gateway Authorization Proxy and hosted PAC files (open beta)](https://developers.cloudflare.com/changelog/post/2026-03-04-gateway-authorization-proxy-open-beta/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

The [Gateway Authorization Proxy](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint) and [PAC file hosting](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file) are now in open beta for all plan types.

Previously, [proxy endpoints](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint) relied on static source IP addresses to authorize traffic, providing no user-level identity in logs or policies. The new authorization proxy replaces IP-based authorization with [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) authentication, verifying who a user is before applying Gateway filtering without installing the WARP client.

This is ideal for environments where you cannot deploy a device client, such as virtual desktops (VDI), mergers and acquisitions, or compliance-restricted endpoints.

#### Key capabilities

  * **Identity-aware proxy traffic** — Users authenticate through your identity provider (Okta, Microsoft Entra ID, Google Workspace, and others) via Cloudflare Access. Logs now show exactly which user accessed which site, and you can write [identity-based policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/) like "only the Finance team can access this accounting tool."
  * **Multiple identity providers** — Display one or multiple login methods simultaneously, giving flexibility for organizations managing users across different identity systems.
  * **Cloudflare-hosted PAC files** — Create and host [PAC files](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file) directly in Cloudflare One with pre-configured templates for Okta and Azure, hosted at `https://pac.cloudflare-gateway.com/<account-id>/<slug>` on Cloudflare's global network.
  * **Simplified billing** — Each user occupies a seat, exactly like they do with the Cloudflare One Client. No new metrics to track.



#### Get started

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), go to **Networks** > **Resolvers & Proxies** > **Proxy endpoints**.
  2. [Create an authorization proxy endpoint](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint) and configure Access policies.
  3. [Create a hosted PAC file](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file) or write your own.
  4. [Configure browsers](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#3b-configure-browser-to-use-pac-file) to use the PAC file URL.
  5. [Install the Cloudflare certificate](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/) for HTTPS inspection.



For more details, refer to the [proxy endpoints documentation](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/) and the [announcement blog post ↗︎](https://blog.cloudflare.com/gateway-authorization-proxy-identity-aware-policies/).

Feb 27, 2026

## [New protocols added for Gateway Protocol Detection (Beta)](https://developers.cloudflare.com/changelog/post/2026-02-27-new-protocol-detection-protocols/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Gateway [Protocol Detection](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/protocol-detection/) now supports seven additional protocols in beta:

Protocol | Notes  
---|---  
IMAP | Internet Message Access Protocol — email retrieval  
POP3 | Post Office Protocol v3 — email retrieval  
SMTP | Simple Mail Transfer Protocol — email sending  
MYSQL | MySQL database wire protocol  
RSYNC-DAEMON | rsync daemon protocol  
LDAP | Lightweight Directory Access Protocol  
NTP | Network Time Protocol  
  
These protocols join the existing set of detected protocols (HTTP, HTTP2, SSH, TLS, DCERPC, MQTT, and TPKT) and can be used with the _Detected Protocol_ selector in [Network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) to identify and filter traffic based on the application-layer protocol, without relying on port-based identification.

If protocol detection is enabled on your account, these protocols will automatically be logged when detected in your Gateway network traffic.

For more information on using Protocol Detection, refer to the [Protocol detection documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/protocol-detection/).

Dec 17, 2025

## [Shadow IT - domain level SaaS analytics](https://developers.cloudflare.com/changelog/post/2025-12-17-shadow-it-domain-analytics/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Zero Trust has again upgraded its **Shadow IT analytics** , providing you with unprecedented visibility into your organizations use of SaaS tools. With this dashboard, you can review who is using an application and volumes of data transfer to the application.

With this update, you can review data transfer metrics at the domain level, rather than just the application level, providing more granular insight into your data transfer patterns.

![New Domain Level Metrics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=452,format=webp/_astro/shadow-it-domain.DoZnGAtf.png)

These metrics can be filtered by all available filters on the dashboard, including user, application, or content category.

Both the analytics and policies are accessible in the Cloudflare [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/), empowering organizations with better visibility and control.

← Prev

1[2](https://developers.cloudflare.com/changelog/product/gateway/2/)

[Next →](https://developers.cloudflare.com/changelog/product/gateway/2/)
